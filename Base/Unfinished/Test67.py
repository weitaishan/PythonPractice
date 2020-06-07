# *_*coding:utf-8 *_*

'''
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。



'''

list = [12, 6, 90, 57, 7, 99, 239, 81]
a = 0
b = 0
# 找最小数的索引
for i in range(0, len(list)-1):
    if list[a] > list[i+1]:
        a = i+1
# 找最大数的索引
for j in range(0, len(list)-1):
    if list[b] < list[j+1]:
        b = j+1
# 将最小的数与最后一个元素交换
x = list[a]
list[a] = list[-1]
list[-1] = x
# 将最大的数与第一个元素交换
y = list[b]
list[b] = list[0]
list[0] = y
print(list)