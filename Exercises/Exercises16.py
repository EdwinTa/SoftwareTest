# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/10


'''
求s=a+aa+aaa+aaa+aa...a的值，例如2+22+222+2222+22222（此时共有5个数相加），相加数字的个数将由用户键盘输入来指定
'''

n=int(input('input num:'))
a=int(input('input num:'))
s=0
add=a
for i in range(0,n):
    s+=add
    add=add*10+a
print(s)