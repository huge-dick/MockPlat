# encoding=utf-8
# @Author : wangjie
# @Time : 2020/8/13 下午7:23

'''锁仓产品收益检查'''


#计算昨日挖矿总算力
import datetime

from sqlalchemy import func, and_

from exts import db
from kctool.modles.px_staking import LockSnapshot, PolIncome, Product, LockIncome, SoftStakingIncome

'''计算挖矿总算力'''
def cal_total_output(lock_date):
    return db.session.query(func.sum(LockSnapshot.amount*LockSnapshot.price*LockSnapshot.liquidity)).filter(and_(LockSnapshot.lock_date==lock_date,LockSnapshot.staking==1)).scalar()


'''计算锁仓/投票某一产品的算力'''
''':return (lock_output,amount,snapshot_id,if_staking)'''
def cal_lock_output(lock_date,lock_id,user_id):
    result=db.session.query(func.sum(LockSnapshot.amount*LockSnapshot.price*LockSnapshot.liquidity), LockSnapshot.amount, LockSnapshot.id,LockSnapshot.staking,LockSnapshot.liquidity).filter(and_(LockSnapshot.lock_date==lock_date,LockSnapshot.lock_id==lock_id,LockSnapshot.user_id==user_id)).one()
    data={
        "lock_output":result[0],
        "amount":result[1],
        "snapshot_id":result[2],
        "if_staking":result[3],
        "liquidity":result[4]
    }
    return data

'''每日挖矿总产出，每180天衰减20%'''
def get_daily_amount_by_date(date):
    startDate=datetime.datetime.strptime('2020-01-09','%Y-%m-%d').date()
    # date=datetime.date.today()
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    diffDays=(date-startDate).days
    cycle=diffDays//180
    amount=250000*0.8**cycle
    return amount


'''查询当个锁仓挖得pol数量'''
def query_lock_pol_income(income_date,snapshot_id,user_id):
    return db.session.query(func.sum(PolIncome.amount)).filter(and_(PolIncome.income_date == income_date,PolIncome.snapshot_id == snapshot_id, PolIncome.user_id==user_id)).scalar()

'''查询总的pol产出'''
def query_total_pol_income(income_date):
    return db.session.query(func.sum(PolIncome.amount)).filter(PolIncome.income_date == income_date).scalar()

'''查询当个锁仓的本币收益'''
def query_currency_income(lock_id,income_date):
    return db.session.query(func.sum(LockIncome.amount)).filter(and_(LockIncome.income_date == income_date,LockIncome.lock_id == lock_id)).scalar()


'''查询活动信息'''
def query_product_info(product_id):
    prod_info=db.session.query(Product.id,Product.expected_return,Product.makeup_ratio,Product.unlock_period).filter(Product.id == product_id).one()
    data={
        "productId":prod_info[0],
        "expected_return":prod_info[1],
        "makeup_ratio":prod_info[2],
        "unlock_period":prod_info[3]
    }
    return data

'''查询soft-staking收益'''
def query_soft_staking_income(incomeDate,userId,currency):
    return db.session.query(func.sum(SoftStakingIncome.amount)).filter(and_(SoftStakingIncome.income_date==incomeDate,SoftStakingIncome.user_id==userId,SoftStakingIncome.currency==currency)).scalar()

if __name__ == '__main__':
    print(get_daily_amount_by_date('2020-12-15'))