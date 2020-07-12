# *_*coding:utf-8 *_*

'''
题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。



'''

def str1():
    b = input('请输入文件名 ')
    a = input('请随意输入一些字符： ')
    list1 = list(a)
    file = open(b, 'w')
    for i in list1:
        if i != '#':
            file.write(i)
        else:
            file.close()
            break
str1()