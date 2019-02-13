# _*_ coding utf-8 _*_

'''
根据你输入的数据，来进行判断学生的成绩。
'''

# num = int(input("请输入学生成绩："))
#
# if num >= 85 and num <=100:
#     print("优秀")
# elif num >= 75 and num <85:
#     print("良好")
# elif num >= 60 and num <75:
#     print("及格")
# elif num >= 0 and num <60:
#     print("不及格")
# else:
#     print("输入有误！")

'''
生成随机整数，从1-9取出来，然后输入一个数，来猜，如果大于，则打印bigger，小了则打印less。如果等于，则打印equal
'''

# import random
#
# num1 = int(input("请输入一个数："))
# num2 = random.randint(1,9)
#
# if num1 == num2:
#     print("equal")
# elif num1 >= num2 and num1 < 10:
#     print("bigger")
# elif num1 <= num2 and num1 > 0:
#     print("less")
# else:
#     print('输入错误！')

'''
写一个菜单显示程序：
'''

# menu = {'平价菜':{'手撕包菜':'10元','茄子豆角':'12元','土豆烧肉':'15元'},'凉菜':{'凉拌黄瓜':'8元','凉拌皮蛋':'9元'},'小锅现炒':{'红烧鱼块':'18元','香煎鲫鱼':'21元','大盆花菜':'16元'}}
# #
# #
# # str = input('请输入菜名：').strip()
# # n = 0
# # for i in menu:
# #     for j in menu[i].keys():
# #         if j == str:
# #             print('%s:%s'%(str,menu[i][j]))
# #             n = 1
# # if n == 0 :
# #     print('没有这道菜！')








'''
利用while循环，完成1-100的证书数字相加和
'''

# sum1 = 0
# i = 1
# while i <= 100:
#     sum1 += i
#     i += 1
# print(sum1)


'''
利用for循环，完成1-10的证书数字相加和
'''

# sum1 = 0
#
# for i in range(1,11):
#     sum1 += i
# print(sum1)


'''
利用for循环输出如下三角行
*
**
***
****
*****
'''

# for i in range(1,6):
#     print('*'*i)


'''
输出下面图形
      *
     * *
    * * *
   * * * *
  * * * * *

'''

# n=5
# for i in range(n):
#     print(' '*(n-1-i),end="")
#     print('* '*(i+1))


'''
输出99乘法表
'''

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(i,j,i*j),end="\t")
#     print()


'''
利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序
'''

# a=[1,7,4,89,34,2]
#
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i] > a[j]:
#             t = a[i]
#             a[i] = a[j]
#             a[j] = t
# for i in range(len(a)):
#     print(a[i],end=" ")


'''
有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？分别是什么？
'''


# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#             if x != y and y != z and x != z:
#                 print(x*100+y*10+z,end="\t")


'''
求0-7所有能组成的奇数个数
'''


# s = 1
# sum_ = 0
#
# for i in range(1, 9):
#     if i == 1: #1位数是只有1 3 5 7
#         s = 4
#     elif i == 2:
#         s = 4 * 7 #第一位不能为0 所以4*7
#     if i > 2:
#         s *= 8 #除了第一位7 最后一位4 其他为8  所以为*8
#     sum_ += s
#
#     print('%d位数的奇数个数为%d' % (i, s))
#
# print('总和为：sum=%d' % sum_) # 4+(4*7)+(4*7*8)+(4*7*8*8)+(4*7*8*8*8)+(4*7*8*8*8*8)+(4*7*8*8*8*8*8)+(4*7*8*8*8*8*8*8)= 8388608



'''
购物车程序
'''

# # 定义商品
# good_name= ['苹果', '鸭梨', '黄桃', '山楂', ]
# good_Price = [10, 5, 20,15]
# status = True
#
# #输入工资
#
# wages = input('请输入你的工资：').strip()
# if wages.upper() == 'Q':
#     status = False
# elif wages.isdigit():
#     wages = int(wages)
# else:
#     status = False
#     print('你输入有误！')
#
# while status:
#
#     #打印商品
#     print('编号\t商品名称\t单价(元)')
#
#     for i in range(len(good_Price)):
#         print('%s\t%s\t\t%s'%(i+1,good_name[i],good_Price[i]))
#
#     #输入购买
#     temp = 0
#     good_num = input('请输入商品编号：').strip()#输入商品名称
#     if good_num.upper() == 'Q':
#         status = False
#         break
#     elif good_num.isdigit() and int(good_num) > 0 and int(good_num) <= len(good_name):
#                 num = input('请输入商品数量：').strip() #输入商品数量
#                 if num.upper() == 'Q':
#                     status = False
#                     break
#                 elif num.isdigit():
#                     #购买流程
#
#                     #显示够买商品信息及数量
#                     print('你要买的商品信息如下：\n编号\t商品名称\t单价(元)\t数量(斤)')
#                     print('%s\t%s\t\t%s\t\t%s'%(good_num,good_name[int(good_num)-1],good_Price[int(good_num)-1],num))
#
#                     # 判断工资是否足够
#                     if wages >= good_Price[int(good_num)-1] * int(num):
#                         wages = wages - good_Price[int(good_num)-1] * int(num)
#                         print('工资余额：', wages)
#
#                         # 判断是否继续购买
#                         status_2 = input('你是否继续购买(Y/N):')
#                         if status_2.upper() == 'Q':
#                             status = False
#                             continue
#                         elif status_2.upper() == 'Y':
#                             continue
#                         elif status_2.upper() == 'N':
#                             status = False
#                             continue
#                         else:
#                             print('你输入有误！')
#                             continue
#                     else:
#                         print('你的工资余额不足，请重新选择！')
#                         continue
#                 else:
#                     print('你输入有误！请重新选择商品')
#                     continue
#     else:
#         print('没有你要买的商品')




