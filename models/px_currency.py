# coding: utf-8
from sqlalchemy import Column, DateTime, Index, Integer, JSON, Numeric, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class NftCurrency(db.Model):
    __tablename__ = 'nft_currency'
    __bind_key__ = 'px_currency'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='币种名称')
    code = db.Column(db.String(16), nullable=False, unique=True, server_default=db.FetchedValue(), info='币种')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class NftToken(db.Model):
    __tablename__ = 'nft_token'
    __bind_key__ = 'px_currency'
    __table_args__ = (
        db.Index('uniq_idx_currency_token_id', 'currency', 'token_id'),
    )

    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='币种')
    token_id = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='Token_id')
    # metadata = db.Column(db.JSON, info='元数据')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)


