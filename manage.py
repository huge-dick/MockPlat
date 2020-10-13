from flask_script import Manager
from app import app

manager = Manager(app) # 注册一个manager实例，自带了runserver命令

@manager.command
def hello():
    """这只是一个测试命令"""
    print("OK")
    return "Hello World!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