'''
字符串函数
'''
# str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# str2 = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
#
# a = 'sdsdsfdAdsdsdfsfdASDSDFDSFa'
#
# print(a.translate(str.maketrans(str1,str2)).swapcase())
#
# print(a.swapcase().translate(str.maketrans(str1,str2)))



'''
字符串分析
'''

# #通过索引找出连续同类型字符放在一起输出
# def continuity_char(fun,fun_no):
#     temp = []
#     t = fun_no[0]
#     for i in range(1,len(fun_no)):
#
#         if fun_no[i] - fun_no[i-1] != 1 :
#             temp.append(''.join(fun[t:fun_no[i-1]+1]))
#             t = fun_no[i]
#         elif i == len(fun_no)-1:
#             temp.append(''.join(fun[t:fun_no[i]+1]))
#     return temp
#
#
# #获取对应分类索引号
# def str_parse(fun):
#     num_no = []
#     chi_no = []
#     letter_no = []
#     sym_no = []
#     for i in range(len(fun)):
#         if fun[i].isdecimal():
#             num_no.append(i)
#         elif fun[i].isupper() or fun[i].islower():
#             letter_no.append(i)
#         elif fun[i].isalpha():
#             chi_no.append(i)
#         else:
#             sym_no.append(i)
#
#     print("数字：",',\t'.join(continuity_char(fun,num_no)))
#     print("中文：",',\t'.join(continuity_char(fun,chi_no)))
#     print("拼音：",',\t'.join(continuity_char(fun,letter_no)))
#     print("字符：",',\t'.join(continuity_char(fun,sym_no)))
#
# #主调用函数
# if __name__ == '__main__':
#     str_test =input("请输入你要分析的字符串：")
#     str_parse(str_test)



'''
写一个函数，判断传入对象长度是否大于5
'''

# def re_length(*args):
#     if len(*args) > 5:
#         return True
#     else:
#         return False
#
#
# test1 = 'stasdfdfa'
# test2 = 'ass'
# test3 = [1,2,3,4,5,6,7]
# test4 = [1,2,3]
# test5 = (1,2,3,4,5,6)
# test6 = (1,2)
# test7 = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6}
# test8 = {'1':1,'2':2,'3':3}
#
# print(re_length(test1))
# print(re_length(test2))
# print(re_length(test3))
# print(re_length(test4))
# print(re_length(test5))
# print(re_length(test6))
# print(re_length(test7))
# print(re_length(test8))
#
#
# def re_list(list):
#
#     if len(list)>2:
#         return list[:2]
#     else:
#         return False
#
# print(re_list([1,2,3,4,5,6,7]))
# print(re_list([1]))
#
# def re_dic(str1,dic):
#     t = 0
#     for key in dic.keys():
#         if key == str1:
#             t += 1
#
#     if t == 0 :
#         dic[len(dic)] = str1
#     return dic
#
# print(re_dic('sdfsdf',{'1':1,'2':2,'3':3,'4':4,'5':5,'6':6}))
#
#
# static1 = True
# static2 = True
# sum1 = 0
# def re(sex,age):
#     if sex == 'F' and age >= 10 and age <= 15 :
#         return True
#     else:
#         return False
#
# while static1:
#     sex = input("请输入性别(男M/女F)：")
#     age = int(input("请输入年龄："))
#
#     if re(sex.upper(),age):
#         print("此人可以加入！")
#         sum1 += 1
#     else:
#         print("此人不可以加入！")
#     static2 = True
#     while static2:
#         t = input("是否继续输入(Y/N)：")
#
#         if t.upper() == 'Y':
#             static2 = False
#         elif t.upper() == 'N':
#             print('一共加入%d人'%sum1)
#             static2 = False
#             static1 = False
#         else:
#             static2 = True


