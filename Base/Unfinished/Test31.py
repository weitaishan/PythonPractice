# *_*coding:utf-8 *_*

'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。


'''


'''
星期一：Monday
星期二：Tuesday
星期三：Wednesday
星期四：Thursday
星期五：Friday
星期六：Saturday
星期日：Sunday
'''

list = input("请用英文输入星期一到星期日任意一天： ")
if list[0] == "M":
    print("星期一")
elif list[0] == "T":
    if list[1] == "u":
        print("星期二")
    else:
        print("星期四")
elif list[0] == "W":
    print("星期三")
elif list[0] == "F":
    print("星期五")
elif list[0] == "S":
    if list[1] == "a":
        print("星期六")
    else:
        print("星期天")
