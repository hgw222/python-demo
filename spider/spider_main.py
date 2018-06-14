#! /usr/bin/env python
# -*- coding: utf-8 -*-

import url_manager, html_downloader, html_parser, html_output


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutPuter()

    def craw(self, root_url):  # 爬虫的调度程序
        count = 1  # 记录当前爬的第几个url
        # 入口 url 添加到 url 管理器
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():  # 有待取去url
            try:

                new_url = self.urls.get_new_url()  # 获取最新的url
                print('craw %d :%s' % (count, new_url))
                # 启动下载器并存储
                html_cont = self.downloader.downlad(new_url)  # 下载url
                new_urls, new_data = self.parser.paser(new_url, html_cont)  # 得到新的url和数据
                self.urls.add_new_urls(new_urls)  # 添加到url管理器
                self.output.collect_data(new_data)  # 收集数据

                if count == 100:
                    break
                count += 1
            except Exception as error:
                print(error)

                # 输出收集好的数据
        self.output.output_html()

if __name__ == "__main__":   # main函数   __name__中间是两个下划线  main函数不能写错！！！！
    root_url="https://baike.baidu.com/item/Python/407313.html"  # 入口地址
    obj_spider = SpiderMain()  # 创建一个spider
    obj_spider.craw(root_url)   #  调用spider的craw方法，启动爬虫
