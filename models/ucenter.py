# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Index, Integer, JSON, Numeric, SmallInteger, String, Table, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.mysql.types import BIT
from sqlalchemy.dialects.mysql.enumerated import ENUM
from flask_sqlalchemy import SQLAlchemy

from exts import db


class AccessToken(db.Model):
    __tablename__ = 'access_token'
    __table_args__ = (
        db.Index('ux-token-domain_id', 'token', 'domain_id'),
        db.Index('ux-token-domain_id-status', 'token', 'domain_id', 'status'),
        db.Index('ux-refresh_token-status', 'refresh_token', 'status')
    )

    token = db.Column(db.String(32), primary_key=True, info='令牌，票据')
    user_id = db.Column(db.String(24), nullable=False, index=True, info='用户id')
    domain_id = db.Column(db.String(10), nullable=False, info='租户id')
    refresh_token = db.Column(db.String(64), nullable=False, unique=True, info='刷新后的令牌，票据')
    device = db.Column(db.String(64), info='设备')
    device_no = db.Column(db.String(256), info='设备号')
    system = db.Column(db.String(26), info='系统')
    system_version = db.Column(db.String(16), info='系统版本')
    app_version = db.Column(db.String(32), info='APP版本')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='token状态 0（过期失效）1（有效）-1（登出失效）-2 (账号冻结导致失效) -3 (被强制踢出失效)')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class AccountManager(db.Model):
    __tablename__ = 'account_manager'

    id = db.Column(db.String(12, 'utf8mb4_bin'), primary_key=True, info='客户经理编号')
    admin_uid = db.Column(db.String(24), nullable=False, unique=True, info='关联管理后台用户ID')
    name = db.Column(db.JSON, nullable=False, info='客户经理名称')
    gen_name = db.Column(db.String(20), server_default=db.FetchedValue(), info='生成字段，中文名称')
    phone = db.Column(db.String(16), nullable=False, server_default=db.FetchedValue(), info='手机号')
    email = db.Column(db.String(120), nullable=False, info='邮箱')
    dept_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='所在部门id')
    title_name = db.Column(db.String(24), nullable=False, index=True, info='职位名称')
    avatar = db.Column(db.String(1024), info='头像')
    is_show_avatar = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否展示头像')
    is_admin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为负责人')
    contact_info = db.Column(db.JSON, nullable=False, info='其它联系方式')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态0-离职 1-在职')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class AmDept(db.Model):
    __tablename__ = 'am_dept'

    id = db.Column(db.Integer, primary_key=True, info='id')
    dept_name = db.Column(db.String(18), nullable=False, info='部门名称')
    parent_id = db.Column(db.Integer, info='上级部门')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class AmUserRelation(db.Model):
    __tablename__ = 'am_user_relation'

    id = db.Column(db.String(24), primary_key=True, info='ID')
    user_id = db.Column(db.String(24), nullable=False, index=True, info='用户ID')
    am_id = db.Column(db.String(16), nullable=False, index=True, server_default=db.FetchedValue(), info='客户经理ID')
    dept_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='所属部门')
    assign_at = db.Column(db.DateTime, info='指定客户经理时间')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class ApiKey(db.Model):
    __tablename__ = 'api_key'

    api_key = db.Column(db.String(64), primary_key=True, info='Api-key')
    secret = db.Column(db.String(128), nullable=False, info='秘钥')
    domain_id = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue(), info='租户ID')
    user_id = db.Column(db.String(24), nullable=False, index=True, info='用户ID')
    api_name = db.Column(db.String(32), info='api名称')
    passphrase = db.Column(db.String(128), nullable=False, info='api秘钥，在创建时由用户自己输入')
    auth_groups = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='权限组信息')
    ip_whitelist_status = db.Column(db.Integer, nullable=False, info='ip白名单状态：0.禁用 1.启用 ')
    ip_whitelist = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue(), info='ip白名单')
    status = db.Column(db.Integer, nullable=False, info='状态：1.删除 0.未删除')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    ip_whitelist_scope = db.Column(db.String(64), info='IP白名单作用范围(auth_groups逗号,分隔)')



