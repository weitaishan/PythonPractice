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


for i in range(1,8):
    if i % 2 != 0:
        print("*" * i)