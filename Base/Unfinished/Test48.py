# *_*coding:utf-8 *_*

'''
题目：数字比较。

比较2个数字的大小
'''


def compare(x, y):
    if x - y > 0:
        print("%d大于%d" % (x, y))
    elif x - y == 0:
        print("%d等于%d" % (x, y))
    else:
        print("%d小于%d" % (x, y))

compare(1, 3)