class ApiPartner(db.Model):
    __tablename__ = 'api_partner'

    id = db.Column(db.Integer, primary_key=True)
    partner = db.Column(db.String(24, 'utf8_bin'), nullable=False, unique=True, info='第三方合作商名称，唯一标示')
    secret = db.Column(db.String(64, 'utf8_bin'), nullable=False, info='密钥')
    ip = db.Column(db.String(255, 'utf8_bin'), info='第三方IP地址，多个逗号分隔')
    discount_rate = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue(), info='手续费折扣率')
    intro = db.Column(db.String(1024, 'utf8_bin'), info='第三方简介，说明')
    is_enabled = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否禁用。0-禁用，1-启用')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class ChannelConfig(db.Model):
    __tablename__ = 'channel_config'
    __table_args__ = (
        db.Index('uk_platform_channel', 'platform', 'channel'),
    )

    id = db.Column(db.String(24), primary_key=True, info='主键')
    platform = db.Column(db.String(16), nullable=False, info='平台')
    channel = db.Column(db.String(16), nullable=False, info='渠道')
    support_trade_type = db.Column(db.String(16), nullable=False, info='支持的交易类型')
    is_allow_cancel = db.Column(db.Integer, nullable=False, info='是否支持取消订单')
    is_display = db.Column(db.Integer, nullable=False, info='是否展示订单详情')
    order_handler_name = db.Column(db.String(32), nullable=False, info='下单时订单处理器')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class ChannelOrder0(db.Model):
    __tablename__ = 'channel_order_0'
    __table_args__ = (
        db.Index('idx_created_status', 'created_at', 'status'),
        db.Index('idx_user_relate_order', 'user_id', 'relate_order_id')
    )

    id = db.Column(db.String(24), primary_key=True, info='主键')
    user_id = db.Column(db.String(24), nullable=False, info='用户id')
    quote_id = db.Column(db.String(24), nullable=False, info='报价Id')
    platform = db.Column(db.String(16), nullable=False, info='平台')
    dispatch_channel = db.Column(db.String(16), nullable=False, info='分发渠道')
    device_channel = db.Column(db.String(16), nullable=False, info='设备渠道')
    relate_account_id = db.Column(db.String(24), info='关联account的id')
    relate_order_id = db.Column(db.String(24), info='关联渠道的订单id')
    side = db.Column(db.String(16), nullable=False, info='方向')
    pay_type_code = db.Column(db.String(24), nullable=False, info='支付方式code')
    base_currency = db.Column(db.String(16), nullable=False, info='支出币种')
    target_currency = db.Column(db.String(16), nullable=False, info='购买币种')
    trade_currency_type = db.Column(db.String(16), nullable=False, info='购买币种类型:target、base')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='单价')
    base_currency_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='支出总额')
    target_currency_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='订单购买数量')
    direct_status = db.Column(db.String(16), nullable=False, info='直接购买、间接购买')
    domain_id = db.Column(db.String(32), nullable=False, info='租户')
    status = db.Column(db.String(16), nullable=False, info='状态init、processing、finish、cancel')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class ChannelOrder1(db.Model):
    __tablename__ = 'channel_order_1'
    __table_args__ = (
        db.Index('idx_created_status', 'created_at', 'status'),
        db.Index('idx_user_relate_order', 'user_id', 'relate_order_id')
    )

    id = db.Column(db.String(24), primary_key=True, info='主键')
    user_id = db.Column(db.String(24), nullable=False, info='用户id')
    quote_id = db.Column(db.String(24), nullable=False, info='报价Id')
    platform = db.Column(db.String(16), nullable=False, info='平台')
    dispatch_channel = db.Column(db.String(16), nullable=False, info='分发渠道')
    device_channel = db.Column(db.String(16), nullable=False, info='设备渠道')
    relate_account_id = db.Column(db.String(24), info='关联account的id')
    relate_order_id = db.Column(db.String(24), info='关联渠道的订单id')
    side = db.Column(db.String(16), nullable=False, info='方向')
    pay_type_code = db.Column(db.String(24), nullable=False, info='支付方式code')
    base_currency = db.Column(db.String(16), nullable=False, info='支出币种')
    target_currency = db.Column(db.String(16), nullable=False, info='购买币种')
    trade_currency_type = db.Column(db.String(16), nullable=False, info='购买币种类型:target、base')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='单价')
    base_currency_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='支出总额')
    target_currency_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='订单购买数量')
    direct_status = db.Column(db.String(16), nullable=False, info='直接购买、间接购买')
    domain_id = db.Column(db.String(32), nullable=False, info='租户')
    status = db.Column(db.String(16), nullable=False, info='状态init、processing、finish、cancel')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class ChannelOrder2(db.Model):
    __tablename__ = 'channel_order_2'
    __table_args__ = (
        db.Index('idx_user_relate_order', 'user_id', 'relate_order_id'),
        db.Index('idx_created_status', 'created_at', 'status')
    )

    id = db.Column(db.String(24), primary_key=True, info='主键')
    user_id = db.Column(db.String(24), nullable=False, info='用户id')
    quote_id = db.Column(db.String(24), nullable=False, info='报价Id')
    platform = db.Column(db.String(16), nullable=False, info='平台')
    dispatch_channel = db.Column(db.String(16), nullable=False, info='分发渠道')
    device_channel = db.Column(db.String(16), nullable=False, info='设备渠道')
    relate_account_id = db.Column(db.String(24), info='关联account的id')
    relate_order_id = db.Column(db.String(24), info='关联渠道的订单id')
    side = db.Column(db.String(16), nullable=False, info='方向')
    pay_type_code = db.Column(db.String(24), nullable=False, info='支付方式code')
    base_currency = db.Column(db.String(16), nullable=False, info='支出币种')
    target_currency = db.Column(db.String(16), nullable=False, info='购买币种')
    trade_currency_type = db.Column(db.String(16), nullable=False, info='购买币种类型:target、base')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='单价')
    base_currency_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='支出总额')
    target_currency_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='订单购买数量')
    direct_status = db.Column(db.String(16), nullable=False, info='直接购买、间接购买')
    domain_id = db.Column(db.String(32), nullable=False, info='租户')
    status = db.Column(db.String(16), nullable=False, info='状态init、processing、finish、cancel')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class ChannelOrder3(db.Model):
    __tablename__ = 'channel_order_3'
    __table_args__ = (
        db.Index('idx_created_status', 'created_at', 'status'),
        db.Index('idx_user_relate_order', 'user_id', 'relate_order_id')
    )

    id = db.Column(db.String(24), primary_key=True, info='主键')
    user_id = db.Column(db.String(24), nullable=False, info='用户id')
    quote_id = db.Column(db.String(24), nullable=False, info='报价Id')
    platform = db.Column(db.String(16), nullable=False, info='平台')
    dispatch_channel = db.Column(db.String(16), nullable=False, info='分发渠道')
    device_channel = db.Column(db.String(16), nullable=False, info='设备渠道')
    relate_account_id = db.Column(db.String(24), info='关联account的id')
    relate_order_id = db.Column(db.String(24), info='关联渠道的订单id')
    side = db.Column(db.String(16), nullable=False, info='方向')
    pay_type_code = db.Column(db.String(24), nullable=False, info='支付方式code')
    base_currency = db.Column(db.String(16), nullable=False, info='支出币种')
    target_currency = db.Column(db.String(16), nullable=False, info='购买币种')
    trade_currency_type = db.Column(db.String(16), nullable=False, info='购买币种类型:target、base')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='单价')
    base_currency_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='支出总额')
    target_currency_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='订单购买数量')
    direct_status = db.Column(db.String(16), nullable=False, info='直接购买、间接购买')
    domain_id = db.Column(db.String(32), nullable=False, info='租户')
    status = db.Column(db.String(16), nullable=False, info='状态init、processing、finish、cancel')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class ChannelQuote(db.Model):
    __tablename__ = 'channel_quote'

    id = db.Column(db.String(24), primary_key=True, info='主键')
    group_id = db.Column(db.String(24), nullable=False, info='报价组')
    channel = db.Column(db.String(16), nullable=False, info='渠道')
    platform = db.Column(db.String(16), nullable=False, info='平台')
    quote_id = db.Column(db.String(24), info='关联渠道的报价id')
    side = db.Column(db.String(16), nullable=False, info='方向')
    pay_type_code = db.Column(db.String(16), nullable=False, info='支付方式')
    price = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='单价')
    base_currency = db.Column(db.String(16), nullable=False, info='支出币种')
    target_currency = db.Column(db.String(16), nullable=False, info='购买币种')
    trade_target_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='购买数量')
    trade_base_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='支出数量')
    trade_currency_type = db.Column(db.String(16), nullable=False, info='购买币种类型:target、base')
    created_at = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class ChannelSymbolConfig(db.Model):
    __tablename__ = 'channel_symbol_config'
    __table_args__ = (
        db.Index('uk_channel_symbol', 'platform', 'channel', 'target_currency', 'base_currency'),
    )

    id = db.Column(db.String(24), primary_key=True, info='主键')
    platform = db.Column(db.String(16), nullable=False, info='平台')
    channel = db.Column(db.String(16), nullable=False, info='渠道')
    target_currency = db.Column(db.String(16), nullable=False, info='购买币种')
    base_currency = db.Column(db.String(16), nullable=False, info='支出币种')
    min_target_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='最低购买数量')
    max_target_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='最多购买数量')
    min_base_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='最低支出数量')
    max_base_amount = db.Column(db.Numeric(38, 20), nullable=False, server_default=db.FetchedValue(), info='最多支出数量')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    target_currency_precision = db.Column(db.Integer, server_default=db.FetchedValue())
    base_currency_precision = db.Column(db.Integer, server_default=db.FetchedValue())



