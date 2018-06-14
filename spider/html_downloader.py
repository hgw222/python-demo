#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib

# 下载器代码——下载网页
class HtmlDownloader(object):

    def downlad(self, new_url):
        if new_url is None:
            return None

        response = urllib.request.urlopen(new_url)
        if response.getcode() != 200:
            return None
        return response.read().decode('utf-8')