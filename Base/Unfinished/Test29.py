# *_*coding:utf-8 *_*

'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。


'''

number = int(input("请输入一个不超过5位数的正整数： "))
# 求证该数是个几位数？    分别//（10000、1000、100、10）就可以判断出位数
if number // 10000 != 0:
    print("是五位数")
elif number // 1000 != 0:
    print("是四位数")
elif number // 100 != 0:
    print("是三位数")
elif number // 10 != 0:
    print("是2位数")
else:
    print("是1位数")

# 逆序打印出各位数字
list = list(input("请输入一个不超过5位数的正整数： "))
for i in range(1, len(list)+1):
    print(list[len(list) -i ], end=" ")

