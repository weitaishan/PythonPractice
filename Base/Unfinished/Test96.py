# *_*coding:utf-8 *_*

'''
题目：计算字符串中子串出现的次数。

1.可以用系统方法
2.不用系统方法，自己写一个方法出来


'''

# str1 = 'sdghasdhsihahakljdfaha'
#
# 系统方法
# print(str1.count('aha'))     # 2


# 自己写的方法
# def counter(str2, elements):
#     sum = 0
#     n = 0
#     while n < len(str2):
#         a = str2[n:].find(elements)     # 因为find每次只能匹配到子串第一次出现
#         if a != -1:
#             sum += 1
#             n += (a+1)
#         else:
#             break
#     print(sum)
# counter('sdghasdhsihahakljdfahahaca', 'cb')
# counter("hhhhhhaaahhha", 'hh')    # 7



def counter(str2,elements):
    sum1 = 0
    n = 0
    while n < len(str2):
        a = str2[n:].find(elements)     # 因为find每次只能匹配到子串第一次出现
        if a != -1:
            sum1 += 1
            n += a + len(elements)
        else:
            break
    print(sum1)
# counter('sdghasdhsihahakljdfahahaca', 'ha')
counter('adfhhhhhhaaahhha', 'hh')


