# *_*coding:utf-8 *_*

'''
题目：输入某年某月某日，判断这一天是这一年的第几天？

'''

'''
闰年：年份是4的倍数，但不是100的倍数



'''

months = [1,2,3,4,5,6,7,8,9,10,11,12]
days = [31,28,31,30,31,30,31,31,30,31,30,31]
year = int(input("请输入当前年份： "))
month = int(input("请输入当前月份： "))
day = int(input("请输入当前日期： "))


result = 0
for index in range(0, len(months)):
    if month > months[index]:
        result += days[index]
result += day
if year % 4 == 0 and year % 100 != 0  and month > 2:
    result += 1
print(result)















'''
for index in range(0,len(months)):
    if year/4==0 and year%100!=0:               #判断是否为闰年
        if month>months[index] and month>2:   #判断月份是不是大于2月份
            result = months[index]*days[index]+day+1
            print(result)
            print('1')
        elif month>months[index] and month<=2:
            result = months[index]*days[index] + day
            print(result)
            print('1')
    elif month>months[index]:
        result = months[index]*days[index]+day
        print(result)
        print('1')
print(result)
'''
