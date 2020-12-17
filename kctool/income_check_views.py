# encoding=utf-8
# @Author : wangjie
# @Time : 2020/8/13 下午5:59
import decimal

from flask import request, jsonify

from kctool import kctool
from kctool.commonMethods.staking_income import *

DISTRIBUTE_COEFFICIENT = 0.2 #发放系数
MAXDIFF=0.00001 #精度误差

def to_float(a):
    if a==None:
        return 0
    elif isinstance(a, decimal.Decimal):
        return float(a)
    else:
        return a


def check_result_json(code,exp_currency_income=1,acc_currency_income=1,exp_pol_income=1,acc_pol_income=1,msg="检查不通过"):
    if code==200 or code=='200':
        if (abs(exp_currency_income-acc_currency_income)<MAXDIFF and abs(exp_pol_income-acc_pol_income)<MAXDIFF ):
            data={
                "code":code,
                "result":"success",
                "progress":100,
                "exp_currency_income":exp_currency_income,
                "acc_currency_income":acc_currency_income,
                "exp_pol_income":exp_pol_income,
                "acc_pol_income":acc_pol_income
            }
        else:
            data = {
                "code": code,
                "result": "wrong",
                "progress":65,
                "exp_currency_income": exp_currency_income,
                "acc_currency_income": acc_currency_income,
                "exp_pol_income": exp_pol_income,
                "acc_pol_income": acc_pol_income
            }
        return jsonify(data)
    else:
        data={
            "code": code,
            "result": "wrong",
            "msg": msg
        }
        return jsonify(data)

'''质押期间/活期计算收益及收益检查'''
def cal_and_query_income(date, user_id, product_id, lock_id,type=None):
    total_output = to_float(cal_total_output(date))
    snapshot_result = to_float(cal_lock_output(date, lock_id=lock_id, user_id=user_id))
    expect_total = to_float(get_daily_amount_by_date(date) * DISTRIBUTE_COEFFICIENT)
    lock_output=to_float(snapshot_result['lock_output'])
    snapshot_id = snapshot_result['snapshot_id']
    amount = to_float(snapshot_result['amount'])
    prodinfo = query_product_info(product_id)
    expected_return = to_float(prodinfo['expected_return'])
    makeup_ratio = to_float(prodinfo['makeup_ratio'])
    if_staking = to_float(snapshot_result['if_staking'])
    if total_output==0:
        return check_result_json(code=1003, msg='总算力为0，无法计算，请检查是否该日期锁仓快照未生成')
    if type =='SUBSCRIBE':
        if if_staking == 0:
            exp_pol_income = 0
            exp_currency_income = amount * expected_return*makeup_ratio / 365
        else:
            return check_result_json(code=1002, msg='快照数据错误')
    elif type == 'BLACK':
        exp_pol_income=lock_output / total_output * expect_total
        exp_currency_income=0
    elif type == 'FAKE':
        exp_pol_income = lock_output / total_output * expect_total
        exp_currency_income = 0
    else:
        exp_currency_income = amount * expected_return / 365
        exp_pol_income = lock_output / total_output * expect_total

    acc_pol_income = to_float(query_lock_pol_income(date, snapshot_id, user_id))
    acc_currency_income = to_float(query_currency_income(lock_id=lock_id, income_date=date))

    return check_result_json(200, exp_currency_income, acc_currency_income, exp_pol_income, acc_pol_income)



'''核算总的POL收益,通过result为True'''
@kctool.route('/income/check_total', methods=['GET'])
def check_total_pol_income():
    date=request.args['date']
    expect_total=get_daily_amount_by_date(date)*DISTRIBUTE_COEFFICIENT
    acc_total=query_total_pol_income(date)
    if (abs(to_float(acc_total)-expect_total)<0.0001):
        rs="success"
    else:
        rs="wrong"
    data={
        "code":200,
        "result":rs,
        "expect_total": expect_total,
        "acc_total": acc_total
    }
    return jsonify(data)

'''定期产品申购期收益检测'''
@kctool.route('/income/check_subscribe_income', methods=['GET'])
def check_subscribe_income():
    lock_id=610196
    user_id='insertdirec1600849808522'
    product_id=126
    date=request.args['date']
    type = 'SUBSCRIBE'
    return cal_and_query_income(date, user_id, product_id, lock_id, type)



