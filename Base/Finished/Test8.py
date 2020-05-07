# *_*coding:utf-8 *_*

'''
题目：输出 9*9 乘法口诀表。


'''
list = [1,2,3,4,5,6,7,8,9]
for i in list:
    for j in range(1,i+1):
        print("%d*%d=%d "%(j,i,i*j),end=" ")
    print("\n")