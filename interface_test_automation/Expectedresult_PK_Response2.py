#import Special_char_process
import copy
import mysql.connector
from globalconfig import Global

global_config = Global()
db1_conn = global_config.get_db1_conn()
#
#预期结果为sql语句查询情况时，对查询结果进行字典化：查询字段属性名为字典键，查询值组成列表为字典值
# def ExpectedResults_dict_SqlQuery(Param_Sql):
#     try:
#         # conn = mysql.connector.connect(host='127.0.0.1', port='3306', user='root', password='testdb', database='test',
#         #                                charset='utf8')
#         # print("conn", conn)
#         # cur = conn.cursor()  # buffered=True
#         # print("cur", cur)
#         db1_conn=global_config.get_db1_conn()
#         db1_cursor=db1_conn.cursor()
#         db1_cursor.execute(Param_Sql)  # .fetchone()
#         Query_Result = db1_cursor.fetchall()
#         print("Query_Result", Query_Result)
#         column_name = db1_cursor.description  # 获取数据表列名
#         print("column_name", column_name)
#         char_list=[]
#         for char_list_num in range(len(column_name)):
#             char_list.append(column_name[char_list_num][0])#查询属性字段组成列表
#         print("char_list",char_list)
#         column_name_temp_list = []
#         Query_Result_dict = {}
#         # for k in index:
#         # print("k",k[0])
#         # 集合数据库中同属性值
#         for z in range(0, len(Query_Result[0])):
#             for i in range(0, len(Query_Result)):
#                 column_name_temp_list.append(Query_Result[i][z])
#         print("column_name_temp_list",column_name_temp_list)
#         # 把同属性值归到属性名下并组成字典
#         p = len(Query_Result)
#         for k in column_name:
#             Query_Result_dict[k[0]] = column_name_temp_list[p * (column_name.index(k) + 1 - 1):p * (column_name.index(k) + 1)]
#             print("Query_Result_dict1", Query_Result_dict)
#         # 字典去掉重复值
#         for key in Query_Result_dict.keys():  # print("a", a)
#             lista = list(set(Query_Result_dict[key]))
#             Query_Result_dict[key] = lista
#
#         print("Query_Result_dict", Query_Result_dict)
#         db1_cursor.close()
#         db1_conn.close()
#         return Query_Result_dict,char_list
#     except mysql.connector.Error as e:
#         print(e)
#
#
#把需要检查的关键字段及值从返回结果中抽取出来重新组成新字典
# def New_Response_Rusults_KeyCheck_Dict(Check_key, Response_result_dict, New_Response_result_value_list):
#         Response_dict = Response_result_dict
#         New_list = New_Response_result_value_list
#         print("Check_key",Check_key)
#         New_KeyCheck_Value_Dict = {}
#         for z in range(0,len(Check_key)):
#             print("z",Check_key[z])
#             if Check_key[z] in New_KeyCheck_Value_Dict.keys():
#                 print("New_KeyCheck_Value_Dict[Check_key[z]]=",New_KeyCheck_Value_Dict[Check_key[z]])
#                 print("New_list3=", New_list)
#                 New_list.append(New_KeyCheck_Value_Dict[Check_key[z]])
#                 print("New_list4=", New_list)
#             else:
#                 New_list = []
#                 print("New_list3", type(New_list))
#             if isinstance(Response_dict, dict):
#                 for i in Response_dict.keys():
#                     print("New_list",type(New_list))
#                     print("i==", i)
#                     if isinstance(Response_dict[i], dict) or isinstance(Response_dict[i], list) or isinstance(Response_dict[i], tuple):  #
#                         if len(Response_dict[i]) == 1 and Response_dict[i] not in New_list and i == Check_key[z]:  # isinstance(ob[i][0])=='faul' :
#                             New_list.append(Response_dict[i])
#                             New_KeyCheck_Value_Dict[i] = New_list
#                             print("New_list.append(Response_dict[i])--1",New_list.append(Response_dict[i]))
#                             print("New_KeyCheck_Value_Dict[i]--1", New_KeyCheck_Value_Dict[i])
#                         New_Response_Rusults_KeyCheck_Dict(Check_key, Response_dict[i], New_list)
#                     elif Response_dict[i] not in New_list and i  == Check_key[z]:
#                         print("Response_dict[i]--2",Response_dict[i])
#                         print("New_list--21", New_list)
#                         New_list.append(Response_dict[i])
#                         New_KeyCheck_Value_Dict[i] = New_list
#                         aa=New_KeyCheck_Value_Dict
#                         print("New_list--22", New_list)
#                         print("New_KeyCheck_Value_Dict[i]--2",New_KeyCheck_Value_Dict[i])
#             if isinstance(Response_dict, list):
#                 for i in Response_dict:
#                     if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
#                         New_Response_Rusults_KeyCheck_Dict(Check_key, i, New_list)
#             if isinstance(Response_dict, tuple):
#                 for i in Response_dict:
#                     if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
# #                         New_Response_Rusults_KeyCheck_Dict(Check_key, i, New_list)
#         #print(listzzja)
#             # New_KeyCheck_Value_Dict={}
#             # print("New_list2", type(New_list))
#             # print("New_list2", New_list)
#             # # New_KeyCheck_Value_Dict[Check_key[z]]=New_list
#             # New_KeyCheck_Value_Dict=aa
#             # # # # New_KeyCheck_Value_Dict +=aa
#             # print("New_KeyCheck_Value_Dict1",aa)
#
#
#         print("New_KeyCheck_Value_Dict2", New_KeyCheck_Value_Dict)
#         return New_KeyCheck_Value_Dict
#
# #返回结果跟预期结果完全比较函数
# def ExpResultVsResponse_json(ExpResult3,Response3):
#     ExpResult=copy.deepcopy(ExpResult3)#self.ExpResult
#     Response = copy.deepcopy(Response3)
#     #Response={'t':2,'y':1,'z':2}
#     #dict3={}
#     #dict4={}
#     str0 = ""
#     str1=""
#     str2=""
#     str3=""
#     str4=""
#     str5 = ""
#     #ExpResult=ExpResult.relpace('{','(').relpace('}',')')
#     #print(" ExpResult", ExpResult)
#     #Response={Special_char_process.SpCharReplace(str(Response))}
#     if ExpResult==Response:         #如果预期结果与返回值相等则结果完全测试通过
#         str0='Pass'
#         #print("str0")
#     else:
#         #dict11=dict(dict1.items()-dict2.items())
#         #dict22=dict(dict2.items()-dict1.items())
#         #print("dict11",dict11)
#         #print("dict22", dict22)
#         str0 = 'Fail'
#         #键值比较
#         for keys1,value1 in ExpResult3.items() :
#             for keys2,value2 in Response3.items():
#                 if keys1==keys2 and value1==value2:  #删除掉相同值，检查出不同项
#                     del ExpResult[keys1]
#                     del Response[keys1]
#         for keys in ExpResult.keys() & Response.keys(): #键值相同，值不同
#            #print(keys)
#            str1="预期结果的"+keys+"="+str(ExpResult[keys])[0:299]+'\n'+"实际结果的."+keys+"="+str(Response[keys])[0:299]+";"+'\n'
#            str2=str2+str1
#            #print("str1:",str1)
#            #print("str2:", str2)
#            del ExpResult[keys]   #删除相同键项
#            del Response[keys]
#         if ExpResult!={}:#如果预期结果字典为空，则说明预期结果键都存在匹配
#             str3 = "预期结果参数" + str(list(ExpResult.keys()))+ "无对应返回参数;" + '\n'
#         if Response != {}:#如果返回结果字典为空，则说明返回结果键都存在匹配
#             str4 = "返回的参数" + str(list(Response.keys()))+ "无对应预期参数;" + '\n'
#         if ExpResult=={} and Response == {}:
#             str3="预期结果与返回参数个数、名称完全相同,但"
#             #print(ExpResult)
#             #print(Response)
#             #print(str3)
#             #print(str4)
#         str5=str3+str4+str2
#         #print("str5:",str5)
#     #print("str0",str0)
#     return str0,str5
# #1、完全比较；2、
#
# def ExpResultVsResponse_char(ExpResult3,Response3):
#     ExpResult=ExpResult3.split("&&")#self.ExpResult
#     print("ExpResult",ExpResult,type(ExpResult))
#     Response = str(Response3)
#     print("Response", Response,type(Response))
#     result_str=""
#     reason_str = ""
#     for check_char in ExpResult:
#         print("check_char", check_char)
#         if check_char in Response:
#             reason_str=reason_str+""
#         else:
#             reason_str = reason_str+check_char+","
#             print("str1", reason_str)
#     print("str12", reason_str)
#     if reason_str=="":
#         result_str="Pass"
#     else:
#         result_str = "Fail"
#         reason_str="字符串"+reason_str+"等不存在于返回结果中"
#     return result_str,reason_str
# def ExpResultVsResponse_text(ExpResult3,Response3):
#     ExpResult=copy.deepcopy(ExpResult3)#self.ExpResult
#     Response = str(Response3)
#     result = ""
#     reason=""
#     if isinstance(ExpResult,dict) and ExpResult!={}:
#         for i in ExpResult.values():
#             if str(i) in Response:
#                 reason+=""
#             else:
#                 reason+=","+str(i)
#     elif isinstance(ExpResult, list) and ExpResult!=[]:#or isinstance(ExpResult, tuple) :
#         for i in ExpResult:
#             if str(i) in Response:
#                 reason += ""
#             else:
#                 reason += ","+str(i)
#     elif isinstance(ExpResult, tuple) and ExpResult!=() :
#         for i in ExpResult:
#             if str(i) in Response:
#                 reason += ""
#             else:
#                 reason += ","+str(i)
#     else:
#         ExpResult = str(ExpResult3).split("&&")  # self.ExpResult
#         Response = str(Response3)
#         for check_char in ExpResult:
#             if check_char in Response:
#                 reason +=  ""
#             else:
#                 reason += "," + check_char
#                 print("str1", reason)
#     if reason=="":
#         result='Pass'
#     else:
#         result = 'Fail'
#         reason=reason+"等检查点信息不在返回结果信息中"
#     return result,reason
# ExpResult3='{2,[3],(4,5),{8}}'#''a&&1&&2&&[3,6]&&(4,5)&&{8,9}&&zuozhijun'
# Response3={'a':1,'b':(2,[3],(4,5),{8})}
# a1,a2=ExpResultVsResponse_text(ExpResult3,Response3)
# print(a1,a2)
#
# # sql="select case_id from test_data"


