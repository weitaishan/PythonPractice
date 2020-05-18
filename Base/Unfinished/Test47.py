# *_*coding:utf-8 *_*

'''
题目：两个变量值互换。

封装成一个函数方便调用 exchange(x,y)
'''

def exchange(x, y):
    a = x
    x = y
    y = a
    print(x, y)

exchange(123, '你好')