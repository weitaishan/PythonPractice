# *_*coding:utf-8 *_*

'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？


'''

'''
2 2 4 6 10 16 26 42 ……
是个斐波那契数列：f(n) = f(n-1) + f(n-2)  n > 2

'''
month = int(input("请输入一个月数： "))
def rabbit(n):
    if n <= 2:
        return 2
    return rabbit(n-1) + rabbit(n-2)
print(rabbit(month))





'''
2 2 2 4 6 8 12 18 26 38 ……
规律：f(n) = f(n-1) + f(n-3)  n>3
使用递归函数解决该问题


# month = int(input("请输入一个月数： "))
def rabbit(n):
    if n <= 3:
        return 2
    return rabbit(n-1) + rabbit(n-3)

for i in range(0,10):
    print(i,rabbit(i))
'''





'''

2,2,2       1~3个月   1       f(1) = 2
4,4,4       4~6个月   2       f(2) = 4
8,8,8       7~9个月   3       f(3) = 8
16,16,16    10~12个月 4       f(4) = 16
32,32,32    13~15个月 5       f(5) = 32
64,64,64    16~18个月 6       f(6) = 64
那么n月之后，兔子的数量为：f(n) =2*f(n-1) 


import math
month = int(input("请输入一个月数： "))
a = math.ceil(month/3)
print(a)
def rabit(n):
    if n < 2:
        return 1
    return 2*rabit(n-1)

print(rabit(a))

'''
