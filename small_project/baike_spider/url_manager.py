# *_*coding:utf-8 *_*

#本类是一个Url的管理器
class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #添加新的url到集合中，单个添加
    def add_new_url(self, url):
        pass

    #添加新的url到集合中，批量添加
    def add_new_urls(self, urls):
        pass

    #判断是否是添加过的url
    def has_new_url(self):
        pass

    #获取新的url
    def get_new_url(self):
        pass