# *_*coding:utf-8 *_*

'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


'''
'''
分析：该题想要使用递归函数调用，来实现反顺序打印，就只有从索引入手。而且索引和递归函数必须是相反的才能实现。
列表有5个字符，那么列表的索引是0~4
f(1)=4   f(2)=3    f(3)=2   f(4)=1  f(5)=0     即：f(n)=f(n-1)-1   n>1

'''

def index(n):
    if n <= 1:
        return 4
    return index(n-1) - 1

list = list(input("请输入5个字符： "))
for i in range(1, len(list)+1):
    print(list[index(i)])