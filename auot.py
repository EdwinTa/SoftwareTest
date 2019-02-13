# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/12

import pymysql


class ConnDB(object):
    def __init__(self):
        host = '101.201.68.194'
        name = 'root'
        passwd = 'Adkl231@xfyl2018'
        db_name = 'wnyl_dev'

        self.db = pymysql.connect(host, name, passwd, db_name)

    def go_query(self, sql_list):
        try:
            # sql = f"""select * from {table_name} where {col_name} in {value}"""
            data_list = []
            cursor = self.db.cursor()
            for sql in sql_list:
                cursor.execute(sql)
                data_list.append(cursor.fetchall())
            return data_list
        except Exception as e:
            print(e)
        finally:
            self.db.close()

    def do_assert(self, data_tuple):
        if data_tuple and len(data_tuple) == 2 :
            if data_tuple[0] == data_tuple[1]:
                print('test pass')
            else:
                print('test failed')
        else:
            print('test failed')

    def gene_sql(self, value1, value2, value3):

        # 计算结果SQL
        sql_1 = f"""select * from t_user where user_id in ('{value1}', '{value2}')"""
        # 预期结果SQL
        sql_2 = f"""select * from t_user where user_id in ('{value3}')"""
        return [sql_1, sql_2]

if __name__ == '__main__':
    # from config import TEST_DATA


    value1='u10003'
    value2='u10004'
    value3 ='u10003'

    db_mysql = ConnDB()
    sql_list = db_mysql.gene_sql(value1, value2, value3)
    data_tuple = db_mysql.go_query(sql_list)
    for i in data_tuple:
        print(i)
    db_mysql.do_assert(data_tuple)




# 打开数据库连接
# db = pymysql.connect("101.201.68.194", "root", "Adkl231@xfyl2018", "wnyl_dev")

# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表




#
# sql_list = [sql, sql1]
# data_list = []
# for sql in sql_list:
#     cursor.execute(sql)
#     data_list.append(cursor.fetchall())


# 关闭数据库连接
# db.close()

