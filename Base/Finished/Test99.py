# *_*coding:utf-8 *_*

'''
题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。



'''

# 先创建两个文件A和B，并存入相应的数据
file = open('A.txt', 'w')
file.write('auc')
file.close()
file = open('B.txt', 'w')
file.write('bgz')
file.close()

# 读取文件A和B中的数据出来，并且需要排好序之后，放入新文件C中
with open('A.txt', 'r') as file:
    A = file.read()
with open('B.txt', 'r') as file:
    B = file.read()
list1 = list(A + B)
list1.sort()
str1 = ''.join(list1)
file = open('C.txt', 'w')
file.write(str1)
file.close()

