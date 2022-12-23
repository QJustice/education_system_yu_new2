import tkinter


class LoginUi:
    """登录界面UI"""

    def __init__(self):
        """建立UI界面并初始化"""
        # 凳录界面UI主窗口
        self.root = tkinter.Tk()
        # 接收登录函数
        self.log_fun = None
        # 接收注册函数
        self.res_fun = None
        # 忘记密码函数
        self.fpd_fun = None

    def ui_run(self, _log, _res, _fpd):
        """建立UI界面细节"""
        # 接收登录函数
        self.log_fun = _log
        # 接收注册函数
        self.res_fun = _res
        # 接收忘记密码函数
        self.fpd_fun = _fpd
        # 锁定主窗口大小
        self.root.resizable(False, False)
        # 主要界面
        # 主界面标题
        self.root.title('教务管理系统')
        # 设置主界面大小和弹出的位置
        self.root.geometry('500x300+450+200')
        # 获取背景图
        bgImage = tkinter.PhotoImage(file="image_1.png")
        # 设置背景图
        labbg = tkinter.Label(image=bgImage)
        # 放置背景图
        labbg.pack()
        # 设置欢迎界面
        labTop = tkinter.Label(self.root,
                               text='欢迎来到教务管理系统\n请登录',
                               bg='white',
                               font=('华文行楷', 20))
        # 放置欢迎界面
        labTop.place(x=120, y=50)
        # 设置小字
        labTopNext = tkinter.Label(self.root,
                                   text='教务管理系统',
                                   font='华文行楷')
        # 放置小字
        labTopNext.place(x=200, y=120)

        # 用户名
        # 将输入框里面的东西拿出来，用于接收用户输入的用户名
        var_login_name = tkinter.StringVar()
        # 设置用户名字样
        show_login_name = tkinter.Label(self.root,
                                        bg='yellow',
                                        text='用户名:',
                                        font=('华文行楷', 12),
                                        width=8)
        # 放置用户名字样
        show_login_name.place(x=140, y=160)
        # 设置用户名输入框
        input_login_name = tkinter.Entry(self.root,
                                         textvariable=var_login_name,
                                         width=20)
        # 放置用户名输入框
        input_login_name.place(x=230, y=160)

        # 密码
        # 将输入框里面的东西拿出来用于接收密码
        var_password = tkinter.StringVar()
        # 设置密码字样
        show_password = tkinter.Label(self.root,
                                      bg='yellow',
                                      text='密码:',
                                      font=('华文行楷', 12),
                                      width=8)
        # 放置密码字样
        show_password.place(x=140, y=190)
        # 设置密码输入框
        input_password = tkinter.Entry(self.root,
                                       textvariable=var_password,
                                       show='*',
                                       width=20)
        # 放置密输入框
        input_password.place(x=230, y=190)

        # 主界面登录按钮 x间距50 y间距相等
        button1 = tkinter.Button(self.root,
                                 text='登录',
                                 width=5,
                                 bg='blue',
                                 font='华文行楷',
                                 command=lambda: self.log_fun(self.root, var_login_name.get(), var_password.get()))
        # 放置登录按钮
        button1.place(x=130, y=220)
        # 主界面注册按钮
        button2 = tkinter.Button(self.root,
                                 font='华文行楷',
                                 bg='blue',
                                 text='注册',
                                 width=5,
                                 command=lambda: self.res_fun(self.root))
        # 放置主界面注册按钮
        button2.place(x=220, y=220)
        # 设置主界面忘记密码按钮
        button3 = tkinter.Button(self.root,
                                 font='华文行楷',
                                 bg='blue',
                                 text='忘记密码',
                                 command=self.fpd_fun)
        # 放置主界面忘记密码按钮
        button3.place(x=310, y=220)
        # 显示主界面
        self.root.mainloop()

    def stop_ui(self):
        """关闭UI"""
        # 关闭UI主窗口
        self.root.destroy()
