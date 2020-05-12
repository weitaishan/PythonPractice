# *_*coding:utf-8 *_*

'''
题目：判断101-200之间有多少个素数，并输出所有素数。


'''

#方法三
'''
思考：写出一定数量的素数，可发现个位数的素数有：1、2、3、5、7，但是多位数的素数都是以1、3、7、9结尾。
所以可以先排除偶数和5的倍数的非个位数。进行取模运算的时候，不需要将所有小于的数都除一遍。
'''
import math
list = []
zs = 1
for i in range(101, 201):
    if i % 2 == 0 or i % 5 == 0:
        continue
    a = math.sqrt(i)
    b = int(a) + 1
    for j in range(2, b):
        if i % j == 0:
            zs = 0
    if zs == 1:
        list.append(i)
    zs = 1
print(list)



'''
方法二：

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


'''
方法一：

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