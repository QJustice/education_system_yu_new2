import tkinter


class RegisterUi:
    """注册UI"""

    def __init__(self, _root):
        """建立UI界面并初始化"""
        # _root 主窗口
        # 主窗口上创建注册界面
        self.root_login = tkinter.Toplevel(_root)
        # 接收注册函数
        self.res_fun = None

    def run_ui(self, _res):
        """建立UI界面细节"""
        # 获取注册函数
        self.res_fun = _res
        # 注册界面标题
        self.root_login.title('教务管理系统')
        # 设置注册界面大小和弹出的位置
        self.root_login.geometry('350x350+550+200')
        # 设置欢迎字样
        wel = tkinter.Label(self.root_login, text='欢迎进入注册界面', font=('Arial', 10))
        # 放置欢迎字样
        wel.pack()
        # 注册窗口界面
        # 注册用户名
        # 将输入框里面的东西拿出来，用于接收用户输入的新用户名
        new_var_name = tkinter.StringVar()
        # 设置新用户名字样
        show_new_name = tkinter.Label(self.root_login, text='新用户名', font=('Arial', 9))
        # 放置新用户名字样
        show_new_name.place(x=70, y=50)
        # 设置新用户名输入框
        input_new_name = tkinter.Entry(self.root_login, textvariable=new_var_name)
        # 放置新用户名输入框
        input_new_name.place(x=125, y=50)

        # 注册密码
        # 将输入框里面的东西拿出来，用于接收用户输入的注册密码
        new_var_password = tkinter.StringVar()
        # 设置新的密码字样
        show_new_password = tkinter.Label(self.root_login, text='新的密码', font=('Arial', 9))
        # 放置新的密码字样
        show_new_password.place(x=70, y=100)
        # 设置新的密码输入框
        input_new_password = tkinter.Entry(self.root_login, textvariable=new_var_password, show='*')
        # 设置新的密码输入框
        input_new_password.place(x=125, y=100)

        # 重复注册密码
        # 将输入框里面的东西拿出来，用于接收用户输入的重复注册密码
        repeat_var_password = tkinter.StringVar()
        # 设置重复密码字样
        show_repeat_password = tkinter.Label(self.root_login, text='重复密码', font=('Arial', 9))
        # 放置重复密码字样
        show_repeat_password.place(x=70, y=150)
        # 设置重复注册密码输入框
        input_repeat_password = tkinter.Entry(self.root_login, textvariable=repeat_var_password, show='*')
        # 放置重复注册密码输入框
        input_repeat_password.place(x=125, y=150)

        # 真实姓名
        # 将输入框里面的东西拿出来，用于接收用户输入的真实姓名
        new_var_user_name = tkinter.StringVar()
        # 设置姓名字样
        show_new_user_name = tkinter.Label(self.root_login, text='姓名', font=('Arial', 9))
        # 放置姓名字样
        show_new_user_name.place(x=70, y=200)
        # 设置真实姓名输入框
        input_new_user_name = tkinter.Entry(self.root_login, textvariable=new_var_user_name, show=None)
        # 放置真实姓名输入框
        input_new_user_name.place(x=125, y=200)
        # 获取用户名
        new_user_name = new_var_name.get()
        # 获取真实姓名
        new_user_real_name = new_var_user_name.get()
        # 获取密码
        new_user_password = new_var_password.get()
        # 获取重复密码
        repeat_user_password = repeat_var_password.get()
        # 注册界面按钮
        login_button1 = tkinter.Button(self.root_login,
                                       text='注册',
                                       width=7,
                                       command=lambda: self.res_fun(self.root_login, new_var_name.get(),
                                                                    new_var_user_name.get(),
                                                                    new_var_password.get(),
                                                                    repeat_var_password.get()))
        # 放置注册界面注册按钮
        login_button1.place(x=115, y=230)
        # 设置注册界面取消按钮
        login_button2 = tkinter.Button(self.root_login, text='取消', width=7, command=self.root_login.destroy)
        # 放置注册界面取消按钮
        login_button2.place(x=205, y=230)

    def stop_ui(self):
        """关闭UI"""
        # 关闭UI主窗口
        self.root_login.destroy()
