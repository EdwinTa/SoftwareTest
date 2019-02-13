# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/18

'''
有一分数数列：2/1，3/2，5/3，8/5，13/8，21/13……求这个数列前20项和
'''

a = 2.0
b = 1.0
s = 0
for n in range(1,21):
    s += a / b
    t = a
    a = a + b
    b = t
print(s)