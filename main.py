# -*- coding:utf-8 -*-
####系统入口
import os
import pymysql
# import data_load
import Student
import Teacher
import Login
import SystemManager
import tkinter.messagebox
import ConnectDatabase
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

if __name__ == '__main__':
    condaba = ConnectDatabase.ConData()
    conn = condaba.get_con_database()
    log = Login.Login(conn)
    root = tkinter.Tk()
    root.resizable(False, False)
    # 主要界面
    root.title('教务管理系统')
    # 加后面的数字是为了改变界面弹出来的位置
    root.geometry('500x300+450+200')
    bgImage = tkinter.PhotoImage(file="image_1.png")
    labbg = tkinter.Label(image=bgImage)
    labbg.pack()
    labTop = tkinter.Label(root, text='欢迎来到教务管理系统\n请登录', bg='white', font=('华文行楷', 20))
    labTop.place(x=120, y=50)
    labTopNext = tkinter.Label(root, text='教务管理系统', font='华文行楷')
    labTopNext.place(x=200, y=120)

    # 用户名
    # inImage = tkinter.PhotoImage(file="entry_1.png")
    var_login_name = tkinter.StringVar()  # 将输入框里面的东西拿出来
    show_login_name = tkinter.Label(root, bg='yellow', text='用户名:', font=('华文行楷', 12), width=8)
    show_login_name.place(x=140, y=160)
    # inputIamge = tkinter.Label(root, image=inImage, font=('Arial', 8))
    # inputIamge.place(x=195, y=140)
    input_login_name = tkinter.Entry(root, textvariable=var_login_name, show=None, width=20)
    input_login_name.place(x=230, y=160)

    # 密码
    var_password = tkinter.StringVar()  # 将输入框里面的东西拿出来
    show_password = tkinter.Label(root, bg='yellow', text='密码:', font=('华文行楷', 12), width=8)
    show_password.place(x=140, y=190)
    input_password = tkinter.Entry(root, textvariable=var_password, show='*', width=20)
    input_password.place(x=230, y=190)

    # 主界面按钮 x间距50 y间距相等
    button1 = tkinter.Button(root, text='登录', width=5,
                             bg='blue',
                             font='华文行楷',
                             command=lambda: log.MainFunc(root, var_login_name.get(), var_password.get()))  # 生成button1
    button1.place(x=130, y=220)
    button2 = tkinter.Button(root, font='华文行楷', bg='blue', text='注册', width=5, command=lambda :log.login_res(root))
    button2.place(x=220, y=220)
    button3 = tkinter.Button(root, font='华文行楷', bg='blue', text='忘记密码')
    button3.place(x=310, y=220)

    root.mainloop()  # 进入消息循环（必需组件）
    condaba.clos_con(conn)
