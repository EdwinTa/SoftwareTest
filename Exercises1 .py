# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/8


#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# permutations(p[,r]);返回p中任意取r个元素做排列的元组的迭代器

from itertools import permutations

t=0
for i in permutations('1234',3):
    print(int(''.join(i)))
    t+=1
print("1、2、3、4组成%d个互不相同且无重复数字的三位数"%t)
