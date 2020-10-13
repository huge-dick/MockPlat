# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Index, Integer, JSON, Numeric, String, Text
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class AccountSnapshot(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'account_snapshot'
    __table_args__ = (
        db.Index('idx_account_id_date', 'user_id', 'currency', 'date', 'account_tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    account_tag = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户账户子类型')
    available_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户可用余额日平均值')
    hold_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户冻结金额日平均值')
    total_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户总额日平均值')
    currency_min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='参与soft staking 该币种最小持仓量')
    date = db.Column(db.Date, nullable=False, index=True, info='快照日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class AccountSnapshot0(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'account_snapshot_0'
    __table_args__ = (
        db.Index('idx_account_id_date', 'user_id', 'currency', 'date', 'account_tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    account_tag = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户账户子类型')
    available_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户可用余额日平均值')
    hold_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户冻结金额日平均值')
    total_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户总额日平均值')
    currency_min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='参与soft staking 该币种最小持仓量')
    date = db.Column(db.Date, nullable=False, index=True, info='快照日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class AccountSnapshot1(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'account_snapshot_1'
    __table_args__ = (
        db.Index('idx_account_id_date', 'user_id', 'currency', 'date', 'account_tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    account_tag = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户账户子类型')
    available_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户可用余额日平均值')
    hold_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户冻结金额日平均值')
    total_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户总额日平均值')
    currency_min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='参与soft staking 该币种最小持仓量')
    date = db.Column(db.Date, nullable=False, index=True, info='快照日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class AccountSnapshot2(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'account_snapshot_2'
    __table_args__ = (
        db.Index('idx_account_id_date', 'user_id', 'currency', 'date', 'account_tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    account_tag = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户账户子类型')
    available_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户可用余额日平均值')
    hold_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户冻结金额日平均值')
    total_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户总额日平均值')
    currency_min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='参与soft staking 该币种最小持仓量')
    date = db.Column(db.Date, nullable=False, index=True, info='快照日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class AccountSnapshot3(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'account_snapshot_3'
    __table_args__ = (
        db.Index('idx_account_id_date', 'user_id', 'currency', 'date', 'account_tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    account_tag = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户账户子类型')
    available_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户可用余额日平均值')
    hold_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户冻结金额日平均值')
    total_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户总额日平均值')
    currency_min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='参与soft staking 该币种最小持仓量')
    date = db.Column(db.Date, nullable=False, index=True, info='快照日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class AccountSnapshot4(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'account_snapshot_4'
    __table_args__ = (
        db.Index('idx_account_id_date', 'user_id', 'currency', 'date', 'account_tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    account_tag = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户账户子类型')
    available_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户可用余额日平均值')
    hold_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户冻结金额日平均值')
    total_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户总额日平均值')
    currency_min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='参与soft staking 该币种最小持仓量')
    date = db.Column(db.Date, nullable=False, index=True, info='快照日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class AccountSnapshot5(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'account_snapshot_5'
    __table_args__ = (
        db.Index('idx_account_id_date', 'user_id', 'currency', 'date', 'account_tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    account_tag = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户账户子类型')
    available_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户可用余额日平均值')
    hold_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户冻结金额日平均值')
    total_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户总额日平均值')
    currency_min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='参与soft staking 该币种最小持仓量')
    date = db.Column(db.Date, nullable=False, index=True, info='快照日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class AccountSnapshot6(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'account_snapshot_6'
    __table_args__ = (
        db.Index('idx_account_id_date', 'user_id', 'currency', 'date', 'account_tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    account_tag = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户账户子类型')
    available_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户可用余额日平均值')
    hold_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户冻结金额日平均值')
    total_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户总额日平均值')
    currency_min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='参与soft staking 该币种最小持仓量')
    date = db.Column(db.Date, nullable=False, index=True, info='快照日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class AccountSnapshot7(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'account_snapshot_7'
    __table_args__ = (
        db.Index('idx_account_id_date', 'user_id', 'currency', 'date', 'account_tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    account_tag = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户账户子类型')
    available_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户可用余额日平均值')
    hold_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户冻结金额日平均值')
    total_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户总额日平均值')
    currency_min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='参与soft staking 该币种最小持仓量')
    date = db.Column(db.Date, nullable=False, index=True, info='快照日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class AccountSnapshot8(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'account_snapshot_8'
    __table_args__ = (
        db.Index('idx_account_id_date', 'user_id', 'currency', 'date', 'account_tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    account_tag = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户账户子类型')
    available_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户可用余额日平均值')
    hold_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户冻结金额日平均值')
    total_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户总额日平均值')
    currency_min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='参与soft staking 该币种最小持仓量')
    date = db.Column(db.Date, nullable=False, index=True, info='快照日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class AccountSnapshot9(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'account_snapshot_9'
    __table_args__ = (
        db.Index('idx_account_id_date', 'user_id', 'currency', 'date', 'account_tag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    account_tag = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户账户子类型')
    available_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户可用余额日平均值')
    hold_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户冻结金额日平均值')
    total_balance_avg = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='账户总额日平均值')
    currency_min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='参与soft staking 该币种最小持仓量')
    date = db.Column(db.Date, nullable=False, index=True, info='快照日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class CurrencyLiquidity(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'currency_liquidity'

    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(32), nullable=False, unique=True, server_default=db.FetchedValue(), info='币种')
    liquidity = db.Column(db.Numeric(5, 2), nullable=False, info='流动性系数')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class DailyStat(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'daily_stats'

    stat_date = db.Column(db.Date, primary_key=True, nullable=False, info='统计日期')
    currency = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue(), info='币种')
    total_pool_user_cnt = db.Column(db.Integer, nullable=False, info='开通总人数')
    pol_total_available_amount = db.Column(db.Numeric(38, 20), nullable=False, info='POL总可用数量')
    curr_day_newadd_user_cnt = db.Column(db.Integer, nullable=False, info='当天开通总人数')
    curr_day_register_user_cnt = db.Column(db.Integer, nullable=False, info='当天注册人数')
    pool_in_user_cnt = db.Column(db.Integer, nullable=False, info='当天转入矿池人数')
    pool_in_amt = db.Column(db.Numeric(38, 20), nullable=False, info='当天转入矿池数量')
    pool_in_amt_btc = db.Column(db.Numeric(38, 20), nullable=False, info='当天转入矿池市值(BTC)')
    pool_out_user_cnt = db.Column(db.Integer, nullable=False, info='当天转出矿池人数')
    pool_out_amt = db.Column(db.Numeric(38, 20), nullable=False, info='当天转出矿池数量')
    pool_out_amt_btc = db.Column(db.Numeric(38, 20), nullable=False, info='当天转出矿池市值(BTC)')
    pool_depsoit_user_cnt = db.Column(db.Integer, nullable=False, info='当天充值人数')
    pool_depsoit_amt = db.Column(db.Numeric(38, 20), nullable=False, info='当天充值数量')
    pool_depsoit_amt_btc = db.Column(db.Numeric(38, 20), nullable=False, info='当天充值市值(BTC)')
    pool_lock_user_cnt = db.Column(db.Integer, nullable=False, info='当天锁仓人数')
    pool_lock_amt = db.Column(db.Numeric(38, 20), nullable=False, info='当天锁仓数量')
    pool_lock_amt_btc = db.Column(db.Numeric(38, 20), nullable=False, info='当天锁仓市值(BTC)')
    pool_unlock_amt = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='当天未锁仓数量')
    pool_unlock_amt_btc = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='当天未锁仓市值(BTC)')



class Lock(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'lock'
    __table_args__ = (
        db.Index('uniq_idx_user_id_product_id', 'user_id', 'product_id'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    product_id = db.Column(db.Integer, nullable=False, info='产品Id')
    name = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='产品名称(不区分语言)')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    type = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='产品类型：定期TIME，活期DEMAND')
    amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='累计锁仓数量')
    unlocked_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='已解锁的数量')
    unlocking_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='解锁中的数量')
    freezing_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='下单冻结中的数量')
    apply_start_time = db.Column(db.DateTime, info='申购开始时间(定期才有)')
    apply_end_time = db.Column(db.DateTime, info='申购结束时间(定期才有)')
    lock_start_time = db.Column(db.DateTime, info='锁仓开始时间(定期才有)')
    lock_end_time = db.Column(db.DateTime, info='锁仓结束时间(定期才有)')
    unlock_period = db.Column(db.Integer, nullable=False, info='解锁周期(活期)，单位天')
    lock_time = db.Column(db.DateTime, nullable=False, info='最近锁仓时间')
    status = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='锁仓状态：已锁仓LOCKED,赎回中REDEEMING,已赎回REDEEMED，已取消CANCELED')
    fake = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否是假锁仓：1是，0否')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class LockIncome(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'lock_income'
    __table_args__ = (
        db.Index('uniq_idx_lock_id_income_date', 'lock_id', 'income_date'),
    )

    id = db.Column(db.Integer, primary_key=True)
    lock_id = db.Column(db.Integer, nullable=False, info='锁仓Id')
    user_id = db.Column(db.String(32), nullable=False, index=True, server_default=db.FetchedValue(), info='用户Id')
    type = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='收益类型：锁仓收益STAKING，定期认购期补偿MAKEUP，投票治理收益VOTE')
    currency = db.Column(db.String(32), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    amount = db.Column(db.Numeric(38, 20), nullable=False, info='收益数量')
    full_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='本币全额收益数量')
    income_date = db.Column(db.Date, nullable=False, info='收益日期')
    remark = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue(), info='备注')
    created_at = db.Column(db.DateTime, nullable=False, info='发放时间')
    updated_at = db.Column(db.DateTime, nullable=False)



class LockSnapshot(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'lock_snapshot'
    __table_args__ = (
        db.Index('uniq_idx_lock_id_lock_date', 'lock_id', 'lock_date'),
    )

    id = db.Column(db.Integer, primary_key=True)
    lock_id = db.Column(db.Integer, nullable=False, info='锁仓Id')
    user_id = db.Column(db.String(32), nullable=False, index=True, server_default=db.FetchedValue(), info='用户Id')
    product_id = db.Column(db.Integer, nullable=False, index=True, info='产品Id')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='价格')
    liquidity = db.Column(db.Numeric(5, 3), nullable=False, server_default=db.FetchedValue(), info='调整系数')
    type = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='产品类型：定期TIME，活期DEMAND，投票VOTE')
    fake = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否是假锁仓：1是，0否')
    staking = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否在Staking锁仓中：1是，0否；定期产品认购期在锁仓中')
    staking_return = db.Column(db.Numeric(5, 4), nullable=False, info='预期年化收益率(Staking)')
    amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='锁仓数量')
    lock_date = db.Column(db.Date, nullable=False, index=True, info='锁仓日期')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class LockSnapshotFull(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'lock_snapshot_full'

    id = db.Column(db.Integer, primary_key=True)
    lock_id = db.Column(db.Integer, nullable=False, index=True, info='锁仓Id')
    amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='锁仓数量')
    staking_return = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='预期年化收益率(Staking)')
    status = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='锁仓状态：已锁仓LOCKED,赎回中REDEEMING,已赎回REDEEMED，已取消CANCELED')
    lock_date = db.Column(db.Date, nullable=False, index=True, info='锁仓日期')
    created_at = db.Column(db.DateTime, nullable=False, info='快照时间')
    updated_at = db.Column(db.DateTime, nullable=False)



