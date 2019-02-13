# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/10


'''
输出指定格式日期，使用datetime模块
'''
import datetime

year=int(input('input Year:'))
month=int(input('input Month:'))
day=int(input('input Day:'))

a=datetime.date(year,month,day)
print(a.__format__('%Y-%m-%d'))