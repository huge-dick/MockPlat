# encoding=utf-8
# @Author : wangjie
# @Time : 2020/11/27 下午2:18
import requests

from kctool.commonMethods.eureka import Eureka
from kctool.commonMethods.service_enum import ServiceEnum

CURRENCY_HOST=Eureka().get_service_ip(ServiceEnum.CURRENCY.value)

def clear_cache():
    path='/currency/clear-cache'
    url=CURRENCY_HOST+path
    rs=requests.post(url=url)
    return rs.json()