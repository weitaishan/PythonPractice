# *_*coding:utf-8 *_*

'''
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。



'''

# def leave(n):
#     list = []
#     for i in range(1, n+1):
#         list.append(i)
#     while len(list) > 1:
#         a = len(list) % 3
#         if a == 0:
#             for j in range(0, len(list)):
#                 if (j+1) % 3 == 0:
#                     list.pop(j)
#         if a == 1:
#             for j in range(0, len(list)):
#                 if (j + 2) % 3 == 0:
#                     list.pop(j)
#         if a == 2:
#             for j in range(0, len(list)):
#                 if (j + 3) % 3 == 0:
#                     list.pop(j)
#
# print(leave(18))


n = int(input('请输入总人数:'))
list1 = list(range(1, n + 1))
print(list1)
count = 0
while len(list1) > 1:
    list2 = []
    for (index, value) in enumerate(list1):
        if (index + 1 + count) % 3 != 0:    # index + 1 + count指的是报的数是1还是2还是3
            list2.append(value)
    count += len(list1) % 3
    list1 = list2
    print('count', count)
    print(list2)

print(list1)


# list1 = list(range(1, n + 1))
# print(list1)
# value = 1
# while len(list1) > 1:
#     if value % 3 == 0:
#         list1.pop(list1.index(value))
#     value += 1
#     print(value)
#     if value > len(list1):
#         value = value - len(list1)
#     print(list1)
#
# print(list1)


'''
def leave(n):
    list = []
    x = n % 3
    for i in range(1, n+1):
        list.append(i)
    while n > 2:
        for j in range(0, n):
            if (j+1) % 3 == 0:
                list.pop(j)
        n = len(list)
    print(list)

leave(5)
'''

'''
  nmax = 50
    n = int(raw_input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)

    i = 0
    k = 0
    m = 0

    while m < n - 1:
        if num[i] != 0 : k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n : i = 0

    i = 0
    while num[i] == 0: i += 1
    print num[i]
'''