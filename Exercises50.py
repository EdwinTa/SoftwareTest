# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/25

'''
输入三个数a,b,c,按照大小顺序输出
'''

a=[]
for i in range(3):
    a.append(input("请输入一个数字："))
a.sort()
print(a)