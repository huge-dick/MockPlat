# encoding=utf-8
# @Author : wangjie
# @Time : 2020/7/9 下午6:44

'''给用户充值'''

from flask import request, jsonify

from kctool.commonMethods.account_common import AccountApi, AccountFrontApi
from . import kctool


@kctool.route('/account/receipt', methods=['GET', 'POST'])
def receipt():
    ownerId = request.form['userId']
    currency=request.form['currency']
    amount=request.form['amount']
    accountApi=AccountApi()
    r=accountApi.receipt_common(amount=amount, accountType='POOL', tag='DEFAULT', currency=currency, ownerId=ownerId,
            bizFrom="PAYMENT", bizType="DEPOSIT", context="test", domainId="kucoin", fee="0", feeTag="DEFAULT",
            remark="test", subBizType="")
    return jsonify(r)


@kctool.route('/sharding-account',methods=['GET'])
def sharding_account():
    ownerId=request.args['userId']
    accountFrontApi=AccountFrontApi()
    rs=accountFrontApi.sharding_account(ownerId)
    return jsonify(rs)





