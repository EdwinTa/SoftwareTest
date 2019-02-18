# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/10

'''
输出9X9乘法口诀
'''

for i in range(1, 10):
    print('\n')
    for j in range(1, i+1):
        print("%d*%d=%d" %(i, j, i*j),end='\t')