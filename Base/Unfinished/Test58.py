# *_*coding:utf-8 *_*

'''
题目：画图，学用rectangle画方形。　　　


学习网址：http://wenku.uml.com.cn/document/mobile/2020011043.html

'''

from tkinter import *
root = Tk()
cv = Canvas(root, bg='yellow')     # bg指定画布的背景色为黄色
cv.pack()
rt = cv.create_rectangle(10, 10, 110, 110, dash=9, fill='red', outline='blue', width='3')  # 还可以添加stipple='gray12'等属性
cv.coords(rt, (40, 40, 80, 80))
root.mainloop()
# dash属性指的是边框为虚线，值只能为奇数
# fill属性指的是图形的填充色
# outline属性指的是图形的边框颜色
# width属性指的是线的宽度
# stipple属性指的是边框为自定义画刷