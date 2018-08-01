import base64
import io
import Special_char_process
import json
import copy
import urllib.request
import http.cookiejar
import urllib.parse
import configparser
import requests
'''a = "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
b = base64.b64encode(bytes(a,'gb2312')) # 对字符串编码  URLError(ConnectionRefusedError(10061, '由于目标计算机积极拒绝，无法连接。', None, 10061),) this is a test   <urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>
print ('b11:',b)
print ('b12:',base64.b64decode(b) )# 对字符串解码
c = io.StringIO()
c.write(a)
d = io.StringIO()
e = io.StringIO()
c.seek(0)
print(c, d)
#s1=str(c)
print(type(c))
base64.b64encode(bytes(str(c),'gb2312'))# 对StringIO内的数据进行编码
print (d.getvalue())
d.seek(0)
base64.decode(d, e) # 对StringIO内的数据进行解码
print (e.getvalue())
a = "this is a +test"
b = base64.urlsafe_b64encode(bytes(a,'gb2312')) # 进行url的字符串编码
print (b)
print (base64.urlsafe_b64decode(b))

a="qwert"
temp = a[:]
for i in temp:
    if 'q' in i:
        print(i)
        str(i)
        li=i.replace('q','a')
        print(li)
        li +=li
        #i.
        #a[2]=""
print(a)

char="<te'e\\e\"e&e||e%r*t（y-u)3>"
temp=str(char)
for i in  temp:
        if '<'==i:
            char= char.replace('<','《')
        if '>' == i:
            char = char.replace('>', '》')
        if '\'' == i:
            char = char.replace('\'', '') #处理单引号
        if '\\' == i:
            char = char.replace('\\', '') #处理反斜杠 \
        if '\"' == i:
            char = char.replace('\"', '_')  # 处理双引号"
        if '&' == i:
            char = char.replace('&', '_')  # 处理双引号&
        if '|' == i:
            char = char.replace('|', '')
        if '@' == i:
            char = char.replace('@', '.')
        if '%' == i:
            char = char.replace('%', "`")  # 处理单引号
        if '*' == i:
            char = char.replace('*', '`')  # 处理反斜杠\
        if '("' == i:
            char = char.replace('\"', '`')  # 处理双引号"
        if ')"' == i:
            char = char.replace(')"', '`')
        if '-' == i:
            char = char.replace('-', '`')  # 处理&号"
            print(char)
print(char)'''
'''list1=[]
list2=[]
dict1={'t':{1},'y':3,'z':4}
y={str(dict1).replace('{','').replace('}','')}#{Special_char_process.SpCharReplace(str(dict1))}
#print(eval(y))
#y=y.lstrip('(')
#y=y.rstrip(')')

a=json.loads(y)#dict(y)#list(y)# {"'y': 3, 'z': 4, 't': 1"}
b=a
print(str(dict1))
print(y)
print(a)'''
'''dict2={'t':2,'y':1,'z':2}
dict3={}
dict4={}
str1=""
str2=""
str3=""
str4=""
if dict1==dict2:
    print("pass")
else:

    dict11=dict(dict1.items()-dict2.items())
    dict22=dict(dict2.items()-dict1.items())
    print("dict11",dict11)
    print("dict22", dict22)
    for keys in dict11.keys() & dict22.keys():
       #print(keys)
       str1="预期结果的"+keys+"="+str(dict11[keys])+'\n'+"实际结果的."+keys+"="+str(dict22[keys])+";"+'\n'
       str2=str2+str1
       print("str1:",str1)
       print("str2:", str2)
       del dict11[keys]
       del dict22[keys]
    if dict11!={}:
        str3 = "预期结果参数" + str(list(dict11.keys()))+ "无对应返回参数;" + '\n'
    if dict22 != {}:
        str4 = "返回的参数" + str(list(dict22.keys()))+ "无对应预期参数;" + '\n'
        print(dict11)
        print(dict22)
        print(str3)
        print(str4)
    str5=str2+str3+str4
    print("str5:",str5)'''
