# *_*coding:utf-8 *_*

'''
题目：求100之内的素数。

质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数。1不是素数。

'''
import math
list = []
zs = 1
for i in range(2, 101):
    if i % 2 == 0:
        continue
    a = math.sqrt(i)
    b = int(a) + 1
    for j in range(2, b):
        if i % j == 0:
            zs = 0
    if zs == 1:
        list.append(i)
    zs = 1
print(list)

'''
[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''