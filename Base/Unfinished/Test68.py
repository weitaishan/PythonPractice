# *_*coding:utf-8 *_*

'''
题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数



'''
n = int(input("请输入一个整数： "))
list = []
a = n
for i in range(1, n + 1):
    list.append(i)
print(list)
'''
while a >= 2:
    for j in range(0, a):
        if j % 3 == 0:
            list.pop(j)
    a = len(list)
print(list)
'''