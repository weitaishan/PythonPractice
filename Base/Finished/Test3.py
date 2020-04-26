# *_*coding:utf-8 *_*
'''
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？


a + 100 = n*n
a + 100 + 168 = m*m

m*m - n*n = 168
(m+n)*(m-n) = 168

m + n   肯定是偶数

m - n    肯定也是偶数，那么m是

'''
def squareNumber(b,c):
    for i in range(1,int(b/2+1)):
        if i%2 == 0:
            j = b/i
            if j%2 == 0 and i>j:
                m = (i+j)/2
                n = (i-j)/2
                a = n*n - c
                print(a)
squareNumber(168,100)