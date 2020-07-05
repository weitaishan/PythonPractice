# *_*coding:utf-8 *_*

'''
题目：取一个整数a从右端开始的4〜7位。



'''

def number(num):
    a = str(num)
    list1 = list(a)
    print(list1[-7:-3])
number(14869785758)   #  ['9', '7', '8', '5']


