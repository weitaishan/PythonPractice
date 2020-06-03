# *_*coding:utf-8 *_*

'''
题目：查找字符串。　　


'''
'''
有四种方法：find、rfind、index、rindex
'''
# 第一种：find()方法检测字符串中是否包含子字符串str，如果指定beg（开始）和end（结束）范围，左开右闭区间。
# 则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。如果不指定beg和end则默认在整个字符串中检查。
# 语法：str.find(str, beg=0, end=len(string))
# astr = "bvnhingdhaaddfsfx"
#
# print(astr.find('gdh'))    # 结果是6
# print(astr.find('gxh'))    # 结果是-1（没有找到）
# print(astr.find('aa', 6))  # 结果是9。6代表从索引为6开始查找
# print(astr.find('aa', 6, 10))   # 结果是-1 （10不包含在内，左开右闭区间）


# 第二种：rfind()方法和find方法相比是从右往左开始查找，但是返回来的索引还是从左往右的索引位置
astr = "bvnhingdhaaddfsfx"
print(astr.rfind('dd'))   # 结果是11，是从右往左找，但是返回来的索引还是从左往右的索引位置

# 第三种