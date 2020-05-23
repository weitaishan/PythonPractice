# *_*coding:utf-8 *_*

'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。


'''


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


sortList = [0, 6, 7, 13, 14, 70, 78, 81, 89]
number = int(input("请输入一个数： "))
if number > sortList[-1]:
    sortList.append(number)
else:
    for i in range(0, len(sortList)-1):
        if number < sortList[i]:
            t = sortList[i]
            sortList[i] = number
            break
        

print(sortList)