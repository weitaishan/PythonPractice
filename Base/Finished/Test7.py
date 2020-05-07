# *_*coding:utf-8 *_*

'''
题目：将一个列表的数据复制到另一个列表中。


'''


#方法一
list1 = [1,2,3,4,5,6,7,8]
list2 = []
for i in list1:
    list2.append(i)
print(list2)

#方法二
list1 = [1,2,3,4,5,6,7,8,]
list2 = list1[:]
print(list2)