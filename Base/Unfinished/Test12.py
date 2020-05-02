# *_*coding:utf-8 *_*

'''
题目：判断101-200之间有多少个素数，并输出所有素数。


'''
list = []
zs = 1
for i in range(101, 201):
    for j in range(2, i):
        if i%j == 0:
            zs = 0
    if zs == 1:
        list.append(i)
    zs = 1
print(list)







'''
list1 = []
list2 = []
for i in range(101, 201):
    for j in range(2, i):
        a = i % j
        list1.append(a)
    if 0 not in list1:
        list2.append(i)
    list1 = []

print(list2)
'''