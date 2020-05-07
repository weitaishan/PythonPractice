# *_*coding:utf-8 *_*

'''
题目：输出指定格式的日期。

程序分析：使用 datetime 模块。
'''




# 分析：打印时间格式为：2020-5-4 19:33
from datetime import datetime

print(datetime.now().timestamp())    #datetime转时间戳
print(datetime.now().strftime('%Y/%m/%d  %H:%M:%S'))
print(datetime.fromtimestamp(1699594842.843823))



'''
时间的表现形式：时间戳、字符串、datetime
熟悉之间的互相转换
datetime----字符串
datetime----时间戳
字符串-------时间戳
'''