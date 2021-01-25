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

class AccountFrontApi():
    def __init__(self):
        self._Host = Eureka().get_service_ip(ServiceEnum.ACCOUNT_FRONT.value)

    def sharding_account(self,user_id):
        '''查询用户账务分库分表,默认10库10表'''
        url = self._Host + '/sharding-account'
        data = {"ownerId": user_id}
        rs = requests.get(url=url, params=data)
        return rs.json()

class PoolAccountApi():
    def __init__(self):
        self._Host= Eureka().get_service_ip(ServiceEnum.PX_ACCOUNT.value)

    def receipt(self,userId,currency,tokenId):
        path='/inner/nft/receipt'
        bizNo = round(datetime.datetime.now().timestamp() * 1000000)

        data={
              "biz_from": "PAYMENT",
              "biz_type": "DEPOSIT",
              "biz_no": str(bizNo),
              "user_id": userId,
              "currency": currency,
              "token_id": tokenId,
              "amount": 1,
              "context": {},
              "fee": "0",
              "fee_currency": currency,
              "remark": "test"
            }
        url=url_comb(self._Host, path=path)
        rs=requests.post(url=url,json=data)
        return rs.json()

if __name__ == '__main__':
    # accountApi=AccountApi()
    # accountApi.eazy_receipt('insertdirec1597061619285')
    # accountFrontApi = AccountFrontApi()
    # rs = accountFrontApi.sharding_account('insertdirec1597061619285')
    # print(rs)
    poolAccountApi=PoolAccountApi()
    rs=poolAccountApi.receipt(userId='5fe07e0c2ce6cf0009daf552',currency='GEGO_V2',tokenId='80008')
    print(rs)
