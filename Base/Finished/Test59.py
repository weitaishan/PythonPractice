# *_*coding:utf-8 *_*

'''
题目：画图，综合例子。　　

自己找一个图来模仿画出来

'''

from tkinter import *
root = Tk()
cv = Canvas(root, bg='green')
cv.pack()
cv.create_oval((10, 10, 210, 210), fill='yellow')
root.mainloop()