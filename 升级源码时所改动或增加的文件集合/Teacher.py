# -*- coding:utf-8 -*-
####教师帐号
import os
import tkinter
from tkinter import INSERT
from tkinter import Text
import pymysql
import score_view
import tkinter.messagebox


class Teacher:
    def __init__(self, conn, account, passwd):
        cur = conn.cursor()
        sqlcmd = "select Name,TeacherNo,Gender,Birth,PositionNo,Salary from TeacherInfo where TeacherNo = '%s'" % account
        cur.execute(sqlcmd)
        temp = cur.fetchone()
        sqlcmd = "select PositionName from PositionList where PositionNo = '%s'" % temp[4]
        cur.execute(sqlcmd)
        pos = cur.fetchone()
        cur.close()

        self.PositionName = pos[0]
        self.width = 150
        self.conn = conn
        self.Name = temp[0]
        self.TeacherNo = temp[1]
        self.Gender = temp[2]
        self.Birth = temp[3]
        self.PositionNo = temp[4]
        self.Salary = temp[5]
        self.Password = passwd
        self.TeaGuiRoot = tkinter.Tk()
        self.TeaGuiRoot.title("教师界面")
        self.TeaGuiRoot.geometry("500x300+450+200")

    def MainFunc(self):
        ####主要执行函数
        info = ''
        self.MainSurface(info)
        buttonP = tkinter.Button(self.TeaGuiRoot, text='P', width=5, bg='blue', command=self.OperatePersonalInfo)
        buttonP.place(x=350, y=70)
        buttonM = tkinter.Button(self.TeaGuiRoot, bg='blue', text='M', width=5, command=self.OperateMessage)
        buttonM.place(x=350, y=105)
        buttonL = tkinter.Button(self.TeaGuiRoot, bg='blue', text='G', width=5, command=self.score_data_view)
        buttonL.place(x=350, y=140)
        buttonS = tkinter.Button(self.TeaGuiRoot, bg='blue', text='S', width=5, command=self.ScoreMark)
        buttonS.place(x=350, y=175)
        buttonQ = tkinter.Button(self.TeaGuiRoot, bg='blue', text='Q', width=5, command=self.TeaGuiRoot.destroy)
        buttonQ.place(x=350, y=210)
        self.TeaGuiRoot.mainloop()

    def ScoreMark(self):
        ###打分
        cur = self.conn.cursor()
        sqlcmd = "select * from lessoninfo"
        cur.execute(sqlcmd)
        print('%10s|%10s|%10s|%20s|%8s' % ('Lesson No', 'LessonName', 'Teacher No', 'Date', 'ClassRoom'))
        while True:
            res = cur.fetchone()
            if not res: break
            print('%10s|%10s|%10s|%20s|%8s' % (res[0], res[1], res[2], res[3], res[4]))
        print('-' * self.width)
        Cno = input('enter class number :')
        Sno = input('enter student number :')
        if cur.execute("select lesNo from stchoose where lesNo = '%s' and StudentNo = '%s'" % (Cno, Sno)) == 0:
            cur.close()
            return 'No Selected Class'
        Sc = input('enter score :')
        sqlcmd = "update stchoose set score = %s where lesNo = '%s' and StudentNo = '%s'" % (Sc, Cno, Sno)
        cur.execute(sqlcmd)
        print('Successfully!!!')

        self.conn.commit()
        cur.close()

    def OperatePersonalInfo(self):
        ####操作个人信息
        info = ''
        while True:
            self.PersonalInfoSurface(info)
            choice = input('What to do?')
            choice = choice.upper()
            if choice == 'C':
                info = self.ChangePersonalInfo()
            elif choice == 'Q':
                break
            else:
                info = 'Error Action'
        return info

    def ChangePersonalInfo(self):
        ####修改个人信息
        NewGender = self.Gender
        NewBirth = self.Birth
        NewPw = self.Password
        cur = self.conn.cursor()
        while True:
            choice = input('Change Gender?(y/n)')
            choice = choice.lower()
            if choice == 'y':
                NewGender = input('New Gender:')
                break
            elif choice == 'n':
                break
            else:
                pass
        while True:
            choice = input('Change Born Data?(y/n)')
            choice = choice.lower()
            if choice == 'y':
                NewBirth = input('New Born Date:')
                break
            elif choice == 'n':
                break
            else:
                pass
        while True:
            choice = input('Change Password?(y/n)')
            choice = choice.lower()
            if choice == 'y':
                NewPw = input('New Password:')
                break
            elif choice == 'n':
                break
            else:
                pass
        if NewBirth != self.Birth or NewGender != self.Gender:
            sqlcmd = "update TeacherInfo set Birth='%s',Gender='%s' where TeacherNo = '%s'" % (
                NewBirth, NewGender, self.TeacherNo)
            if 0 == cur.execute(sqlcmd):
                self.conn.rollback()
                cur.close()
                return 'Changer Fail'
        if NewPw != self.Password:
            sqlcmd = "update LoginAccount set Password='%s' where Account='%s'" % (NewPw, self.TeacherNo)
            if 0 == cur.execute(sqlcmd):
                self.conn.rollback()
                cur.close()
                return 'Change Fail!'
            else:
                self.conn.commit()
        self.Gender = NewGender
        self.Password = NewPw
        self.Birth = NewBirth
        cur.close()
        return 'Change Success!'

    def MessageList(self):
        #####查看消息列表
        cur = self.conn.cursor()
        print()
        sqlcmd = "select Id,SenderName,SendTime,Title from AllMessage where statu = 'pass' and MsgLevel <= 1"
        if cur.execute(sqlcmd) == 0:  return
        print('-' * self.width)
        while True:
            temp = cur.fetchone()
            if not temp: break;
            print('%3d%-20s%-50s%s' % (temp[0], temp[1], temp[3], temp[2]))
            print('-' * self.width)
        cur.close()

    def MessageInfo(self, MsgNo):
        ####查看详细消息, MsgNo消息编号
        cur = self.conn.cursor()
        sqlcmd = "select SenderName,SendTime,Title,Content from AllMessage where Id = %d" % MsgNo
        if cur.execute(sqlcmd) == 0:
            cur.close()
            return 'Read Fail!'
        article = cur.fetchone()
        cur.close()
        os.system('cls')
        print('=' * self.width)
        print(' ' * ((self.width - len(article[2])) / 2), article[2])
        head = article[0] + '     ' + str(article[1])
        print(' ' * ((self.width - len(head)) / 2), head)
        print('-' * self.width)
        print(article[3])
        print('=' * self.width)
        input('Press any key to return!')
        return ''

    def CreateMessage(self):
        ####发布消息
        print()
        print('    Publish Messsage')
        title = input('Message Title:')
        path = input('Message Path:')
        fp = open(path, 'r')
        body = fp.read()
        fp.close()
        sqlcmd = "insert into AllMessage(MsgLevel,SenderNo,SenderName,SendTime,Title,Content,statu) values(1,'%s','%s',now(),'%s','%s','wait')" % (
            self.TeacherNo, self.Name, title, body)
        cur = self.conn.cursor()
        info = 'Publish Success!'
        if 0 == cur.execute(sqlcmd):
            info = 'Publish Fail'
            self.conn.rollback()
        else:
            self.conn.commit()
        cur.close()
        return info

    def OperateMessage(self):
        #####管理消息
        info = ''
        while True:
            self.MessageSurface(info)
            self.MessageList()
            choice = input('What to do?')
            choice = choice.upper()
            if choice == 'P':
                info = self.CreateMessage()
            elif choice == 'Y':
                info = self.PersonalMessage()
            elif choice == 'M':
                msg = input('Message Id:')
                info = self.MessageInfo(msg)
            elif choice == 'Q':
                break
            else:
                info = 'Error Action'
        return info

    def PersonalMessageList(self):
        cur = self.conn.cursor()
        sqlcmd = "select Id,SenderName,SendTime,Title from AllMessage where SenderNo='%s'" % self.TeacherNo
        if cur.execute(sqlcmd) != 0:
            print('-' * self.width)
            while True:
                temp = cur.fetchone()
                if not temp: break;
                print('%3d%-20s%-50s%s' % (temp[0], temp[1], temp[3], temp[2]))
                print('-' * self.width)
        cur.close()

    def PersonalMessage(self):
        #####查看个人消息
        info = ''
        while True:
            self.PersonalMessageSurface(info)
            self.PersonalMessageList()
            choice = input('What to do?')
            choice = choice.upper()
            if choice == 'M':
                msg = input('Message Id:')
                info = self.MessageInfo(msg)
            elif choice == 'D':
                info = self.DeleteMessage()
            elif choice == 'Q':
                break
            else:
                info = 'Error Action!'
        return info

    def DeleteMessage(self):
        ####删除个人消息
        print()
        print('    Delete Message')
        MsgNo = input('Message id = ')
        cur = self.conn.cursor()
        sqlcmd = "delete from AllMessage where Id = %d and SenderNo = '%s'" % (MsgNo, self.TeacherNo)
        info = 'Delete Success!'
        if cur.execute(sqlcmd) == 0:
            info = 'Delete Fail'
            self.conn.rollback()
        else:
            self.conn.commit()
        cur.close()
        return info

    def score_data_view(self):
        score_GUI_root = tkinter.Toplevel(self.TeaGuiRoot)
        score_GUI_root.title("学生成绩可视化")
        score_GUI_root.geometry('350x200+550+200')

        def show_less(_data):
            score_GUI_showLes = tkinter.Toplevel(self.TeaGuiRoot)
            score_GUI_showLes.title("课程列表")
            score_GUI_showLes.geometry('350x200+550+400')
            text = Text(score_GUI_showLes, undo=True, autoseparators=False)
            # 适用 pack(fill=X) 可以设置文本域的填充模式。比如 X表示沿水平方向填充，Y表示沿垂直方向填充，BOTH表示沿水平、垂直方向填充
            text.pack()
            i = 1
            for item in _data:
                # INSERT 光标处插入；END 末尾处插入
                text.insert(INSERT, str(i) + '. ' + item[0] + '\n')
                i = i + 1
            buttonR = tkinter.Button(score_GUI_showLes,
                                     text='重新输入',
                                     width=7,
                                     bg='blue',
                                     command=self.score_data_view)
            buttonR.place(x=70, y=150)
            buttonQ = tkinter.Button(score_GUI_showLes,
                                     bg='blue',
                                     text='取消',
                                     width=5,
                                     command=score_GUI_showLes.destroy)
            buttonQ.place(x=250, y=150)
        def query_data(_lesname):
            # 数据库游标
            cur = self.conn.cursor()
            # 用于数据库查询的语句
            sqlcmd = "SELECT lesName, lesNo FROM lessoninfo GROUP BY lesName"
            cur.execute(sqlcmd)
            # 未查询到任何匹项
            allLesName = cur.fetchall()
            nocanfind = True
            for item in allLesName:
                if item[0] == _lesname:
                    nocanfind = False
                    score_tools = score_view.ScoreVis(self.conn)
                    score_GUI_view = tkinter.Toplevel(score_GUI_root)
                    score_GUI_view.title("学生成绩可视化")
                    score_GUI_view.geometry('350x350+550+200')
                    buttonP = tkinter.Button(score_GUI_view,
                                             text='P',
                                             width=5,
                                             bg='blue',
                                             command=lambda: score_tools.student_score_view(_lesname))
                    buttonP.place(x=250, y=70)

                    buttonM = tkinter.Button(score_GUI_view,
                                             bg='blue',
                                             text='M',
                                             width=5,
                                             command=lambda: score_tools.less_view(_lesname))
                    buttonM.place(x=250, y=105)
                    buttonL = tkinter.Button(score_GUI_view,
                                             bg='blue',
                                             text='G',
                                             width=5,
                                             command=lambda: score_tools.student_pass_rate(_lesname))
                    buttonL.place(x=250, y=140)
                    buttonV = tkinter.Button(score_GUI_view,
                                             bg='blue',
                                             text='V',
                                             width=5,
                                             command=score_tools.score_view)
                    buttonV.place(x=250, y=175)
                    buttonQ = tkinter.Button(score_GUI_view,
                                             bg='blue',
                                             text='Q',
                                             width=5,
                                             command=score_GUI_view.destroy)
                    buttonQ.place(x=250, y=210)
                    ####主界面
                    title = "Welcome, %s" % _lesname
                    body1 = '[P]%s课程成绩分布\n\n' % _lesname
                    body2 = '[M]%s课程平均分\n\n' % _lesname
                    body3 = '[G]%s课程及格率\n\n' % _lesname
                    body4 = '[V]课程横向对比\n\n'
                    body5 = '[Q]Quit\n\n'
                    msfToplab = tkinter.Label(score_GUI_view, anchor='w', justify='left', bg='yellow',
                                              text=title, font=("", 16))
                    msfToplab.place(x=140, y=10)
                    msflab = tkinter.Label(score_GUI_view, anchor='w', justify='left', bg='yellow',
                                           text=(body1 + body2 + body3 + body4 + body5))
                    msflab.place(x=70, y=70)
            if nocanfind:
                login_s = tkinter.messagebox.askokcancel(title='教务管理系统',
                                                         message='您输入的课程不存在，请确认课程名，是否需要查看课程列表')
                if login_s:
                    show_less(allLesName)
                else:
                    self.score_data_view()

        wel = tkinter.Label(score_GUI_root, text='欢迎进入学生成绩可视化查看界面', font=('Arial', 10))
        wel.pack()
        # 将输入框里面的东西拿出来，用于接收用户输入的课程名
        les_name = tkinter.StringVar()
        # 设置提升字样
        show_new_name = tkinter.Label(score_GUI_root, text='请输入课程名', font=('Arial', 9))
        show_new_name.place(x=70, y=50)
        input_new_name = tkinter.Entry(score_GUI_root, textvariable=les_name)
        input_new_name.place(x=155, y=50)
        login_button2 = tkinter.Button(score_GUI_root, text='查询', width=7, command=lambda: query_data(les_name.get()))
        login_button2.place(x=75, y=130)
        login_button3 = tkinter.Button(score_GUI_root, text='取消', width=7, command=score_GUI_root.destroy)
        login_button3.place(x=225, y=130)

    def MainSurface(self, info):
        os.system('cls')
        ####主界面
        title = "Welcome, %s" % self.Name
        body1 = '[P]Personal Information\n\n'
        body2 = '[M]Message Management\n\n'
        body3 = '[G]Grop Score\n\n'
        body4 = '[S]Score Mark\n\n'
        body5 = '[Q]Quit\n\n'
        msfToplab = tkinter.Label(self.TeaGuiRoot, anchor='w', justify='left', bg='yellow',
                                  text=title, font=("", 16))
        msfToplab.place(x=140, y=10)
        msflab = tkinter.Label(self.TeaGuiRoot, anchor='w', justify='left', bg='yellow',
                               text=(body1 + body2 + body3 + body4 + body5))
        msflab.place(x=70, y=70)

    def PersonalInfoSurface(self, info):
        ####个人信息界面
        os.system('cls')
        title = 'Personal Information'
        body1 = '[C]Change Information'
        body2 = '[Q]Quit'
        body3 = '     Name: %s' % self.Name
        body4 = '   Gender: %s' % self.Gender
        body5 = 'Born Date: %s' % self.Birth
        body6 = ' Position: %s' % self.PositionName
        body7 = '   Salary: %.2f' % self.Salary
        print('=' * self.width)
        print(title)
        print(body1)
        print(body2)
        print(info)
        print('-' * self.width)
        print(body3)
        print(body4)
        print(body5)
        print(body6)
        print(body7)
        print('=' * self.width)

    def MessageSurface(self, info):
        #####消息界面
        os.system('cls')
        title = 'MESSAGE'
        body1 = '[P]Publish Message'
        body2 = '[Y]Your Message'
        body3 = '[M]Message Detail'
        body4 = '[Q]Quit'
        print('=' * self.width)
        print(title)
        print(body1)
        print(body2)
        print(body3)
        print(body4)
        print(info)
        print('=' * self.width)

    def PersonalMessageSurface(self, info):
        #####个人消息界面
        os.system('cls')
        title = 'PERSONAL MESSAGE'
        body1 = '[M]Message Detail'
        body2 = '[D]Delete Message'
        body3 = '[Q]Quit'
        print('=' * self.width)
        print(title)
        print(body1)
        print(body2)
        print(body3)
        print(info)
        print('=' * self.width)


if __name__ == '__main__':
    conn = pymysql.connect(user='root', passwd='root', db='student2022')
    t = Teacher(conn, '20022', '123456')
    t.MainFunc()
    conn.close()
