#-*- coding:utf-8 -*-
'''
filename : http_return_type.py
create by : 
create time : 2021/07/02
introduce : 接口返回的数据模板定义
'''

from flask import jsonify

def success(msg = None):
    result = {
                "code":200,
                "data":msg and msg or "请求成功",
                "error":"OK"
            }
    return jsonify(result)

def faliure(msg = None):
    result = {
                "code":400,
                "data":msg and msg or "请求失败",
                "error":"请求失败,{}".format(msg)
            }
    return jsonify(result)

def error(msg = None):
    result = {
                "code":500,
                "data":msg and msg or "系统错误",
                "error":"系统错误,{}".format(msg)
            }
    return jsonify(result)