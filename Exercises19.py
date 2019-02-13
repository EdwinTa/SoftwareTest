# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/11


'''
一个球从100m高度自由落下，每次落地后反跳回原来高度的一半，再落下，那么它在第10次落地时，共经过多少米？第10次反弹多高？
'''

sm=0
h=100
for i in range(10):
    sm=sm+h+h/2
    h/=2
    print(h)
print(sm)
