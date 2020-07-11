# *_*coding:utf-8 *_*

'''
题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

程序分析：999999 / 13 = 76923。



'''

A = int(input("请随意输入一个奇数： "))
a = '9'
for i in range(1, 1000):
    if int(a*i) % A == 0:
        print(i)
        break