#把需要检查的关键字段及值从返回结果中抽取出来重新组成新字典
# def New_Response_Rusults_KeyCheck_Dict(Check_key, Response_result_dict, New_Response_result_value_list,New_KeyCheck_Value_Dict,vkey):
#     Response_dict = Response_result_dict
#     New_list = list(New_Response_result_value_list)
#     New_KeyCheck_Value_Dict = New_KeyCheck_Value_Dict
#     posit_key = vkey #重新定位键
#     k=0 #迭代次数统计，用来过滤包含子健（即键包含在值中）数据
#     if isinstance(Response_dict, dict):#返回值为字典，则按字典处理
#         for i in Response_dict.keys():
#             print("字典处理开始,键值i=",i,"New_KeyCheck_Value_Dict=",New_KeyCheck_Value_Dict,"New_list=",New_list)
#             New_list = []
#             if isinstance(Response_dict[i], dict) or isinstance(Response_dict[i], list) or isinstance(Response_dict[i],tuple):  #判断字典值类型，如果是字典 、列表、元组则进行如下处理，最终进行迭代进入子集搜索查找需要的值
#                 print("Response_dict[i]-10=", Response_dict[i])
#                 if len(Response_dict[i]) == 1 and Response_dict[i] not in New_list and i in Check_key:
#                     print("Response_dict[i]--101=", Response_dict[i])
#                     k=k+1
#                     if i in New_KeyCheck_Value_Dict.keys() and Response_dict[i] not in New_KeyCheck_Value_Dict[i]:#如果返回值不存在 重组装的字典中，则把此值添加为对应的键的值
#                         print("Response_dict[i]--1011=", Response_dict[i])
#                         New_list = list(New_KeyCheck_Value_Dict[i])
#                         print("New_list-1011=", New_list)
#                     else:
#                         New_list = []
#                     if i not in str(Response_dict[i]):#如果返回键不存在于它的值中，则把值作为此键的值
#                         print("Response_dict[i]-1012=", Response_dict[i])
#                         print("New_list-10121=", New_list)
#                         New_list.append(Response_dict[i])
#                         print("New_list-101221=", New_list)
#                     New_KeyCheck_Value_Dict[i] = New_list
#                     print("New_KeyCheck_Value_Dict[i]--101=", New_KeyCheck_Value_Dict[i])
#                 elif i not in str(Response_dict[i])and i in Check_key:#如果返回键不存在于它的值中，则把值作为此键的值，以下逻辑同上
#                     print("Response_dict[i]-102=", Response_dict[i])
#                     if i in New_KeyCheck_Value_Dict.keys() and Response_dict[i] not in New_KeyCheck_Value_Dict[i]:
#                         print("Response_dict[i]-1021=", Response_dict[i])
#                         print("New_list-10221=", New_list)
#                         New_KeyCheck_Value_Dict[i].append(Response_dict[i])#New_list = list(New_KeyCheck_Value_Dict[i])
#                         print("New_list-10222=", New_list)
#                     else:
#                         New_list = []
#                     # New_list.append(Response_dict[i])
#                     # print("New_list-1031=", New_list)
#                     #
#                     # New_KeyCheck_Value_Dict[i] = New_list
#                     # print("New_KeyCheck_Value_Dict[i]-1031=", New_KeyCheck_Value_Dict[i])
#
#                 print("字典中开始迭代:","Check_key==",Check_key,"Response_dict[i]==",Response_dict[i],"New_list==",New_list,"New_KeyCheck_Value_Dict=",New_KeyCheck_Value_Dict,"i==",i)
#                 New_Response_Rusults_KeyCheck_Dict(Check_key, Response_dict[i], New_list,New_KeyCheck_Value_Dict,i)
#                 print("字典中迭代结束:", "Check_key==", Check_key, "Response_dict[i]==", Response_dict[i], "New_list==", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "i==", i)
#             elif Response_dict[i] not in New_list and i in Check_key:# 如果非上述三种类型数据，如数字、字符串等，则直接作为对应键的值
#                 print("Response_dict[i]-20=", Response_dict[i])
#                 k = k+1
#                 if i in New_KeyCheck_Value_Dict.keys() and Response_dict[i] not in New_KeyCheck_Value_Dict[i]:
#                     print("Response_dict[i]-201=", Response_dict[i])
#                     print("New_list-2011=", New_list)
#                     New_list =list(New_KeyCheck_Value_Dict[i])
#                     print("New_list-2012=", New_list)
#                 else:
#                     New_list=[]
#                 New_list.append(Response_dict[i])
#                 print("New_list-2021=", New_list)
#
#                 New_KeyCheck_Value_Dict[i] = New_list
#                 print("New_KeyCheck_Value_Dict[i]-2021=", New_KeyCheck_Value_Dict[i])
#
#     if isinstance(Response_dict, list):#返回值为列表，则按字典处理，内处理逻辑基本等同字典
#         print("开始处理列表:", "Check_key==", Check_key, "Response_dict[i]==", Response_dict, "New_list==", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#         if posit_key in New_KeyCheck_Value_Dict.keys() :
#             New_list = list(New_KeyCheck_Value_Dict[posit_key])
#             print("New_list-3011=", New_list)
#         else:
#             New_list = []
#         for i in Response_dict:
#             if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
#                 print("列表中开始迭代:", "Check_key==", Check_key, "", i, "New_list==",New_list, "New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#                 New_Response_Rusults_KeyCheck_Dict(Check_key, i, New_list,New_KeyCheck_Value_Dict,posit_key)
#                 print("列表中结束迭代:", "Check_key==", Check_key, "Response_dict[i]==", i, "New_list==", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#         if k == 0 and posit_key in Check_key:
#             if posit_key not in New_KeyCheck_Value_Dict.keys():
#                 print("posit_key--3021=",posit_key)
#                 New_KeyCheck_Value_Dict.setdefault(posit_key, [])#即键不存在于字典中，将会添加键并将值设为默认值
#                 print("New_KeyCheck_Value_Dict-30211=", New_KeyCheck_Value_Dict)
#             if Response_dict not in New_KeyCheck_Value_Dict[posit_key]:
#                 if posit_key not in str(Response_dict):
#                     print("New_list-30221=", New_list)
#                     New_list.append(Response_dict)
#                     print("New_list-30222=", New_list)
#                 else:
#                     print("New_list-30231=", New_list)
#                     New_list=New_KeyCheck_Value_Dict[posit_key]
#                     print("New_list-30232=", New_list)
#             New_KeyCheck_Value_Dict[posit_key] = New_list
#             print("New_KeyCheck_Value_Dict-303=", New_KeyCheck_Value_Dict)
#         print("结束处理列表:", "Check_key==", Check_key, "Response_dict[i]==", Response_dict, "New_list==", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#     if isinstance(Response_dict, tuple):#返回值为列表，则按字典处理，内处理逻辑基本等同字典
#         print("开始处理元组:", "Check_key==", Check_key, "Response_dict[i]==", Response_dict, "New_list==", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#         if posit_key in New_KeyCheck_Value_Dict.keys() :
#             New_list = list(New_KeyCheck_Value_Dict[posit_key])
#             print("New_list-4011=", New_list)
#         else:
#             New_list = []
#
#         for i in Response_dict:
#             if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
#                 print("列表中开始迭代:", "Check_key==", Check_key, "", i, "New_list==", New_list, "New_KeyCheck_Value_Dic=t",New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#                 New_Response_Rusults_KeyCheck_Dict(Check_key, i, New_list,New_KeyCheck_Value_Dict,posit_key)
#                 print("列表中结束迭代:", "Check_key==", Check_key, "", i, "New_list==", New_list, "New_KeyCheck_Value_Dict=",New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#
#         if k == 0 and posit_key in Check_key:
#             if posit_key not in New_KeyCheck_Value_Dict.keys():
#                 print("posit_key--4021=", posit_key)
#                 New_KeyCheck_Value_Dict.setdefault(posit_key, ())#即键不存在于字典中，将会添加键并将值设为默认值
#                 print("New_KeyCheck_Value_Dict-40211=", New_KeyCheck_Value_Dict)
#
#             if Response_dict not in New_KeyCheck_Value_Dict[posit_key]:
#                 if posit_key not in str(Response_dict):
#                     print("New_list-40221=", New_list)
#                     New_list.append(Response_dict)
#                     print("New_list-40222==", New_list)
#
#                 else:
#                     print("New_list-40231", New_list)
#                     New_list=New_KeyCheck_Value_Dict[posit_key]
#                     print("New_list-40232=", New_list)
#
#             New_KeyCheck_Value_Dict[posit_key] = New_list
#             print("New_KeyCheck_Value_Dict-403==", New_KeyCheck_Value_Dict)
#         print("结束处理列表:", "Check_key=", Check_key, "Response_dict[i]=", Response_dict, "New_list=", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key=", posit_key)
#     return New_KeyCheck_Value_Dict