class CompanyKyc(db.Model):
    __tablename__ = 'company_kyc'

    id = db.Column(db.String(24), primary_key=True)
    user_id = db.Column(db.String(24), nullable=False, index=True, info='用户ID')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='kyc类型. =0 个人账户; =1 机构账户')
    commit_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='提交状态,0初次提交，1重新提交，2从未提交过')
    verify_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='审核状态,=0未审核，=1审核通过，=2审核不通过，=3 待AML人工审核，=4AML人工审核不通过')
    verify_result = db.Column(db.String(2000), info='审核描述')
    operator = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    verify_user = db.Column(db.String(24), info='审核人员')
    commit_at = db.Column(db.DateTime, info='申请时间，第一次提交设置')
    apply_at = db.Column(db.DateTime, info='最近提交时间，用户每次提交都要更新')
    verify_at = db.Column(db.DateTime, info='审核时间')
    verify_fail_reason = db.Column(db.String(5000), info='审核失败原因')
    final_kyc_status = db.Column(db.Integer)
    source = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue(), info='提交来源：web,android,ios')
    code = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司编码')
    name = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='公司名')
    registration_date = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='注册日期')
    registration_country = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='注册国家')
    registration_province = db.Column(db.String(100), info='所在省')
    registration_city = db.Column(db.String(100), info='所在城市')
    registration_street = db.Column(db.String(200), info='街道名')
    registration_home = db.Column(db.String(100), info='门牌号')
    registration_postcode = db.Column(db.String(100), info='邮编')
    work_country = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='办公地点所在国家')
    work_province = db.Column(db.String(100), info='办公省份')
    work_city = db.Column(db.String(100), info='办公城市')
    work_street = db.Column(db.String(200), info='办公街道')
    work_home = db.Column(db.String(100), info='办公门牌号')
    work_postcode = db.Column(db.String(40), info='办公邮编')
    duty_paragraph = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='税号')
    government_website = db.Column(db.String(400), info='验证公司注册地址的政府网站')
    official_website = db.Column(db.String(300), info='公司网站')
    capital_source = db.Column(db.String(100), info='投资资金来源')
    trade_amount = db.Column(db.String(100), info='交易量')
    director = db.Column(db.String(500), info='最高执行官')
    registration_attachment = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='注册证书')
    handle_registration_attachment = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='手持注册照')
    director_attachment = db.Column(db.String(100), info='董事名单')
    first_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='名')
    last_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='姓')
    duty = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='职务')
    telephone = db.Column(db.String(100), info='电话号码')
    incumbency_photo = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='在职证明')
    front_photo = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='正面照')
    back_photo = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='背面照')
    handle_photo = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='手持照')
    id_expire_date = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='证件到期日')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    middle_name = db.Column(db.String(500), info='中间名1')
    middle_name2 = db.Column(db.String(500), info='中间名2')
    old = db.Column(db.Integer, info='是否是kyc老用户，0否，1是')
    telephoneVerify = db.Column(db.String(10), server_default=db.FetchedValue(), info="'nonsupport','checked','unchecked'")



class CompanyKycOld(db.Model):
    __tablename__ = 'company_kyc_old'
    __table_args__ = (
        db.Index('ix_name', 'first_name', 'last_name'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_oid = db.Column(db.String(24), nullable=False)
    first_name = db.Column(db.String(50), server_default=db.FetchedValue())
    middle_name = db.Column(db.String(50), server_default=db.FetchedValue())
    middle_name2 = db.Column(db.String(50), server_default=db.FetchedValue())
    last_name = db.Column(db.String(50), server_default=db.FetchedValue())
    gender = db.Column(db.Enum('female', 'male', 'unknown'), server_default=db.FetchedValue())
    telephone = db.Column(db.String(20))
    telephone_verify = db.Column(db.Enum('nonsupport', 'checked', 'unchecked'), server_default=db.FetchedValue())
    duty = db.Column(db.String(100), server_default=db.FetchedValue(), info='职务')
    incumbency_photo = db.Column(db.String(100), info='在职证明')
    front_photo = db.Column(db.String(100))
    back_photo = db.Column(db.String(100))
    handle_photo = db.Column(db.String(100))
    contacts_submit_status = db.Column(db.Enum('unsubmitted', 'submitted', 'resubmitted'), server_default=db.FetchedValue())
    verify_status = db.Column(db.Enum('first_trial_fail', 'first_trial_pass', 'retrial_fail', 'retrial_pass', 'spot_check_pass', 'spot_check_fail', 'unchecked'), index=True, server_default=db.FetchedValue())
    verify_user = db.Column(db.String(24))
    verify_at = db.Column(db.DateTime)
    contacts_fail_reason = db.Column(db.String(1000))
    company_name = db.Column(db.String(100), index=True, info='公司名')
    registration_date = db.Column(db.BigInteger, info='注册日期')
    registration_country = db.Column(db.String(30), index=True, info='注册地址')
    registration_province = db.Column(db.String(100))
    registration_city = db.Column(db.String(100))
    registration_subdistrict = db.Column(db.String(100))
    registration_home = db.Column(db.String(100))
    registration_postcode = db.Column(db.String(20))
    work_country = db.Column(db.String(30), info='办公地址')
    work_province = db.Column(db.String(100))
    work_city = db.Column(db.String(100))
    work_subdistrict = db.Column(db.String(100))
    work_home = db.Column(db.String(100))
    work_postcode = db.Column(db.String(20))
    company_code = db.Column(db.String(100), info='公司编码')
    duty_paragraph = db.Column(db.String(100), info='税号')
    government_website = db.Column(db.String(300), info='验证公司注册地址的政府网站')
    official_website = db.Column(db.String(300), info='公司网站')
    capital_source = db.Column(db.String(100), info='资金来源')
    trade_amount = db.Column(db.String(100), index=True, info='交易量')
    registration_attachment = db.Column(db.String(100), info='注册证书')
    handle_registration_attachment = db.Column(db.String(100), info='手持注册照')
    director_attachment = db.Column(db.String(100), info='董事名单')
    company_submit_status = db.Column(db.Enum('unsubmitted', 'submitted', 'resubmitted'), server_default=db.FetchedValue())
    company_fail_reason = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, index=True)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    submit_status = db.Column(db.Enum('unsubmitted', 'submitted', 'resubmitted'), server_default=db.FetchedValue())
    source = db.Column(db.String(10))



class Domain(db.Model):
    __tablename__ = 'domain'
    __table_args__ = (
        db.Index('idx-host-type', 'host', 'type'),
    )

    id = db.Column(db.String(20), nullable=False, index=True, info='租户ID')
    secret = db.Column(db.String(64), nullable=False, info='租户密钥')
    host = db.Column(db.String(128), primary_key=True, info='租户域名')
    callback_url = db.Column(db.String(255), nullable=False, info='回调地址')
    ip_white_list = db.Column(db.String(255), info='ip白名单，逗号分隔')
    scopes = db.Column(db.String(255), info='可申请资源范围，逗号分隔')
    name = db.Column(db.String(64), nullable=False, info='租户名称')
    type = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue(), info='domain类型, OAuth - 用于第三方授权的domain, SSO - 用于单点登录的domain')
    is_enable = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



