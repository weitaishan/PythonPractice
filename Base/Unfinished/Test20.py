# *_*coding:utf-8 *_*

'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？


'''


'''
分析：可以使用递归方法
f(1)=100    f(2)=50     f(n) = f(n-1)/2 n>1
'''

# 求出反弹多高
'''
def ball(n):
    if n <= 1:
        return 100
    return ball(n-1)/2
print(ball(5))
'''

# a = int(input("请输入球落地的次数： "))
# sum = 0
# for i in range(1, a+1):
#     sum += 2*ball(i)
# print(sum-ball(1))


# 使用循环解题（求高度）
number = int(input("请输入小球的落地次数： "))
a = 100
b = 0
for i in range(1, number):
    a = a/2
    b += 2*a
print(a, b+100)