# def New_Response_Rusults_KeyCheck_Dict(Check_key, Response_result_dict, New_Response_result_value_list,New_KeyCheck_Value_Dict,vkey):
#     Response_dict = Response_result_dict
#     New_list = list(New_Response_result_value_list)
#     New_KeyCheck_Value_Dict = New_KeyCheck_Value_Dict
#     posit_key = vkey #重新定位键
#     k=0 #迭代次数统计，用来过滤包含子健（即键包含在值中）数据
#     if isinstance(Response_dict, dict):#返回值为字典，则按字典处理
#         for i in Response_dict.keys():
#             print("字典处理开始,键值i=",i,"New_KeyCheck_Value_Dict=",New_KeyCheck_Value_Dict,"New_list=",New_list)
#             New_list = []
#             if isinstance(Response_dict[i], dict) or isinstance(Response_dict[i], list) or isinstance(Response_dict[i],tuple):  #判断字典值类型，如果是字典 、列表、元组则进行如下处理，最终进行迭代进入子集搜索查找需要的值
#                 print("Response_dict[i]-10=", Response_dict[i])
#                 if i not in str(Response_dict[i])and i in Check_key:#如果返回键不存在于它的值中，则把值作为此键的值，以下逻辑同上
#                     print("Response_dict[i]-102=", Response_dict[i])
#                     if i in New_KeyCheck_Value_Dict.keys() and Response_dict[i] not in New_KeyCheck_Value_Dict[i]:
#                         print("Response_dict[i]-1021=", Response_dict[i])
#                         print("New_list-10211=", New_list)
#                         New_list = list(New_KeyCheck_Value_Dict[i])
#                         New_list.append(Response_dict[i])
#                         New_KeyCheck_Value_Dict[i] = New_list#New_list = list(New_KeyCheck_Value_Dict[i])
#                         print("New_list-10212=", New_KeyCheck_Value_Dict)
#                     if i in New_KeyCheck_Value_Dict.keys() and  Response_dict[i]  in New_KeyCheck_Value_Dict[i]:
#                         New_list = list(New_KeyCheck_Value_Dict[i])
#                         New_KeyCheck_Value_Dict[i] = New_list
#                         print("New_KeyCheck_Value_Dict-10213=", New_KeyCheck_Value_Dict)
#                     else:
#                         New_list = []
#                         New_list.append(Response_dict[i])
#                         print("New_list-1022=", New_list)
#
#                         New_KeyCheck_Value_Dict[i] = New_list
#                         print("New_KeyCheck_Value_Dict[i]-10221=", New_KeyCheck_Value_Dict[i])
#
#                 print("字典中开始迭代:","Response_dict[i]==",Response_dict[i],"New_list==",New_list,"New_KeyCheck_Value_Dict=",New_KeyCheck_Value_Dict,"i==",i)
#                 New_Response_Rusults_KeyCheck_Dict(Check_key, Response_dict[i], New_list,New_KeyCheck_Value_Dict,i)
#                 print("字典中迭代结束:", "Response_dict[i]==", Response_dict[i], "New_list==", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "i==", i)
#             elif Response_dict[i] not in New_list and i in Check_key:# 如果非上述三种类型数据，如数字、字符串等，则直接作为对应键的值
#                 print("Response_dict[i]-20=", Response_dict[i])
#                 k = k+1
#                 if i in New_KeyCheck_Value_Dict.keys() and Response_dict[i] not in New_KeyCheck_Value_Dict[i]:
#                     print("Response_dict[i]-201=", Response_dict[i])
#                     print("New_list-2011=", New_list)
#                     print("New_KeyCheck_Value_Dict[i]t-2011=", New_KeyCheck_Value_Dict[i])
#                     New_list =list(New_KeyCheck_Value_Dict[i])
#                     New_list.append(Response_dict[i])
#                     New_KeyCheck_Value_Dict[i] = New_list
#                     print("New_list-2012=", New_list)
#                 if i in New_KeyCheck_Value_Dict.keys() and  Response_dict[i]  in New_KeyCheck_Value_Dict[i]:
#                     New_list = list(New_KeyCheck_Value_Dict[i])
#                     New_KeyCheck_Value_Dict[i] = New_list
#                     print("New_KeyCheck_Value_Dict-2013=", New_KeyCheck_Value_Dict)
#                 else:
#                     New_list=[]
#                     New_list.append(Response_dict[i])
#                     print("New_list-2021=", New_list)
#
#                     New_KeyCheck_Value_Dict[i] = New_list
#                     print("New_KeyCheck_Value_Dict[i]-2021=", New_KeyCheck_Value_Dict[i])
#
#     if isinstance(Response_dict, list):#返回值为列表，则按列表处理，内处理逻辑基本等同字典
#         print("开始处理列表:",  "Response_dict[i]==", Response_dict, "New_list==", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#         if posit_key in New_KeyCheck_Value_Dict.keys() :
#             New_list = list(New_KeyCheck_Value_Dict[posit_key])
#             print("New_list-3011=", New_list)
#         else:
#             New_list = []
#         for i in Response_dict:
#             if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
#                 print("列表中开始迭代:", "i=", i, "New_list==",New_list, "New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#                 New_Response_Rusults_KeyCheck_Dict(Check_key, i, New_list,New_KeyCheck_Value_Dict,posit_key)
#                 print("列表中结束迭代:",  "Response_dict[i]==", i, "New_list==", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#         if k == 0 and posit_key in Check_key:
#             if posit_key not in New_KeyCheck_Value_Dict.keys():
#                 print("posit_key--3021=",posit_key)
#                 New_KeyCheck_Value_Dict.setdefault(posit_key, [])#即键不存在于字典中，将会添加键并将值设为默认值
#                 print("New_KeyCheck_Value_Dict-30211=", New_KeyCheck_Value_Dict)
#             if Response_dict not in New_KeyCheck_Value_Dict[posit_key]:
#                 if posit_key not in str(Response_dict):
#                     print("New_list-30221=", New_list)
#                     New_list.append(Response_dict)
#                     print("New_list-30222=", New_list)
#                 else:
#                     print("New_list-30231=", New_list)
#                     New_list=New_KeyCheck_Value_Dict[posit_key]
#                     print("New_list-30232=", New_list)
#             New_KeyCheck_Value_Dict[posit_key] = New_list
#             print("New_KeyCheck_Value_Dict-303=", New_KeyCheck_Value_Dict)
#         print("结束处理列表:", "Response_dict[i]==", Response_dict, "New_list==", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#     if isinstance(Response_dict, tuple):#返回值为元组，则按元组处理，内处理逻辑基本等同字典
#         print("开始处理元组:", "Response_dict[i]==", Response_dict, "New_list==", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#         if posit_key in New_KeyCheck_Value_Dict.keys() :
#             print("New_KeyCheck_Value_Dict[posit_key]-4011=", New_KeyCheck_Value_Dict[posit_key])
#             New_list = list(New_KeyCheck_Value_Dict[posit_key])
#             print("New_list-4011=", New_list)
#         else:
#             New_list = []
#
#         for i in Response_dict:
#             if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
#                 print("列表中开始迭代:",  "i=", i, "New_list==", New_list, "New_KeyCheck_Value_Dic=t",New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#                 New_Response_Rusults_KeyCheck_Dict(Check_key, i, New_list,New_KeyCheck_Value_Dict,posit_key)
#                 print("列表中结束迭代:", "i=", i, "New_list==", New_list, "New_KeyCheck_Value_Dict=",New_KeyCheck_Value_Dict, "posit_key==", posit_key)
#
#         if k == 0 and posit_key in Check_key:
#             if posit_key not in New_KeyCheck_Value_Dict.keys():
#                 print("posit_key--4021=", posit_key)
#                 New_KeyCheck_Value_Dict.setdefault(posit_key, [])#即键不存在于字典中，将会添加键并将值设为默认值
#                 print("New_KeyCheck_Value_Dict-40211=", New_KeyCheck_Value_Dict)
#
#             if Response_dict not in New_KeyCheck_Value_Dict[posit_key]:
#                 if posit_key not in str(Response_dict):
#                     print("New_list-40221=", New_list)
#                     New_list.append(Response_dict)
#                     print("New_list-40222==", New_list)
#
#                 else:
#                     print("New_list-40231", New_list)
#                     New_list=New_KeyCheck_Value_Dict[posit_key]
#                     print("New_list-40232=", New_list)
#
#             New_KeyCheck_Value_Dict[posit_key] = New_list
#             print("New_KeyCheck_Value_Dict-403==", New_KeyCheck_Value_Dict)
#         print("结束处理列表:",  "Response_dict[i]=", Response_dict, "New_list=", New_list,"New_KeyCheck_Value_Dict=", New_KeyCheck_Value_Dict, "posit_key=", posit_key)
#     return New_KeyCheck_Value_Dict
# #
# # key=('case_id3','case_id2','case_id1')
# # # rpd={'case_id1':(1,2),'case_id2':{2},'case_id3':{'case_id2':[[{'case_id2':4,'case_id4':({'case_id2':5,'case_id1':(3,[6])})}]]}}#'case_id1':1,'case_id2':2,'
# rpd={'case_id1':(1),'case_id2':{2},'case_id3':{'case_id2':[[{'case_id2':4,'case_id4':({'case_id2':5,'case_id1':(3,[6])})}]]}}
# # # rpd={'case_id1':(1,2,{'case_id2':7}),'case_id2':{2},'case_id3':{'case_id2':[[{'case_id2':4,'case_id4':({'case_id2':5,'case_id1':(3,[6])})}]]}}
# # # rpd={'case_id1':(1,2,{'case_id2':7}),'case_id2':{2},'case_id3':{'case_id2':[[{'case_id2':4,'case_id3':({'case_id2':5,'case_id1':(3,[6])})}]]}}
# # # rpd={'case_id1':(1,2,{'case_id2':7}),'case_id2':{2},'case_id3':{'case_id2':(({'case_id2':4,'case_id3':({'case_id2':5,'case_id1':(3,[6])})}))}}
# # # rpd={'case_id1':(1,2,{'case_id2':7}),'case_id2':{2},'case_id3':{'case_id2':(({'case_id2':(4,{}),'case_id3':({'case_id2':5,'case_id1':(3,[6])})}))}}
# # # rpd={'case_id1':(1,2,{'case_id2':7}),'case_id2':7,'case_id3':{'case_id2':(({'case_id2':(4,{'case_id2':5}),'case_id3':({'case_id2':8,'case_id1':(3,[6])})}))}}
# # # rpd={'case_id1':(1,2,{'case_id2':7}),'case_id2':7,'case_id3':{'case_id2':(({'case_id2':(4,{'case_id2':7}),'case_id3':({'case_id2':8,'case_id1':(3,[6])})}))}}
# # # rpd={'case_id1':(1,2,{'case_id2':7}),'case_id2':7,'case_id3':{'case_id2':(({'case_id2':(4,{'case_id2':7}),'case_id3':({'case_id2':8,'case_id1':(1,2,{'case_id2':7})})}))}}
# # # rpd={'case_id1':(1,2,{'case_id2':7}),'case_id2':7,'case_id3':{'case_id2':(({'case_id2':(4,{'case_id1':7}),'case_id3':({'case_id2':8,'case_id1':(1,2,{'case_id2':7})})}))}}
# # # rpd=({'case_id1':(1),'case_id2':{2},'case_id3':{'case_id2':[[{'case_id2':4,'case_id4':({'case_id2':5,'case_id1':(3,[6])})}]]}})
# # # rpd=[{'case_id1':(1,2,{'case_id2':7}),'case_id2':7,'case_id3':{'case_id2':(({'case_id2':(4,{'case_id1':7}),'case_id3':({'case_id2':8,'case_id1':(1,2,{'case_id2':7})})}))}}]
# # # rpd=[{'case_id1':(1,2,{'case_id2':7}),'case_id2':2,'case_id3':{'case_id2':(({'case_id2':(4,{'case_id2':5}),'case_id3':({'case_id2':8,'case_id1':(1,2,{'case_id1':(3,[6])})})}))}}]
# # rpd={'case_id3': [{'case_id2': [[{'case_id2': {'case_id2': 5, 'case_id1': (3, [6])}}]]}], 'case_id2': [{'case_id2': [[{'case_id2': {'case_id2': 5, 'case_id1': (3, [6])}}]]}, [[{'case_id2': {'case_id2': 5, 'case_id1': (3, [6])}}]], {2}], 'case_id1': [(3, [6]), 1]}
# # rpdk=New_Response_Rusults_KeyCheck_Dict(key,rpd,[],{},'')
# # ln=[]
# sql="select case_id as case_id1 ,test_desc from test_data"
# # eqd=ExpectedResults_dict_SqlQuery(sql).Query_Result_dict
# key=ExpectedResults_dict_SqlQuery(sql)[0]#char_list
# # # # print("eqd",eqd)
# rpdk=New_Response_Rusults_KeyCheck_Dict(key,rpd,[],{},'')
# print("rpdk",rpdk)
# # a,b=ExpResultVsResponse_json(eqd,rpdk)
# # print("a",a)
# # print("b",b)
# testr='12345'
# teste=1#[]#()#{}#(1,2,3,7,9)#1#{'a':123,'b':7}
# t1,t2=ExpResultVsResponse_text(teste,testr)
# print(t1,t2)
#{'case_id3': [{'case_id2': [[{'case_id2': {'case_id2': 5, 'case_id1': (3, [6])}}]]}], 'case_id2': [{'case_id2': [[{'case_id2': {'case_id2': 5, 'case_id1': (3, [6])}}]]}, [[{'case_id2': {'case_id2': 5, 'case_id1': (3, [6])}}]], {2}], 'case_id1': [(3, [6]), 1]}

