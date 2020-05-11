# *_*coding:utf-8 *_*

'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。

字符串.isalnum()	所有字符都是数字或者字母，为真返回 Ture，否则返回 False。
字符串.isalpha() 所有字符都是字母，为真返回 Ture，否则返回 False。
字符串.isdigit() 所有字符都是数字，为真返回 Ture，否则返回 False。
字符串.islower()	所有字符都是小写，为真返回 Ture，否则返回 False。
字符串.isupper()	所有字符都是大写，为真返回 Ture，否则返回 False。
字符串.istitle()	所有单词都是首字母大写，为真返回 Ture，否则返回 False。
字符串.isspace()	所有字符都是空白字符，为真返回 Ture，否则返回 False。
'''
# list = list(input("请输入一串字符： "))
# list1 = [chr(i) for i in range(97, 123)]   #生成26位小写英文字母
# list2 = [chr(x) for x in range(65, 91)]    #生成26位大写英文字母
# list3 = ['0','1','2','3','4','5','6','7','8','9']
# a,b,c,d = 0,0,0,0
# for i in list:
#     if i == " ":
#         a += 1
#     elif i in list3:
#         b += 1
#     elif i in list1 or i in list2:
#         c += 1
#     else:
#         d = len(list) - a - b - c
# print(a, b, c, d)

# string = input("请输入一串字符： ")
string = 'abc123ABC 你好'
print(string)
a, b, c, d = 0, 0, 0, 0
for i in range(0, len(string)):
    if string[i].encode('UTF-8').isalpha():  #中文的汉字会被 isalpha 判定为 True：如果想区分中文和英文可以使用 unicode。中文的范围为：['/u4e00'，'/u9fa5']。
        a += 1
    elif string[i].isspace():
        b += 1
    elif string[i].isdigit():
        c += 1
    else:
        d += 1

print(a, b, c, d)