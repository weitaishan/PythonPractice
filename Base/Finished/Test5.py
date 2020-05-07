# *_*coding:utf-8 *_*


'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

x = int(input("请输入一个整数： "))
y = int(input("请输入一个整数： "))
z = int(input("请输入一个整数： "))
if x > y:
    a = x
    x = y
    y = a
if x > z:
    b = x
    x = z
    z = b
if y > z:
    c = y
    y = z
    z = c
print(x,y,z)









'''
x = int(input("请输入一个整数： "))
y = int(input("请输入一个整数： "))
z = int(input("请输入一个整数： "))
if x > y:
    x,y = y,x
if x > z:
    x,z = z,x
if y > z:
    y,z = z,y
print(x,y,z)
'''






'''
x = int(input("请输入一个整数： "))
y = int(input("请输入一个整数： "))
z = int(input("请输入一个整数： "))
list = []
if x > y:
    list.append(y)
    list.append(x)    # y ,x
else:
    list.append(x)
    list.append(y)    # x ,y
if x > z:
    a = list.index(x)
    list.insert(a, z)
else:
    a = list.index(x)
    list.insert(a+1, z)
if y > z:
    list.remove(z)
    b = list.index(y)
    list.insert(b, z)
else:
    list.remove(z)
    b = list.index(y)
    list.insert(b+1, z)
print(list)
'''








'''
x = int(input("请输入一个整数： "))
y = int(input("请输入一个整数： "))
z = int(input("请输入一个整数： "))
if x > y and y > z:
    print(z,y,x)
if x < y and y < z:
    print(x,y,z)
if x > y and y < x:
'''






'''
if x >= y:
    if x >= z:
        if y >= z:
            print(z,y,x)
        else:
            print(y,z,x)
    else:
        print(y,x,z)
else:
    if y > z:
        if x < z :
            print(x,z,y)
        else:
            print(z,x,y)
'''


'''
a = x - y
b = x - z
c = y - z
if a >= 0:   #即x>=y
    if b >= 0:   #即x>=z
        if c >=0:     #即y>=z
            print(z,y,x)
        else:
            print(y,z,x)
else:         #即x<y
    if c > 0:   #即z<y
        if b < 0:
            print(x,z,y)
        else:
            print(z,x,y)
'''



