# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/10

'''
利用条件运算符的嵌套来完成此题：高于90分的学习成绩用A表示，60分到89分之间的学习成绩用B表示，60分一下的学习成绩用C表示
'''
score = int(input('input(0~100):'))
if score >89:
    print('A')
elif score>59 and score<90:
    print('B')
else:
    print('C')