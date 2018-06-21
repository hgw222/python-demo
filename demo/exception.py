#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

number = random.randint(1, 100)

while True:
    try:
        guess = int(raw_input("enter 1 到 100："))
    except ValueError, e:
        print "enter 1 到 100："
        continue

    if guess > number:
        print "guess bigger: ",guess
    elif guess < number:
        print "guess smaller: ", guess
    else:
        print "guess ok ,game over!"
        break
    print "\n"