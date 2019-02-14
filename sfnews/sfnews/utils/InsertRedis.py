# -*- coding: utf-8 -*-
import redis
"""
def inserintotc(str,type):
    try:
        r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    except:
        print('连接redis失败')
    else:
        if type == 1:
            r.lpush('content_urls', str)
"""

def inserintota(str):
    try:
        r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    except:
        print ('连接redis失败')
    else:
         r.lpush('content_urls', str)