# *_*coding:utf-8 *_*

'''
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n



'''

def add(num):
    if num % 2 == 0:
        sum1 = 0
        for i in range(2, num+1):
            if i % 2 == 0:
                a = 1/i
                sum1 += a
        print(sum1)
    else:
        sum2 = 0
        for j in range(1, num+1):
            if j % 2 != 0:
                b = 1/j
                sum2 += b
        print(sum2)

add(4)
add(12)
add(15)