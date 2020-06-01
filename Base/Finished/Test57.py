# *_*coding:utf-8 *_*

'''
题目：画图，学用line画直线。



'''
'''
python中tkinter模块的学习：http://request.uml.com.cn/chengzhang/mobile/oneSubject.asp?wID=902&utype=kf

'''
# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=500, heigth=500)
# canvas.pack()
# canvas.create_line(0, 0, 500, 500)



from tkinter import *
class line:
    def __init__(self):
        canvas = Canvas(width=500, height=500, bg="yellow")
        canvas.pack()
        x0, y0, x1, y1 = 10, 10, 500, 500
        for i in range(25):
            canvas.create_line(x0, y0, x1, y1, width=1, fill="red")
            x0 += 10
            y0 += 10
            x1 -= 10
            y1 -= 10
        mainloop()
if __name__ == "__main__":
    a_line = line()