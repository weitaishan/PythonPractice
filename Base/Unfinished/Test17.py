# *_*coding:utf-8 *_*

'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
'''
list = list(input("请输入一串字符： "))
print(list)
list1 = [chr(i) for i in range(97, 123)]
list2 = [chr(x) for x in range(65, 91)]
list3 = ['0','1','2','3','4','5','6','7','8','9']
a,b,c,d = 0,0,0,0
for i in list:
    if i == " ":
        a += 1
    elif i in list3:
        b += 1
    elif i in list1 or i in list2:
        c += 1
    else:
        d = len(list) - a - b - c
print(a, b, c, d)