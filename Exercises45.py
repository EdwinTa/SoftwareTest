# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/24

'''
输入两个数，然后比较大小
'''

num1=int(input("input num1:"))
num2=int(input("input num2:"))

if num1 > num2:
    print("%d比%d大"%(num1,num2))
elif num1 == num2:
    print("%d和%d一样大" % (num1, num2))
else:
    print("%d比%d小"%(num1,num2))
