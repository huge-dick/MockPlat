from flask_script import Manager

from app import app
from exts import scheduler

'''用于flask app的启动'''
manager = Manager(app)


if __name__ == '__main__':
    scheduler.start()
    app.run(host='0.0.0.0', port=5000, threaded=True)
