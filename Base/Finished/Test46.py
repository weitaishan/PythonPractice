# *_*coding:utf-8 *_*

'''
题目：求输入数字的平方，如果平方运算后小于 50 则退出。


'''



result = 0
while result < 50:
    number = int(input("请输入一个数字： "))
    result = number * number
    print(result)