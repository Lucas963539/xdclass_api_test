import pymysql
from warnings import filterwarnings
# from config.Config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT
from util import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

#
# conn = pymysql.connect(host=DB_HOST,
#                        user=DB_USER,
#                        password=DB_PASSWORD,
#                        database=DB_NAME,
#                        port=DB_PORT)
#
# # 使用cursor方法获得一个游标，得到一个可以执行sql语句并且返回数据结果为字典的游标
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#
# try:
#     sql = "SELECT * FROM `case`"
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     print(data)
# except Exception as e:
#     print(f'SQL语句有误，错误是{e}')
# finally:
#     conn.close()

# 忽略mysql告警信息
filterwarnings('ignore', category=pymysql.Warning)


class MySqlUtil:
    def __init__(self):
        # 创建数据库连接
        self.conn = pymysql.connect(host=DB_HOST,
                                    user=DB_USER,
                                    password=DB_PASSWORD,
                                    database=DB_NAME,
                                    port=DB_PORT)
        # 使用cursor方法获得一个游标，得到一个可以执行sql语句并且返回数据结果为字典的游标
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()

    def query(self,sql,state='all'):
        """
        查询方法
        :param sql:
        :param state: 查询条数，默认all查询全部
        :return:
        """
        self.cursor.execute(sql)

        # 返回查询结果
        if state == 'all':
            # 查询全部
            data = self.cursor.fetchall()
        else:
            # 查询一条
            data = self.cursor.fetchone()
        return data

    def execute(self,sql):
        try:
            rows = self.cursor.execute(sql)
            # 提交事务
            self.conn.commit()
            print(f'SQL已执行，影响了{rows}行')
            return rows
        except Exception as e:
            print(f'数据库操作异常:{e}')
            # 回滚事务
            self.conn.rollback()


if __name__ == '__main__':
    mydb = MySqlUtil()

    query_sql = "SELECT * FROM `case`"
    data = mydb.query(query_sql)
    print(data)

    # insert_sql = "INSERT INTO `case` VALUES (3,'小滴课堂','index','首页','get','/api/teacher/v1/list','yes','{}',-1,'[]','{}','0','code','True','','2023-01-04 14:57:11',''),"\
    #             "(4,'小滴课堂','index','首页-教师列表','get','/api/teacher/v1/list','yes','{}',-1,'[]','{}','0','code','True','','2023-01-04 14:57:11',''),"\
    #            "(5,'小滴课堂','index','首页-教师列表','get','/api/teacher/v1/list','yes','{}',-1,'[]','{}','0','code','True','','2023-01-04 14:57:11','')"
    #rows = mydb.execute(insert_sql)



