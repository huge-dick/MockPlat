# encoding=utf-8
# @Author : wangjie
# @Time : 2020/6/22 下午5:40
eureka = 'http://10.2.1.29:1111'
ding_token = '0163bd5af9efd00c67a08ddf2c66a355acbd9cef04e4a0212e161f96f50a83f5'
# ding_token = '398fcad1ec766e083d63e76537d644b7b85fa91980d34a0d318489948c982b64' #调试

HOST = '10.2.1.29'
PORT = '3306'
DATABASE = 'UCENTER'
USERNAME = 'kucoin'
PASSWORD = 'test_kucoin.123.com'

UCENTER_DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                                password=PASSWORD,
                                                                                                host=HOST, port=PORT,
                                                                                                db=DATABASE)
STAKING_DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                                password=PASSWORD,
                                                                                                host=HOST, port=PORT,
                                                                                                db='px_staking')
PX_CURRENCY_DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                                    password=PASSWORD,
                                                                                                    host=HOST,
                                                                                                    port=PORT,
                                                                                                    db='px_currency')

SQLALCHEMY_BINDS = {
    'ucenter': UCENTER_DB_URI,
    'px_staking': STAKING_DB_URI,
    'px_currency': PX_CURRENCY_DB_URI
}

SQLALCHEMY_DATABASE_URI = UCENTER_DB_URI  # 默认的数据库
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
