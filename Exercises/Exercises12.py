# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/10

'''
输出第10个斐波那契数列
'''
n=int(input('input:'))
for i in range(0,n+1):
    print('%d'%((1/(5**0.5))*(((1+(5**0.5))/2)**i - ((1-(5**0.5))/2)**i)),end=',')