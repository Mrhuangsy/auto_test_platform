#-*- coding:utf-8 -*-
'''
filename : util.py
create by : 
create time : 2021/07/01
introduce : 工具
'''
import random,time
import snowflake.client
from hashlib import md5

def get_snowflake_uuid():
    '''获取雪花算法id，需先后台启动雪花算法程序，cmd输入：snowflake_start_server.exe'''
    guid = snowflake.client.get_guid()
    return guid

def get_session_id(value=None):
    '''生成sessionID'''
    if value is None:
        value = str(time.time()).encode('utf-8')
    return md5(value).hexdigest()

if __name__ == '__main__':
    # for i in range(10):
    #     print(random.randint(0, 10))
    #     print(get_snowflake_uuid())
    print(get_session_id())
    