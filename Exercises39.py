# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/24

'''
模仿静态变量用法
'''



class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print('The num = %d' % nNum)
        inst.inc()