#用预期结果去跟返回结果比较，如果预期结果包含或等于返回结果，则测试通过，否则失败
def ExpResultVsResponse_ExpResult_json(ExpResult,Response):
    ExpResult=copy.deepcopy(ExpResult)#self.ExpResult
    Response = copy.deepcopy(Response)
    result = ""
    str1=""
    str2=""
    str3=""
    str4=""
    reason = ""
    if ExpResult==Response:         #如果预期结果与返回值相等则结果完全测试通过
        result='Pass'
    else:
        #键值比较
        for keys1,value1 in ExpResult.items() :
            for keys2,value2 in Response.items():
                if keys1==keys2 and value1==value2:  #删除掉相同值，检查出不同项
                    del ExpResult[keys1]
                    del Response[keys1]
        if ExpResult=={}:#如果上面已经将预期结果字典删除为空，说明预期结果全部符合预期输出，则测试通过
            result = 'Pass'
        else:
            result = 'Fail'
            if Response=={}:
                str3 = "预期结果参数" + str(list(ExpResult.keys()))+ "无对应返回参数;" + '\n'
            else:
                for keys in ExpResult.keys() & Response.keys(): #键相同，值不同
                   #print(keys)
                   str1="预期结果的"+keys+"="+str(ExpResult[keys])[0:299]+','+"实际结果的"+keys+"="+str(Response[keys])[0:299]+";"+'\n'
                   str2=str2+str1
                   del ExpResult[keys]   #删除相同键项
                   del Response[keys]
                if ExpResult!={}:#如果预期结果字典为空，则说明预期结果键都存在匹配
                    str3 = "预期结果参数" + str(list(ExpResult.keys()))+ "无对应返回参数;" + '\n'
                if ExpResult=={}:
                    str4="预期结果与返回参数个数、名称完全相同,但"
        reason=str3+str4+str2
    return result,reason
ek={'a':1,'b':2,'c':4}
rk={'a':1,'b':2,'d':5}
result,reason=ExpResultVsResponse_ExpResult_json(ek,rk)
print("result",result)
print("reason",reason)
