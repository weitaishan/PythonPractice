# *_*coding:utf-8 *_*
from small_project.baike_spider import html_downloader, html_parser, html_outputer, url_manager

class SpiderMain(object):
    #这里初始化模块
    def __init__(self):
        pass

    #这里开始爬取链接
    def craw(self, root_url):
        print(root_url)
        pass


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    spider = SpiderMain()
    spider.craw(root_url)