# *_*coding:utf-8 *_*

'''
题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。
'''
import time

for i in range(0,11):
    print("当前日期：%s" % time.ctime())
    time.sleep(1)
