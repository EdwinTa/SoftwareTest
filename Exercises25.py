# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/18

'''
利用递归方法求5!。
'''
def Factorial(n):
    if n == 1:
        fn=1
    else:
        fn = n*Factorial(n-1)
    return fn
print(Factorial(5))