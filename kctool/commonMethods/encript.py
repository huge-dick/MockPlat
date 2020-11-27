# encoding=utf-8
# @Author : wangjie
# @Time : 2020/6/16 下午7:53
# -*- coding:utf-8 -*-
import base64,time
import binascii

import pyDes

#密匙
ACCOUNT_ENCRIPT_KEY = "I4wXRxIj"
# key="l8ADSmlh"
#ip_record加密ip
# key = "!@#$%^14"

def encript_account(account):
    """
    DES 解密
    :param account: 需要加密的帐户（邮箱或手机号）
    :return:  加密后的数据
    """

    kucoin_dec = pyDes.des(ACCOUNT_ENCRIPT_KEY,pyDes.ECB,padmode= pyDes.PAD_PKCS5)
    ciphertext = kucoin_dec.encrypt(account)
    code = base64.b64encode(ciphertext)
    return code.decode()

def descrypt_account(data):
    """
    DES 解密
    :param data: 加密后的字符串
    :return:  解密后的字符串
    """
    kucoin_dec = pyDes.des(ACCOUNT_ENCRIPT_KEY, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
    de = kucoin_dec.decrypt(binascii.a2b_base64(data), padmode=pyDes.PAD_PKCS5)
    return de.decode()



if __name__ == '__main__':
    account='cool.liang@kupogroup.com'
    a=encript_account(account)
    print(a)
    print(descrypt_account('DEKpvWuoLSnPscBQI1ReRGfcpVB6Ut8kgb5tZovMdlY='))

