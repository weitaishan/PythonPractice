# *_*coding:utf-8 *_*

'''
题目：回答结果（结构体变量传递）。

熟悉什么是结构体

'''
'''
了解c语言的人，一定会知道struct结构体在c语言中的作用，它定义了一种结构，里面包含不同类型的数据(int,char,bool等等)，方便对某一结构对象进行处理。
而在网络通信当中，大多传递的数据是以二进制流（binary data）存在的。当传递字符串时，不必担心太多的问题，而当传递诸如int、char之类的基本数据的时候，
就需要有一种机制将某些特定的结构体类型打包成二进制流的字符串然后再网络传输，而接收端也应该可以通过某种机制进行解包还原出原始的结构体数据。
python中的struct模块就提供了这样的机制，该模块的主要作用就是对python基本类型值与用python字符串格式表示的C struct类型间的转化
（This module performs conversions between Python values and C structs represented as Python strings.）。stuct模块提供了很简单的几个函数，下面写几个例子。


用处
按照指定格式将Python数据转换为字符串,该字符串为字节流,如网络传输时,不能传输int,此时先将int转化为字节流,然后再发送;
按照指定格式将字节流转换为Python指定的数据类型;
处理二进制数据,如果用struct来处理文件的话,需要用’wb’,’rb’以二进制(字节流)写,读的方式来处理文件;
处理c语言中的结构体;


学习地址：https://www.cnblogs.com/mikew/p/11650680.html

'''

