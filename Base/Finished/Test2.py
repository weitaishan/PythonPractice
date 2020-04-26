# *_*coding:utf-8 *_*

'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
'''
'''
P<=10万,         P*10%
10<P<20,        10*10%+(P-10)*7.5%
20<=P<40,       10*10%+10*7.5%+(P-20)*5%
40<=P<60,       10*10%+10*7.5%+20*5%+(P-40)*3%
60<=P<100,      10*10%+10*7.5%+20*5%+20*3%+(P-60)*1.5%
P>=100,         10*10%+10*7.5%+20*5%+20*3%+40*1.5%+(P-100)*1%

'''


'''
P = int(input("请输入公司的当月利润（万）： "))
I = 0
if P<=10:
    I = P*0.1
elif  10<P<20:
    I = 10*0.1+(P-10)*0.075
elif  20<=P<40:
    I = 10*0.1+10*0.075+(P-20)*0.05
elif   40<=P<60:
    I = 10*0.1+10*0.075+20*0.05+(P-40)*0.03
elif   60<=P<100:
    I= 10*0.1+10*0.075+20*0.05+20*0.03+(P-60)*0.015
else:
    I = 10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(P-100)*0.01
print(I)
'''


profits = int(input("请输入公司的当月利润： "))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
result = 0
for index in range(0, len(arr)):    # range(0, 6)    0、1、2、3、4、5
    if profits > arr[index]:
         result += (profits-arr[index]) * rat[index]
         profits = arr[index]

print(result)