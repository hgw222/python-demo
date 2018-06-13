#! /usr/bin/env python
# -*- coding: utf-8 -*-
import redis

# r = redis.Redis(host='10.10.2.14',port=6379)
# r = redis.StrictRedis(host="192.20.11.78", port=6379,db=0)
r = redis.StrictRedis(host="10.26.117.65", port=6380,db=0,password='wevnr25&8*(7dd')
r.set('name','jack')
print(r.get('name').decode())