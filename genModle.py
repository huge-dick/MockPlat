# encoding=utf-8
# @Author : wangjie
# @Time : 2020/6/23 下午5:23
import os

# ACCOU
cmd=r'flask-sqlacodegen "mysql+pymysql://kucoin:test_kucoin.123.com@10.2.1.29:3306/px_staking" --outfile "models/px_staking.py"  --flask'

os.system(cmd)
