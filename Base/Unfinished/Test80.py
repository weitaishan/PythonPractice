# *_*coding:utf-8 *_*

'''
题目：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，
它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？


'''
def peach(part, monkey):
    for i in range((part+monkey+1), 10000):
        if (i - 1) % part == 0:
            b = i
            c = 0
            for j in range(1, monkey+1):
                if (b - 1) % part == 0:
                    a = (b - 1)/part
                    b -= a + 1
                    c += 1
            if c == 5:
                print(i)
                break
peach(5, 5)



