# encoding=utf-8
# @Author : wangjie
# @Time : 2020/6/23 下午4:18
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler as _BaseAPScheduler


class APScheduler(_BaseAPScheduler):
    def run_job(self, id, jobstore=None):
        with self.app.app_context():
            super().run_job(id=id, jobstore=jobstore)


db=SQLAlchemy()
scheduler=APScheduler()
