# *_*coding:utf-8 *_*

'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。


'''

'''
分析：分解质因数
最终可以分解为素数的乘积

'''
import math
number = int(input("请输入一个正整数: "))
n = number
a = math.sqrt(number)
b = int(a) + 1
result = str(number) + "="
list = []
while number>1:
    for i in range(2, b):
        if number % i == 0:
            result = result + str(i) + "*"
            list.append(str(i))
            number = number // i
            break
print(result.strip('*'))
print(str(n) + '=' + '*'.join(list))
# print("%d = %d"% (number, ))

