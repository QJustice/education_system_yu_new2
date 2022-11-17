import pymysql
import pandas as pd


# Scripts\pip install  pandas
# 函数（面向过程编程）+对象（面向对象编程 oop）

class MySQL_csv(object):

    # 定义一个init方法，用于读取数据库
    def __init__(self):
        # 读取数据库和建立游标对象
        self.connect = pymysql.connect(host="127.0.0.1", \
                                       port=3306, user="root", password="root", \
                                       database="student2022", charset="utf8")
        self.cursor = self.connect.cursor()

    # 定义一个del方法（动作），用于运行完所有程序以后关闭数据源和游标对象
    def __del__(self):
        self.connect.close()
        self.cursor.close()

    # 读取csv文件的列索引，用来建立数据表的字段
    def read_csv_colnmns(self):
        # 读取csv文件的索引
        csv_name = './students.csv'
        data = pd.read_csv(csv_name, encoding="utf-8")
        data_list = data.values
        return data_list

    # 往数据库写入数据
    def write_mysql(self):
        # 在数据表中写入数据，因为数据是列表类型，把他转化为元组更符合sql语句
        for i in self.read_csv_colnmns():
            data = tuple(i)
            print(data)
            sql = "insert into studentinfo(StudentNo,Name,Gender)  values{}".format(data)
            print(sql)
            self.cursor.execute(sql)
            self.commit()
        print("\n数据写入完成")

    # 定义一个确认事务运行的方法
    def commit(self):
        self.connect.commit()

    # 新建数据库表
    def create(self):
        # 若已有数据库表s，则删除
        query1 = "CREATE DATABASE IF NOT EXISTS `student2022` "
        query2 = "use student2022;"  # 更改表名
        self.cursor.execute(query1)
        self.cursor.execute(query2)
        # 创建数据表，用刚才提取的列索引作为字段
        data_2 = self.read_csv_colnmns()
        # 根据自己要创建的表格更改sql语句
        sql = "create table if not exists student(sno varchar(13) not null,sname varchar(20) not null, sex varchar(2) not null,primary key(sno))default charset=utf8;"
        self.cursor.execute(sql)
        self.commit()

    # 运行程序
    def run(self):
        # self.create()
        self.write_mysql()


# 封装函数
def main():
    sql = MySQL_csv()
    sql.run()


if __name__ == '__main__':
    main()
