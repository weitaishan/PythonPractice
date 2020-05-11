# *_*coding:utf-8 *_*

'''
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

程序分析：采取逆向思维的方法，从后往前推断。
'''

'''
倒推出规律
第10天：剩下1个桃子     f(1)
第9天：剩下4个桃子      f(2)
第8天：剩下10个桃子     f(3)
第7天：剩下22个桃子     f(4)

第1天：剩下n个桃子     f(n) n=10    f(n) = (f(n-1)+1)*2     n>1
'''


def peach(n):
    if n <= 1:
        return 1
    return (peach(n-1)+1)*2
print(peach(10))