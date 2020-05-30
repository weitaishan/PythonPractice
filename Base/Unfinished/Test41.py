# *_*coding:utf-8 *_*

'''

题目：模仿静态变量的用法。


'''

'''

静态方法，其实就是我们学过的函数，和函数唯一的区别是，静态方法定义在类这个空间（类命名空间）中，而函数则定义在程序所在的空间（全局命名空间）中。

静态方法没有类似 self、cls 这样的特殊参数，因此 Python 解释器不会对它包含的参数做任何类或对象的绑定。也正因为如此，类的静态方法中无法调用任何类属性和类方法。

静态方法需要使用＠staticmethod修饰

推荐学习网址：http://c.biancheng.net/view/4552.html

'''


class pyLanguage:
    @staticmethod
    def info(name, add):
        print(name, add)
pyLanguage.info("Python教程", "http://c.biancheng.net/python")       # 使用类名直接调用调用静态方法
python = pyLanguage()
python.info("Python教程","http://c.biancheng.net/python")            # 使用类对象调用静态方法
