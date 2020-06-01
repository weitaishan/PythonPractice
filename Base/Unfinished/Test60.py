# *_*coding:utf-8 *_*

'''
题目：计算字符串长度。　　


'''

# 方法一
Astr = input("请随意输入一串字符： ")
print(len(Astr))

# 方法二
Alist = list(input("请随意输入一串字符："))
a = 0
for i in Alist:
    a += 1
print(a)

