# -*- coding:utf-8 -*-
# import data_load
import Login_ui
import Login
import ConnectDatabase

if __name__ == '__main__':
    """系统入口"""
    # 建立数据库连接
    condaba = ConnectDatabase.ConData(_host='127.0.0.1',
                                      _db='student2022',
                                      _port=3306,
                                      _user='root',
                                      _password='root',
                                      _charset='utf8')
    # 获取数据库连接
    conn = condaba.get_con_database()
    # 建立登录
    log = Login.Login(conn)
    # 建立登录UI
    log_ui = Login_ui.LoginUi()
    # 开启登录UI
    # 需要给出登录逻辑函数,注册逻辑函数与忘记密码逻辑函数
    log_ui.ui_run(log.MainFunc, log.login_res, log.forgot_password)
    # 关闭数据库连接
    condaba.clos_con(conn)