class DomainToken(db.Model):
    __tablename__ = 'domain_token'
    __table_args__ = (
        db.Index('ux-token-status', 'token', 'status'),
        db.Index('idx-refresh_token-status', 'refresh_token', 'status')
    )

    token = db.Column(db.String(24), primary_key=True, info='access token')
    user_id = db.Column(db.String(24), nullable=False, info='用户ID')
    domain_id = db.Column(db.String(20), nullable=False, info='租户ID')
    ip_white_list = db.Column(db.String(255), info='IP白名单')
    scopes = db.Column(db.String(255), nullable=False, info='资源范围，对应ucenter的枚举ResourceScopeEnum')
    refresh_token = db.Column(db.String(64), nullable=False, info='刷新token')
    status = db.Column(db.Integer, nullable=False, info='token状态 0（过期失效）1（有效）-1（手动失效，refresh_token同时失效）')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')



class File(db.Model):
    __tablename__ = 'file'

    id = db.Column(db.String(50), primary_key=True)
    key_name = db.Column(db.String(200), nullable=False)
    user_oid = db.Column(db.String(24), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    deleted_at = db.Column(db.DateTime)



class ForbiddenEmail(db.Model):
    __tablename__ = 'forbidden_email'

    id = db.Column(db.String(24, 'utf8_bin'), primary_key=True, info='id')
    email = db.Column(db.String(320), nullable=False, unique=True, info='邮箱地址')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class IntentionUser(db.Model):
    __tablename__ = 'intention_user'

    account = db.Column(db.String(190, 'utf8mb4_bin'), primary_key=True)
    send_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class IpRecord(db.Model):
    __tablename__ = 'ip_record'
    __table_args__ = (
        db.Index('idx-user_id-event-created_at', 'user_id', 'event', 'created_at'),
    )

    id = db.Column(db.String(24), primary_key=True, server_default=db.FetchedValue())
    domain_id = db.Column(db.String(10), nullable=False, info='租户id')
    event = db.Column(db.Integer, nullable=False, info='事件类型:1.注册, 2.登录失败 3.激活api 4.移除api 5.添加api 6.提现 7.添加两步验证 8.登录')
    user_id = db.Column(db.String(24), nullable=False, info='用户id')
    session_id = db.Column(db.String(64), nullable=False)
    ip = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    new_flag = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否是新设备的标识：1.新设备 0，不是新设备')
    system = db.Column(db.String(24), nullable=False, info='系统')
    system_version = db.Column(db.String(16), info='系统版本')
    platform = db.Column(db.Integer, nullable=False, info='平台类型： 1.browser 2.android 3.ios 4.unkown')
    device_id = db.Column(db.String(32))
    device_no = db.Column(db.String(128), info='设备号')
    device_name = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue(), info='设备名称:手机名称或者浏览器名称')
    version = db.Column(db.String(24), info='版本（app）')
    created_at = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class Kyc(db.Model):
    __tablename__ = 'kyc'

    id = db.Column(db.String(24), primary_key=True, info='id')
    user_id = db.Column(db.String(24), nullable=False, unique=True, info='用户ID')
    source = db.Column(db.String(10), nullable=False, info='提交来源：web,android,ios,h5')
    first_name = db.Column(db.String(64), nullable=False, info='名')
    last_name = db.Column(db.String(128), nullable=False, info='姓')
    region = db.Column(db.String(2), nullable=False, info='两位国家地区码 iso3361-2。 可后台设置')
    user_region = db.Column(db.String(2), nullable=False, info='用户选择的国家')
    identity_type = db.Column(db.String(24), nullable=False, info='证件类型，护照passport，身份证idcard，驾驶证drivinglicense')
    identity_number = db.Column(db.String(255), nullable=False, info='证件号码')
    front_photo = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='证件照正面')
    backend_photo = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='证件照背面')
    handle_photo = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='手持证件照')
    face_image_photo = db.Column(db.String(1024), info='人脸认证图片')
    verify_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='高级审核方式-1-未知 0-人工审核 1-人脸实名认证')
    verify_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='高级审核状态,=-1未提交 =0待审核，=1审核通过，=2审核不通过 =3 该KYC国家不能通过高级认证')
    primary_verify_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='初级认证状态0-未通过 1-已通过')
    primary_attempt_times = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='初级认证校验尝试次数')
    face_attempt_times = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='人脸认证尝试次数')
    failure_reason = db.Column(db.String(1024), info='认证失败原因 json格式')
    apply_at = db.Column(db.DateTime, info='当前KYC级别初次提交时间')
    last_apply_at = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='最近提交时间，用户每次提交kyc信息都要刷新')
    verify_at = db.Column(db.DateTime, info='审核时间')
    operator = db.Column(db.String(24), info='后台审核用户，用户后台筛选')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class KycCode(db.Model):
    __tablename__ = 'kyc_code'

    id = db.Column(db.String(24), primary_key=True, info='id')
    code = db.Column(db.String(8), nullable=False, info='kyc验证码')
    date = db.Column(db.DateTime, nullable=False, unique=True, info='日期')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class KycMetadatum(db.Model):
    __tablename__ = 'kyc_metadata'
    __table_args__ = (
        db.Index('IX_type_code', 'type', 'language', 'code'),
    )

    oid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(3), info='元数据类型。100:预期投资金额; 200:机构交易量选择(BTC/24h); 300:资金规模; 400:行业')
    language = db.Column(db.String(5), server_default=db.FetchedValue(), info='元数据语言')
    code = db.Column(db.String(5), info='元数据code')
    value = db.Column(db.String(100), info='元数据值')
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)



