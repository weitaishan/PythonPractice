# *_*coding:utf-8 *_*

'''
题目：模仿静态变量(static)另一案例。

程序分析：演示一个python作用域使用方法
'''

# 模仿静态方法

class Num:      # 首先我们定义一个Num的类
    nNum = 1     # 将1赋值给nNum变量
    def inc(self):   #定义一个inc的方法，这里也可把inc称作是子类。
        self.nNum += 1 # 方法调用nNum的变量
        print("nNum = %d" % self.nNum) #打印

if __name__ == "__main__": # 程序运行入口
    nNum = 2 # 初始化nNum变量
    inst = Num() # 调用Num类，创建一个类对象inst
    for i in range(3): # 循环三次
        nNum += 1 # nNum每次循环+=1
        print("The num = %d" % nNum) #
        inst.inc() # 调用实例方法inc

'''
运行结果：
The num = 3
nNum = 2
The num = 4
nNum = 3
The num = 5
nNum = 4

'''