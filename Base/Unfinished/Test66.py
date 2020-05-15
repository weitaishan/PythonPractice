# *_*coding:utf-8 *_*

'''
题目：输入3个数a,b,c，按大小顺序输出。　　　


'''

def compare(a, b, c):
    if a > b:
        x = a
        a = b
        b = x
    if a > c:
        y = a
        a = c
        c = y
    if b > c:
        z = b
        b = c
        c = z
    print(c, b, a)    #从大到小排序
    print(a, b, c)    #从小到大排序

compare(34, 5, 78)