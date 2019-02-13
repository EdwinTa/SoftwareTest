# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/24

'''
编写一个程序，使用关键字auto定义变量
'''

num = 2
def autofunc():
    num = 1
    print('internal block num = %d' % num)
    num += 1
for i in range(3):
    print ('The num = %d' % num)
    num += 1
    autofunc()