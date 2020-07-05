# *_*coding:utf-8 *_*

'''
题目：将一个数组逆序输出。

使用2种方法写出来
'''



# 方法一：reserve方法
list2 = [2, 5, 22, 13, 99, 87]
list2.reverse()
print(list2)     #  [87, 99, 13, 22, 5, 2]


# 方法二，定义一个函数
def location(listData):
    list3 = []
    for i in range(0, len(listData)):
        list3.append(listData[len(listData)-1-i])
    print(list3)
location([2, 5, 22, 13, 99, 87])     #  [87, 99, 13, 22, 5, 2]

