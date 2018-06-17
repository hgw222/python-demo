#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("10.26.117.65", "user_pms2", "R5qDx8VEx2JZHdNPzbeF", "db_pms2")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM zt_user WHERE id < '%d'" % (10)

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      account = row[2]
      role = row[4]
      email = row[12]
      #  # 打印结果
      # print "账号：",account
      print "账号=%s,真实姓名=%s,邮箱=%s" % (account, role, email)
      # print "%s-%s-%s" % (account,role,realname)
except:
   print ("Error: unable to fetch data")


# 关闭数据库连接
db.close()