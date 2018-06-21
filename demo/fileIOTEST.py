#!/usr/bin/python
# -*- coding: UTF-8 -*-

#1、写入
# fo = open("foo.txt", "w")
# fo.write("hello,this is hangaowen !")

#2、读取
fo = open("foo.txt","r+")
str = fo.read(10)
print "读取的字符串是：",str

# 查找当前位置
position = fo.tell()
print "当前文件位置 : ", position
#关闭打开的文件
fo.close()