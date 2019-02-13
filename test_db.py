# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/12

import unittest

from auot import ConnDB


class TestDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        host = '101.201.68.194'
        name = 'root'
        passwd = 'Adkl231@xfyl2018'
        db_name = 'wnyl_dev'

        cls.db_mysql = ConnDB()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_user_001(self):
        sql_1 = """select user_id,username,phone_no from t_user where user_id in ('u10001','u10002')"""
        sql_2 = """select user_id,username,phone_no from t_user where user_id in ('u10001','u1000')"""
        sql_list = [sql_1, sql_2]
        data_tuple = self.db_mysql.go_query(sql_list)
        self.db_mysql.do_assert(data_tuple)

    def test_user_002(self):
        pass


if __name__ == '__main__':
    unittest.main()