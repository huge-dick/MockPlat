# encoding=utf-8
# @Author : wangjie
# @Time : 2020/11/27 下午2:42
from flask import jsonify, request

from kctool import kctool
from kctool.commonMethods.currency_common import CurrencyApi
from kctool.modles.px_currency import NftTokenModle


@kctool.route('/currency/clear')
def currency_clear_cache():
    currencyApi=CurrencyApi()
    return jsonify(currencyApi.clear_cache())

@kctool.route('/currency/nft/tokens')
def nft_tokens():
    currency=request.args['currency']
    tokens=NftTokenModle.query_by_currency(currency)
    tokenList=[]
    for item in tokens:
        tokenList.append(item.token_id)
    data={
        "code": 200,
        "status": "success",
        "currency":currency,
        "tokenList":tokenList
    }
    return jsonify(data)
