# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/20


'''


求一个3*3矩阵主对角线元素之和
'''



if __name__ == '__main__':
    a = []
    sum1 = 0.0
    sum2 = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input("input num:\n")))
    for i in range(3):
        sum1 += a[i][i]
        sum2 += a[i][2-i]
    print(sum1,sum2)


# import re
# stopword = ''
# str = ''
# num = []
# result = 0
# print('请输入一个n阶方阵:数字之间用空格隔开，回车输入下一行元素，双回车表示结束\n' \
#         '例如： 11 12 13\n' \
#         '      21 22 23\n' \
#         '      31 32 33\n')
# for line in iter(input, stopword):#输入方阵，将回车作为字符输入
#     str = str + line + '\n'
# row = len(re.findall(r'\n', str))
# for x in re.finditer(r'\d+', str):#将字符串的数字取出并存入到num数列
#     num.append(int(x.group()))
# i = 0
# for j in range(row):#将主对角线元素进行相加
#     result += num[i]
#     i = i + row + 1
# print(num)
# print('主对角线元素和为:',result)