'''list1=[]
list2=[]
dict3={'t':{1},'y':3,'z':5}
dict4={'t':{1},'y':4,'u':6}
dict1 = copy.deepcopy(dict3)
dict2 = copy.deepcopy(dict4)
#print("dict41", dict4)
#del dict1['t']
#del dict2['t']
#print("dict42", dict4)
str1=""
str2=""
str3=""
str4=""
str5=""
if dict3==dict4:
    print("pass")
else:
    #dict11=dict(dict1.items()-dict2.items())
    #dict22=dict(dict2.items()-dict1.items())
    #print("dict11",dict11)
    #print("dict22", dict22)
    #yy=dict1.items() & dict2.items()
    #print("yy",yy)
       for keys1,value1 in dict3.items():
           print("dict3",dict3)
           for keys2, value2 in dict4.items():
               print("dict4", dict4)
               if keys1==keys2 and value1==value2:
                   # print("dict41", dict4)
                    del dict1[keys1]
                    del dict2[keys1]
                    print("dict42", dict4)
                    print("dict1",dict1)
               print("dict11", dict1)
print("dict12", dict1)
                #dict3 = dict1
                #print("dict1",dict1)
for keys in dict1.keys() & dict2.keys():
        print("www",dict1.keys() & dict2.keys())
       #print(keys)
        str1="预期结果的"+keys+"="+str(dict1[keys])+'\n'+"实际结果的."+keys+"="+str(dict2[keys])+";"+'\n'
        str2=str2+str1
       #print("str1:",str1)
       #print("str2:", str2)
       #del dict1[keys]
       #del dict2[keys]
        if dict1!={}:
            str3 = "预期结果参数" + str(list(dict1.keys()))+ "无对应返回参数;" + '\n'
        if dict2 != {}:
            str4 = "返回的参数" + str(list(dict2.keys()))+ "无对应预期参数;" + '\n'
        #print(dict1)
        #print(dict2)
        #print(str3)
        #print(str4)
        str5=str2+str3+str4
print("str5:",str5)
#取值<br>import types'''
'''allGuests = {'Alice': {'apples': 5, 'pretzels': {'12':{'beijing':456}}},
             'Bob': {'ham sandwiches': 3, 'apple': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
def dictget(dict1,obj,default=None):
    for k,v in dict1.items():
        if k == obj:
            print("V",v)
        else:
            if type(v) is dict:
                re=dictget(v,obj)
                if re is not default:
                    print("re",re)
dictget(allGuests,'beijing')'''
'''import copy
def ExpResultVsResponse(ExpResult3,Response3):
    ExpResult=copy.deepcopy(ExpResult3)#self.ExpResult
    Response = copy.deepcopy(Response3)
    #Response={'t':2,'y':1,'z':2}
    #dict3={}
    #dict4={}
    str0 = ""
    str1=""
    str2=""
    str3=""
    str4=""
    str5 = ""
    #ExpResult=ExpResult.relpace('{','(').relpace('}',')')
    #print(" ExpResult", ExpResult)
    #Response={Special_char_process.SpCharReplace(str(Response))}
    if ExpResult==Response:
        str0='Pass'
        #print("str0")
    else:
        #dict11=dict(dict1.items()-dict2.items())
        #dict22=dict(dict2.items()-dict1.items())
        #print("dict11",dict11)
        #print("dict22", dict22)
        str0 = 'Fail'
        for keys1,value1 in ExpResult3.items() :
            for keys2,value2 in Response3.items():
                if keys1==keys2 and value1==value2:
                    del ExpResult[keys1]
                    del Response[keys1]
                    print("ExpResult[keys133]", ExpResult)
                else:
                    if keys1==keys2 and type(ExpResult[keys1]) is dict and type(Response[keys1]) is dict:
                        print("ExpResult[keys111]", ExpResult[keys1])
                        ExpResultVsResponse(ExpResult[keys1], Response[keys1])
                        print("ExpResult[keys122]", ExpResult[keys1])
    print("ExpResult[keys144]", ExpResult)
    return ExpResult,Response
#######################################
#def ExpResultVsResponse(ExpResult3,Response3):
ExpResult3={'data': {'processingTypes': '0', 'assignTime': None, 'modifyUserId': None, 'pushCount': 0, 'isMultiItem': True, 'settleStatus': None, 'batchType': 0, 'batchStatus': 0, 'createUserId': 0, 'pushStatus': 0, 'basketTypeId': '07a612aeb6784c5b88cd3fabce85141c', 'createTime': '2017-11-22 11:31:32', 'taskComputeStatus': 0, 'computeBatchCode': 'CB-17112211170001', 'settleUserId': None, 'fnCode': 'FN-7-00039', 'allocateTaskDetails': [{'batchCode': 'OBG-17112211120837001', 'quantity': 10, 'detailId': None, 'products': {'propuctRackStocklist': [], 'productName_EN': 'xxx', 'pbeBarCode': 'PBE131996', 'productCode': 'SKU059911', 'propertyId': 68016, 'productName': '华为Mate10 金色手机套', 'propertyCode': 'POA062514', 'processCenterId': 9, 'productType': 1, 'productStatus': 1, 'productDocumentNum': 0, 'propuctRackStockmain': None, 'productId': 131996, 'propertyValue': '透明色'}, 'productCode': 'SKU059911', 'propertyId': 68016, 'productId': 131996, 'propertyCode': 'POA062514', 'taskCode': 'MK1711221118001', 'remarks': None}], 'fn2Orders': [{'batchCode': 'OBG-17112211120837001', 'orderCode': 'A0000922021702DA'}], 'pushTime': None, 'assignUserId': 0, 'taskCode': 'MK1711221118001', 'batchCode': 'OBG-17112211120837001', 'processCenterId': 7, 'batchPrintType': 0, 'settleTime': None, 'taskId': 22, 'taskStatus': 2, 'allocateUserId': 0, 'taskComputedDate': None, 'modifyTime': None}, 'message': None, 'isSuccess': True}
#{'t':{'t1':{2},'t2':{2}},'u':3} #{'t1': {2}, 't2': {2}}#
Response3={'data': {'processingTypes': '0', 'assignTime': None, 'modifyUserId': 909, 'pushCount': 3, 'isMultiItem': True, 'settleStatus': None, 'batchType': 0, 'batchStatus': 0, 'createUserId': 0, 'pushStatus': 1, 'basketTypeId': '07a612aeb6784c5b88cd3fabce85141c', 'createTime': '2017-11-22 11:31:32', 'taskComputeStatus': 0, 'computeBatchCode': 'CB-17112114024393587', 'settleUserId': None, 'fnCode': 'FN-7-00039', 'allocateTaskDetails': [{'batchCode': 'OBG-17112211120837001', 'quantity': 10, 'detailId': None, 'products': {'propuctRackStocklist': [], 'processCenterId': 7, 'pbeBarCode': 'PBE131996', 'productCode': 'SKU059911', 'productStatus': 1, 'productName': 'xxx', 'propertyCode': 'POA062514', 'productDocumentNum': 0, 'productType': 1, 'propertyId': 68016, 'productName_EN': 'xxx', 'propuctRackStockmain': None, 'productId': 131996, 'propertyValue': '透明'}, 'completeQuantity': 5, 'productCode': 'SKU059911', 'propertyId': 68016, 'productId': 131996, 'propertyCode': 'POA062514', 'taskCode': 'MK1711221118001', 'remarks': None}], 'fn2Orders': [{'batchCode': 'K171219000461', 'orderCode': 'A0004317121900WP'}], 'pushTime': '2017-12-18 14:24:54', 'assignUserId': 0, 'taskCode': 'MK1711221118001', 'batchCode': 'K171219000461', 'processCenterId': 7, 'batchPrintType': 1, 'settleTime': None, 'taskId': 22, 'taskStatus': 0, 'allocateUserId': 0, 'taskComputedDate': None, 'modifyTime': '2017-11-23 17:51:45'}, 'message': '成功', 'isSuccess': True}
#{'t':{'t1':{3},'t2':{2}},'u':3}#{'t1': {3}, 't2': {2}}#
ExpResult=copy.deepcopy(ExpResult3)#self.ExpResult
Response = copy.deepcopy(Response3)
    #Response={'t':2,'y':1,'z':2}
    #dict3={}
    #dict4={}
str0 = ""
str1=""
str2=""
str3=""
str4=""
str5 = ""
x=''
y=''
    #ExpResult=ExpResult.relpace('{','(').relpace('}',')')
    #print(" ExpResult", ExpResult)
    #Response={Special_char_process.SpCharReplace(str(Response))}
if ExpResult==Response:
    str0='Pass'
        #print("str0")
else:
        #dict11=dict(dict1.items()-dict2.items())
        #dict22=dict(dict2.items()-dict1.items())
        #print("dict11",dict11)
        #print("dict22", dict22)
        str0 = 'Fail'
        for keys1,value1 in ExpResult3.items() :
            for keys2,value2 in Response3.items():
                if keys1==keys2 and value1==value2:
                    del ExpResult[keys1]
                    del Response[keys1]
                else:
                    if keys1==keys2 and type(ExpResult[keys1]) is dict and type(Response[keys1]) is dict:
                        print("ExpResult[keys1]", ExpResult[keys1])
                        print("Response[keys1]", Response[keys1])
                        (x,y)=ExpResultVsResponse(ExpResult[keys1], Response[keys1])
                        #print("ExpResult1", x)
                    #print("ExpResult2",x)
                #print("ExpResult3", x)
            #print("ExpResult4", x)
        #print("ExpResult5", x)
print("ExpResult6", x,'\n'"Response6", y)
print(type({3}))
for keys in x.keys() & y.keys():
           #print(keys)
           str1="预期结果的"+keys+"="+str(x[keys])[0:299]+'\n'+"实际结果的."+keys+"="+str(y[keys])[0:299]+";"+'\n'
           str2=str2+str1
           #print("str1:",str1)
           #print("str2:", str2)
           #del ExpResult[keys]
           #del Response[keys]
print (str2)'''