class KycRegion(db.Model):
    __tablename__ = 'kyc_region'

    id = db.Column(db.Integer, primary_key=True, info='id')
    code = db.Column(db.String(2, 'utf8mb4_unicode_ci'), nullable=False, unique=True, info='两位国家或地区代号，格式：ISO 3166-2')
    display_code = db.Column(db.String(2), nullable=False, server_default=db.FetchedValue(), info='用户显示国家或地区代号')
    name = db.Column(db.String(64), nullable=False, info='国家或地区名称')
    chinese_name = db.Column(db.String(32), info='中文名称')
    is_restricted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否政策受限国家或地区')
    is_phone_credible = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否是手机号实名制国家或地区')
    is_support_senior_kyc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否支持kyc高级认证')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class OfficialChannel(db.Model):
    __tablename__ = 'official_channel'
    __table_args__ = (
        db.Index('uk_channel_type_domainid', 'channel', 'domain_id', 'type'),
    )

    id = db.Column(db.Integer, primary_key=True, info='id')
    channel = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False, info='渠道链接或id名称地址')
    type = db.Column(db.Integer, nullable=False, info='渠道类型 渠道类型 0-官方网站 1-手机 2-邮箱 3-微信 4-Twitter 5-Skype 6-facebook 7-telegram 8-youtube 9-medium 10-reddit 11-linkedin 12-instagram 13-微博 14-vk')
    lang = db.Column(db.String(24), nullable=False, server_default=db.FetchedValue(), info='渠道语言')
    platform = db.Column(db.String(24), nullable=False, info='kucoin或kumex或poolx')
    domain_id = db.Column(db.String(24), nullable=False, info='租户ID')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class OperationLog(db.Model):
    __tablename__ = 'operation_log'

    id = db.Column(db.String(24), primary_key=True)
    relation_id = db.Column(db.String(24), nullable=False, info='关联业务ID')
    module = db.Column(db.String(50), nullable=False, index=True, info='功能模块,如apikey')
    event = db.Column(db.String(50), nullable=False, info='操作事件,如创建')
    intro = db.Column(db.String(10000), info='操作描述')
    operator_id = db.Column(db.String(24), server_default=db.FetchedValue(), info='操作人ID')
    operator_name = db.Column(db.String(50), info='操作人姓名')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    reason = db.Column(db.String(256), info='原因')



class ReferrerRelation(db.Model):
    __tablename__ = 'referrer_relation'

    user_id = db.Column(db.String(24), primary_key=True, unique=True, server_default=db.FetchedValue())
    direct_refferer_id = db.Column(db.String(24), index=True)
    secondhand_refferer_id = db.Column(db.String(24), index=True)
    thirdhand_refferer_id = db.Column(db.String(24), index=True)
    refferer_path = db.Column(db.Text)
    tag = db.Column(db.String(64), index=True, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class SecurityQuestion(db.Model):
    __tablename__ = 'security_question'
    __table_args__ = (
        db.Index('idx_user_id_status', 'user_id', 'status'),
        db.Index('idx_user_id_type', 'user_id', 'type')
    )

    id = db.Column(db.String(24), primary_key=True, unique=True, server_default=db.FetchedValue())
    user_id = db.Column(db.String(24), nullable=False, index=True)
    type = db.Column(db.String(24))
    status = db.Column(db.String(31), info='安全问题状态，可选值(CONFIRMING\xa0验证中|CONFIRMED已验证)')
    answer = db.Column(db.String(256))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)



t_security_question_20190224 = db.Table(
    'security_question_20190224',
    db.Column('id', db.String(24), nullable=False, server_default=db.FetchedValue()),
    db.Column('user_id', db.String(24), nullable=False),
    db.Column('type', db.String(24)),
    db.Column('status', db.String(31), info='安全问题状态，可选值(CONFIRMING\xa0验证中|CONFIRMED已验证)'),
    db.Column('answer', db.String(256)),
    db.Column('created_at', db.DateTime),
    db.Column('updated_at', db.DateTime)
)



class SensitiveOperation(db.Model):
    __tablename__ = 'sensitive_operation'
    __table_args__ = (
        db.Index('idx-user_id-operation-created_at', 'user_id', 'operation', 'created_at'),
    )

    id = db.Column(db.String(24), primary_key=True)
    user_id = db.Column(db.String(24), nullable=False)
    target_id = db.Column(db.String(64), info='行为影响的ID，当为API变化事件时对应值为ApiKey，当为用户相关对应值为userId')
    operation = db.Column(db.String(64))
    device_info = db.Column(db.Text)
    status = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='事件消息发送状态 0- 未发送 1 - 已发送 2 - 不需要发送')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class SensitiveUpdateLog(db.Model):
    __tablename__ = 'sensitive_update_log'

    id = db.Column(db.String(24), primary_key=True)
    relation_id = db.Column(db.String(24), nullable=False, index=True, info='关联业务ID')
    pre_value = db.Column(db.String(512), index=True, info='修改前的value')
    after_value = db.Column(db.String(512), info='修改后的value')
    type = db.Column(db.String(16), nullable=False, info='类型')
    operator_id = db.Column(db.String(24), server_default=db.FetchedValue(), info='操作人ID')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = (
        db.Index('uk-nickname-domain_id', 'nickname', 'domain_id'),
        db.Index('uk-sub_name-domain_id', 'sub_name', 'domain_id'),
        db.Index('uk-phone-country_code-domain_id', 'phone', 'country_code', 'domain_id'),
        db.Index('uk-email-domain_id', 'email', 'domain_id')
    )

    id = db.Column(db.String(24), primary_key=True, info='用户ID')
    uid = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='UID')
    domain_id = db.Column(db.String(10), nullable=False, info='租户ID')
    sub_name = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='子帐号名称（加密）')
    parent_id = db.Column(db.String(24), index=True, info='主账号ID，不为空表示当前账号为子账号')
    email = db.Column(db.String(190), info='邮箱地址')
    country_code = db.Column(db.String(16), info='手机号国际区号')
    phone = db.Column(db.String(64), info='手机号')
    password = db.Column(db.String(32), info='用户密码（加密存储）')
    nickname = db.Column(db.String(32), info='用户昵称')
    trade_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开通的交易类型，二进制形式表示，每一位表示一种类型，第一位现货交易，第二位合约交易，两者都开通值为3')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户状态 1（未激活状态）2（新用户，已激活状态）3 （冻结状态）-1（已删除）0（禁用）9(迁移完成状态) 10 (升级交易密码完成状态，老用户激活状态)')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户类型 1（普通用户）2 （内部账号）3（子账号）')
    is_email_validate = db.Column(db.Integer, nullable=False)
    is_phone_validate = db.Column(db.Integer, nullable=False)
    avatar = db.Column(db.String(256), info='头像')
    language = db.Column(db.String(16), info='语言')
    currency = db.Column(db.String(16), info='货币')
    time_zone = db.Column(db.String(64), info='时区')
    referral_code = db.Column(db.String(8), unique=True, info='用户自己的推荐码')
    last_login_at = db.Column(db.DateTime)
    last_login_country = db.Column(db.String(2), info='上次登录国家')
    created_at = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



