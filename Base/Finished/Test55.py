# *_*coding:utf-8 *_*

'''
题目：学习使用按位取反~。



'''
'''
在Python中，位运算符包括位与（&）、位或（|）、位求反（~）、位异或（^）、左移位（<<）和右移位（>>）

运算方法与规则：位运算符只能适用于整数，其总体运算规则为：首先把整数转换为二进制表示形式，按最低位对齐，短的高位补0，然后进行位运算，最后把得到的二进制转换为十进制数。

按位求反运算符运算规则：~0=1，~1=0，对于整数x有~x=-(x+1)

首先把13转换为二进制数1101，把17转换为10001

13转换为二进制为：1101        按位取反之后为：0010
17转换为二进制为：10001       按位取反之后为：01110


'''