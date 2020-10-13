# encoding=utf-8
# @Author : wangjie
# @Time : 2020/6/19 上午11:57
from flask import Blueprint

moco=Blueprint('moco',__name__)

from .views import *