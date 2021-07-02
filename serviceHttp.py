#-*- coding:utf-8 -*-
'''
filename : serviceHttp.py
create by : 
create time : 2021/07/01
introduce : http协议的接口服务
'''

import json,time
from flask import request,Flask,jsonify
from db_fixture.mysql_db import DB
from authentication import verify,register_login
from authentication.register_login import RegisterAndLogin
from utils import http_return_type as ht
from db_fixture.redis_db import redis_db

server = Flask(__name__) #启动一个服务，把当前的python文件当作一个服务
db = DB() #数据库连接


@server.route('/api/register',methods=['post'])
def register():
    data = request.get_json() # 获取请求数据
    _register = RegisterAndLogin(db)
    return _register.register(data)

@server.route('/api/login',methods=['post'])
def login():
    data = request.get_json()
    return jsonify("login")

@server.route('/api/getToken',methods=['post'])
def gettoken():
    return jsonify("none")

@server.route('/xiaohuang',methods=['get','post']) #默认是get请求，可以不写或同时写get post
def xiaohuang():
    print("in!!")
    result = {
                "code":200,
                "data":"server_utter",
                "error":""
            }
    return jsonify(result)

server.run(host='0.0.0.0',port=8000,debug=True)
