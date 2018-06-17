#!/usr/bin/python
# -*- coding: UTF-8 -*-
from urllib import urlopen
import bs4
import re
import pymysql

resp = urlopen("https://baike.baidu.com/item/%E5%88%98%E5%BE%B7%E5%8D%8E/114923.html").read().decode("utf-8")

soup = bs4.BeautifulSoup(resp, "html.parser")

listUrls = soup.findAll("a", href=re.compile("^/item/"))

for url in listUrls:

    print url.get_text(), "<------>", url["href"]

# print(listUrls)

