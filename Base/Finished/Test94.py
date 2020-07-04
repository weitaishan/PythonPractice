# *_*coding:utf-8 *_*

'''
题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。



'''
import time
import random
number = random.randint(0, 1)
print(number)
play = input("do you want to play it?('yes' or 'no'): ")
if play == 'yes':
    start = time.time()
    print(start)


while play == 'yes':
    your_number = int(input("please enter your guess number: "))
    if your_number == number:
        end = time.time()
        print(end)
        print("Great! you guess it!")
        print('different is %f' % (end - start))
        play = 'no'


