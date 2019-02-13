# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/10

'''
输入一行字符，分别统计出其中的英文字母，空格，数字和其他字符的个数
'''

str=input('input string:')

strnum,spacenum,snum,tnum=0,0,0,0
resoult = {}
for i in str:
    if i.isalnum():
        if i.isdigit():
            snum+=1
        else:
            strnum+=1
    else:
        tnum+=1
    resoult[i]=str.count(i)
print(resoult)
print(len(resoult))
spacenum=resoult.get(' ')
print(strnum,spacenum,snum,(tnum-spacenum))
