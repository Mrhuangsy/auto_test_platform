#-*- coding:utf-8 -*-
'''
filename : verify.py
create by : 
create time : 2021/07/01
introduce : 密码加密与验证等
'''

from passlib.apps import custom_app_context as pwd_context
import base64,hmac,time
from db_fixture.redis_db import redis_db

def hash_password(password):
    '''密码加密'''
    return pwd_context.encrypt(password)

def verify_password(input_pwd,db_pwd):
    '''密文比较'''
    return pwd_context.verify(input_pwd,db_pwd)

def generate_token(key,value):
    '''生成token'''
    ts_byte = str(time.time()).encode("utf-8")
    token = hmac.new(value.encode("utf-8"),ts_byte,'sha1').hexdigest()
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    redis_db.handle_redis_access(key,b64_token) # 缓存至redis
    return b64_token

def certify_token(key,token):
    '''验证token'''
    tmp_token = redis_db.handle_redis_access(key)
    if tmp_token:
        if tmp_token != token:
            return False
        return True
    else:
        return False
