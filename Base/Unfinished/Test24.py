# *_*coding:utf-8 *_*

'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
分子： f(1)=2   f(n) = f(n-1) + f(n-2)  n>2
分母： f(1)=2   f(n) = f(n-1) + f(n-2)   n>2

'''

result = 0
def number1(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    return number1(n-1) + number1(n-2)
def number2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return number2(n-1) + number2(n-2)
for i in range(1,4):
    result += number1(i)/number2(i)
print(result)