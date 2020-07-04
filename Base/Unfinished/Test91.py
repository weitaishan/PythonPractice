# *_*coding:utf-8 *_*

'''
题目：时间函数举例1


熟悉time模块

在我们平常的代码中，经常需要和时间打交道。在Python中，与时间处理相关的模块有：time、datetime以及calendar。学会计算时间，对程序的调优非常重要，
可以在程序中狂打时间戳，来具体判断程序中哪一块耗时最多，从而找到程序调优的重心处。这里先来讲一个time模块。

在开始前，先说明几点：
在Python中，通常有这几种方式表示时间：时间戳、格式化的时间字符串、元组（struct_time 共九种元素）。由于Python的time模块主要是调用C库实现的，所以在不同的平台可能会有所不同。
时间戳（timestamp）的方式：时间戳表示是从1970年1月1号 00:00:00开始到现在按秒计算的偏移量。查看一下type(time.time())的返回值类型，可以看出是float类型。返回时间戳的函数主要有time()、clock()等。
UTC（世界协调时），就是格林威治天文时间，也是世界标准时间。在中国为UTC+8。DST夏令时。
元组方式：struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()。
>>> import time
>>> ls = time.localtime()
>>> ls
time.struct_time(tm_year=2015, tm_mon=8, tm_mday=24, tm_hour=9, tm_min=39, tm_sec=38, tm_wday=0, tm_yday=236, tm_isdst=0)
1、直接使用元组索引获取对应项的值：
>>> ls[0]
2015
>>> ls[1]
8
>>> ls[-1]
0
2、使用成员符号调用：
>>> ls.tm_year
2015

既然是一个元组，那么就遵循元组的所有特性，比如索引（都从0开始），切片等。下面元组中各元素的解释：
tm_year ：年
tm_mon ：月（1-12）
tm_mday ：日（1-31）
tm_hour ：时（0-23）
tm_min ：分（0-59）
tm_sec ：秒（0-59）
tm_wday ：星期几（0-6,0表示周日）
tm_yday ：一年中的第几天（1-366）
tm_isdst ：是否是夏令时（默认为-1）

'''

# 引入time时间模块
import time

# 1、返回当前时间的时间戳
print(time.time())   # 返回当前时间的时间戳   1593320007.187168
print(int(time.time()))    #对时间戳取整     1593320007

# 2、将一个时间戳转换为当前时区的struct_time：time.localtime（[sec]），即时间数组格式的时间。可选参数sec为转换为time.struct_time类型的对象的秒数。如果secs参数未提供，则以当前时间为准
# 不给定sec参数
print(time.localtime())
# 给定sec参数
print(time.localtime(1593330202))

# 3、将一个时间戳转换为UTC时区(0时区)的struct_time: time.gmtime([sec]),可选参数sec为转换为time.struct_time类型的对象的秒数。如果secs参数未提供，则以当前时间为准
# 不给定sec参数
print(time.gmtime())
# 给定sec参数
print(time.gmtime(1593330759))

# 4、time.mktime(t):将一个struct_time转化为时间戳。time.mktime() 函数执行与gmtime(), localtime()相反的操作，它接收struct_time对象作为参数,返回用秒数表示时间的浮点数。
# 如果输入的值不是一个合法的时间，将触发 OverflowError 或 ValueError。其中参数t为结构化的时间或者完整的9位元组元素
print(time.mktime(time.localtime()))

# 5、time.sleep(secs):线程推迟指定的时间运行。线程睡眠指定时间单位为秒。
# 线程睡眠10秒
time.sleep(10)

# 6、time.clock():这个函数， 函数以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。在不同的系统上含义不同。在NUix系统上，它返回的是“进程时间”，
# 它是用秒表示的浮点数（时间戳）。而在Windows中，第一次调用，返回的是进程运行时实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。
# 该函数有两个功能：（1）在第一次调用的时候，返回的是程序运行的实际时间；
# （2）第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔在win32系统下，这个函数返回的是真实时间（wall time），而在Unix/Linux下返回的是CPU时间。

# 7、time.asctime([t]):把一个表示时间的元组或者struct_time表示为 ‘Sun Aug 23 14:31:59 2015’ 这种形式。如果没有给参数，会将time.localtime()作为参数传入。
# 参数t为：9个元素的元组或者通过函数 gmtime() 或 localtime() 返回的时间值
# 不给定参数
print(time.asctime())
# 给定参数
print(time.asctime(time.gmtime()))

# 8、time.ctime([sec])：把一个时间戳转换为time.asctime()的形式，参数sec为要转换为字符串时间的秒数。如果未指定参数，将会默认使用time.time()作为参数。它的作用相当于time.asctime(time.localtime(secs))
# 未指定参数
print(time.ctime())
# 指定参数
print(time.ctime(1593332349))

# 9、time.strftime(format[,t]):返回字符串表示的当地时间。把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串，
# 格式由参数format决定。如果未指定，将传入time.localtime()。如果元组中任何一个元素越界，就会抛出ValueError的异常。函数返回的是一个可读表示的本地时间的字符串。
# 参数： format：格式化字符串。       t ：可选的参数是一个struct_time对象
'''
时间字符串支持的格式符号：（区分大小写）
%a  本地星期名称的简写（如星期四为Thu）      
%A  本地星期名称的全称（如星期四为Thursday）      
%b  本地月份名称的简写（如八月份为agu）    
%B  本地月份名称的全称（如八月份为august）       
%c  本地相应的日期和时间的字符串表示（如：15/08/27 10:20:06）       
%d  一个月中的第几天（01 - 31）  
%f  微妙（范围0.999999）    
%H  一天中的第几个小时（24小时制，00 - 23）       
%I  第几个小时（12小时制，0 - 11）       
%j  一年中的第几天（001 - 366）     
%m  月份（01 - 12）    
%M  分钟数（00 - 59）       
%p  本地am或者pm的相应符      
%S  秒（00 - 61）    
%U  一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之    前的所有天数都放在第0周。     
%w  一个星期中的第几天（0 - 6，0是星期天）    
%W  和%U基本相同，不同的是%W以星期一为一个星期的开始。    
%x  本地相应日期字符串（如15/08/01）     
%X  本地相应时间字符串（如08:08:10）     
%y  去掉世纪的年份（00 - 99）两个数字表示的年份       
%Y  完整的年份（4个数字表示年份）
%z  与UTC时间的间隔（如果是本地时间，返回空字符串）
%Z  时区的名字（如果是本地时间，返回空字符串）       
%%  ‘%’字符 
'''
# 未指定参数t
print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 指定了参数t
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 10、time.strptime(string[,format]):把格式化字符串转化成struct_time.该函数是time.strftime()函数的逆操作。time strptime() 函数根据指定的格式把一个时间字符串解析为时间元组。所以函数返回的是struct_time对象。
# 参数： string ：时间字符串         format：格式化字符串
# 注意在使用strptime()函数将一个指定格式的时间字符串转化成元组时，参数format的格式必须和string的格式保持一致，如果string中日期间使用“-”分隔，format中也必须使用“-”分隔，时间中使用冒号“:”分隔，后面也必须使用冒号分隔，否则会报格式不匹配的错误。
stime = "2020-06-28 17:06:30"                           # 创建一个时间字符串变量stime
formattime = time.strptime(stime, "%Y-%m-%d %H:%M:%S")  #通过strptime()函数将stime转化成strcut_time形式
print(formattime)   # 返回的结果：time.struct_time(tm_year=2020, tm_mon=6, tm_mday=28, tm_hour=17, tm_min=6, tm_sec=30, tm_wday=6, tm_yday=180, tm_isdst=-1)