import os

from flask_cors import CORS
from flask import render_template
from flask_bootstrap3 import Bootstrap

import config
from exts import db, scheduler
from kctool import kctool
from moco import moco
from re_flask import Flask
from scheduler import SchedulerConfig

app = Flask(__name__)

#跨域
CORS(app)

#为flask实例引入db配置,任务配置
app.config.from_object(config)
app.config.from_object(SchedulerConfig())

#注册蓝图
app.register_blueprint(kctool,url_prefix='/kctool')
app.register_blueprint(moco,url_prefix='/')


app.secret_key = '123456'
bootstrap = Bootstrap(app)

#CONFIGPATH,用来存放moco文件的绝对路径
COFIGPATH = os.path.join(os.getcwd(), 'moco/moco_file')
#将db载入flask实例
db.init_app(app)
scheduler.init_app(app)


@app.route('/restart')
def restart():
    return render_template('restart.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/http')
def http():
    return render_template('index.html')







if __name__ == '__main__':

    scheduler.start()
    app.run(host='0.0.0.0', port=5000)