#def post(self, url, data):
data='pageIndex=1&pageSize=10&orderBy=OperateBarCodeLogId+desc&search=%60op%60op%7CUserName%60OperatedDate%60OperatedDate%7C%E9%82%93%E5%BF%97%E9%94%8B%602017-12-24+0%3A00%602018-1-25+19%3A40%7Ceq%60GreatEq%60LessEq&rowCount=0'
url='http://192.168.1.81:1111/Admin/OperateBarCodeLog'
#headers = {'Accept':'*/*','Accept-Encoding': 'gzip, deflate','Accept-Language':'zh-CN',
        # 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
          #}
headers = {'Host':'192.168.1.81:1111',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://192.168.1.81:1111/Admin/OperateBarCodeLog?sMenuId=46',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest',
'Content-Length': '220',
'Cookie': 'EWS_USER_Email=SXIlMmJzJTJiNDVsc09DSTZtVG93dzZEZUtZaVpLYktlc2FobGl6b3Y1VjNYREVMVTlYRmlaYyUyYjdFdURCVnhWRlh3WFpoUmI3UjhUZGNnems2SkpkeiUyYklBQ1NySFM0eUFuN1M=',
'Connection': 'keep-alive'}
'''headers ='Host: 192.168.1.81:1111
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Referer: http://192.168.1.81:1111/Admin/OperateBarCodeLog?sMenuId=46
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 220
Cookie: SXIlMmJzJTJiNDVsc09DSTZtVG93dzZEZUtZaVpLYktlc2FobGl6b3Y1VjNYREVMVTlYRmlaYyUyYjdFdURCVnhWRlh3WFpoUmI3UjhUZGNnems2SkpkeiUyYklBQ1NySFM0eUFuN1M=
Connection: keep-alive'''
#data = json.dumps(eval(data))
#print("eval(data):",data)
data = data.encode('utf-8')
print("data.encode('utf-8'):",data)
#headers=headers.encode('utf-8')
print("headers.encode('utf-8')",headers)
#url = 'http://' + self.host + ':' + str(self.port) + url
print("url:",url)
try:
    request = urllib.request.Request(url, headers)
    print("request:",request)
    response = urllib.request.urlopen(request, data)
    #response = requests.post(url, data)
    print("response:",response)
    response = response.read().decode('utf-8')
    print("decode('utf-8')response:", response)
    json_response = (json.loads(response))
    print("json_response:",json_response)
       # return json_response
