# -*- coding:utf-8 -*-
import os
import pymysql
import time
import tkinter
import tkinter.messagebox
import Student
import Teacher
import SystemManager


class Login:
    def __init__(self, conn):
        self.account = ''
        self.password = ''
        self.level = 2
        self.conn = conn
        self.err_time = 3

    def MainFunc(self, _gui_root, _account, _password):
        err = ''
        self.account = _account
        self.password = _password
        if self.err_time <= 0:
            tkinter.messagebox.showerror(title='教务管理系统', message='警告！输入错误次数太多！系统自动退出')
            _gui_root.destroy()
        elif self.account == '':
            tkinter.messagebox.showerror(title='教务管理系统', message='警告！用户名不能为空！')
        elif self.CheckAccount():


            _gui_root.destroy()
            account = self.GetLoginAccount()
            if account[2] == 0:
                usr = SystemManager.SystemManager(self.conn, account[0], account[1])
                usr.MainFunc()
            elif account[2] == 1:
                usr = Teacher.Teacher(self.conn, account[0], account[1])
                usr.MainFunc()
            elif account[2] == 2:
                usr = Student.Student(self.conn, account[0], account[1])
                usr.MainFunc()
        else:
            self.err_time = self.err_time - 1
            tkinter.messagebox.showerror(title='教务管理系统',
                                         message='用户名或密码错误!\n您还能输入' + str(self.err_time) + '次')

    def login_res(self, _root):
        def login_run():
            cur = self.conn.cursor()
            # 用get提取
            new_user_name = new_var_name.get()
            new_user_real_name = new_var_user_name.get()
            new_user_password = new_var_password.get()
            repeat_user_password = repeat_var_password.get()

            if new_user_password != repeat_user_password:
                tkinter.messagebox.showerror(title='教务管理系统', message='警告！您输入的两次密码不一致！')
                """"""
            elif 0 != cur.execute("select Account,Password,AccountLevel "
                                  "from LoginAccount where Account = '%s'" % new_user_name):
                tkinter.messagebox.showerror(title='教务管理系统', message='警告！您输入的用户名已存在！')
            elif new_user_real_name == '':
                tkinter.messagebox.showerror(title='教务管理系统', message='警告！姓名不能为空！')
            elif new_user_name == '':
                tkinter.messagebox.showerror(title='教务管理系统', message='警告！用户名不能为空！')
            elif new_user_password == '':
                tkinter.messagebox.showerror(title='教务管理系统', message='警告！密码不能为空！')
            else:
                # login_user_info[new_user_name] = new_user_password
                try:
                    # insert into loginaccount(Account, Password, AccountLevel, sname) values('2002', '123', '2', '456')
                    sqlWord = "insert into loginaccount(Account, Password, AccountLevel, sname) values ('%s', '%s', '2', '%s')" % (
                        new_user_name, new_user_password, new_user_real_name)
                    cur.execute(sqlWord)
                    self.conn.commit()
                    tkinter.messagebox.showinfo(title='教务管理系统', message='注册成功，欢迎您')
                except Exception as e:
                    print(e)
                    tkinter.messagebox.showinfo(title='教务管理系统', message='注册失败，错误' + e.__str__())
                finally:
                    root_login.destroy()
            cur.close()

        root_login = tkinter.Toplevel(_root)
        root_login.title('教务管理系统')
        root_login.geometry('350x350+550+200')
        a = tkinter.Label(root_login, text='欢迎进入注册界面', font=('Arial', 10))
        a.pack()

        # 注册窗口界面
        # 注册用户名
        new_var_name = tkinter.StringVar()  # 将输入框里面的东西拿出来
        show_new_name = tkinter.Label(root_login, text='新用户名', font=('Arial', 9))
        show_new_name.place(x=70, y=50)
        input_new_name = tkinter.Entry(root_login, textvariable=new_var_name, show=None)
        input_new_name.place(x=125, y=50)

        # 注册密码
        new_var_password = tkinter.StringVar()  # 将输入框里面的东西拿出来
        show_new_password = tkinter.Label(root_login, text='新的密码', font=('Arial', 9))
        show_new_password.place(x=70, y=100)
        input_new_password = tkinter.Entry(root_login, textvariable=new_var_password, show='*')
        input_new_password.place(x=125, y=100)

        # 重复注册密码
        repeat_var_password = tkinter.StringVar()  # 将输入框里面的东西拿出来
        show_repeat_password = tkinter.Label(root_login, text='重复密码', font=('Arial', 9))
        show_repeat_password.place(x=70, y=150)
        input_repeat_password = tkinter.Entry(root_login, textvariable=repeat_var_password, show='*')
        input_repeat_password.place(x=125, y=150)

        new_var_user_name = tkinter.StringVar()  # 将输入框里面的东西拿出来
        show_new_user_name = tkinter.Label(root_login, text='姓名', font=('Arial', 9))
        show_new_user_name.place(x=70, y=200)
        input_new_user_name = tkinter.Entry(root_login, textvariable=new_var_user_name, show=None)
        input_new_user_name.place(x=125, y=200)

        # 注册界面按钮
        login_button1 = tkinter.Button(root_login, text='注册', width=7, command=login_run)
        login_button1.place(x=115, y=230)
        login_button2 = tkinter.Button(root_login, text='取消', width=7, command='quit')
        login_button2.place(x=205, y=230)

    def CheckAccount(self):
        cur = self.conn.cursor()
        sqlcmd = "select Account,Password,AccountLevel from LoginAccount where Account = '%s'" % self.account
        if cur.execute(sqlcmd) == 0:
            login_s = tkinter.messagebox.askokcancel(title='教务管理系统',
                                                     message='您输入的用户名不存在，您需要要创建新用户吗')
        else:
            temp = cur.fetchone()
            cur.close()
            if temp[1] == self.password:
                self.level = temp[2]
                return True
            else:
                return False


if __name__ == '__main__':
    conn = pymysql.connect(user='root', passwd='root', db='student2022');
    a = Login(conn)
    # a.MainFunc()
    a.login_res()
    a.Quit()
    conn.close()
