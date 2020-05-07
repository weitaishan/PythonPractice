# *_*coding:utf-8 *_*

'''
题目：将一个列表的数据复制到另一个列表中。


'''

list1 = list(input("请输入你喜欢的任意数据： "))
list2 = []
for index in range(0,(len(list1)+1)):
    a = list1[index]
    list2.append(a)
print(list2)