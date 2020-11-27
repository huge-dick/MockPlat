# encoding=utf-8
# @Author : wangjie
# @Time : 2020/11/27 下午2:42
from flask import jsonify

from kctool import kctool
from kctool.commonMethods.currency_common import CurrencyApi


@kctool.route('/currency/clear')
def currency_clear_cache():
    currencyApi=CurrencyApi()
    return jsonify(currencyApi.clear_cache())