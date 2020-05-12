# *_*coding:utf-8 *_*

'''
题目：练习函数调用。

总结一下函数有哪些，怎么写
'''


'''
定义一个函数：
你可以定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

定义函数的语法：
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''


#  1、定义一个求斐波那契前n位的函数。n为用户自定义的数(有返回值的函数)
def fibs(n):
    result = [0, 1]
    for i in range(0, n-2):
        result.append(result[-1] + result[-2])
    return result

print(fibs(5))    # 返回值是 [0, 1, 1, 2, 3]

#  2、定义一个求斐波那契前n位的函数。n为用户自定义的数(无返回值的函数)
def fibs1(n):
    result = [0, 1]
    for i in range(0, n-2):
        result.append(result[-1] + result[-2])

print(fibs1(5))    # 返回值是 None

#  3、定义一个求斐波那契前n位的函数。n为用户自定义的数(return不带表达式的函数)
def fibs2(n):
    result = [0, 1]
    for i in range(0, n-2):
        result.append(result[-1] + result[-2])
    return

print(fibs2(5))    # 返回值是 None


def printme(str):
   "打印传入的字符串到标准显示设备上"
   print(str)
   return
print(printme(123456))   # 结果是：123456    但是函数的返回值是None



# 4、传不可变变量参数实例
def ChangeInt(a):
    print(a)   #结果是2
    a = 10
    print(a)   #结果是10
b = 2
ChangeInt(b)
print(b)  # 结果是 2。 b是不会被改变的

# 5、传可变变量参数实例
def changeme(mylist):
    '修改传入的列表'
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return
mylist = [10, 20, 30]
changeme(mylist)                 #结果是[10, 20, 30, [1, 2, 3, 4]],函数返回值是None
print("函数外取值: ", mylist)     #打印结果是：[10, 20, 30, [1, 2, 3, 4]]   会发现mylist这个列表是被改变了的


# 函数的参数（用函数时可使用的正式参数类型）：必备参数、关键字参数、默认参数、不定长参数

# 6、必备参数：必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样，否则会出现语法错误。
'''
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return
printme()
'''
'''
会报错：Traceback (most recent call last):
  File "E:/PyCharmProject/PythonPractice/Base/Unfinished/Test34.py", line 100, in <module>
    printme()
TypeError: printme() missing 1 required positional argument: 'str'
'''

# 7、关键字参数：关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return
printinfo(age=50, name="runoob")
'''
结果是：
名字:  runoob
年龄:  50
函数返回值是None
'''

# 8、默认参数：调用函数时，如果没有传递参数，则会使用默认参数。
def printinfo(name, age=35):   # 调用时，如果age没有传值，则为默认的35；如果传了值，则age的值为所传值
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")
'''
结果是：
名字:  runoob
年龄:  50
------------------------
名字:  runoob
年龄:  35
函数返回值是None
'''

# 9、不定长参数：你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述3种参数不同，声明时不会命名。

'''
def functionname([formal_args,] *var_args_tuple ):       
   "函数_文档字符串"
   function_suite
   return [expression]
'''
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)
printinfo(70, 60, 50)
'''
结果是：
输出: 
70
(60, 50)
函数的返回值是None
'''
# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
printinfo(10)
printinfo(70, 60, 50)
'''
结果是：
10
输出: 
70
60
50
函数的返回值是None
'''

# 加了两个星号 ** 的参数会以字典的形式导入。
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)
printinfo(1, a=2, b=3)
'''
结果是：
输出: 
1
{'a': 2, 'b': 3}
函数的返回值是None
'''

# 声明函数时，参数中*可以单独出现。如果单独出现星号，*后的参数必须用关键字传入
def f(a,b,*,c):
    return a+b+c
#f(1,2,3)
'''
会报错：
Traceback (most recent call last):
  File "E:/PyCharmProject/PythonPractice/Base/Unfinished/Test34.py", line 204, in <module>
    f(1,2,3)
TypeError: f() takes 2 positional arguments but 3 were given
'''
print(f(1, 2, c=3))    # 结果是：6   返回值也是6

# 10：强制位置参数：Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
#def f(a, b, /, c, d, *, e, f):       #形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参
#    print(a, b, c, d, e, f)
# 以下都是错误用法
#f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
#f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
# 以下是正确用法
#f(10, 20, 30, d=40, e=50, f=60)
#f(10, 20, c=30, d=40, e=50, f=60)


# 11、匿名函数
'''
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

语法：lambda [arg1 [,arg2,.....argn]]:expression
'''

sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))     # 结果是 "相加后的值为：30"
print("相加后的值为 : ", sum(20, 20))     # 结果是 "相加后的值为：40"

# 12、参数形式
