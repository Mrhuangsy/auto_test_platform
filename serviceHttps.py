#-*- coding:utf-8 -*-
'''
filename : serviceHttp.py
create by : 
create time : 2021/07/01
introduce : https协议的接口服务，有证书签名验证
'''
import json
from flask import request,Flask,jsonify

server = Flask(__name__) #启动一个服务，把当前的python文件当作一个服务

@server.route('/fuck',methods=['get','post'])
def fuck():
    return "hehe"

@server.route('/xiaohuang',methods=['get','post']) #默认是get请求，可以不写或同时写get post
def xiaohuang():
    print("in!!")
    result = {
                "code":200,
                "data":"server_utter",
                "error":""
            }
    # try:
    #     if request.method == 'GET':
    #         utter = request.args.get('utter')
    #         NowTime = request.args.get('nowtime')
    #         session_id = request.args.get('session_id')
    #     elif request.method == 'POST':
    #         data = request.get_json()
    #         utter = data.get('utter')
    #         NowTime = data.get('nowtime')
    #         session_id = data.get('session_id')

    #     server_utter = plan.make_response(utter,NowTime,session_id)
    #     result = {
    #             "code":200,
    #             "data":server_utter,
    #             "error":""
    #         }
    #     print("取得结果成功：",result)
    # except Exception as e:
    #     result = {
    #             "code":400,
    #             "data":"",
    #             "error":str(e)
    #         }
    #     print("取得结果失败：",result)
    return jsonify(result)

server.run(host='0.0.0.0',port=8000,debug=True,ssl_context='adhoc')
