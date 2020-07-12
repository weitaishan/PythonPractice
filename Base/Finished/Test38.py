# *_*coding:utf-8 *_*

'''
题目：求一个3*3矩阵主对角线元素之和。


'''

X = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
A = 0
B = 0
for i in range(0, len(X)):
    A += X[i][i]
    B += X[i][2-i]
print(A)
print(B)
