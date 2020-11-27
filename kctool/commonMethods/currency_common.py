# encoding=utf-8
# @Author : wangjie
# @Time : 2020/11/27 下午2:18
import requests

from kctool.commonMethods.eureka import Eureka
from kctool.commonMethods.service_enum import ServiceEnum

class CurrencyApi():

    def __init__(self):
        self._HOST=Eureka().get_service_ip(ServiceEnum.CURRENCY.value)

    def clear_cache(self):
        path='/currency/clear-cache'
        url=self._HOST+path
        rs=requests.post(url=url)
        return rs.json()