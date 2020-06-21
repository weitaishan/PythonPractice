# *_*coding:utf-8 *_*

'''
题目：列表转换为字典。


'''

# 方法一：嵌套列表转字典
list1 = [["sex", "boy"], ["name", "Jenny"], ["age", 18]]
print(dict(list1))



# 方法二：嵌套列表转字典
list1 = [["sex", "boy"], ["name", "Jenny"], ["age", 18]]
dic = {}
for i in list1:
    dic[i[0]] = i[1]   # 字典赋值，左边为key，右边为value
print(dic)

# 方法三：嵌套列表转字典
list4 = ['tyc=ddo56365f', 'cmb=13652d22d', 'eay=53896d' ]
newDict = {}
for i in range(len(list4)):
    newDict[list4[i]] = list4[i].split('=')[1]
print(newDict)

# 方法四：两个列表转换为字典。使用zip函数   zip函数学习地址：https://www.runoob.com/python3/python3-func-zip.html
list2 = ["sex", "name", "age"]
list3 = ["boy", "Jenny", 18]
print(dict(zip(list2, list3)))

