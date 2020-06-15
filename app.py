import os
import subprocess
import time

from flask import Flask, render_template, request, session, make_response, flash, redirect, url_for, jsonify
from flask_bootstrap3 import Bootstrap

app = Flask(__name__)
app.secret_key = '123456'
bootstrap = Bootstrap(app)
COFIGPATH = os.path.join(os.getcwd(), 'moco/moco_file')


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    dateformat = time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)
    return dateformat

@app.route('/restart')
def restart():
    return render_template('restart.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/http')
def http():
    return render_template('index.html')


@app.route('/file/list', methods=['GET'])
def file_list():
    def contains(a):
        if 'json' in a:
            return True
        else:
            return False

    files = list(filter(contains, os.listdir(COFIGPATH)))
    data = []
    for file in files:
        fileinfo = {}
        fileinfo['name'] = file
        fileinfo['code'] = file[0:-5]
        filepath = os.path.join(COFIGPATH, file)
        updateAt=os.path.getmtime(filepath)
        dateformat = TimeStampToTime(updateAt)
        fileinfo['updateAt'] = dateformat
        data.append(fileinfo)
    json = {
        "code": 200,
        "status": "success",
        "data": data
    }

    return jsonify(json)


@app.route('/file/<filename>', methods=['GET'])
def file(filename):
    file = os.path.join(COFIGPATH, filename)
    with open(file, 'r') as f:
        content = f.read()
        json = {
            "code": 200,
            "status": "success",
            "data": {
                "filename":filename,
                "content":content
            }
        }
        return jsonify(json)


# 创建或更新
@app.route('/file/create', methods=['POST'])
def file_create():

    filename = request.form['filename']
    if '.json' not in filename:
        filename=filename+'.json'
    content = request.form['content']
    file = os.path.join(COFIGPATH, filename)
    with open(file, 'w') as f:
        f.write(content)
    json = {
        "code": 200,
        "status": "success",
        "message": "操作成功"
    }
    return jsonify(json)


@app.route('/file/delete', methods=['POST'])
def file_delete():
    filename = request.form['filename']
    file = os.path.join(COFIGPATH, filename)
    os.remove(file)
    json = {
        "code": 200,
        "status": "success",
        "message": "操作成功"
    }
    return jsonify(json)

@app.route('/moco/rrestart',methods=['POST'])
def restart_moco():
    try:
        port=request.form['port']
    except:
        port=9999
    if port==None or port=='':
        port=9999
    # os.system("kill `ps -ef|grep moco|grep -v grep| awk '{print $2}'`")
    # os.system("nohup java -jar moco/moco-runner-0.12.0-standalone.jar http -p {} -g moco/settings.json >/dev/null 2>&1 &".format(port))

    subprocess.call("kill `ps -ef|grep moco|grep -v grep| awk '{print $2}'`", shell = True)
    rs=subprocess.call("nohup java -jar moco/moco-runner-0.12.0-standalone.jar http -p {} -g moco/settings.json >/dev/null 2>&1 &".format(port),shell=True)

    if rs==0:
        json = {
            "code": 200,
            "status": "success",
            "message": "重启成功"
        }
        return jsonify(json)
    else:
        json = {
            "code": rs,
            "status": "fail",
            "message": "重启失败，请尝试修改端口重试"
        }
        return jsonify(json)




if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)