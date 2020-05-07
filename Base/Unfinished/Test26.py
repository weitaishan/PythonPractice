# *_*coding:utf-8 *_*

'''
题目：利用递归方法求5!。


'''

'''
分析：5！= 5*4*3*2*1 = 1*2*3*4*5      f(1)=1  f(n)=f(n-1)+1
'''
# def factorial(n):
#     if n <= 1:
#         return 1
#     return factorial(n-1) + 1
#
# result = 1
# number = int(input("请输入一个正整数： "))
# for i in range(1, number+1):
#     result *= factorial(i)
# print(result)


#方法一：      分析：f(1)=1    f(n)=f(n+1)*n    n>1
'''
def factorial(n):
    if n <= 1:
        return 1
    return factorial(n-1)*n
print(factorial(5))
'''


#方法二：
number = int(input("请输入一个正整数： "))
result = 1
for i in range(1, number+1):
    result *= i
print(result)