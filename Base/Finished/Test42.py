# *_*coding:utf-8 *_*

'''
题目：学习使用auto定义变量的用法。

程序分析：没有auto关键字，使用变量作用域来举例吧。
'''

num = 2
def autoFunc():
    num = 1
    print("internal = %d" % num)
    num += 1
    print(num)
for i in range(10):
    print("The number = %d" % num)
    num += 1
    autoFunc()


'''
程序运行结果：
The number = 2
internal = 1
2
The number = 3
internal = 1
2
The number = 4
internal = 1
2
The number = 5
internal = 1
2
The number = 6
internal = 1
2
The number = 7
internal = 1
2
The number = 8
internal = 1
2
The number = 9
internal = 1
2
The number = 10
internal = 1
2
The number = 11
internal = 1
2

'''