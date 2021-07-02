#-*- coding:utf-8 -*-
'''
filename : redis_db.py
create by : 
create time : 2021/07/01
introduce : redis数据库存取操作类
'''
import redis
from utils.readConfig import readConfig as cf

# ======== Reading db_config.ini setting ===========
REDIS_HOST = cf.get_redis("host")
REDIS_PORT = cf.get_redis("port")
REDIS_PASSWD = cf.get_redis("password")
EXPIRE_TIME = cf.get_redis("expire_time")
# ======== MySql base operating ===================

class RedisDb():
    def __init__(self):
        # 建立redis数据库连接
        self.r = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWD,
            decode_responses=True # get()时 能够得到字符串类型数据
        )
    
    def handle_redis_access(self,key,value=None):
        if value: # 如果value值非空，则执行存储,EXPIRE_TIME代表失效时间
            self.r.set(key, value,ex=EXPIRE_TIME)
        else: # 如果value为空，则执行取值
            redis_value = self.r.get(key)
            return redis_value

redis_db = RedisDb()