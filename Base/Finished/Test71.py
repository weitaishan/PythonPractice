# *_*coding:utf-8 *_*

'''
题目：编写input()和output()函数输入，输出5个学生的数据记录。


'''

# # 方法一
# student1 = input("请输入你的性别、姓名、年龄，中间用空格间隔： ")
# student2 = input("请输入你的性别、姓名、年龄，中间用空格间隔： ")
# student3 = input("请输入你的性别、姓名、年龄，中间用空格间隔： ")
# student4 = input("请输入你的性别、姓名、年龄，中间用空格间隔： ")
# student5 = input("请输入你的性别、姓名、年龄，中间用空格间隔： ")
#
# def output():
#     print(student1)
#     print(student2)
#     print(student3)
#     print(student4)
#     print(student5)
# output()


# 方法二
N = 5
# stu
# num : string
# name : string
# score[4]: list
student = []
for i in range(5):
    student.append(['', '', []])


def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('input student num:')
        stu[i][1] = input('input student name:')
        for j in range(3):
            stu[i][2].append(int(input('score:')))


def output_stu(stu):
    for i in range(N):
        print('%-6s%-10s' % (stu[i][0], stu[i][1]))
        for j in range(3):
            print('%-8d' % stu[i][2][j])


if __name__ == '__main__':
    input_stu(student)
    print(student)
    output_stu(student)





"""

 男 18 小一
 男 18 小二
 女 16 小三
 男 17 小四
 女 15 小五

"""