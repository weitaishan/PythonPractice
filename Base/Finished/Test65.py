# *_*coding:utf-8 *_*

'''
题目：一个最优美的图案。　　


'''

from tkinter import *
root = Tk()
cv = Canvas(root, bg='yellow')     # bg指定画布的背景色为黄色
cv.pack()
rt = cv.create_rectangle(10, 10, 110, 110, dash=9, fill='red', outline='blue', width='3')  # 还可以添加stipple='gray12'等属性
cv.coords(rt, (40, 40, 80, 80))
root.mainloop()


