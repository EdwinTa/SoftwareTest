# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/9

'''
输入某年某月某日，判断这一天是这一年的第几天？
'''

import time

D=input("请输入年份，格式如XXXX-XX-XX：")
d=time.strptime( D,'%Y-%m-%d').tm_yday
print("the {} day of this year!" .format(d))