class LockStatu(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'lock_status'

    id = db.Column(db.Integer, primary_key=True)
    lock_id = db.Column(db.Integer, nullable=False, index=True, info='锁仓Id')
    status = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='锁仓状态：已锁仓LOCKED，赎回中REDEEMING，已赎回REDEEMED，已取消CANCELED，已冻结FROZEN，已解冻结UNFROZEN，已交易结算TRADE_SETTLED(已弃用)，交易买入BOUGHT，交易卖出SOLD')
    amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='数量')
    tx_id = db.Column(db.String(32), nullable=False, index=True, server_default=db.FetchedValue(), info='账务TXID')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class Lockdrop(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'lockdrop'
    __table_args__ = (
        db.Index('idx_sn_cycle', 'sn', 'cycle'),
    )

    id = db.Column(db.Integer, primary_key=True)
    history_id = db.Column(db.Integer, nullable=False, unique=True, info='promotion.lockdrop_history.id')
    type = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='类型 REAL真实数据, MOCK 生成数据')
    sn = db.Column(db.Integer, nullable=False, info='活动的期数')
    cycle = db.Column(db.Integer, nullable=False, info='锁仓周期')
    currency = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='锁仓币种')
    user_id = db.Column(db.String(32), nullable=False, index=True, server_default=db.FetchedValue(), info='用户Id')
    amount = db.Column(db.Numeric(38, 20), nullable=False, info='锁仓数量')
    lock_time = db.Column(db.BigInteger, nullable=False, info='锁仓时间戳，单位毫秒')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class LockdropPol(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'lockdrop_pol'
    __table_args__ = (
        db.Index('uniq_idx_user_id_sn', 'user_id', 'sn'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    sn = db.Column(db.Integer, nullable=False, info='活动的期数')
    currency = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='锁仓币种')
    amount = db.Column(db.Numeric(38, 20), nullable=False, info='POL数量')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class NodeVoteProposal(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'node_vote_proposal'
    __table_args__ = (
        db.Index('idx_uniq', 'proposal_id', 'product_id'),
    )

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False, info='product表ID(type=VOTE)')
    proposal_id = db.Column(db.Integer, nullable=False, info='proposal提案表ID')
    opinion = db.Column(db.String(64), info='投票意见:AGREE,STRONGLY_AGREE,DISAGREE,STRONGLY_DISAGREE,ABSTENTION')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class PolIncome(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'pol_income'
    __table_args__ = (
        db.Index('uniq_idx_user_lock_snapshot_id_type_income_date', 'user_id', 'snapshot_id', 'type', 'income_date'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    snapshot_id = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='快照Id：type为STAKING时指锁仓资产快照Id，type为SOFT_STAKING时指持仓资产快照Id；补偿发收益格式为原snapshot_id+M+补偿日期')
    type = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='收益类型：LOCKDROP，STAKING，SOFT_STAKING，VOTE')
    amount = db.Column(db.Numeric(38, 20), nullable=False, info='收益数量')
    fee = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='手续费')
    fee_rate = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='手续费费率，小于1的小数')
    income_date = db.Column(db.Date, nullable=False, index=True, info='收益日期')
    currency = db.Column(db.String(16), index=True, info='锁仓币种')
    created_at = db.Column(db.DateTime, nullable=False, info='发放时间')
    updated_at = db.Column(db.DateTime, nullable=False)



class PolIncomeRelease(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'pol_income_release'
    __table_args__ = (
        db.Index('uniq_idx_pol_income_id_user_id_type_income_date', 'pol_income_id', 'user_id', 'type', 'income_date'),
    )

    id = db.Column(db.Integer, primary_key=True)
    pol_income_id = db.Column(db.Integer, nullable=False, info='收益Id')
    user_id = db.Column(db.String(32), nullable=False, index=True, server_default=db.FetchedValue(), info='用户Id')
    type = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='收益类型：LOCKDROP，STAKING，SOFT_STAKING，VOTE')
    status = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='释放状态：释放中PENDING，RELEASED已释放')
    amount = db.Column(db.Numeric(38, 20), nullable=False, info='数量(实发数量，扣除手续费后)')
    original_amount = db.Column(db.Numeric(38, 20), nullable=False, info='原始数量(未扣除手续费)')
    fee = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='手续费')
    income_date = db.Column(db.Date, nullable=False, index=True, info='收益时间')
    currency = db.Column(db.String(16), index=True, server_default=db.FetchedValue(), info='锁仓币种')
    released_at = db.Column(db.DateTime, index=True, info='释放时间')
    tx_id = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='账务TXID')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class PosStat(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'pos_stats'
    __table_args__ = (
        db.Index('uniq_idx_cur_date_type', 'currency', 'date', 'type'),
    )

    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='币种')
    date = db.Column(db.Date, nullable=False, index=True, info='统计日期')
    type = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='挖矿类型：锁仓挖矿STAKING，持仓挖矿SOFT_STAKING，投票治理VOTE')
    amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='本币锁仓量/持仓量')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='该币种对BTC价格')
    return_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='本币实际发放收益数量')
    full_return_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='本币全额发放收益数量')
    market_value = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='对BTC市值')
    pol_price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='POL价格')
    pol_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='pol量')
    pol_release_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='pol释放量')
    remark = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue(), info='备注')
    created_at = db.Column(db.DateTime, nullable=False, info='插入时间')
    updated_at = db.Column(db.DateTime, nullable=False, info='更新时间')



