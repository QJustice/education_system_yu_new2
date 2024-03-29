﻿import pymysql  # 先安装再引入包

# 创建链接数据库

try:
    # 创建链接数据库
    conn = pymysql.connect(host='127.0.0.1', database='student2022', port=3306, user='root', password='root',
                           charset='utf8mb4')
except pymysql.Error as e:
    print('数据库链接失败！', str(e))
else:  # try没有异常的时候才会执行
    print("sucessfully!")
    cur = conn.cursor()
    cur.execute("select * from loginaccount")
    rs = cur.fetchall()
    print(rs)

    cur1 = conn.cursor()
    # 第二个游标

try:

    # 第三种：可以一次插入多条，效率比一条条插高,用的方法是executemany，整个一个班的同学的信息插入进去！！！！！！！！！！！！！！！！！！！！！
    stmt = 'insert into loginaccount(account,stuname) values (%s,%s)'
    data = [
        ('20197000010', '宝力德巴特尔'),
        ('20202103412', '李春玲'),
        ('20202103413', '德格金'),
        ('20202103414', '松布日'),
        ('20202103415', '阿音'),
        ('20202103416', '朝路门'),
        ('20202103417', '迎春'),
        ('20202103418', '永富'),
        ('20202103419', '意拉嘎其'),
        ('20202103420', '阿亚拉嘎'),
        ('20202103421', '钦白'),
        ('20202103422', '都日那腾格尔'),
        ('20202103423', '伊茹'),
        ('20202103424', '呼斯勒'),
        ('20202103425', '鑫鑫'),
        ('20202103426', '金莫日根'),
        ('20202103427', '布日古德'),
        ('20202103428', '伊力奇'),
        ('20202103429', '乌日力格'),
        ('20202103430', '王世民'),
        ('20202103431', '都日苏拉'),
        ('20202103432', '恩和图拉嘎'),
        ('20202103433', '吴成格勒'),
        ('20202103434', '白斯拉'),
        ('20202103435', '鲁文晶'),
        ('20202103436', '多蓝'),
        ('20202103437', '陈杜来胡'),
        ('20202103438', '乃日嘎'),
        ('20202103439', '贺希格宝音'),
        ('20202103440', '格根苏德'),
        ('20202105183', '布日格图'),
        ('201014009', '包老师')]
    # 列表，元组
    cur1.executemany(stmt, data)


except pymysql.Error as e:
    print('插入数据报错！', str(e))
finally:  # 无论如何都会执行下面的语句
    cur1.close()  # 关闭游标
    conn.commit()
    conn.close()  # 关闭数据库链接
