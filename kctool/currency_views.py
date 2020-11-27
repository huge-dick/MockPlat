# encoding=utf-8
# @Author : wangjie
# @Time : 2020/11/27 下午2:42
from flask import jsonify

from kctool import kctool
from kctool.commonMethods.currency_common import clear_cache


@kctool.route('/currency/clear')
def currency_clear_cache():
    return jsonify(clear_cache())