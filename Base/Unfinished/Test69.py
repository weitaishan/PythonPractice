# *_*coding:utf-8 *_*

'''
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。



'''


def leave(n):
    list = []
    x = n % 3
    for i in range(1, n+1):
        list.append(i)
    while n > 2:
        for j in range(0, n):
            if (j+1) % 3 == 0:
                list.pop(j)
        n = len(list)
    print(list)

leave(5)