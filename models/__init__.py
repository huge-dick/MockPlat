# encoding=utf-8
# @Author : wangjie
# @Time : 2020/6/23 下午6:13
'''逆向工程生成的Modle'''
import datetime

from sqlalchemy.ext.declarative import declarative_base


def _to_dict(self):
    """
    to dict
    """
    d = {}
    for c in self.__table__.columns:
        if c.name not in self._hidden_not_safe:
            val = getattr(self, c.name, None)

            # 处理 datetime 格式化
            if isinstance(val, datetime):
                val = val.strftime("%Y-%m-%d %H:%M:%S")

            d.update({
                c.name: val
            })

    return d


# Model 基类
Base = declarative_base()
# do not show when convert it to dict
Base._hidden_not_safe = []
Base.to_dict = _to_dict
