# *_*coding:utf-8 *_*

'''
题目：反向输出一个链表。

至少写3个方法
1.用系统方法
2.用循环笨方法
3.优化循环方法
'''

if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a number:'))
        ptr.append(num)
    print(ptr)
    ptr.reverse()
    print(ptr)