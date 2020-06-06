# *_*coding:utf-8 *_*

'''
题目：利用ellipse 和 rectangle 画图。。　



'''

from tkinter import *
root = Tk()
cv = Canvas(root, bg = "yellow")
left = 10
top = 10
right = 20
buttom = 20
for i in range(0, 10):
    cv.create_rectangle(left + 2*i, top + 2*i, right + 2*i, buttom + 2*i, fill = 'green', width = 5)
    cv.create_oval(left + 4*i, top + 4*i, right + 4*i, buttom + 4*i, fill = 'blue')
cv.pack()
root.mainloop()
