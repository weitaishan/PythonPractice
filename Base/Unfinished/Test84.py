# *_*coding:utf-8 *_*

'''
题目：连接字符串。



'''

# 方法一
str1 = "你好，"
str2 = "世界"
print(str1+str2)

# 方法二：使用join方法，jion方法是split的逆方法，用于连接序列中的元素
seq = ["你好", "世界"]
sep = ","
print(sep.join(seq))
print(",".join(seq))

# 方法三
print("你好，" + "世界")

# 格式化连接
# "%"格式化连接
print('%s world !' % ('hello'))
print('PI = %f' % (3.1415926))
# "format"格式化连接
print('{} world !'.format('hello'))
print('PI = {}' .format(3.1415926))