'''定期产品质押期间收益检测'''
@kctool.route('/income/check_time_income',methods=['GET'])
def check_time_income():
    lock_id = 610197
    user_id = 'insertdirec1600849808522'
    product_id = 127
    date = request.args['date']
    return cal_and_query_income(date,user_id,product_id,lock_id)


'''活期产品收益检测'''
@kctool.route('/income/check_demand_income',methods=['GET'])
def check_demand_income():
    lock_id = 610198
    user_id = 'insertdirec1600849808522'
    product_id = 128
    date = request.args['date']
    return cal_and_query_income(date,user_id,product_id,lock_id)

'''本币收益黑名单收益检测'''

@kctool.route('/income/check_blacklist_income',methods=['GET'])
def check_black_income():
    lock_id = 610199
    user_id = 'insertdirec1595313823279'
    product_id = 127
    date = request.args['date']
    type='BLACK'
    return cal_and_query_income(date, user_id, product_id, lock_id,type)


@kctool.route('/income/check_fake_income',methods=['GET'])
def check_fake_income():
    lock_id = 610121
    user_id = '5d359e3b4504b51cf0b869ee'
    product_id = 1
    date = request.args['date']
    type = 'FAKE'
    return cal_and_query_income(date, user_id, product_id, lock_id, type)

@kctool.route('/income/check_vote_income',methods=['GET'])
def check_vote_income():
    lock_id = 610200
    user_id = 'insertdirec1600849808522'
    product_id = 130
    date = request.args['date']
    type = 'VOTE'
    return cal_and_query_income(date, user_id, product_id, lock_id, type)

#检查赎回期系数,（暂未考虑币种系数）
@kctool.route('/check/liquidity',methods=['GET'])
def check_liquidity():
    lock_id = 610203
    user_id = 'insertdirec1600849808522'
    product_id = 17
    date = request.args['date']

    snapshot_rs=cal_lock_output(date,lock_id,user_id)
    liquidity=snapshot_rs['liquidity']

    prod_info=query_product_info(product_id)
    unlock_period=prod_info['unlock_period']
    if unlock_period<7:
        exp_liquidity=0.4
    elif unlock_period>=7 and unlock_period<14:
        exp_liquidity=0.6
    elif unlock_period>=14 and unlock_period<21:
        exp_liquidity=0.8
    else:
        exp_liquidity = 0.8
    if to_float(liquidity) == to_float(exp_liquidity):
        data={
            "code":200,
            "result":"success"
        }
    else:
        data={
            "code":200,
            "result":"wrong",
            "liquidity":liquidity,
            "exp_liquidity":exp_liquidity
        }
    return jsonify(data)


#检查收益实际到账
'''TODO:'''
@kctool.route('/check/income/account',methods=['GET'])
def check_income_account():
    pass

#持仓收益小于最小锁仓
@kctool.route('/soft/lower/check',methods=['GET'])
def check_lower_soft():
    user_id = 'insertdirec1597053032747'
    currency = 'EOSC'
    date = request.args['date']

    softincome=to_float(query_soft_staking_income(date,user_id,currency))

    if softincome==0:
        data={
            "code":200,
            "result":"success"
        }
    else:
        data={
            "code":200,
            "result":"wrong",
            "income":softincome,
            "exp_income":0
        }
    return jsonify(data)

#持仓收益
@kctool.route('/soft/income/check',methods=['GET'])
def check_soft_income():
    user_id = 'insertdirec1597053032747'
    currency = 'ATOM'
    date = request.args['date']

    softincome=to_float(query_soft_staking_income(date,user_id,currency))
    expect_min=25.953125*0.06/365
    expect_max=25.953125*0.06*1.1/365

    if (softincome<=expect_max and softincome>=expect_min):
        data={
            "code":200,
            "result":"success"
        }
    else:
        data={
            "code":200,
            "result":"wrong",
            "income":softincome,
            "exp_income":"0.00426626-0.00469289"
        }
    return jsonify(data)





