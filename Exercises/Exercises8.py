# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/10

'''
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''

n = int(input("第几个月： "))
# 斐波那契数列的通项公式
f =(1/(5**0.5))*(((1+(5**0.5))/2)**n - ((1-(5**0.5))/2)**n)
print("第%d个月：共%d只"  %(n,f))