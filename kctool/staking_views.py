# encoding=utf-8
# @Author : wangjie
# @Time : 2020/12/8 下午3:02
from flask import jsonify, request

from kctool import kctool
from kctool.commonMethods.staking_common import StakingApi


@kctool.route('/px-redis/clear', methods=['GET'])
def px_clear_cache():
    stakingApi=StakingApi()
    rs=stakingApi.clear_redis_cache()
    return jsonify(rs)

@kctool.route('/px_sharding_table', methods=['GET'])
def px_sharding_table():
    userId=request.args['userId']
    stakingApi = StakingApi()
    rs=stakingApi.sharding_table(userId)
    return jsonify(rs)