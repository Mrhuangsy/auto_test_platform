# -*- coding:utf-8 -*-
'''
filename : register_login.py
create by : 
create time : 2021/07/02
introduce : 注册与登录操作类
'''
import time
from flask import request,Flask,jsonify
from db_fixture.redis_db import redis_db
from authentication import verify
from utils import util,http_return_type as ht

class RegisterAndLogin:

    def __init__(self,db):
        self.db = db
    
    def register(self,data):
        '''注册'''
        try:
            user_data = {
                "t_id":util.get_snowflake_uuid(),# 获取雪花算法ID
                "userid":data.get('username'),
                "userpswd":verify.hash_password(data.get('password')),
                "username":data.get('realname'),
                "usermob":data.get('mobile')
            }
            token = verify.generate_token(user_data["t_id"], user_data["userid"]) # 获取token

            reuser = self.db.select("prod_system_user",{"userid":user_data["userid"]},"t_id")
            if reuser :
                return ht.faliure("用户{}已经存在".format(user_data["userid"]))
            remobile = self.db.select("prod_system_user",{"usermob":user_data["usermob"]},"t_id")
            if remobile :
                return ht.faliure("手机号{}已被注册".format(user_data["usermob"]))

            self.db.insert("prod_system_user", user_data)
            self.db.close()
        except Exception as e:
            self.db.rollback()
            self.db.close()
            return ht.error(str(e))
        return ht.success({ "token":token })

    def login(self,data):
        username = data.get("username")
        pwd = data.get("password")
        user_info = self.db.select("prod_system_user",{"userid":username},"t_id,userid,userpswd")
        if user_info:
            t_id = user_info[0].get("t_id")
            userpswd = user_info[0].get("userpswd")
            if not verify.verify_password(pwd, userpswd):
                return ht.faliure("密码错误")
            token = verify.generate_token(t_id, username)
            return ht.success({"token":token})
        else:
            return ht.faliure("用户名不存在")