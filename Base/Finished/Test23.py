# *_*coding:utf-8 *_*

'''
题目：打印出如下图案（菱形）:

   *
  ***
 *****
*******
 *****
  ***
   *
'''

'''
a = 4
b = 0
c = 0
for i in range(1, 8):
    if i % 2 != 0:
        a -= 1
        print(' ' * a + "*" * i)
for j in range(1, 6):
    if j % 2 != 0:
        b = 6 - j
        c += 1
        print(' ' * c + "*" * b)
'''


def star(n):
    a = (n-1)//2 + 1
    b = 0
    c = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            a -= 1
            print(' ' * a + "*" * i)
    for j in range(1, n-1):
        if j % 2 != 0:
            b = n-1 - j
            c += 1
            print(' ' * c + "*" * b)
star(11)