# *_*coding:utf-8 *_*

import re
import urllib.parse
from  bs4 import BeautifulSoup

#本类是一个html内容的解析器，用于解析html中的内容
class HtmlParser(object):

    #公开方法，用BeautifulSoup去解析下载的url中的内容
    def parse(self, page_url, html_cont):
        pass

    #私有方法，获取新的url
    def _get_new_urls(self, page_url, soup):
        pass

    #私有方法，获取新的data
    def _get_new_data(self, page_url, soup):
        pass