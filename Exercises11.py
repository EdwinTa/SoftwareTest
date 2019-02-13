# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/10
'''
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
'''
def count_number(value):
    l=[]
    n = 2
    while n <= value:
        while value != n: # 如果value等于n，说明只有一个质因数，否则就进行循环
            if value % n == 0: # 说明n为一个质因数
                l.append(n)
                value /= n # 更新下一轮value的值
            else:
                break
        n += 1
    l.append(n-1)# 打印出最后一个值
    return l
num=int(input('input:'))
list1=count_number(num)
if len(list1) != 1:
    print(num,'=',end=' ')
    for i in range(0,len(list1)):
        if i != len(list1)-1:
            print(list1[i],'*',end=' ')
        else:
            print(list1[i])
else:
    print(num, '= 1 *',list1[0])