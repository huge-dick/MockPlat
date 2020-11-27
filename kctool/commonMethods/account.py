# encoding=utf-8
# @Author : wangjie
# @Time : 2020/7/9 下午8:15
import datetime

import requests

from kctool.commonMethods.eureka import Eureka
from kctool.commonMethods.service_enum import ServiceEnum

ACCOUNT_HOST=Eureka().get_service_ip(ServiceEnum.ACCOUNT.value)
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

def account_post(url,data):
    return requests.post(url, json=data, verify=False, auth=(admin, password))

def receipt_common(amount,accountType,tag,currency,ownerId,bizFrom="PAYMENT",bizType="DEPOSIT",context="test",domainId="kucoin",fee="0",feeTag="DEFAULT",remark="test",subBizType=""):
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
    url=url_comb(ACCOUNT_HOST,service="",path="/receipt")
    r = account_post(url, data)
    return r.json()


def eazy_receipt(userId):
    currencies = ['EOS', 'EOSC', 'ATOM', 'TRX', 'KCS','BTC','ETH']
    for currency in currencies:
        a = receipt_common(amount=200000, accountType='POOL', tag='DEFAULT', currency=currency, ownerId=userId,
                           bizFrom="PAYMENT", bizType="DEPOSIT", context="test", domainId="kucoin", fee="0",
                           feeTag="DEFAULT",
                           remark="test", subBizType="")
        print(a)



if __name__ == '__main__':
    # a=receipt_common(amount=200000, accountType='POOL', tag='DEFAULT', currency="KTS", ownerId='insertdirec1598253878468',
    #                bizFrom="PAYMENT", bizType="DEPOSIT", context="test", domainId="kucoin", fee="0",
    #                feeTag="DEFAULT",
    #                remark="test", subBizType="")
    # print(a)
    eazy_receipt('insertdirec1598336505393')