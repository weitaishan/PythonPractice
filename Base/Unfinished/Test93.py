# *_*coding:utf-8 *_*

'''
题目：时间函数举例3。



'''
# 按照要求的格式输出当前本地时间：格式为：2020年6月28日 17时16分30秒
import time
now_time = time.localtime()
print(str(now_time.tm_year) + "年" + str(now_time.tm_mon) + "月" + str(now_time.tm_mday) + "日" + str(now_time.tm_hour) + "时" + str(now_time.tm_min) + "分" + str(now_time.tm_sec) + "秒")