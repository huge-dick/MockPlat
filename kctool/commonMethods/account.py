# encoding=utf-8
# @Author : wangjie
# @Time : 2020/7/9 下午8:15
import datetime

import requests

from kctool.commonMethods.eureka import Eureka
from kctool.commonMethods.service_enum import ServiceEnum

admin = "admin"
password = "123"

def url_comb(host,service="",path=""):
    url=host
    if service!=None and service!="":
        if service.startswith('/'):
            service=service[1:]
        url=url+"/"+service
    if path!=None and path!="":
        if path.startswith('/'):
            path=path[1:]
        url=url+"/"+path
    return url

class AccountApi():
    def __init__(self):
        self._Host = Eureka().get_service_ip(ServiceEnum.ACCOUNT.value)

    def account_post(self,url,data):
        return requests.post(url, json=data, verify=False, auth=(admin, password))

    def receipt_common(self,amount,accountType,tag,currency,ownerId,bizFrom="PAYMENT",bizType="DEPOSIT",context="test",domainId="kucoin",fee="0",feeTag="DEFAULT",remark="test",subBizType=""):
        bizNo = round(datetime.datetime.now().timestamp() * 1000000)
        # print(bizNo)
        data = {
            "accountType": accountType,
            "amount": amount,
            "bizFrom": bizFrom,
            "bizNo": bizNo,
            "bizType": bizType,
            "context": context,
            "currency": currency,
            "domainId": domainId,
            "fee": 0,
            "feeTag": feeTag,
            "ownerId": ownerId,
            "remark": remark,
            "subBizType": subBizType,
            "tag": tag
        }
        url=url_comb(self._Host,service="",path="/receipt")
        r = self.account_post(url, data)
        return r.json()


    def eazy_receipt(self,userId):
        currencies = ['EOS', 'EOSC', 'ATOM', 'TRX', 'KCS','BTC','ETH']
        for currency in currencies:
            a = self.receipt_common(amount=200000, accountType='POOL', tag='DEFAULT', currency=currency, ownerId=userId,
                               bizFrom="PAYMENT", bizType="DEPOSIT", context="test", domainId="kucoin", fee="0",
                               feeTag="DEFAULT",
                               remark="test", subBizType="")
            print(a)



if __name__ == '__main__':
    accountApi=AccountApi()
    accountApi.eazy_receipt('insertdirec1597061619285')