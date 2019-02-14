# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/25

'''
输出杨辉三角
'''

n =10
def lst(i,j):
    if i==j or j==1:
        return 1
    else:
        return lst(i-1,j-1) + lst(i-1,j)

for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(1,i+1):
        print("%3d" %lst(i,j),end=" ")
    print()