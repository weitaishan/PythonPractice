# *_*coding:utf-8 *_*

'''
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''

# list1 = ['a', 'b', 'c']
# list2 = ['x', 'y', 'z']
# list3 = []
# for i in list1:
#     for j in list2:
#         if i == 'a' and j == 'x':
#             continue
#         elif i == 'c' and (j == 'x' or j == 'z'):
#             continue
#         else:
#             list3.append(i + j)
# print(list3)
# list4 = []
# for k in range(0, len(list3)):
#     if 'c' in list3[k]:
#         list4.append(list3[k])
#         p = list3[k][1]
#         list3.pop(k)
# P = p
# for l in range(0, len(list3)):
#     if 'M' in list3[l]:
#         list3.pop(l)
# for m in range(0, len(list3)):
#     if 'a' in list3[m]:
#         list4.append(list3[m])
#         q = list3[m][1]
#         list3.pop(m)
# Q = q
# for n in range(0, len(list3)):
#     if 'N' in list3[n]:
#         list3.pop(n)
#         list4.append(list3[0])
# print(list4)



# for i in range(ord('x'), ord('z') + 1):
#     for j in range(ord('x'), ord('z') + 1):
#         if i != j:
#             for k in range(ord('x'), ord('z') + 1):
#                 if (i != k) and (j != k):
#                     print(chr(i), chr(j), chr(k))
#                     if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
#                         print('order is a -- %s\t b -- %s\tc--%s' % (chr(i), chr(j), chr(k)))