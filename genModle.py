# encoding=utf-8
# @Author : wangjie
# @Time : 2020/6/23 下午5:23
import os

# 逆向工程，自动生成modles

cmd=r'flask-sqlacodegen "mysql+pymysql://kucoin:test_kucoin.123.com@10.2.1.29:3306/px_currency" --outfile "models/px_currency.py"  --flask'

os.system(cmd)
