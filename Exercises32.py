# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/20

'''
按逗号分隔列表。
'''

L = [1,2,3,4,5]

#利用JOIN将通过迭代器生成的字符串进行拼接
s1 = ','.join(str(n) for n in L)
print(s1)
print(type(s1))


L = [1, 2, 3, 4, 5]
L = repr(L)[1:-1]
print(L)
print(type(L))