except Exception as e:
    print('%s' % e)
    E_response = ({}, e)
        #return E_response
#post(self,url='http://192.168.1.81:1111/Admin/OperateBarCodeLog',data='pageIndex=1&pageSize=10&orderBy=OperateBarCodeLogId+desc&search=%60op%60op%7CUserName%60OperatedDate%60OperatedDate%7C%E9%82%93%E5%BF%97%E9%94%8B%602017-12-24+0%3A00%602018-1-25+19%3A40%7Ceq%60GreatEq%60LessEq&rowCount=0')


#runcase.py
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
                 db1_cursor.execute('SELECT http_method, request_name,interface_name, request_url, request_param, test_method, test_desc '
                                      'FROM test_data WHERE case_id = %s',(case_id,))
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
                 runner.run(test_suite)
                 db1_cursor.close()
                 db2_cursor.close()
        else:   # 运行部分用例
            # 循环执行测试用例
            for case_id in run_case_list:
                 db1_cursor = db1_conn.cursor()
                 db2_cursor = db2_conn.cursor()
                 db1_cursor.execute('SELECT http_method, request_name,interface_name,request_url, request_param, test_method, test_desc '
                                      'FROM test_data WHERE case_id = %s',(case_id,))
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
                    test_data.result = ''
                    test_data.reason = ''
                 else:
                     test_data.case_id = case_id
                     test_data.http_method = 'empt'
                     test_data.request_name = 'empt'
                     test_data.interface_name = 'empt'
                     test_data.request_url = 'test'
                     test_data.request_param = 'empt'
                     test_data.test_method = 'EWMS'
                     test_data.test_desc = ''
                     test_data.result = ''
                     test_data.reason = str(case_id)+ '不存在与用例表中'

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
                 runner.run(test_suite)
                 db1_cursor.close()

                 测试