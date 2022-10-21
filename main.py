# -*- coding:utf-8 -*-
####系统入口
# import data_load
import Login_ui
import Login
import tkinter.messagebox
import ConnectDatabase

if __name__ == '__main__':
    condaba = ConnectDatabase.ConData()
    conn = condaba.get_con_database()
    log = Login.Login(conn)
    log_ui = Login_ui.LoginUi()
    log_ui.ui_run(log.MainFunc, log.login_res)
    condaba.clos_con(conn)
