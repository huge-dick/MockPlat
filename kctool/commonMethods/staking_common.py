# encoding=utf-8
# @Author : wangjie
# @Time : 2020/12/7 下午7:28
import requests

from kctool.commonMethods.eureka import Eureka
from kctool.commonMethods.service_enum import ServiceEnum


class StakingApi():

    def __init__(self):
        self._HOST=Eureka().get_service_ip(ServiceEnum.PX_STAKING.value)

    def clear_redis_cache(self):
        path='/inner/clear-cache'
        url=self._HOST+path
        rs=requests.get(url=url)
        return rs.json()

    def sharding_table(self,split_keyword,table_count=10):
        path='/inner/sharding-table-index'
        url=self._HOST+path
        data={
            "split_keyword":split_keyword,
            "table_count":table_count
        }
        rs=requests.get(url=url, params= data)
        return rs.json()

