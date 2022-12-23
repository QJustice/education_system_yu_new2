# -*- coding:utf-8 -*-
####学生账号
import pymysql
import os
import tkinter.messagebox
import tkinter


class Student:
    def __init__(self, conn, account, passwd):
        ###构造,conn连接数据库
        cur = conn.cursor()
        sqlcmd = "select Name,Gender,Birth,Academy,Major,Grade,TeacherNo from studentinfo where StudentNo = '%s'" % account
        cur.execute(sqlcmd)
        res = cur.fetchone()
        sqlcmd = "select Name from studentinfo where TeacherNo = '%s'" % res[6]
        cur.execute(sqlcmd)
        TeacherName = cur.fetchone()
        cur.close()
        self.conn = conn
        self.account = account
        self.Password = passwd
        self.width = 50
        self.Name = res[0]
        self.Gender = res[1]
        self.Birth = res[2]
        self.Academy = res[3]
        self.Major = res[4]
        self.Grade = res[5]
        self.Teacher = TeacherName[0]
        self.stuGuiRoot = tkinter.Tk()
        self.stuGuiRoot.title("学生界面")
        self.stuGuiRoot.geometry("500x300+450+200")

    def MainFunc(self):
        ###主要执行函数
        info = ''

        self.MainSurface(info)
        buttonP = tkinter.Button(self.stuGuiRoot, text='P', width=5, bg='blue', command=self.PersonalInfo)
        buttonP.place(x=350, y=70)
        buttonM = tkinter.Button(self.stuGuiRoot, bg='blue', text='M', width=5, command=self.OperatMessage)
        buttonM.place(x=350, y=105)
        buttonL = tkinter.Button(self.stuGuiRoot, bg='blue', text='L', width=5, command=self.ChooseLessonInfo)
        buttonL.place(x=350, y=140)
        buttonS = tkinter.Button(self.stuGuiRoot, bg='blue', text='S', width=5, command=self.stchoose)
        buttonS.place(x=350, y=175)
        buttonQ = tkinter.Button(self.stuGuiRoot, bg='blue', text='Q', width=5, command=self.Quit)
        buttonQ.place(x=350, y=210)
        self.stuGuiRoot.mainloop()

    def PersonalInfo(self):
        ###个人信息
        info = ''
        while True:
            self.PersonalInfoSurface(info)
            choice = input('What to do?')
            choice = choice.upper()
            if choice != 'C' and choice != 'Q':
                info = 'Error Action!'
                continue
            if choice == 'C':
                info = self.ChangePersonalInfo()
            else:
                break
        return info

    def ChangePersonalInfo(self):
        ###修改个人信息
        NewGender = self.Gender
        NewBirth = self.Birth
        NewPw = self.Password
        ##########
        print('=' * self.width)
        print('ChangePersonalInfo')
        bd0 = '[G]Gender'
        bd1 = '[B]Birth'
        bd2 = '[P]Password'
        bd3 = '[Q]Gender'
        print(bd0)
        print(bd1)
        print(bd2)
        print(bd3)
        choice = input('What to do?')
        choice = choice.upper()
        if choice != 'G' and choice != 'B' and choice != 'P' and choice != 'Q':
            info = 'Error Action!'
        # continue
        if choice == 'G':
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
        elif choice == 'B':
            while True:
                choice = input('change Born Date?(y/n)')
                choice = choice.lower()
                if choice == 'y':
                    NewBirth = input('New Born Date:')
                    break
                elif choice == 'n':
                    break
                else:
                    pass
        elif choice == 'P':
            while True:
                choice = input('change Password?(y/n)')
                choice = choice.lower()
                if choice == 'y':
                    NewPw = input('New Password:')
                    break
                elif choice == 'n':
                    break
                else:
                    pass
        # else : break
        ##########'''
        '''while True:
			choice = input('Change Gender?(y/n)')
			choice = choice.lower()
			if choice == 'y':
				NewGender =input('New Gender:')
				break
			elif choice == 'n': break
			else : pass
		while True:
			choice =input('change Born Date?(y/n)')
			choice = choice.lower()
			if choice == 'y':
				NewBirth =input('New Born Date:')
				break
			elif choice == 'n': break
			else : pass
		while True:
			choice =input('change Password?(y/n)')
			choice = choice.lower()
			if choice == 'y':
				NewPw =input('New Password:')
				break
			elif choice == 'n': break
			else : pass'''
        info = 'Change Success!'
        cur = self.conn.cursor()
        if NewGender != self.Gender or NewBirth != self.Birth:
            sqlcmd = "update StudentInfo set Gender = '%s',Birth = '%s' where StudentNo = '%s'" % (
                NewGender, NewBirth, self.account)
            if cur.execute(sqlcmd) == 0:
                self.conn.rollback()
                cur.close()
                return 'Change Fail!'
        if NewPw != self.Password:
            sqlcmd = "update LoginAccount set Password = '%s' where Account='%s'" % (NewPw, self.account)
            if cur.execute(sqlcmd) == 0:
                self.conn.rollback()
                cur.close()
                return 'Change Fail!'
            else:
                self.conn.commit()
        self.Gender = NewGender
        self.Birth = NewBirth
        self.Password = NewPw
        cur.close()
        return 'Change Success!'

    def OperatMessage(self):
        info = ''
        while True:
            self.MessageSurface(info)
            self.MessageList()
            choice = input('What to do?')
            choice = choice.upper()
            if choice == 'M':
                msg = input('Message Id:')
                info = self.MessageInfo(msg)
            elif choice == 'Q':
                break;
            else:
                info = 'Error Action!'
        return info

    def MessageList(self):
        ###查看消息列表
        cur = self.conn.cursor()
        print()
        sqlcmd = "select Id,SenderName,SendTime,Title from AllMessage where statu = 'pass' and MsgLevel = 1"
        if cur.execute(sqlcmd) == 0:  return
        print('-' * self.width)
        while True:
            temp = cur.fetchone()
            if not temp: break;
            print('%3d%-20s%-50s%s' % (temp[0], temp[1], temp[3], temp[2]))
            print('-' * self.width)
        cur.close()

    def MessageInfo(self, MsgNo):
        ###查看详细消息, No消息编号
        cur = self.conn.cursor()
        sqlcmd = "select SenderName,SendTime,Title,Content from AllMessage where Id = %s" % MsgNo
        if cur.execute(sqlcmd) == 0:
            cur.close()
            return 'Read Fail!'
        article = cur.fetchone()
        cur.close()
        os.system('cls')
        print('*.' * self.width)
        print(article[2])
        head = article[0] + '     ' + str(article[1])
        print(head)
        print('-' * self.width)
        print(article[3])
        print('*' * self.width)
        input('Press any key to return!')
        return ''

    def ChooseLessonInfo(self):
        ####选课操作

        cur = self.conn.cursor()
        sqlcmd = "select * from lessoninfo"
        cur.execute(sqlcmd)
        print('%10s|%10s|%10s|%20s|%8s' % ('Lesson No', 'LessonName', 'Teacher No', 'Date', 'ClassRoom'))
        while True:
            res = cur.fetchone()
            if not res: break
            print('%10s|%10s|%10s|%20s|%8s' % (res[0], res[1], res[2], res[3], res[4]))
        print('-' * self.width)
        Cno = input('enter class number:')
        # print(cur.execute("select lesNo from lessoninfo where lesNo = '%s'" % Cno))
        if cur.execute("select lesNo from lessoninfo where lesNo = '%s'" % Cno) == 0:
            cur.close()
            return 'No Selected Class'

        # print(self.account)
        # print(Cno)
        sqlcmd = "select * from lessoninfo where LesNo= '%s'" % Cno
        cur.execute(sqlcmd)
        res = cur.fetchone()
        print(res[0])
        print(res[1])
        print(res[2])
        print(res[3])
        print(res[4])
        sqlcmd = "insert into stchoose(studentno,lesNo,LesName,date,classroom) values('%s','%s','%s','%s','%s')" % (
            self.account, res[0], res[1], res[3], res[4])
        if cur.execute(sqlcmd) == 0:
            return ('error')
        else:
            self.conn.commit()
            cur.close()
            return 'Choose Class Successfully!'

    def stchoose(self):
        # 查看选课表
        cur = self.conn.cursor()
        while True:
            print('Your Lessons :')
            sqlcmd = "select  stchoose.lesNo as '课程编号', lesName as '课程名', date as '上课时间', classRoom as '教室' from " \
                     "stchoose, lessoninfo where stchoose.lesNo = lessoninfo.lesNo AND stchoose.StudentNo = '%s' " % \
                     self.account
            cur.execute(sqlcmd)
            # cone = cur.fetchone()
            # print(cone)
            print('%10s|%20s|%25s|%15s|' % ('课程编号', '课程名', '上课时间', '教室'))
            while True:
                res = cur.fetchone()
                if not res: break
                print('%12s|%22s|%28s|%17s' % (res[0], res[1], res[2], res[3]))
            print('-' * self.width)
            body1 = '[S]Search Score'
            body2 = '[Q]Quit'
            print(body1)
            print(body2)
            print('-' * self.width)
            choice = input('What to do?')
            choice = choice.upper()
            if choice == 'S':
                cur = self.conn.cursor()
                Cno = input('enter class number:')
                # sqlcmd = "select * from lessoninfo where lesNo = '%s'" % cond[1]
                # cur.execute(sqlcmd)
                # res = cur.fetchone()
                # info = self.seacerchscore(res[0],res[3])
                info = self.seacerchscore(Cno, self.account)
            elif choice == 'Q':
                break;
            else:
                info = 'Error Action!'
        self.conn.commit()
        cur.close()

    def seacerchscore(self, lNo, sNo):
        cur = self.conn.cursor()
        sqlcmd = "select lesName from lessoninfo where lesNo = '%s'" % lNo
        cur.execute(sqlcmd)
        lname = cur.fetchone()
        print('-' * self.width)
        print('StudentNo :%s' % sNo)
        print('lesson :%s' % lname)
        sqlcmd = "select score from stchoose where lesNo = '%s' and studentno = '%s'" % (lNo, sNo)
        cur.execute(sqlcmd)
        scor = cur.fetchone()
        print('score : %s' % scor)
        print('-' * self.width)
        self.conn.commit()
        cur.close()
        while True:
            choice = input('[S]Sure')
            choice = choice.upper()
            if choice == 'S':
                break;
            else:
                info = 'Error Action!'
        print('-' * self.width)

    def Quit(self):
        ###退出
        pass

    def MainSurface(self, info):
        ###主界面

        title = '  Welcome %s!' % self.Name
        body1 = '    [P]Personal Information\n\n'
        body2 = '    [M]Message\n\n'
        body3 = '    [L]Lessons Choose\n\n'
        body4 = '    [S]Stchoose\n\n'
        body5 = '    [Q]Quit\n'
        msfToplab = tkinter.Label(self.stuGuiRoot, anchor='w', justify='left', bg='yellow',
                                  text=title, font=("", 16))
        msfToplab.place(x=140, y=10)
        msflab = tkinter.Label(self.stuGuiRoot, anchor='w', justify='left', bg='yellow',
                               text=(body1 + body2 + body3 + body4 + body5))
        msflab.place(x=70, y=70)

    def MessageSurface(self, info):
        ###消息界面
        os.system('cls')
        print('=' * self.width)
        title = 'MESSAGES'
        body1 = '[M]Message Detail'
        body2 = '[Q]Quit'
        # ' ' * ((self.width - len(title))/2),
        print(title)
        print(body1)
        print(body2)
        # print(' ' * ((self.width - len(body1)/2),body1)
        # print(' ' * ((self.width - len(body2))/2),body2)
        # print(' ' * ((self.width - len(info))/2),info)
        print(info)
        print('=' * self.width)

    def PersonalInfoSurface(self, info):
        ###个人信息界面
        os.system('cls')
        print('*' * self.width)
        title = 'PERSONAL INFORMATION'
        body1 = '[C]Change Information'
        body2 = '[Q]Quit'
        print(title)
        print(body1)
        print(body2)
        print(info)
        print('-' * self.width)
        body3 = '          Name: %s' % self.Name
        body4 = 'Student Number: %s' % self.account
        body5 = '        Gender: %s' % self.Gender
        body6 = '         Birth: %s' % self.Birth
        body7 = '      Academy: %s' % self.Academy
        body8 = '         Major: %s' % self.Major
        body9 = '         Grade: %s' % self.Grade
        body10 = '       Teacher: %s' % self.Teacher
        print(body3)
        print(body4)
        print(body5)
        print(body6)
        print(body7)
        print(body8)
        print(body9)
        print(body10)
        print('=' * self.width)


if __name__ == '__main__':
    conn = pymysql.connect(user='root', passwd='root', db='student2022')
    # stu = Student(conn,'0000001','123456')
    stu = Student(conn, '202001', '444444')
    # stu = Student(conn, '20201103035', '123456')
    stu.MainFunc()
    conn.close()
