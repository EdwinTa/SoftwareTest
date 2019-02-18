# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2019/2/15


'''
数字加减运算通关游戏。要求，第一关10以内数字相加减，第二关20以内数字相加减，一直到第十关的100以内数字相加减。
保证减法时，大数减去小数。
每一关答对9道题，算通关，否则通关失败，提示是否继续游戏，如果继续，从第一关重新开始。
'''

#引入包
import random

#加法运算
def add(num1,num2):
    print('%d + %d =' %(num1,num2),end=" ")
    numSum = int(input())
    if (num1 + num2) == numSum:
        print('√')
        return 1
    else:
        print('X')
        return 0

#减法运算
def sub(num1,num2):
    print('%d - %d =' %(num1,num2),end=" ")
    numSum = int(input())
    if (num1 - num2) == numSum:
        print('√')
        return 1
    else:
        print('X')
        return 0

#随机生成数
def rangeNum(n):
    return random.randint(0,n*10)

#判断哪一种运算
def operation():
    return random.randint(0,1)

#闯关
def gamePass(n):
    i = 0

    for j in range(1,11):
        num1 = rangeNum(n)
        num2 = rangeNum(n)
        if num1 >= num2:
            if operation():
                i += add(num1,num2)
            else:
                i += sub(num1,num2)
        else:
            i += add(num1, num2)
    return i
#游戏
def playGame():
    for i in range(10,11):
        print("第%d关闯关开始" % i)
        print("%d以内的数字相加减，共10题，答对9题，闯关成功，进入下一关！" % (i*10))
        if gamePass(i) >= 9:
            print("第%d关闯关成功"%i)
        else:
            print("闯关失败")
            temp = input('是否继续游戏？(y/n)').upper()
            if temp == 'Y':
                playGame()
            elif temp == 'N':
                print('游戏结束')
                break
            else:
                print('输入错误,游戏结束！')
                break


playGame()


'''
通过代码实现一下配置文件config.conf,内容如下：
Host:
    www.jd.com
Port:
    8080
Ip:
    10.11.12.13
Addr:
    xxxxxxxxxxx
请把配置文件中端口号8080修改为8090，请在Ip10.11.12.13下面再增加一个ip为11.12.13.14
通过代码，实现以上需求，把配置文件的内容更改为：
Host:
    www.jd.com
Port:
    8090
Ip:
    10.11.12.13
    11.12.13.14
Addr:
    xxxxxxxxxxx
'''
import os,re

#拼接路径
confname = os.path.join(os.getcwd(),"config.conf")

#读取文件内容到列表
f = open(confname,'r+')
list1 = f.readlines()

#获取字符串位置
num =0
for i in list1:

    n = re.findall(r"10.11.12.13", i)

    if n:
        break
    num += 1

#向指定位置插入数据
list1.insert((num+1),'\t11.12.13.14\n')
s = ''.join(list1)
f = open(confname,'w+')
f.writelines(s)

#打印文件
for i in list1:

    print(i,end='')

#关闭文件
f.close()




'''
随机生成20个域名，拼接成如下结构：
D = {"version":123456,"add_domains":
    [{"1fdix.1bka.axy1.com":{"host":"1fdix.1bka.axy1.com","preproy":"switch","TLL":0}},
   {"rus1f.07hf.2xms.com":{"host":"rus1f.07hf.2xms.com","preproy":"switch","TLL":1}},
  {"cqphe.r7mw.nh6u.com":{"host":"cqphe.r7mw.nh6u.com","preproy":"switch","TLL":2}},
   {"sz8al.d69n.2b6o.com":{"host":"sz8al.d69n.2b6o.com","preproy":"switch","TLL":3}}]}
   保证add_domains的域名内容都是随机生成的，对应的TLL内容也不断递增。
其中，域名都是以com结尾，且com前由三部分组成，第一部分是随机的5位，后两部分是随机的4位。
'''
import random,string

D = {"version":123456,"add_domains":[]}

def urlstr(n):
    return ''.join(random.sample(string.ascii_lowercase + string.digits,n))

for i in range(20):
    url='.'.join((urlstr(5),urlstr(4),urlstr(4),"com"))
    D["add_domains"].append({url:{"host":url,"preproy":"switch","TLL":i}})
    print(D["add_domains"][i])


'''
1-9数字不重复实现@@@@*@=@@@@
把这个等式实现一下，看有几种结果
'''



######方法一######
print('方法一')
def addlist(i):
    for k in range(len(str(i))):
        if str(i)[k] != '0':
            date2.append(str(i)[k])




for i in range(1234,9878):
    for j in range(2,9):
        date2 = []
        addlist(i)
        addlist(j)
        if len(str(i*j)) ==4 :
            addlist(i*j)

        if len(set(date2)) == 9:
            print("%d * %d = %d" %(i,j,i*j))




######方法二######

print('方法二')
def dellist(i):
    try:
        date.remove(i)
    except:
        pass

def redate(result):
    for m in range(len(str(result))):
        dellist(int(str(result)[m]))


for i in range(1,10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                for x in range(2, 9):
                    date = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    dellist(i)
                    dellist(j)
                    dellist(k)
                    dellist(l)
                    dellist(x)
                    result = (i*1000+j*100+k*10+l)*x
                    redate(result)
                    if len(date) == 0 and len(str(result)) == 4:
                        print("%d * %d = %d" %(i*1000+j*100+k*10+l,x,result))
                    else:
                        continue
