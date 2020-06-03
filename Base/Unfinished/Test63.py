# *_*coding:utf-8 *_*

'''
题目：画椭圆。　

程序分析：使用 Tkinter。

'''

from tkinter import *
root = Tk()    # 创建一个Tk对象
cv = Canvas(root, bg = 'white')   # 创建一个Canvas，背景设置为白色
cv.create_oval((10, 10, 210, 110), fill = 'red')   # 创建一个长200，宽100的椭圆，并用红色填充
cv.pack()
root.mainloop()
