# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/18

'''
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''

# x = int(input("请输入一个数:\n"))
# a = x // 10000
# b = x % 10000 // 1000
# c = x % 1000 // 100
# d = x % 100 // 10
# e = x % 10
#
# if a != 0:
#     print("5 位数：", e, d, c, b, a)
# elif b != 0:
#     print("4 位数：", e, d, c, b)
# elif c != 0:
#     print("3 位数：", e, d, c)
# elif d != 0:
#     print("2 位数：", e, d)
# else:
#     print("1 位数：", e)


num = list(input('输入一个最多5位的数字:'))
print(len(num))
num.reverse() #reverse()是list反向函数
for i in range(len(num)):
    print(num[i], end=',')