# *_*coding:utf-8 *_*

'''
题目：利用ellipse 和 rectangle 画图。。　



'''

from tkinter import *
root = Tk()
cv = Canvas(root, width = 500, height = 500, bg = "yellow")
left = 10
top = 10
right = 20
num = 15
# cv.create_oval(230, 240, 270, 260)
# cv.create_oval(210, 230, 290, 270)
for i in range(0, 10):
    cv.create_oval(250 - right, 250 - left, 250 + right, 250 + left)
    cv.create_oval(250 - 20, 250 - top, 250 + 20, 250 + top)
    cv.create_rectangle(20 - 2*i, 20 - 2*i, 10*(i+2), 10*(i+2))
    right += 5
    left += 5
    top += 10
cv.pack()
root.mainloop()
