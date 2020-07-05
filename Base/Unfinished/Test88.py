# *_*coding:utf-8 *_*

'''
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。



'''
import random
def number(n):      # n为读取n个数
    for i in range(1, n+1):
        a = random.randint(1, 50)
        print(a)
        print('*' * a)
number(3)