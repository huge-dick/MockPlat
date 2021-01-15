# encoding=utf-8
# @Author : wangjie
# @Time : 2021/1/12 下午3:20
import random

from flask import request

from exts import scheduler
from kctool import kctool


@kctool.route('/scheduler/pause')
def pausetask():  # 暂停
    id = request.args['id']
    scheduler.pause_job(id)
    return "Success!"


@kctool.route('/scheduler/resume')
def resumetask():  # 恢复
    id = request.args['id']
    scheduler.resume_job(id)
    return "Success!"


@kctool.route('/scheduler/gettask')
def get_task():
    jobs = scheduler.get_jobs()
    joblist = []
    for job in jobs:
        item = {
            "id": job.id,
            "name": job.name,
        }
        joblist.append(item)

    return str(joblist)


# @kctool.route('/scheduler/remove')
# def remove_task(id):#移除
#     scheduler.delete_job(id)
#     return 111
#
# @kctool.route('/scheduler/addjob', methods=['GET','POST'])
# def addtask():
#     func=request.form('func')
#     scheduler.add_job(func=func, id='1', args=(1, 2), trigger='interval', seconds=5, replace_existing=True)
#     return 'sucess'

if __name__ == '__main__':
    get_task()
