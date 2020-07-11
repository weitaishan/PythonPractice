# *_*coding:utf-8 *_*

'''
题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。



'''

def password(num):
    strNum = str(num)
    list1 = list(strNum)
    list2 = []
    for i in list1:
        list2.append((int(i)+5) % 10)
    a = list2[3]
    list2[3] = list2[0]
    list2[0] = a
    b = list2[2]
    list2[2] = list2[1]
    list2[1] = b
    print(list2)

password(2567)