# encoding=utf-8
# @Author : wangjie
# @Time : 2020/6/22 下午5:40
eureka='http://10.2.1.29:1111'

HOST = '10.2.1.29'
PORT = '3306'
DATABASE = 'UCENTER'
USERNAME = 'kucoin'
PASSWORD = 'test_kucoin.123.com'

UCENTER_DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)
STAKING_DB_URI="mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db='px_staking')
PX_CURRENCY_DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db='px_currency')

SQLALCHEMY_BINDS = {
    'ucenter': UCENTER_DB_URI,
    'px_staking': STAKING_DB_URI,
    'px_currency':PX_CURRENCY_DB_URI
}

SQLALCHEMY_DATABASE_URI = UCENTER_DB_URI #默认的数据库引擎
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True