#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'zuozhijun'

import  unittest
import json
import urllib.parse
import base64
import Special_char_process
import Expectedresult_PK_Response
# 测试用例(组)类
class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', test_data=None, http=None, db1_cursor=None, db2_cursor=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.test_data = test_data
        print("self.test_data",self.test_data.request_param)
        self.http = http
        self.db1_cursor = db1_cursor
        self.db2_cursor = db2_cursor


class TestInterfaceCase(ParametrizedTestCase):
   def setUp(self):
       pass

   # 测试接口1
   print("EWMStart1")
   def EWMS(self):
       print("EWMStart2")
       # 根据被测接口的实际情况，合理的添加HTTP头
       header = {'Accept':'*/*',#'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language':'zh-CN',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Cookie': 'VL=AC4D2B65E93A39F61F760F375B18212a;EWS_USER_Email=SXIlMmJzJTJiNDVsc09DSTZtVG93dzZEZUtZaVpLYktlc2FobGl6b3Y1VjNYREVMVTlYRmlaYyUyYjdFdURCVnhWRlh3WFpoUmI3UjhUZGNnems2SkpkeiUyYklBQ1NySFM0eUFuN1M=',
                 'Connection': 'keep-alive'
          }
       '''header = {'Host': '192.168.1.81:1111',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                  'Accept-Encoding': 'gzip, deflate',
                  'Referer': 'http://192.168.1.81:1111/Admin/OperateBarCodeLog?sMenuId=46',
                  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'X-Requested-With': 'XMLHttpRequest',
                  'Content-Length': '220',
                  'Cookie': 'VL=AC4D2B65E93A39F61F760F375B18212;EWS_USER_Email=SXIlMmJzJTJiNDVsc09DSTZtVG93dzZEZUtZaVpLYktlc2FobGl6b3Y1VjNYREVMVTlYRmlaYyUyYjdFdURCVnhWRlh3WFpoUmI3UjhUZGNnems2SkpkeiUyYklBQ1NySFM0eUFuN1M=',
                  'Connection': 'keep-alive'}'''
       self.http.set_header(header)
       if self.test_data.http_method=='GET':
           self.test_data.request_param = urllib.parse.urlencode(eval(self.test_data.request_param))
           response = self.http.get(self.test_data.request_url,  self.test_data.request_param)
       if self.test_data.http_method == 'POST':
           if self.test_data.content_type=='json':
               self.test_data.request_param= json.dumps(eval(self.test_data.request_param))
           if self.test_data.content_type=='formdata':
               pass
           if self.test_data.content_type=='xml':
               pass
           # if self.test_data.content_type==None:
           #     self.test_data.request_param = urllib.parse.urlencode(eval(self.test_data.request_param))
           #     print("self.test_data.content_type",self.test_data.content_type)
           response = self.http.post(self.test_data.request_url, self.test_data.request_param)
       if {} == response[0]:         #请求失败
            self.test_data.result = 'Error'
            Lresponse = Special_char_process.SpCharReplace(str(response[1])) #对返回结果中的特殊字符做转换处理
            self.test_data.reason = Lresponse
            try:
                # 更新结果表中的用例运行结果
                self.db1_cursor.execute('UPDATE test_result SET result = %s,reason = %s  WHERE case_id = %s', (self.test_data.result,self.test_data.reason, self.test_data.case_id))
                self.db1_cursor.execute('commit')
            except Exception as e:
                print('%s' % e)
                self.db1_cursor.execute('rollback')
       else:
            try:
                if self.test_data.expectedresults==None:      #检查未填写预期结果情况
                    self.test_data.result='Fail'
                    self.test_data.reason ="测试用例预期结果为空，请编写预期结果"
                if self.test_data.check_mark == 'sql':
                    expectedresults_list, check_key_list = Expectedresult_PK_Response.ExpectedResults_dict_SqlQuery(self.test_data.expectedresults)  # 执行expectedresults为sql语句查询的预期结果和返回属性列表
                    New_response = Expectedresult_PK_Response.New_Response_Rusults_KeyCheck_Dict(check_key_list,response[0], [], {},'')
                    self.test_data.result, self.test_data.reason = Expectedresult_PK_Response.ExpResultVsResponse_ExpResult_json(expectedresults_list, New_response)
                if self.test_data.check_mark == 'char':
                    self.test_data.result, self.test_data.reason = Expectedresult_PK_Response.ExpResultVsResponse_text(self.test_data.expectedresults, response[0])
                if self.test_data.check_mark==None:
                    print("self.test_data.expectedresults",self.test_data.expectedresults)
                    expectedresults_list = json.loads(self.test_data.expectedresults)
                    check_key_list=expectedresults_list.keys()
                    New_response = Expectedresult_PK_Response.New_Response_Rusults_KeyCheck_Dict(check_key_list,response[0], [], {},'')
                    self.test_data.result, self.test_data.reason = Expectedresult_PK_Response.ExpResultVsResponse_ExpResult_json(expectedresults_list, New_response)
            except AssertionError as e:
               print('%s' % e)
               self.test_data.result = 'Fail'
               self.test_data.reason = '%s' % e # 记录失败原因
       # 更新结果表中的用例运行结果
       try:
          self.db1_cursor.execute('UPDATE test_result SET result = %s WHERE case_id = %s', (self.test_data.result, self.test_data.case_id))
          self.db1_cursor.execute('UPDATE test_result SET reason = %s WHERE case_id = %s', (self.test_data.reason, self.test_data.case_id))
          self.db1_cursor.execute('commit')
       except Exception as e:
           print('%s' % e)
           self.db1_cursor.execute('rollback')
       self.db1_cursor.close()

#2017-12-08从尾端复制过来

   def tearDown(self):
       pass