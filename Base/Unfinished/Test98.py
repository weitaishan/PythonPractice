# *_*coding:utf-8 *_*

'''
题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。



'''

A = input('请随意输入一个字符串： ')
B = str.upper(A)
file = open('test.txt', 'w')
file.write(B)
file.close()