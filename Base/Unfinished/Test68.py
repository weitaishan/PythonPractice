# *_*coding:utf-8 *_*

'''
题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数



'''

list1 = [12, 6, 90, 57, 7, 99, 239, 81]
def change(list1, m):
    for i in range(0, m):
        list1.insert(0, list1[-1])
        list1.pop(-1)
    print(list1)
change(list1, 3)
