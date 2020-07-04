# *_*coding:utf-8 *_*

'''
题目：字符串日期转换为易读的日期格式。


nn
'''

import time
stime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(time.strptime(stime, "%Y-%m-%d %H:%M:%S"))
