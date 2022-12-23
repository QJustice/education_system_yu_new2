import pymysql


class ConData:
    """与数据库握手"""
    def __init__(self, _host, _user, _password, _port, _db, _charset):
        """初始化数据库各类参数"""
        # host
        self.dbhost = _host
        # 数据库登录用户名
        self.dbuser = _user
        # 数据库登录密码
        self.dbpassword = _password
        # 数据库端口
        self.dbport = _port
        # 数据库名
        self.dbname = _db
        # 数据库字符集
        self.dbcharset = _charset

    def get_con_database(self):
        """建立连接并返回连接"""
        conn = pymysql.connect(host=self.dbhost,
                               user=self.dbuser,
                               password=self.dbpassword,
                               port=self.dbport,
                               database=self.dbname,
                               charset=self.dbcharset)
        # 返回建立的连接
        return conn

    def clos_con(self, conn):
        """关闭数据库连接"""
        conn.close()
