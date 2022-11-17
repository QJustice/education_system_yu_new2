# -*- coding:utf-8 -*-
import tkinter
import tkinter.messagebox

import pymysql

import Student
import SystemManager
import Teacher
import register_ui


class Login:
    """处理登录函数"""

    def __init__(self, _conn):
        # 用户名
        self.account = ''
        # 密码
        self.password = ''
        # 用户等级
        self.level = 2
        # 数据库连接
        self.conn = _conn
        # 密码可错误次数
        self.err_time = 3

    def MainFunc(self, _gui_root, _account, _password):
        """登录"""
        # 用户名
        self.account = _account
        # 密码
        self.password = _password
        # 试错机会是否耗尽
        if self.err_time <= 1:
            # 密码输入错误太多
            tkinter.messagebox.showerror(title='教务管理系统', message='警告！输入错误次数太多！系统自动退出')
            # 关闭登录界面
            _gui_root.destroy()
        else:
            # 用户名不能为空
            if self.account == '':
                tkinter.messagebox.showerror(title='教务管理系统', message='警告！用户名不能为空！')
            else:
                # 判断密码是否正确并获取判断结果
                checkreturn = self.CheckAccount(_gui_root)
                if "ok" == checkreturn:
                    # 密码正确
                    tkinter.messagebox.showinfo(title='教务管理系统', message='登录成功')
                    tkinter.messagebox.showinfo(title='教务管理系统', message='请稍后...')
                    # 关闭登录界面
                    _gui_root.destroy()
                    # 获取用户身份等级
                    account = self.GetLoginAccount()
                    # 管理员
                    if account[2] == 0:
                        usr = SystemManager.SystemManager(self.conn, account[0], account[1])
                        usr.MainFunc()
                    # 教职工
                    elif account[2] == 1:
                        usr = Teacher.Teacher(self.conn, account[0], account[1])
                        usr.MainFunc()
                    # 学生
                    elif account[2] == 2:
                        usr = Student.Student(self.conn, account[0], account[1])
                        usr.MainFunc()
                elif "err" == checkreturn:
                    # 密码错误
                    # 试错机会减一
                    self.err_time = self.err_time - 1
                    # 提示用户剩余可用机会
                    tkinter.messagebox.showerror(title='教务管理系统',
                                                 message='用户名或密码错误!\n您还能输入' + str(self.err_time) + '次')
                else:
                    # 用户注册了新账户
                    pass

    def CheckAccount(self, _ui_root):
        """判断密码是否正确"""
        # 数据库游标
        cur = self.conn.cursor()
        # 用于数据库查询的语句
        sqlcmd = "select Account,Password,AccountLevel from LoginAccount where Account = '%s'" % self.account
        # 未查询到任何匹项
        if cur.execute(sqlcmd) == 0:
            login_s = tkinter.messagebox.askokcancel(title='教务管理系统',
                                                     message='您输入的用户名不存在，您需要要创建新用户吗')
            # 用户试图注册新账户
            if login_s:
                self.login_res(_ui_root)
                return "res"
            # 用户不打算注册新账户
            else:
                return "err"
        # 查询到用户信息
        else:
            # 获取用户信息
            temp = cur.fetchone()
            # 关闭游标
            cur.close()
            # 匹配用户输入的密码和数据库中的密码
            # 密码匹配成功
            if temp[1] == self.password:
                # 获取用户等级
                self.level = temp[2]
                # 允许登录
                return "ok"
            else:
                # 不允许登录
                return "err"

    def GetLoginAccount(self):
        """获取用户等级"""
        # 返回用户等级
        return [self.account, self.password, self.level]

    def login_res(self, _root):
        """注册"""

        def login_run(_res_ui, _user, _real, _password, _repassword):
            """核验注册信息"""
            cur = self.conn.cursor()
            # 用get提取用户注册信息
            # 获取用户名
            new_user_name = _user
            # 获取真实姓名
            new_user_real_name = _real
            # 获取注册密码
            new_user_password = _password
            # 获取重复密码
            repeat_user_password = _repassword
            # 校验两次密码
            if new_user_password != repeat_user_password:
                tkinter.messagebox.showerror(title='教务管理系统', message='警告！您输入的两次密码不一致！')
            # 当前真实用户名是否为空
            elif new_user_real_name == '':
                tkinter.messagebox.showerror(title='教务管理系统', message='警告！姓名不能为空！')
            # 当前用户名是否为空
            elif new_user_name == '':
                tkinter.messagebox.showerror(title='教务管理系统', message='警告！用户名不能为空！')
            # 当前密码是否为空
            elif new_user_password == '':
                tkinter.messagebox.showerror(title='教务管理系统', message='警告！密码不能为空！')
            # 当前用户名是否存
            elif 0 != cur.execute("select Account,Password,AccountLevel "
                                  "from LoginAccount where Account = '%s'" % new_user_name):
                tkinter.messagebox.showerror(title='教务管理系统', message='警告！您输入的用户名已存在！')
            else:
                try:
                    # insert into loginaccount(Account, Password, AccountLevel, sname) values('2002', '123', '2', '456')
                    # mysql插入语句
                    sql_word = "insert into loginaccount(Account, Password, AccountLevel, sname) values ('%s', '%s', " \
                               "'2', '%s')" % (new_user_name, new_user_password, new_user_real_name)
                    # 执行mysql语句插入数据
                    cur.execute(sql_word)
                    # 提交数据
                    self.conn.commit()
                    tkinter.messagebox.showinfo(title='教务管理系统', message='注册成功，欢迎您')
                except Exception as e:
                    # 提示异常
                    tkinter.messagebox.showinfo(title='教务管理系统', message='注册失败，错误' + e.__str__())
                finally:
                    # 关闭注册界面
                    _res_ui.destroy()
            # 关闭游标
            cur.close()

        # 建立注册UI需要提供根界面
        res_ui = register_ui.RegisterUi(_root)
        # 开启登录UI
        # 需要提供注册信息函数
        res_ui.run_ui(login_run)

    def forgot_password(self):
        """忘记密码"""
        tkinter.messagebox.showinfo(title='教务管理系统', message='请联系统管理员重置密码！')


if __name__ == '__main__':
    conn = pymysql.connect(user='root', passwd='root', db='student2022');
    a = Login(conn)
    conn.close()
