# *_*coding:utf-8 *_*

'''
题目：统计 1 到 100 之和。


'''

def sum(n):
    result = 0
    if n % 2 == 0:
        result = (n+1) * (n//2)
    else:
        result = (n+1)*(n//2) + (n//2 + 1)
    print(result)

def sumWithFor(n):
    result = 0
    for i in range(1, n+1):
        result += i
    print(result)
sum(101)
sumWithFor(101)
