# *_*coding:utf-8 *_*


'''
题目：对10个数进行排序。

用选择法或者冒泡法
'''

'''
选择排序算法的原理如下：
对比数组中前一个元素跟后一个元素的大小，如果后面的元素比前面的元素小则用一个变量k来记住他的位置，
接着第二次比较，前面“后一个元素”现变成了“前一个元素”，继续跟他的“后一个元素”进行比较如果后面的元素比他要小
则用变量k记住它在数组中的位置(下标)，等到循环结束的时候，我们应该找到了最小的那个数的下标了，然后进行判断，
如果这个元素的下标不是第一个元素的下标，就让第一个元素跟他交换一下值，这样就找到整个数组中最小的数了。然后
找到数组中第二小的数，让他跟数组中第二个元素交换一下值，以此类推。



冒泡排序算法的原理如下：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

'''

list = [13, 6, 78, 14, 89, 7, 0, 81, 16, 70]

# 冒泡法

# 方法一
# b = len(list) - 1
# while b > 1:
#     for i in range(0, b):
#         if list[i] > list[i+1]:
#             a = list[i]
#             list[i] = list[i+1]
#             list[i+1] = a
#             print(list)
#     b -= 1
#
# # 方法二
# for i in range(0, len(list)-1):
#     for j in range(0, len(list)-1-i):
#         if list[j] > list[j + 1]:
#             a = list[j]
#             list[j] = list[j + 1]
#             list[j + 1] = a



# 选择法

# for i in range(0, len(list)-1):
#     if list[i] - list[i+1] >= 0:
#         a = i + 1
# print(a)
for i in range(0, len(list)-1):
    minIndex = i
    for j in range(i+1, len(list)):
        if list[minIndex] > list[j]:
            minIndex = j
    t = list[minIndex]
    list[minIndex] = list[i]
    list[i] = t
print(list)








# b = len(list) - 2
# for j in range(0, b):
#     if list[j] - list[j+1] >= 0:
#         c = list[j]
#         list[j] = list[j+1]
#         list[j+1] = c
#         print(list)
# b -= 1

