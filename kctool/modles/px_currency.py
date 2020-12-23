# encoding=utf-8
# @Author : wangjie
# @Time : 2020/12/16 下午5:54
from flask_sqlalchemy import SQLAlchemy

from models.px_currency import NftToken

db = SQLAlchemy()



class NftCurrency(db.Model):
    __bind_key__ = 'px_currency'
    __tablename__ = 'nft_currency'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='币种名称')
    code = db.Column(db.String(16), nullable=False, unique=True, server_default=db.FetchedValue(), info='币种')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class NftTokenModle(NftToken):
    __bind_key__ = 'px_currency'

    @classmethod
    def query_by_currency(cls, currency):
        if currency=='':
            return cls.query
        return cls.query.filter_by(currency=currency)