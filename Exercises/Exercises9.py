# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/10

'''
判断101~200之间有多少个素数，并输出所有素数
'''
l=[n for n in range(101,200) if not [m for m in range(2,n) if n % m ==0]]
print(len(l),'\n',l)

