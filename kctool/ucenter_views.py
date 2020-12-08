# encoding=utf-8
# @Author : wangjie
# @Time : 2020/6/19 下午2:58
'''快速生成一个用户，TODO 手机号用户'''
import datetime
import re

from kctool.commonMethods.account_common import AccountApi
from kctool.commonMethods.google_code import getGoogleCheckCode

'''给用户充值'''
import time

from flask import request, jsonify

from exts import db
from kctool.commonMethods.encript import encript_account
from kctool.modles.ucenter import UserModle, UserSecurityMethodModle
from . import kctool

@kctool.route('/ping')
def ping():
    json = {
        "1": 1,
        "2": "2",
        "3": "3"
    }
    return jsonify(json)


@kctool.route('/user/add',methods=['GET', 'POST'])
def gen_user():
    '''快速生成一个用户'''
    email=request.form['email']
    if not re.search('[a-zA-Z0-9_+]+@[0-9a-z]+(\\.[a-z]+)+', email):
        json = {
            "code": 1000,
            "status": "success",
            "msg": "帐户格式不正确"
        }
        return jsonify(json)
    if is_user_exit(email):
        json = {
            "code": 1001,
            "status": "success",
            "msg": "帐户已存在"
        }
        return jsonify(json)
    else:
        uid=str(round(time.time()*1000))
        userid='insertdirec'+uid
        fomattime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        nick=str(email).split('@')[0]
        print(nick)
        user=UserModle(nickname=nick,domain_id='kucoin',uid=uid,trade_type='1',status='2',type='1',is_phone_validate='1',is_email_validate='1',created_at=fomattime,updated_at=fomattime)
        user.email=encript_account(email)
        user.id=userid
        user.password='6aa4c6f9f2e98b05a8c362d073f4f91a'
        try:
            user.save_to_db()
        except:
            json = {
                "code": 1002,
                "status": "falure",
                "msg": "保存用户信息失败"
            }
            return jsonify(json)

        #快速生成两步验证和交易密码
        googlesecurity=UserSecurityMethodModle(user_id=userid,method='GOOGLE2FA',value='Gl2A1VFyWAez9akD2+PF1VxqRC+KQysD')
        try:
            googlesecurity.save_to_db()
        except:
            json = {
                "code": 1003,
                "status": "falure",
                "msg": "保存用户google key失败"
            }
            return jsonify(json)

        tradesecurity=UserSecurityMethodModle(user_id=userid,method='WITHDRAW_PASSWORD',value='958a09f1510ce2afa1e0ce3beeb1389b')
        try:
            tradesecurity.save_to_db()
        except:
            json = {
                "code": 1004,
                "status": "falure",
                "msg": "保存用户交易密码失败"
            }
            return jsonify(json)

        json = {
            "code": 200,
            "status": "success",
            "data":{
                "id":userid,
                "email":email,
                "password":"Aa123456",
                "trade_pwd":"930925",
                "google_key":"hehe"
            }
        }
        '''生成帐户的同时充值'''
        try:
            accountApi=AccountApi()
            accountApi.eazy_receipt(userid)
        except:
            pass
        return jsonify(json)




# @kctool.route('/user/del/<userid>')
# def del_user(userid):
#     user = UserModle(id=userid)
#
#     user.delete_from_db()

def is_user_exit(email):
    '''查询用户是否存在'''
    email=encript_account(email)
    exist=UserModle.query_by_email(email)
    if exist:
        return True
    else:
        return False


@kctool.route('/user')
def get_user_list():
    '''查询通过本程序生成的用户列表'''
    try:
        email=request.args['email']
    except:
        email=''
    if email!='':
        email = encript_account(email)
    try:
        page=request.args['page']
    except:
        page=1
    try:
        pageSize=request.args['pageSize']
    except:
        pageSize=10
    if (email=='' or email == None):
        users=UserModle.get_user_list().order_by(UserModle.uid.desc()).paginate(page=int(page),per_page=int(pageSize))
    else:
        users=UserModle.query.filter_by(email=email).order_by(UserModle.uid.desc()).paginate(page=int(page),per_page=int(pageSize))
    data=[]
    for user in users.items:
        data.append(user.to_json())
    json = {
            "code": 200,
            "status": "success",
            "total":users.total,
            "currentPage":users.page,
            "totalPage":users.pages,
            "data": data
        }
    return jsonify(json)


@kctool.route('/google_code')
def get_google_code():
    '''获取google两步验证码'''
    try:
        google_key=request.args['key']
    except:
        google_key='X77XCDFMM6FEFY3A'
    code=getGoogleCheckCode(google_key)
    json={
        "code":200,
        "status":"success",
        "google_code":code
    }
    return jsonify(json)
