# *_*coding:utf-8 *_*

'''
题目：画椭圆。　

程序分析：使用 Tkinter。

学习网址：http://www.uml.org.cn/python/201912161.asp
学习网址：http://wenku.uml.com.cn/document/mobile/2020011041.html
'''

from tkinter import *
root = Tk()    # 创建一个Tk对象（创建窗口）
cv = Canvas(root, bg = 'white')   # 创建并添加一个Canvas，背景设置为白色。Canvas组件的用法与其他GUI组件一样简单，程序只要创建并添加Canvas组件，然后调用该组件的方法来绘制图形即可。
cv.create_oval((10, 10, 210, 110), fill = 'red')   # 创建一个长200，宽100的椭圆，并用红色填充
cv.pack()   # pack是一个布局管理器，可将它视为一个弹性的容器
root.mainloop()  # 进入消息循环   对mainloop()的理解，网址：https://www.zhihu.com/question/23542885

'''
1、布局管理器:实现组件布局的方法被称为布局管理器或几何管理器。负责管理各组件的大小和位置，此外，当用户调整了窗口的大小之后，
布局管理器还会自动调整窗口中各组件的大小和位置。
2、如果使用Pack布局，以块的方式布局组件。意味着当程序向容器中添加组件时，这些组件会依次向后排列，排列方向既可是水平排列，也可是垂直排列。
3、tkinter使用三种方法来实现布局：pack()、grid()、place()
4、pack()方法的参数：side表示组件在容器中的位置；expand表示组件可拉伸；fill取值为x、y或BOTH，填充x或y方向上的空间；anchor表示组件在窗口中位置


'''