# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/12

'''
输出下面图形
      *
     ***
    *****
   *******
    *****
     ***
      *
'''

n=4
for i in range(4):
    print(' '*(3-i),end="")
    print('*'*(2*i+1))
for i in range(2,-1,-1):
    print(' '*(3-i),end="")
    print('*'*(2*i+1))


