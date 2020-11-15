# *_*coding:utf-8 *_*
#  from small_project.baike_spider import html_downloader, html_parser, html_outputer, url_manager

import urllib
import url_mannger,html_downloader,html_parser,pic_outputer    #这四个类会在后面进行创建


class SpiderMain(object):
    #这里初始化模块
    def __init__(self):
        self.urls = url_mannger.UrlMannger()    #创建一个url管理器实例对象
        self.downloader = html_downloader.HtmlDownloader()   #创建一个HTML下载器实例对象
        self.parser = html_parser.HtmlParser()    #创建一个HTML解析器实例对象
        self.outputer = pic_outputer.PicOutputer()    #创建一个图片输出实例对象

    #这里开始爬取链接
    def craw(self, root_url, keyword):         #将要访问的主链接URL和关键字传入craw方法
        # 将需要访问的url及想要搜索的关键字拼接成完整的访问地址
        data = {"word":keyword}                #将需要搜索的关键字转换为字典的形式传入
        encode.data = urllib.parse.urlencode(data)      #需要使用urllib.parse模块中的urlencode方法将字典构形式的参数序列化为url编码后的字符串（常用来构造get请求和post请求的参数）
        base_url = root_url + '&' + encode.data        #将需要访问的url及想要搜索的关键字合并为最终想要访问的地址

        # 下载HTML源码（需要用到urllib.request模块）
        response = self.downloader.download(base_url)

        #解析下载页面中图片链接
        new_urls = self.parser.parse(response)
        #将图片链接集放到url管理器中
        self.urls.add_new_urls(new_urls)
        #遍历下载url文件（使用while循环进行遍历）
        while


if __name__ == "__main__":
    root_url = "https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8"
    spider = SpiderMain()
    spider.craw(root_url)