# *_*coding:utf-8 *_*

'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。


'''
import math
n = int(input("请输入一个正整数： "))
a = int(input("请输入一个数字： "))
result = 0
sum = 0
for i in range(0, n):
    result += a * math.pow(10, i)
    sum += result
print(sum)

