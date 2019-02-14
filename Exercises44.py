# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/24


'''
编写一个程序，将两个变量的值互换
'''

a=input("input_str1:")
b=input("input_str2:")

t=a
a=b
b=t
print(a,b)


a=int(input("input_str1:"))
b=int(input("input_str2:"))
a=a+b
b=a-b
a=a-b

print(a,b)