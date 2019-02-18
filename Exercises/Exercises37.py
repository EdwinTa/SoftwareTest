# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/24


'''
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''

List1=[2,5,4,8,3,1,9]
List1=sorted(List1)
print("打印原来的数组:",List1)
print()

num=int(input("请输入一个数:"))
List1.append(num)
print("打印新的数组:",sorted(List1))