import pymysql


class ConData:
    def __init__(self):
        pass

    def get_con_database(self):
        conn = pymysql.connect(user='root', password='root', db='student2022')
        return conn

    def clos_con(self, conn):
        conn.close()
