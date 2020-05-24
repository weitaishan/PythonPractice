# *_*coding:utf-8 *_*

'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。


'''

# 方法一
# sortList = [0, 6, 7, 13, 14, 70, 78, 81, 89]
# number = int(input("请输入一个数： "))
# if number > sortList[-1]:
#     sortList.append(number)
# else:
#     for i in range(0, len(sortList)-1):
#         if number < sortList[i]:
#             sortList.insert(i, number)
#             break
# print(sortList)

# 方法二
# sortList = [0, 6, 7, 13, 14, 70, 78, 81, 89]
# emptyList = []
# number = int(input("请输入一个数： "))
# if number > sortList[-1]:
#     sortList.append(number)
# else:
#     for i in range(0, len(sortList)):
#         if number < sortList[i]:
#             emptyList.append(number)
#             break
#         else:
#             emptyList.append(sortList[i])
#     for j in range(i, len(sortList)):
#         emptyList.append(sortList[j])
# print(emptyList)
#
#
# # 方法二的改进
# sortList = [0, 6, 7, 13, 14, 70, 78, 81, 89]
# emptyList = []
# number = int(input("请输入一个数： "))
# if number > sortList[-1]:
#     sortList.append(number)
# else:
#     isAppend = 0
#     for i in range(0, len(sortList)):
#         if number < sortList[i]:
#             if isAppend == 0:
#                 emptyList.append(number)
#                 emptyList.append(sortList[i])
#                 isAppend = 1
#             else:
#                 emptyList.append(sortList[i])
#         else:
#             emptyList.append(sortList[i])
# print(emptyList)



# 方法三
# sortList = [0, 6, 7, 13, 14, 70, 78, 81, 89]
# number = int(input("请输入一个数： "))
# sortList.append(number)
# a = 0
# for i in range(a, len(sortList)-1):        # [0, 6, 7, 13, 14, 15, 78, 81, 89, 70]
#     if sortList[-1] < sortList[i]:
#         t = sortList[i]
#         sortList[i] = sortList[-1]
#         sortList[-1] = t
#         a = i + 1
# print(sortList)



# 方法三的改进
sortList = [0, 6, 7, 13, 14, 70, 78, 81, 89]
number = int(input("请输入一个数： "))
sortList.append(number)
a = -1
judge = 1
while judge:
    if sortList[a] < sortList[a-1]:
        t = sortList[a-1]
        sortList[a-1] = sortList[a]
        sortList[a] = t
        a -= 1
    else:
        judge = 0
print(sortList)
