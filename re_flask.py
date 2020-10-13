# encoding=utf-8
# @Author : wangjie
# @Time : 2020/8/20 下午3:08
import datetime

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

'''将decimal等数据类型序列化'''


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        import decimal
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, datetime.date):
            return o.strftime("%Y-%m-%d")
        super(JSONEncoder, self).default(o)

class Flask(_Flask):
    json_encoder = JSONEncoder