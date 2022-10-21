import pymysql

conn = pymysql.connect(host='127.0.0.1', database='student', user='root', password='root', port=3306, charset='utf8mb4')
cur = conn.cursor()
cur.execute("select * from s")
rs = cur.fetchall()

print(rs)

for i in range(3):
    account = input("请输入账号：")
    password1 = input("请输入密码：")

    cur1 = conn.cursor()
    rs = cur1.execute(
        "select * from s where sno=" + "'" + account + "'" + "   and    " + "password_yu=" + "'" + password1 + "'")
    if rs > 0:
        print("账号和密码输入正确，欢迎使用本系统！")
        break
        print("进入下一个界面！")
    else:
        if i >= 2:
            print("您账号和密码输入错误超过3次，对不起，您不能使用本系统！")
            break

        else:
            print("账号和密码输入错误，请重新输入！")
