#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import pymysql

# 打开数据库连接
db = pymysql.connect("10.26.117.65", "user_pms2", "R5qDx8VEx2JZHdNPzbeF", "db_pms2")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# SQL 插入语句
sql = """INSERT INTO zt_feedback(iteration_id,content, uid, create_date)VALUES ('3', '小米的ad阿萨德', 63, date_time)"""
#对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务

try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()