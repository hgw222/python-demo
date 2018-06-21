#!/usr/bin/python
# -*- coding: UTF-8 -*-

#闭包函数
def w1(func):
    def inner():
        print('...验证权限...')
        func()

    return inner

@w1
def f1():
    print('f1 called')

@w1
def f2():
    print('f2 called')

# f1()
# f2()

def deco(func):
    def in_deco(x, y):
        print ('in deco')
        func(x, y)

    print('call deco')
    return in_deco

@deco
def bar(x, y):
    print ('in bar', x+y)

bar(1,2)

