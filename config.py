# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/12


# 计算结果SQL
sql_1 = """select * from t_user where user_id in ('u10001','u10002')"""
# 预期结果SQL
sql_2 = """select * from t_user where user_id in ('u10001','u1000')"""








TEST_DATA = {
    'user': [sql_1, sql_2],
    '': '',
}