t_user_20190220 = db.Table(
    'user_20190220',
    db.Column('id', db.String(24), nullable=False, info='用户ID'),
    db.Column('domain_id', db.String(10), nullable=False, info='租户ID'),
    db.Column('email', db.String(190), info='邮箱地址'),
    db.Column('country_code', db.String(16), info='手机号国际区号'),
    db.Column('phone', db.String(64), info='手机号'),
    db.Column('password', db.String(32), info='用户密码（加密存储）'),
    db.Column('nickname', db.String(32), info='用户昵称'),
    db.Column('status', db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户状态 1（未激活状态）2（新用户，已激活状态）3 （冻结状态）-1（已删除）0（禁用）9(迁移完成状态) 10 (升级交易密码完成状态，老用户激活状态)'),
    db.Column('type', db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户类型 1（普通用户）2 （内部账号）3（子账号）'),
    db.Column('is_email_validate', db.Integer, nullable=False),
    db.Column('is_phone_validate', db.Integer, nullable=False),
    db.Column('avatar', db.String(256), info='头像'),
    db.Column('language', db.String(16), info='语言'),
    db.Column('currency', db.String(16), info='货币'),
    db.Column('time_zone', db.String(64), info='时区'),
    db.Column('referral_code', db.String(8), info='用户自己的推荐码'),
    db.Column('parent_id', db.String(24), info='主账号ID，不为空表示当前账号为子账号'),
    db.Column('last_login_at', db.DateTime),
    db.Column('created_at', db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间'),
    db.Column('updated_at', db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
)



class UserAlert(db.Model):
    __tablename__ = 'user_alert'
    __table_args__ = (
        db.Index('idx-user_id-enable', 'user_id', 'enable'),
    )

    id = db.Column(db.String(24), primary_key=True)
    user_id = db.Column(db.String(24), nullable=False)
    enable = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.Text)
    operator = db.Column(db.String(32))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class UserBlacklist(db.Model):
    __tablename__ = 'user_blacklist'
    __table_args__ = (
        db.Index('idx-user_id-type-deleted', 'user_id', 'type', 'deleted'),
        db.Index('ux-user_id-type', 'user_id', 'type')
    )

    id = db.Column(db.String(24), primary_key=True, info='id')
    user_id = db.Column(db.String(24), nullable=False, info='用户id')
    type = db.Column(db.String(32), nullable=False, info='类型')
    deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='删除标识')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class UserDefinedConfig(db.Model):
    __tablename__ = 'user_defined_config'
    __table_args__ = (
        db.Index('ux-user_id-key-domain_id', 'user_id', 'key', 'domain_id'),
    )

    id = db.Column(db.String(24), primary_key=True, info='id')
    domain_id = db.Column(db.String(10), nullable=False, info='租户ID')
    user_id = db.Column(db.String(24), nullable=False, info='用户id')
    key = db.Column(db.String(255), nullable=False, info='配置名称')
    value = db.Column(db.String(800), nullable=False, info='配置值')
    deleted = db.Column(db.Integer, nullable=False)
    available_before = db.Column(db.DateTime, info='配置有效期截止时间')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    deleted_at = db.Column(db.DateTime, info='删除时间')



class UserDevice(db.Model):
    __tablename__ = 'user_device'
    __table_args__ = (
        db.Index('uk_id-user_id', 'id', 'user_id'),
    )

    id = db.Column(db.String(24), primary_key=True, info='id')
    device_id = db.Column(db.String(32))
    user_id = db.Column(db.String(24), nullable=False, info='用户id')
    credible_flag = db.Column(db.Integer, nullable=False, info='信任标识：1.受信 2.不可信')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class UserFeeLevelConfig(db.Model):
    __tablename__ = 'user_fee_level_config'

    id = db.Column(db.String(24), primary_key=True, info='主键id')
    level = db.Column(db.Integer, nullable=False, info='等级')
    express = db.Column(db.String(256), info='等级表达式')
    rule = db.Column(db.String(64), info='交易数量与持有数量表达式关系，或 ||  与 && ')
    day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='天数，成交量统计天数')
    least_size = db.Column(db.Integer, nullable=False, info='最小成交量')
    max_size = db.Column(db.Integer, nullable=False, info='最大成交量')
    least_hold = db.Column(db.Integer, nullable=False, info='持有最小kcs数量')
    max_hold = db.Column(db.Integer, nullable=False, info='持有最大kcs数量')
    maker_fee_rate = db.Column(db.Numeric(10, 8), nullable=False, info='maker 手续费')
    taker_fee_rate = db.Column(db.Numeric(10, 8), nullable=False, info='taker 手续费')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    domain_id = db.Column(db.String(24))



class UserForbidden(db.Model):
    __tablename__ = 'user_forbidden'
    __table_args__ = (
        db.Index('idx-user_id-enable', 'user_id', 'enable'),
    )

    id = db.Column(db.String(24), primary_key=True)
    user_id = db.Column(db.String(24), nullable=False)
    enable = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.Text)
    operator = db.Column(db.String(32))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class UserIp(db.Model):
    __tablename__ = 'user_ip'
    __table_args__ = (
        db.Index('uk-user_id-device_id-ip', 'user_id', 'device_id', 'ip'),
    )

    id = db.Column(db.String(24), primary_key=True)
    user_id = db.Column(db.String(24), nullable=False, index=True, info='用户ID')
    device_id = db.Column(db.String(24), info='设备ID')
    ip = db.Column(db.String(256, 'utf8mb4_unicode_ci'), info='登录IP')
    area = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='地区')
    credible_flag = db.Column(db.Integer, nullable=False, info='信任标识：1.受信 2.不可信')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class UserKyc(db.Model):
    __tablename__ = 'user_kyc'

    id = db.Column(db.String(24), primary_key=True)
    user_id = db.Column(db.String(24), nullable=False, index=True, info='用户ID')
    commit_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='提交状态,0初次提交，1重新提交，2从未提交过')
    verify_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='审核状态,=0未审核，=1审核通过，=2审核不通过，=3 待AML人工审核，=4AML人工审核不通过')
    verify_result = db.Column(db.String(2000), info='审核描述')
    operator = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    verify_user = db.Column(db.String(24), info='审核人员')
    commit_at = db.Column(db.DateTime, info='申请时间,用户第一次提交kyc信息的时间')
    apply_at = db.Column(db.DateTime, info='最近提交时间，用户每次提交kyc信息都要刷新')
    verify_at = db.Column(db.DateTime, info='审核时间')
    verify_fail_reason = db.Column(db.String(5000), info='审核失败原因')
    final_kyc_status = db.Column(db.Integer)
    source = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue(), info='提交来源：web,android,ios')
    first_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='名')
    middle_name = db.Column(db.String(100), info='中间名1')
    middle_name2 = db.Column(db.String(100), info='中间名2')
    last_name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='姓')
    gender = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='性别. -1 未知; 0 男; 1: 女')
    nationality = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='国籍')
    ID_Type = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='证件类型，全部all,护照passport，身份证idcard，驾驶证drivinglicense')
    ID_Number = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='证件号码')
    id_expire_date = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='证件到期日')
    birthday = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='生日')
    telephone = db.Column(db.String(100), info='电话号码')
    telephone_verify = db.Column(db.String(10), server_default=db.FetchedValue(), info="'nonsupport','checked','unchecked'")
    front_photo = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='证件照正面')
    back_photo = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='证件照背面')
    handle_photo = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='手持证件照')
    employment_status = db.Column(db.String(50), server_default=db.FetchedValue(), info='在职状态')
    trades = db.Column(db.String(50), info='在职行业')
    position = db.Column(db.String(100), info='职位')
    company = db.Column(db.String(300), info='雇主/公司')
    company_country = db.Column(db.String(100), info='公司所在国家')
    company_province = db.Column(db.String(100), info='公司所在省份')
    company_city = db.Column(db.String(100), info='公司所在城市')
    company_street = db.Column(db.String(300), info='公司所在街道')
    company_home = db.Column(db.String(300), info='公司所在门牌号')
    company_postcode = db.Column(db.String(20), info='公司邮编')
    capital_source = db.Column(db.String(60), info='投资资金来源')
    capital_source_comment = db.Column(db.String(200), info='投资资金来源备注(用于其他保存)')
    year_income = db.Column(db.String(40), info='年收入')
    investment_amount = db.Column(db.String(60), info='预期投资金额')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前状态. =0 编辑中; =1 已提交')
    contact_country = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='联系人国家/地区')
    contact_province = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='联系人州/省')
    contact_city = db.Column(db.String(200), info='联系人城市')
    contact_postcode = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='联系人邮编')
    contact_street = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='联系人所在街道')
    contact_pouseNumber = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='联系人门牌号/公寓号')
    old = db.Column(db.Integer, info='是否是kyc老用不，0否，1是')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class UserKycOld(db.Model):
    __tablename__ = 'user_kyc_old'
    __table_args__ = (
        db.Index('IX_name', 'first_name', 'last_name'),
        db.Index('IX_certificate', 'certificate_country', 'type', 'number')
    )

    id = db.Column(db.Integer, primary_key=True)
    user_oid = db.Column(db.String(24), nullable=False)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    middle_name2 = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.Enum('female', 'male', 'unknown'), server_default=db.FetchedValue())
    birthday = db.Column(db.DateTime)
    birthday_char = db.Column(db.String(10))
    telephone = db.Column(db.String(20))
    telephone_verify = db.Column(db.Enum('nonsupport', 'checked', 'unchecked'), server_default=db.FetchedValue())
    residence_country = db.Column(db.String(30), info='现居住地')
    residence_province = db.Column(db.String(100))
    residence_city = db.Column(db.String(100))
    residence_subdistrict = db.Column(db.String(100))
    residence_home = db.Column(db.String(100))
    residence_postcode = db.Column(db.String(20))
    normal_submit_status = db.Column(db.Enum('unsubmitted', 'submitted', 'resubmitted'), server_default=db.FetchedValue())
    normal_fail_reason = db.Column(db.Text)
    type = db.Column(db.Enum('passport', 'idcard', 'drivinglicense'), server_default=db.FetchedValue(), info='证件类型')
    number = db.Column(db.String(50))
    expiry_date = db.Column(db.DateTime)
    expiry_date_char = db.Column(db.String(10))
    same_area = db.Column(db.SmallInteger)
    certificate_country = db.Column(db.String(30), info='证件地址')
    certificate_province = db.Column(db.String(50))
    certificate_city = db.Column(db.String(50))
    certificate_subdistrict = db.Column(db.String(50))
    certificate_home = db.Column(db.String(50))
    certificate_postcode = db.Column(db.String(20))
    front_photo = db.Column(db.String(200))
    back_photo = db.Column(db.String(200))
    handle_photo = db.Column(db.String(200))
    address_photo = db.Column(db.String(200))
    certificate_submit_status = db.Column(db.Enum('unsubmitted', 'submitted', 'resubmitted'), server_default=db.FetchedValue())
    certificate_fail_reason = db.Column(db.Text)
    employment_status = db.Column(db.String(50), server_default=db.FetchedValue(), info='在职状态')
    trades = db.Column(db.String(50), info='在职行业')
    position = db.Column(db.String(100))
    company = db.Column(db.String(200))
    company_country = db.Column(db.String(30))
    company_city = db.Column(db.String(100), server_default=db.FetchedValue())
    company_province = db.Column(db.String(100))
    company_subdistrict = db.Column(db.String(100))
    company_home = db.Column(db.String(100))
    company_postcode = db.Column(db.String(20))
    capital_source = db.Column(db.String(60))
    capital_source_comment = db.Column(db.String(200))
    year_income = db.Column(db.String(40))
    investment_amount = db.Column(db.String(60))
    capital_submit_status = db.Column(db.Enum('unsubmitted', 'submitted', 'resubmitted'), server_default=db.FetchedValue())
    capital_fail_reason = db.Column(db.Text)
    created_at = db.Column(db.DateTime, index=True)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    isold = db.Column(db.SmallInteger, index=True, server_default=db.FetchedValue())
    submit_status = db.Column(db.Enum('unsubmitted', 'submitted', 'resubmitted'), server_default=db.FetchedValue())
    verify_status = db.Column(db.Enum('first_trial_fail', 'first_trial_pass', 'retrial_fail', 'retrial_pass', 'spot_check_pass', 'spot_check_fail', 'unchecked'), server_default=db.FetchedValue())
    verify_user = db.Column(db.String(24))
    verify_at = db.Column(db.DateTime)
    source = db.Column(db.String(10), info='提交来源：web,android,ios')



