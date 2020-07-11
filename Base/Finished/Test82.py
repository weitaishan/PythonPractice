# *_*coding:utf-8 *_*

'''
题目：八进制转换为十进制



'''
'''
方法为：把八进制、十六进制数按权展开、相加即得十进制数。

学习链接：https://www.cnblogs.com/summerdata/p/10722144.html


'''

# 整数版
from functools import reduce

n = [int(x) for x in input('输入一个整数：')]
print(reduce(lambda x, y: x * 8 + y, n))
# 浮点数版
# 感谢分享： http://www.codesc.net
s = input('输入一个数，可以是浮点数：')
try:
    float(s)
except ValueError:
    print('输入错误')
else:
    f = s.index('.')
    s = s[:f] + s[f + 1:]
    s = [int(x) for x in s]
    n = sum([8 ** (f - 1 - i) * s[i] if i < f else 8 ** (i - 1 - f) * s[i] for i in range(len(s))])
    print(n)

'''
#原程序
if __name__ == '__main__':
    n = 0
    p = raw_input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print n
'''