class Product(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'product'
    __table_args__ = (
        db.Index('idx_up_time', 'up_start_time', 'up_end_time'),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='产品名称(不区分语言)')
    currency = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    type = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='产品类型：定期TIME，活期DEMAND，投票VOTE')
    expected_return = db.Column(db.Numeric(5, 4), nullable=False, info='预期年化收益率(Staking+POL)，0到1的小数')
    staking_return = db.Column(db.Numeric(5, 4), nullable=False, info='预期年化收益率(Staking)，0到1的小数')
    base_staking_return = db.Column(db.Numeric(5, 4), nullable=False, info='基础预期年化收益率(Staking)，0到1的小数')
    staking_pol_fee = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='挖矿POL的手续费费率，0到1的小数')
    makeup_ratio = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='申购期补偿本币收益比例 0到1的小数')
    user_lower_limit = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='用户锁仓数量下限')
    user_upper_limit = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='用户锁仓数量上限')
    product_lower_limit = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='产品锁仓总数量下限')
    product_upper_limit = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='产品锁仓总数量上限')
    user_locked_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='所有用户已锁仓的总数量')
    user_upper_limit_list = db.Column(db.JSON, info='用户上限名单列表，优先级高于user_upper_limit')
    vip_lock_list = db.Column(db.JSON, info='VIP锁仓列表，锁仓开始时自动锁入')
    apply_start_time = db.Column(db.DateTime, info='申购开始时间')
    apply_end_time = db.Column(db.DateTime, info='申购结束时间')
    lock_start_time = db.Column(db.DateTime, info='锁仓开始时间')
    lock_end_time = db.Column(db.DateTime, info='锁仓结束时间')
    unlock_period = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='解锁周期，单位天')
    nodes = db.Column(db.JSON, nullable=False, info='节点列表')
    weight = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='权重，越大靠前')
    return_ratio = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='本币收益发放比例 0到1的小数')
    pol_multiple = db.Column(db.Numeric(8, 4), nullable=False, server_default=db.FetchedValue(), info='POL收益加成系数')
    up_status = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='产品上线状态：草稿DRAFT，上线UP，下线DOWN')
    up_start_time = db.Column(db.DateTime, info='产品上线开始时间')
    up_end_time = db.Column(db.DateTime, info='产品上线结束时间')
    trial_type = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='体验金类型：NONE 没有体验金活动，ONLY 仅支持体验金，BOTH 支持体验金与本金')
    trial_batch_num = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='体验金批次号')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class ProductDetail(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'product_detail'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False, unique=True, info='product表ID')
    node_name = db.Column(db.String(512), nullable=False, index=True, server_default=db.FetchedValue(), info='节点名称')
    node_icon = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='节点图标')
    voter_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='委托投票人数量')
    voted_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='节点参与投票次数')
    address = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue(), info='地址')
    desc = db.Column(db.JSON, info='简介')
    switch_limit_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='再转投天数限制')
    promotion = db.Column(db.JSON, info='奖励活动')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class ProductTrade(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'product_trade'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False, unique=True)
    enabled_trade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否开启交易：1是，0否')
    maker_fee_rate = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='maker手续费费率')
    taker_fee_rate = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='taker手续费费率')
    min_order_size = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='taker最小下单数量，0无限制')
    max_order_size = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='taker最大下单数量，0无限制')
    daily_order_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='maker单日发布订单最大限制数量(买+卖)，0无限制')
    active_order_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='maker最大活跃订单数，0无限制')
    min_publish_size = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='maker单笔订单最小发布数量，0无限制')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class Proposal(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'proposal'
    __table_args__ = (
        db.Index('idx_currency_num', 'currency', 'num'),
    )

    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue(), info='提案编号')
    currency = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='代币')
    proposer = db.Column(db.String(512), nullable=False, index=True, server_default=db.FetchedValue(), info='提案发起人')
    block_hash = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue(), info='区块哈希')
    block_height = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue(), info='区块高度')
    type = db.Column(db.JSON, nullable=False, info='提案类型')
    title = db.Column(db.JSON, nullable=False, info='提案标题')
    content = db.Column(db.JSON, nullable=False, info='提案内容')
    launch_time = db.Column(db.DateTime, nullable=False, info='提案发起时间')
    vote_start_time = db.Column(db.DateTime, nullable=False, info='投票开始时间')
    vote_end_time = db.Column(db.DateTime, nullable=False, info='投票结束时间')
    status = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='提案状态,DEPOSITING 等待缴纳押金, VOTING 投票中,FINISHED 已结束,EXPIRED 已失效,DRAFT 未启动,REJECTED 已拒绝, PASSED 已通过')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class SoftStakingCurrency(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'soft_staking_currency'

    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(16), nullable=False, unique=True, server_default=db.FetchedValue(), info='币种')
    min_return = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='预期最小年化收益率 0到1的小数')
    max_return = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='预期最大年化收益率 0到1的小数')
    min_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='最小持仓数额,0表示无最小限制')
    return_ratio = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='本币收益发放比例 0到1的小数')
    pol_multiple = db.Column(db.Numeric(8, 4), nullable=False, server_default=db.FetchedValue(), info='POL收益加成系数')
    weight = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='权重，越大靠前')
    pol_fee_rate = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='持仓挖矿，手续费率')
    tag = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='标签')
    staking_status = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种支持soft staking状态：上线UP，下线DOWN')
    pol_status = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='币种支持POL挖矿状态：上线UP，下线DOWN')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class SoftStakingIncome(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'soft_staking_income'
    __table_args__ = (
        db.Index('uniq_idx_uid_currency_income_date', 'user_id', 'currency', 'income_date'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    currency = db.Column(db.String(32), nullable=False, index=True, server_default=db.FetchedValue(), info='币种')
    amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='收益数量')
    full_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='本币全额收益数量')
    income_date = db.Column(db.Date, nullable=False, index=True, info='收益日期')
    remark = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue(), info='备注')
    created_at = db.Column(db.DateTime, nullable=False, info='发放时间')
    updated_at = db.Column(db.DateTime, nullable=False)



