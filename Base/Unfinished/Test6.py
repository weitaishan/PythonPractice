# *_*coding:utf-8 *_*

'''
题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：

F1 = 1     (n=1)
F2 = 1     (n=2)
Fn = F[n-1]+ F[n-2](n=>3)
'''

'''
输入一个正整数，输出其对应的斐波那契数列

'''

number = int(input("请随意输入一个大于等于2的正整数： "))
# n = 0
# list = []
# for i in range(0, number+1):
#     list.append(i)
#     if i == number:
#         print(list)    #将输入的整数从0打印为一个列表
# for index in range(2, number+1):


# a = 1
# b = 1
# list = [a]
# for i in range(number-1):
#     temp = a
#     a = b
#     b = temp + b
#     list.append(a)
#
# # print(list)
#
# print(a)

# Fn = F[n-1]+ F[n-2](n=>3)


def feb(n):
    print(n)
    if n < 3:
        return  1
    return feb(n-1) + feb(n-2)


print(feb(number))