# *_*coding:utf-8 *_*

'''
题目：809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。



'''
def result(num):
    a = num % 100
    for i in range(10, 100):
        if num*i == (num - a)*i + a*i:
            print(i)
            break
    print(num * i)

result(809)
result(7654)