class UserKycRegionCode(db.Model):
    __tablename__ = 'user_kyc_region_codes'

    id = db.Column(db.String(24), primary_key=True)
    countryId = db.Column(db.String(20))
    country_name = db.Column(db.String(50))
    region_code = db.Column(db.String(20))
    iso_alpha2 = db.Column(db.String(20))
    iso_alpha3 = db.Column(db.String(20))



class UserLevel(db.Model):
    __tablename__ = 'user_level'

    id = db.Column(db.String(32), primary_key=True, info='主键id')
    user_id = db.Column(db.String(24), nullable=False, index=True, info='用户id')
    level = db.Column(db.SmallInteger, nullable=False, index=True, info='当日手续费等级')
    custom_level = db.Column(db.SmallInteger, nullable=False, info='自定义等级')
    statistics_date = db.Column(db.Date, nullable=False, index=True, info='统计日期，格式 yyyy-MM-dd')
    trade_amount = db.Column(db.Numeric(38, 20), nullable=False, info='现货30日交易量折合BTC数量')
    hold_amount = db.Column(db.Numeric(38, 20), nullable=False, info='近30天平均kcs持仓量')
    min_amount = db.Column(db.Numeric(38, 20), server_default=db.FetchedValue(), info='kucoin、kumex过去30天最低持仓总资产(BTC)')
    effective_end_time = db.Column(db.DateTime, info='vip到期日期')
    custom_end_time = db.Column(db.DateTime, info='自定义等级过期时间')
    contract_trade_amount = db.Column(db.Numeric(38, 20), server_default=db.FetchedValue(), info='期货近30天累计交易额')
    contract_min_hold_amount = db.Column(db.Numeric(38, 20), server_default=db.FetchedValue(), info='近30天kcs最小持仓')
    domain_id = db.Column(db.String(24), info='租户id')
    created_at = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')



