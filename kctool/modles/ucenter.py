# encoding=utf-8
# @Author : wangjie
# @Time : 2020/6/30 上午11:38
import datetime
import time

from exts import db
from kctool.commonMethods.encript import descrypt_account
from models.ucenter import User, UserSecurityMethod


class UserModle(User):

    @classmethod
    def query_by_email(cls,email):
        return UserModle.query.filter_by(email=email).first()

    @classmethod
    def get_user_list(cls):
        return UserModle.query.filter(UserModle.id.like('insert%'))

    def to_json(self):
        # dict = self.__dict__
        # if "_sa_instance_state" in dict:
        #     del dict["_sa_instance_state"]
        # return dict
        return {
            "id":self.id,
            "uid":self.uid,
            "email":descrypt_account(self.email),
            "password":"Aa123456",
            "trade_pwd":"930925",
            "google_key":"X77XCDFMM6FEFY3A",
            "created_at":self.created_at
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



class UserSecurityMethodModle(UserSecurityMethod):

    def __init__(self,user_id,method,value):
        fomattime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.id='insertdirec'+str(round(time.time()*1000))
        self.domain_id='kucoin'
        self.deleted=0,
        self.created_at=fomattime
        self.updated_at=fomattime
        self.user_id=user_id
        self.method=method
        self.value=value



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()







