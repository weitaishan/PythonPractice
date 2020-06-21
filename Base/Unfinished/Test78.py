# *_*coding:utf-8 *_*

'''
题目：找到年龄最大的人，并输出。

用多种方法来解



'''


ageList = [35, 26, 9, 66, 71, 99, 86, 29]
# 方法一
print(max(ageList))

# 方法二
for i in range(0, len(ageList)-1):
    if ageList[i] > ageList[i+1]:
        a = ageList[i]
        ageList[i] = ageList[i+1]
        ageList[i+1] = a
print(ageList[-1])
