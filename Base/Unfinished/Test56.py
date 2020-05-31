# *_*coding:utf-8 *_*

'''
题目：画图，学用circle画圆形。　　　

学习网址：http://wenku.uml.com.cn/document/mobile/2020011043.html

'''
from tkinter import *
root = Tk()
cv = Canvas(root, bg='green')
cv.pack()
cv.create_oval((10, 10, 210, 210), fill='yellow')
root.mainloop()
