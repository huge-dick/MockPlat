# encoding=utf-8
# @Author : wangjie
# @Time : 2020/10/12 下午2:09
#kucoin前端加密
import base64
import datetime
import hashlib
import hmac
import time


def md5_password(password):
    md5_data = password
    for i in range(0, 3):
        md5_data = "_kucoin_" + md5_data + "_kucoin_"
        md5_source = md5_data.encode('utf-8')
        md5_data = hashlib.md5(md5_source).hexdigest()
    return md5_data

#生成google验证码
def byte_secret(secret):
    missing_padding = len(secret) % 8
    if missing_padding != 0:
        secret += '=' * (8 - missing_padding)
    return base64.b32decode(secret, casefold=True)

def int_to_bytestring(i, padding=8):
    result = bytearray()
    while i != 0:
        result.append(i & 0xFF)
        i >>= 8
    return bytes(bytearray(reversed(result)).rjust(padding, b'\0'))

#根据约定的密钥计算当前动态密码
def getGoogleCheckCode(secret):
    for_time = datetime.datetime.now()
    i = time.mktime(for_time.timetuple())
    input =  int(i/30)
    digest = hashlib.sha1
    digits = 6
    if input < 0:
        raise ValueError('input must be positive integer')
    hasher = hmac.new(byte_secret(secret),int_to_bytestring(input),digest)
    hmac_hash = bytearray(hasher.digest())
    offset = hmac_hash[-1] & 0xf
    code = ((hmac_hash[offset] & 0x7f) << 24 |
            (hmac_hash[offset + 1] & 0xff) << 16 |
            (hmac_hash[offset + 2] & 0xff) << 8 |
            (hmac_hash[offset + 3] & 0xff))
    str_code = str(code % 10 ** digits)
    while len(str_code) < digits:
        str_code = '0' + str_code
    return str_code

if __name__ == '__main__':
    while True:
        print(getGoogleCheckCode('X77XCDFMM6FEFY3A'))
        time.sleep(1)