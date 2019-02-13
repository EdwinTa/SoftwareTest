# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/13

import requests

# 登录接口
data={'loginName':'admin','password':'e10adc3949ba59abbe56e057f20f883e'}
res = requests.post('http://47.95.212.66:8080/cpqp-management/admin/login',data)
print(res.json())

# 用户合并接口
data1= {'masterId':'u10609','mergedId':'u10897'}
res1= requests.post('http://47.95.212.66:8080/cpqp-management/userManager/mergeUser',data1)
print(res1.json())

data1= {'orderId':'u10609',}
res1= requests.get('http://47.95.212.66:8080/cpqp-management/orderManager/commissionOneOrder',data1)
print(res1.json())