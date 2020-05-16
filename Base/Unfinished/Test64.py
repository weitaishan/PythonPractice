# *_*coding:utf-8 *_*

'''
题目：利用ellipse 和 rectangle 画图。。　



'''


n = int(input("请输入一个正整数： "))
list = []
for i in range(1, n+1):
    list.append(i)
a = len(list) % 3
'''
b = 0
for j in range(0, len(list)):
    if (j + 1) % 3 == 0:
        list.pop(j-b)
        b += 1     #完成第一轮的淘汰3、6、、9、12、15、18
'''
while len(list) > 1:
    if a == 0:
        c = 0
        for x in range(0, len(list)):
            if (x + 1) % 3 == 0:
                list.pop(x - c)
                c += 1
    if a == 1:
        d = 0
        for y in range(0, len(list)):
            if (y + 2) % 3 == 0:
                list.pop(y - d)
                d += 1
    if a == 2:
        e = 0
        for z in range(0, len(list)):
            if (z + 3) % 3 == 0:
                list.pop(z - e)
                e += 1
    a = len(list) % 3
print(list)