# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/24

'''
编写一个程序，使用关键字static定义静态变量
'''
def varfunc():
    var = 0
    print( 'var = %d'% var)
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()

# 类的属性
# 作为类的一个属性吧
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)

print(Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()