class UserLevelCustom(db.Model):
    __tablename__ = 'user_level_custom'

    id = db.Column(db.String(24), primary_key=True, info='主键')
    user_id = db.Column(db.String(24), nullable=False, unique=True, info='用户ID')
    level = db.Column(db.SmallInteger, nullable=False, index=True, info='手续费等级')
    expire_at = db.Column(db.DateTime, nullable=False, info='过期时间')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class UserMemo(db.Model):
    __tablename__ = 'user_memo'

    id = db.Column(db.Integer, primary_key=True, info='id')
    user_id = db.Column(db.String(24), nullable=False, index=True, info='用户ID')
    memo = db.Column(db.String(1024), nullable=False, info='备注信息')
    operator = db.Column(db.String(24), nullable=False, info='添加人员')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    created_at = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class UserMemoCopy1(db.Model):
    __tablename__ = 'user_memo_copy1'

    id = db.Column(db.Integer, primary_key=True, info='id')
    user_id = db.Column(db.String(24), nullable=False, index=True, info='用户ID')
    memo = db.Column(db.String(1024), nullable=False, info='备注信息')
    operator = db.Column(db.String(24), nullable=False, info='添加人员')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    created_at = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class UserOperationApply(db.Model):
    __tablename__ = 'user_operation_apply'

    id = db.Column(db.String(24), primary_key=True)
    user_id = db.Column(db.String(24), nullable=False, index=True, info='用户ID')
    operation = db.Column(db.String(32), info='UNBIND_G2FA、UNFORBIDDEN')
    front_pic = db.Column(db.String(64), info='证件照正面')
    back_pic = db.Column(db.String(64), info='证件照背面')
    hand_pic = db.Column(db.String(64), info='手持证件照')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='0-处理中、1-同意、2-拒绝')
    remark = db.Column(db.String(256), info='备注')
    refuse_reason = db.Column(db.String(64), info='DATE_NOT_MATCH、FACE_NOT_MATCH、PIC_TYPE_WRONG、PIC_FUZZY')
    created_at = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class UserRegisterChannel(db.Model):
    __tablename__ = 'user_register_channel'
    __table_args__ = (
        db.Index('ids-source_campaign_medium', 'utm_source', 'utm_campaign', 'utm_medium'),
    )

    id = db.Column(db.String(24), primary_key=True, info='渠道主键')
    utm_source = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='来源')
    utm_campaign = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='活动')
    utm_medium = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='媒介')
    name = db.Column(db.String(128), nullable=False, info='渠道名称')
    type = db.Column(db.Integer, nullable=False, info='渠道类型 1 为注册页 2为首页 3为自定义')
    url = db.Column(db.String(512), nullable=False, info='跳转URL')
    operator = db.Column(db.String(64), nullable=False, info='创建人')
    effective_days = db.Column(db.Integer, info='有效天数')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='渠道状态 0可用 1不可用')



class UserSecurityMethod(db.Model):
    __tablename__ = 'user_security_method'
    __table_args__ = (
        db.Index('idx-user_id-method-deleted', 'user_id', 'method', 'deleted'),
        db.Index('idx-user_id-method-domain_id', 'user_id', 'method', 'domain_id')
    )

    id = db.Column(db.String(24), primary_key=True, info='id')
    domain_id = db.Column(db.String(10), nullable=False, info='租户ID')
    user_id = db.Column(db.String(24), nullable=False, info='用户id')
    method = db.Column(db.String(32), nullable=False, info='方式')
    value = db.Column(db.String(512), nullable=False, info='方法值')
    deleted = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    deleted_at = db.Column(db.DateTime, info='删除时间')



class UserTracking(db.Model):
    __tablename__ = 'user_tracking'
    __table_args__ = (
        db.Index('idx-user_id-channel_id', 'user_id', 'channel_id'),
    )

    id = db.Column(db.String(24), primary_key=True, server_default=db.FetchedValue())
    user_id = db.Column(db.String(24), nullable=False, server_default=db.FetchedValue())
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='新用户注册1，老用户激活2')
    channel_id = db.Column(db.String(24))
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态，1-可用 0-失效')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class UserVip(db.Model):
    __tablename__ = 'user_vip'

    id = db.Column(db.String(24), primary_key=True, info='id')
    user_id = db.Column(db.String(24), nullable=False, unique=True, info='用户id')
    vip_level = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='vip等级')
    account_manager = db.Column(db.String(24), nullable=False, server_default=db.FetchedValue(), info='客户经理')
    contact_info = db.Column(db.String(2048), info='客户经理联系方式,JSON格式')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class WorkOrder(db.Model):
    __tablename__ = 'work_order'

    id = db.Column(db.String(24), primary_key=True)
    user_id = db.Column(db.String(24))
    email = db.Column(db.String(50, 'utf8mb4_unicode_ci'), info='邮箱')
    work_order_number = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='工单号')
    biz_type = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='业务类型')
    info = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='其它信息')
    front_photo = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='正面证件照')
    back_photo = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='背面证件照')
    handle_photo = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='手持证件照')
    video = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='视频')
    status = db.Column(db.String(20, 'utf8mb4_unicode_ci'), info='状态')
    operator = db.Column(db.String(50, 'utf8mb4_unicode_ci'), info='操作人')
    remarks = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='备注')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
