#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

def download_image():
    """
        demo：下载图片
    """
    url = "http://www.mf08s.com/pic/allimg/170715/2026201503-2.jpg"
    response = requests.get(url)

    print response.status_code, response.reason
    print response.headers
    # b = response.content
    # with open('/Users/oscar.han/python-www/oscar/001.jpg', 'wb') as f:
    #     f.write(b)

if __name__ == '__main__':
    download_image()