class Unlock(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'unlock'

    id = db.Column(db.Integer, primary_key=True)
    lock_id = db.Column(db.Integer, nullable=False, index=True, info='锁仓Id')
    status = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='解锁状态：赎回中REDEEMING,已赎回REDEEMED，已取消CANCELED')
    amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='解锁数量')
    tx_id = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='账务Id')
    unlock_time = db.Column(db.DateTime, nullable=False, info='可解锁的时间，大于此时间才能解锁')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class UnlockStatu(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'unlock_status'

    id = db.Column(db.Integer, primary_key=True)
    unlock_id = db.Column(db.Integer, nullable=False, index=True, info='解锁Id')
    status = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='解锁状态：赎回中REDEEMING,已赎回REDEEMED，已取消CANCELED')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class UserVoteProposal(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'user_vote_proposal'
    __table_args__ = (
        db.Index('idx_uniq', 'user_id', 'product_id', 'proposal_id'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='用户Id')
    product_id = db.Column(db.Integer, nullable=False, index=True, info='product表ID(type=VOTE)')
    proposal_id = db.Column(db.Integer, nullable=False, index=True, info='proposal提案表ID')
    opinion = db.Column(db.String(64), info='投票意见:AGREE,STRONGLY_AGREE,DISAGREE,STRONGLY_DISAGREE,ABSTENTION')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class VoteTransactionLog(db.Model):
    __bind_key__ = 'px_staking'
    __tablename__ = 'vote_transaction_log'

    id = db.Column(db.Integer, primary_key=True)
    tx_id = db.Column(db.String(128), unique=True, info='交易id')
    delegator = db.Column(db.String(128), info='质押者')
    validator = db.Column(db.String(128), info='验证节点')
    currency = db.Column(db.String(64), info='交易币种')
    type = db.Column(db.String(64), info='交易类型 ')
    amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='交易数量')
    status = db.Column(db.String(64), info='成功或失败或待验证,SUCCESS,FAIL,PENDING')
    msg = db.Column(db.Text, info='接口返回msg')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
