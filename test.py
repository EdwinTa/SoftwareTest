# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/10


# if __name__ == '__main__':
#     a = 0o77    #a的二进制00111111
#     b = a & 3   #3的二进制00000011，1&1 =1 1&0=0  0&1=0  0&0=0 所以 b此时为00000011，
#
#     print('{0:b}'.format(a))
#     print('{0:b}'.format(7))
#
#
#     print('a & b = %d' % b) # b此时为00000011，a此时为00111111 通过位运算后 a&b = 00000011 所以最后输出结果3
#     b &= 7 #b此时为00000011，7的二进制00000111 结果 00000011
#     print('a & b = %d' % b)

# if __name__ == '__main__':
#     from tkinter import *
#
#     canvas = Canvas(width=800, height=600, bg='yellow')
#     canvas.pack(expand=YES, fill=BOTH)
#     k = 1
#     j = 1
#     for i in range(0, 26):
#         canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
#         k += j
#         j += 0.3
#
#     mainloop()

# if __name__ == '__main__':
#     import turtle
#     turtle.title("画圆")
#     turtle.setup(800,600,0,0)
#     pen=turtle.Turtle()
#     pen.color("red")
#     pen.width(1)
#     pen.shape("turtle")
#     pen.speed(1)
#     pen.circle(100)


# import math as m
# import matplotlib.pyplot as plt
#
# x = []
# y = []
# for a in range(1, 11):
#     for b in range(0, 360):
#         x.append(a * (m.cos(m.pi * (b / 180))))
#         y.append(a * (m.sin(m.pi * (b / 180))))
# plt.scatter(x, y, s=3)
# plt.axis([-11, 11, -11, 11])
# # 避免因比例而压缩为椭圆
# plt.axis('equal')
# plt.show()


# if __name__ == '__main__':
#     from tkinter import *
#
#     canvas = Canvas(width=300, height=300, bg='green')
#     canvas.pack(expand=YES, fill=BOTH)
#     x0 = 263
#     y0 = 263
#     y1 = 275
#     x1 = 275
#     for i in range(19):
#         canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
#         x0 = x0 - 5
#         y0 = y0 - 5
#         x1 = x1 + 5
#         y1 = y1 + 5
#
#     x0 = 263
#     y1 = 275
#     y0 = 263
#     for i in range(21):
#         canvas.create_line(x0, y0, x0, y1, fill='red')
#         x0 += 5
#         y0 += 5
#         y1 += 5
#
#     mainloop()


# import turtle
#
# def drawline(n):
#     t=turtle.Pen()
#     t.color(0.3,0.8,0.6)  #设置颜色，在0--1之间
#     t.begin_fill()   #开始填充颜色
#     for i in range(n): #任意边形
#         t.forward(50)
#         t.left(360/n)
#     t.end_fill()    #结束填充颜色
#
# drawline(10)


# from tkinter import *
# canvas=Canvas(width=300,height=300,bg='white')
# canvas.pack(expand=YES, fill=BOTH)
# x1,y1=50,20
# x2,y2=100,20
# x3,y3=75,40
# x4,y4=75,100
# canvas.create_line(x1,y1,x3,y3, width=3, fill='red')
# canvas.create_line(x2,y2,x3,y3, width=3, fill='red')
# canvas.create_line(x1,y1,x4,y4, width=3, fill='red')
# canvas.create_line(x2,y2,x4,y4, width=3, fill='red')
# mainloop()

# if __name__ == '__main__':
#     from tkinter import *
#
#     root = Tk()
#     root.title('Canvas')
#     canvas = Canvas(root, width=400, height=400, bg='yellow')
#     x0 = 263
#     y0 = 263
#     y1 = 275
#     x1 = 275
#     for i in range(19):
#         canvas.create_rectangle(x0, y0, x1, y1)
#         x0 -= 5
#         y0 -= 5
#         x1 += 5
#         y1 += 5
#
#     canvas.pack()
#     root.mainloop()


# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.email = "qiwsir@gmail.com"     #这个属性不是通过参数传入的
# info = Person("qiwsir")              #换个字符串和实例化变量
# print("info.name=",info.name)
# print("info.email=",info.email)      #info 通过 self 建立实例，并导入实例属性数据


# import time
#
#
# def timmer(func):
#     def warpper(*args,**kwargs):
#         start_time = time.time()
#         res=func(*args,**kwargs)
#         stop_time = time.time()
#         print("the func run time is %s " % (stop_time - start_time))
#         return res
#     return warpper
#
#
# @timmer
# def test1():
#     time.sleep(2)
#     print("in the test1")
#
#
# @timmer
# def test2():
#     time.sleep(2)
#     print("he is name:")
#
# test1()
# test2()


# user = "jason"
# passwd = "123123"
#
# def auth(auth_type):
#     print(auth_type)
#     def outer_wrapper(func):
#         def wrapper(*args, **kwargs):
#             if auth_type == "local":
#                 username = input("Username:").strip()
#                 password = input("Password:").strip()
#
#                 if user == username and passwd == password:
#                     print("\033[32;1mUser has passed or authentication\033[0m")
#                     res = func(*args, **kwargs)
#                     print("------------------")
#                     return res
#                 else:
#                     exit("\033[31;1mInvalid username or password\033[0m")
#             elif auth_type == "ldep":
#                 print("**********")
#
#         return wrapper
#     return outer_wrapper
# def index():
#     print("welcome to index page")
# @auth(auth_type ="local")
# def home():
#     print("welcome to home page")
#     return "from name"
# @auth(auth_type="ldep")
# def bbs():
#     print("welcome to bbs page")
#
#
# index()
# print(home())
# bbs()


