# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/24

'''
求输入数的平方，如果平方算后小于50则退出
'''



try:
    num = int(input("input a num:"))
    if num*num < 50:
        print("输入数的平方为：%d"%(num*num))
    elif num*num == 50:
        print("输入数的平方为：%d，等于50" %(num * num))
    else:
        print("输入数的平方为：%d，大于50" %( num * num))

except:
    print('输入错误')