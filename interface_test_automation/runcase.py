#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'zuozhijun'

import unittest
from test_interface_case import TestInterfaceCase
from datastruct import DataStruct

global test_data
test_data = DataStruct()

class  RunCase:
    '''运行测试用例'''

    def __init__(self):
        pass

    # 运行测试用例函数
    def run_case(self, runner, run_mode, run_case_list, db1_conn, db2_conn, http):
        global test_data
        print("runcase.run_casestart")
        if 1 == run_mode:  # 运行全部用例
            db1_cursor = db1_conn.cursor()
            # 获取用例个数
            #db1_cursor.execute('SELECT count(case_id)  FROM test_data')
            #test_case_num = db1_cursor.fetchone()[0]
            #获取用例个数
            db1_cursor.execute('SELECT count(case_id)  FROM test_data')
            test_case_num = db1_cursor.fetchone()[0] #因数据库返回数据类型为元组，所以要取【0】值
            # 获取case_id,并拼成case_id列表
            db1_cursor.execute('SELECT case_id  FROM test_data')
            test_case_list_tuple = db1_cursor.fetchall()# [0][0]
            db1_cursor.close()
            test_case_list1=[]
            for i in range(0, test_case_num):
                test_case_list1.append(test_case_list_tuple[i][0])

            # 循环执行测试用例
            for case_id in test_case_list1: #range(1, test_case_num+1):
                 db1_cursor = db1_conn.cursor()
                 db2_cursor = db2_conn.cursor()
                 db1_cursor.execute('SELECT http_method, request_name,interface_name, request_url, request_param, test_method, test_desc,expectedresults,check_mark, '
                                      'content_type FROM test_data WHERE case_id = %s',(case_id,))
                 # 记录数据
                 tmp_result = db1_cursor.fetchone()
                 test_data.case_id = case_id
                 test_data.http_method = tmp_result[0]
                 test_data.request_name = tmp_result[1]
                 test_data.interface_name = tmp_result[2]
                 test_data.request_url = tmp_result[3]
                 test_data.request_param = tmp_result[4]
                 test_data.test_method = tmp_result[5]
                 test_data.test_desc = tmp_result[6]
                 test_data.expectedresults=tmp_result[7]
                 test_data.check_mark=tmp_result[8]
                 test_data.content_type=tmp_result[9]
                 test_data.result = ''
                 test_data.reason = ''
                 try:
                     query = ('INSERT INTO test_result(case_id, http_method, request_name,interface_name, request_url,'
                              'request_param, test_method, test_desc, result, reason) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')

                     data = (test_data.case_id,test_data.http_method,test_data.request_name,test_data.interface_name, test_data.request_url,
                             test_data.request_param, test_data.test_method, test_data.test_desc,
                             test_data.result, test_data.reason)
                     db1_cursor.execute(query, data)
                     db1_cursor.execute('commit')
                 except Exception as e:
                     # 回滚
                     print('%s' % e)
                     db1_cursor.execute('rollback')

                 test_suite = unittest.TestSuite()
                 test_suite.addTest(TestInterfaceCase(test_data.test_method, test_data, http, db1_cursor, db2_cursor))
                 print("runner1")
                 runner.run(test_suite)
                 db1_cursor.close()
                 db2_cursor.close()
        else:   # 运行部分用例
            # 循环执行测试用例
            for case_id in run_case_list:
                 db1_cursor = db1_conn.cursor()
                 db2_cursor = db2_conn.cursor()
                 db1_cursor.execute('SELECT http_method, request_name,interface_name,request_url, request_param, test_method, test_desc,expectedresults,check_mark, '
                                      'content_type FROM test_data WHERE case_id = %s',(case_id,))
                 # 记录数据
                 tmp_result = db1_cursor.fetchone()
                 print("tmp_result",tmp_result)
                 if tmp_result!=None:
                    test_data.case_id = case_id
                    test_data.http_method = tmp_result[0]
                    test_data.request_name = tmp_result[1]
                    test_data.interface_name = tmp_result[2]
                    test_data.request_url = tmp_result[3]
                    test_data.request_param = tmp_result[4]
                    test_data.test_method = tmp_result[5]
                    test_data.test_desc = tmp_result[6]
                    test_data.expectedresults = tmp_result[7]
                    test_data.check_mark = tmp_result[8]
                    test_data.content_type = tmp_result[9]
                    test_data.result = ''
                    test_data.reason = ''
                    try:
                     query = ('INSERT INTO test_result(case_id, http_method, request_name,interface_name, request_url,'
                              'request_param, test_method, test_desc, result, reason) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')

                     data = (test_data.case_id,test_data.http_method,test_data.request_name,test_data.interface_name, test_data.request_url,
                             test_data.request_param, test_data.test_method, test_data.test_desc,
                             test_data.result, test_data.reason)
                     db1_cursor.execute(query, data)
                     db1_cursor.execute('commit')
                    except Exception as e:
                     # 回滚
                         print('%s' % e)
                         db1_cursor.execute('rollback')
                    test_suite = unittest.TestSuite()
                    test_suite.addTest(TestInterfaceCase(test_data.test_method, test_data, http, db1_cursor, db2_cursor))
                    print("runcase.runner2 strat")
                    runner.run(test_suite)
                    print("runner222")
                 else:
                    test_data.case_id = case_id
                    test_data.http_method = 'NULL'
                    test_data.request_name = 'NULL'
                    test_data.interface_name = '用例表中不存在用例id：'+str(case_id)
                    test_data.request_url = 'NULL'
                    test_data.request_param = 'NULL'
                    test_data.test_method = 'NULL'
                    test_data.test_desc = ''
                    test_data.result = ''
                    test_data.reason = '用例表中不存在用例id：'+str(case_id)
                    try:
                        query = ('INSERT INTO test_result(case_id, http_method, request_name,interface_name, request_url,'
                              'request_param, test_method, test_desc, result, reason) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')

                        data = (test_data.case_id,test_data.http_method,test_data.request_name,test_data.interface_name, test_data.request_url,
                             test_data.request_param, test_data.test_method, test_data.test_desc,
                             test_data.result, test_data.reason)
                        db1_cursor.execute(query, data)
                        db1_cursor.execute('commit')
                    except Exception as e:
                     # 回滚
                        print('%s' % e)
                        db1_cursor.execute('rollback')

                    db1_cursor.close()
                    db2_cursor.close()
        print("runcase end")