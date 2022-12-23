import pymysql
import pandas as pd


# Scripts\pip install  pandas
# 函数（面向过程编程）+对象（面向对象编程 oop）
class ScoreLoadCsv(object):
    # 定义一个init方法，用于读取数据库
    def __init__(self, _conn):
        self.connect = _conn
        """
        # 读取数据库和建立游标对象
        self.connect = pymysql.connect(host="127.0.0.1",
                                       port=3306, 
                                       user="root", 
                                       password="root",
                                       database="student2022", 
                                       charset="utf8")
        """
        self.cursor = self.connect.cursor()

    # 定义一个del方法（动作），用于运行完所有程序以后关闭数据源和游标对象
    def __del__(self):
        self.connect.close()
        self.cursor.close()

    # 读取csv文件的列索引，用来建立数据表的字段
    def read_csv_colnmns(self):
        # 读取csv文件的索引
        csv_name = 'student_score.csv'
        data = pd.read_csv(csv_name, encoding="utf-8")
        # data_list = data.values
        # return data_list
        return data

    # 往数据库写入数据
    def write_mysql(self):
        data_dict = self.read_csv_colnmns().to_dict()
        stu_nn_num = {}
        for item_one in data_dict:
            if item_one == '学号':
                stu_nn_num = data_dict[item_one]
            for item_two in data_dict[item_one]:
                if '学号' != item_one:
                    str1 = stu_nn_num[item_two]
                    str2 = item_one
                    str3 = data_dict[item_one][item_two]
                    if str2 == '高数':
                        str2 = 'Math'
                    elif str2 == '英语':
                        str2 = 'English'
                    elif str2 == 'Python':
                        str2 = 'Python'
                    sql = "select lesNo FROM lessoninfo where lesName = '%s'" % str2
                    self.cursor.execute(sql)
                    str2 = self.cursor.fetchone()[0]
                    sql = "INSERT INTO stchoose(`StudentNo`, `lesNo`, `score`) VALUES('%s','%s',%s)" % (
                    str1, str2, str3)
                    # print(sql)
                    self.cursor.execute(sql)
                    self.commit()
                else:
                    print(data_dict[item_one][item_two])
        print("\n数据写入完成")

    # 定义一个确认事务运行的方法
    def commit(self):
        self.connect.commit()

    # 运行程序
    def run(self):
        self.write_mysql()


# 封装函数
def main(_conn):
    sql = ScoreLoadCsv(_conn)
    sql.run()


if __name__ == '__main__':
    main(pymysql.connect(host="127.0.0.1",
                                       port=3306,
                                       user="root",
                                       password="root",
                                       database="student2022",
                                       charset="utf8"))
