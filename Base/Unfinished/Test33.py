# *_*coding:utf-8 *_*

'''
题目：按逗号分隔列表。

使用join()方法来实现。join方法是字符串方法，是split的你方法，用来连接序列中的元素。
例如：seq = ['1','2','3','4','5']
      sep = '+'
      sep.join(seq)   结果是：1+2+3+4+5.需要特别注意：被连接的序列元素都必须是字符串。即seq里面的元素必须是字符串，而不能是其他类型，比如不能是[1,2,3,4,5]这样的数字类型

'''


# 方法一：使用join方法来实现
list1 = ['abc', 123, '你好', 999, 111]
sep = ','
str1 = sep.join(str(i) for i in list1)
print(str1)    #  abc,123,你好,999,111

# 方法二  使用连接字符来实现
def seprate(listData):
    listData = list(listData)
    str2 = str(listData[0])    # 因为第一个元素前面不需要加逗号，所以需要单独拿出来（最后一个元素后面也不需要加逗号）
    for i in listData[1:]:
        str3 = ',' + str(i)
        str2 += str3
    print(str2)
seprate(['你好','世界', 2, 3, 4, 5, 6])    #  你好,世界,2,3,4,5,6
