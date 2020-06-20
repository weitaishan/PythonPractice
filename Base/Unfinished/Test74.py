# *_*coding:utf-8 *_*

'''
题目：列表排序及连接。

列表的排序方法：
list.sort(cmp=None, key=None, reverse=False)
cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。


'''

listSort = [3, 67, 89, 5, 20, 7, 39, 53, 81]

# 升序排列
listSort.sort()
print(listSort)
# 降序排列
listSort.sort(reverse=True)
print(listSort)
