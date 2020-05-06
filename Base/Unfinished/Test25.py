# *_*coding:utf-8 *_*

'''
题目：求1+2!+3!+...+20!的和。
n!为n的阶乘。  n*(n-1)*(n-2)*……*1
'''
number = int(input("请输入一个正整数： "))
sum = 0
result = 1
for i in range(1, number+1):
    for j in range(1, i+1):
        result *= j
    sum += result
    result = 1
print(sum)
