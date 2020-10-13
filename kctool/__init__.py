# encoding=utf-8
# @Author : wangjie
# @Time : 2020/6/19 上午11:56
from flask import Blueprint

kctool=Blueprint('kctool', __name__, static_folder='static_kctool',static_url_path='/lib')

from .views import *
from .accunt_views import *
from .income_check_views import *
