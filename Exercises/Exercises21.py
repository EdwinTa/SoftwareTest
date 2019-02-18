# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/11

'''
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''


m=['a','b','c']
n=['x','y','z']
l=[]
for i in range(3):
    for j in range(3):
        l.append(m[i]+n[j])
l.remove('ax')
l.remove('cx')
l.remove('cz')
l.remove('ay')
l.remove('by')
l.remove('bz')
print(l)