# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/9

str = 'I Love Python!'
#原字符串输出
print(str)
#大小写转换输出
print(str.swapcase())
#全部大写
print(str.upper())
#全部小写
print(str.lower())
#单词首字母大写
print(str.title())
#检查是否单词首字母大写
print(str.istitle())
#检查字符串是否都时小写
print(str.islower())
#检查字符串是否首字母大写
print(str.capitalize())
#获取字符串中字符'u'的起始位置
print(str.find('u'))
#获取字符串中字符'a'的数目
print(str.count('a'))
#分割字符串，以空格为界
print(str.split(' '))
#连接字符串
print(''.join(' life is short'))
#获取字符串长度
print(len(str))