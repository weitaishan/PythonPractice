# *_*coding:utf-8 *_*

'''
题目：按相反的顺序输出列表的值。


'''



list = [32, 'name', '土豆',999, 110]


#方法一
'''
for i in range(1, len(list)+1):
    print(list[len(list)-i], end =" ")
'''

#方法二
list.reverse()     # 注意：reverse()方法是修改列表，而不是返回一个新的列表
print(list)