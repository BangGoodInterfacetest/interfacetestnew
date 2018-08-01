#import Special_char_process
import copy
import mysql.connector
from globalconfig import Global

global_config = Global()
db1_conn = global_config.get_db1_conn()

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
#         #print("Query_Result", Query_Result)
#         column_name = db1_cursor.description  # 获取数据表列名
#         #print("column_name", column_name)
#         column_name_temp_list = []
#         Query_Result_dict = {}
#         # for k in index:
#         # print("k",k[0])
#         # 集合数据库中同属性值
#         for z in range(0, len(Query_Result[0])):
#             for i in range(0, len(Query_Result)):
#                 column_name_temp_list.append(Query_Result[i][z])
#         # 把同属性值归到属性名下并组成字典
#         p = len(Query_Result)
#         for k in column_name:
#             Query_Result_dict[k[0]] = column_name_temp_list[p * (column_name.index(k) + 1 - 1):p * (column_name.index(k) + 1)]
#             #print("Query_Result_dict1", Query_Result_dict)
#         # 字典去掉重复值
#         for key in Query_Result_dict.keys():  # print("a", a)
#             lista = list(set(Query_Result_dict[key]))
#             Query_Result_dict[key] = lista
#
#         #print("Query_Result_dict", Query_Result_dict)
#         db1_cursor.close()
#         db1_conn.close()
#         return Query_Result_dict
#     except mysql.connector.Error as e:
#         print(e)

def ExpectedResults_dict_SqlQuery(Param_Sql):
    try:
        # conn = mysql.connector.connect(host='127.0.0.1', port='3306', user='root', password='testdb', database='test',
        #                                charset='utf8')
        # print("conn", conn)
        # cur = conn.cursor()  # buffered=True
        # print("cur", cur)
        db1_conn=global_config.get_db1_conn()
        db1_cursor=db1_conn.cursor()
        db1_cursor.execute(Param_Sql)  # .fetchone()
        Query_Result = db1_cursor.fetchall()
        # print("Query_Result", Query_Result)
        column_name = db1_cursor.description  # 获取数据表列名
        # print("column_name", column_name)
        char_list=[]
        for char_list_num in range(len(column_name)):
            char_list.append(column_name[char_list_num][0])#查询属性字段组成列表
        # print("char_list",char_list)
        column_name_temp_list = []
        Query_Result_dict = {}
        # for k in index:
        # print("k",k[0])
        # 集合数据库中同属性值
        for z in range(0, len(Query_Result[0])):
            for i in range(0, len(Query_Result)):
                column_name_temp_list.append(Query_Result[i][z])
        # print("column_name_temp_list",column_name_temp_list)
        # 把同属性值归到属性名下并组成字典
        p = len(Query_Result)
        for k in column_name:
            Query_Result_dict[k[0]] = column_name_temp_list[p * (column_name.index(k) + 1 - 1):p * (column_name.index(k) + 1)]
            # print("Query_Result_dict1", Query_Result_dict)
        # 字典去掉重复值
        for key in Query_Result_dict.keys():  # print("a", a)
            lista = list(set(Query_Result_dict[key]))
            Query_Result_dict[key] = lista

        # print("Query_Result_dict", Query_Result_dict)
        db1_cursor.close()
        db1_conn.close()
        return Query_Result_dict,char_list
    except mysql.connector.Error as e:
        print(e)

# #把需要检查的关键字段及值从返回结果中抽取出来重新组成新字典
# def New_Response_Rusults_KeyCheck_Dict(Check_key, Response_result_dict, New_Response_result_value_list):
#         Response_dict = Response_result_dict
#         New_list = New_Response_result_value_list
#         if isinstance(Response_dict, dict):
#             for i in Response_dict.keys():
#                 if isinstance(Response_dict[i], dict) or isinstance(Response_dict[i], list) or isinstance(Response_dict[i], tuple):  #
#                     if len(Response_dict[i]) == 1 and Response_dict[i] not in New_list and i == Check_key:  # isinstance(ob[i][0])=='faul' :
#                         New_list.append(Response_dict[i])
#                     New_Response_Rusults_KeyCheck_Dict(Check_key, Response_dict[i], New_list)
#                 elif Response_dict[i] not in New_list and i == Check_key:
#                     New_list.append(Response_dict[i])
#         if isinstance(Response_dict, list):
#             for i in Response_dict:
#                 if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
#                     New_Response_Rusults_KeyCheck_Dict(Check_key, i, New_list)
#         if isinstance(Response_dict, tuple):
#             for i in Response_dict:
#                 if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
#                     New_Response_Rusults_KeyCheck_Dict(Check_key, i, New_list)
#         #print(listzzja)
#         New_KeyCheck_Value_Dict={}
#         New_KeyCheck_Value_Dict[Check_key]=New_list
#         #print("New_KeyCheck_Value_Dict",New_KeyCheck_Value_Dict)
#         return New_KeyCheck_Value_Dict
#把需要检查的关键字段及值从返回结果中抽取出来重新组成新字典
def New_Response_Rusults_KeyCheck_Dict(Check_key, Response_result_dict, New_Response_result_value_list,New_KeyCheck_Value_Dict,vkey):
    Response_dict = Response_result_dict
    New_list = list(New_Response_result_value_list)
    New_KeyCheck_Value_Dict = New_KeyCheck_Value_Dict
    posit_key = vkey #重新定位键
    k=0 #迭代次数统计，用来过滤包含子健（即键包含在值中）数据
    if isinstance(Response_dict, dict):#返回值为字典，则按字典处理
        for i in Response_dict.keys():
            New_list = []
            if isinstance(Response_dict[i], dict) or isinstance(Response_dict[i], list) or isinstance(Response_dict[i],tuple):  #判断字典值类型，如果是字典 、列表、元组则进行如下处理，最终进行迭代进入子集搜索查找需要的值
                if i not in str(Response_dict[i])and i in Check_key:#如果返回键不存在于它的值中，则把值作为此键的值，以下逻辑同上
                    if i in New_KeyCheck_Value_Dict.keys() and Response_dict[i] not in New_KeyCheck_Value_Dict[i]:
                        New_list = list(New_KeyCheck_Value_Dict[i])
                        New_list.append(Response_dict[i])
                        New_KeyCheck_Value_Dict[i] = New_list#New_list = list(New_KeyCheck_Value_Dict[i])
                    if i in New_KeyCheck_Value_Dict.keys() and  Response_dict[i]  in New_KeyCheck_Value_Dict[i]:
                        New_list = list(New_KeyCheck_Value_Dict[i])
                        New_KeyCheck_Value_Dict[i] = New_list
                    else:
                        New_list = []
                        New_list.append(Response_dict[i])
                        New_KeyCheck_Value_Dict[i] = New_list
                New_Response_Rusults_KeyCheck_Dict(Check_key, Response_dict[i], New_list,New_KeyCheck_Value_Dict,i)
            elif Response_dict[i] not in New_list and i in Check_key:# 如果非上述三种类型数据，如数字、字符串等，则直接作为对应键的值
                k = k+1
                if i in New_KeyCheck_Value_Dict.keys() and Response_dict[i] not in New_KeyCheck_Value_Dict[i]:
                    New_list =list(New_KeyCheck_Value_Dict[i])
                    New_list.append(Response_dict[i])
                    New_KeyCheck_Value_Dict[i] = New_list
                if i in New_KeyCheck_Value_Dict.keys() and  Response_dict[i]  in New_KeyCheck_Value_Dict[i]:
                    New_list = list(New_KeyCheck_Value_Dict[i])
                    New_KeyCheck_Value_Dict[i] = New_list
                else:
                    New_list=[]
                    New_list.append(Response_dict[i])
                    New_KeyCheck_Value_Dict[i] = New_list
    if isinstance(Response_dict, list):#返回值为列表，则按列表处理，内处理逻辑基本等同字典
        if posit_key in New_KeyCheck_Value_Dict.keys() :
            New_list = list(New_KeyCheck_Value_Dict[posit_key])
        else:
            New_list = []
        for i in Response_dict:
            if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
                New_Response_Rusults_KeyCheck_Dict(Check_key, i, New_list,New_KeyCheck_Value_Dict,posit_key)
        if k == 0 and posit_key in Check_key:
            if posit_key not in New_KeyCheck_Value_Dict.keys():
                New_KeyCheck_Value_Dict.setdefault(posit_key, [])#即键不存在于字典中，将会添加键并将值设为默认值
            if Response_dict not in New_KeyCheck_Value_Dict[posit_key]:
                if posit_key not in str(Response_dict):
                    New_list.append(Response_dict)
                else:
                    New_list=New_KeyCheck_Value_Dict[posit_key]
            New_KeyCheck_Value_Dict[posit_key] = New_list
    if isinstance(Response_dict, tuple):#返回值为元组，则按元组处理，内处理逻辑基本等同字典
        if posit_key in New_KeyCheck_Value_Dict.keys() :
            New_list = list(New_KeyCheck_Value_Dict[posit_key])
        else:
            New_list = []
        for i in Response_dict:
            if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
                New_Response_Rusults_KeyCheck_Dict(Check_key, i, New_list,New_KeyCheck_Value_Dict,posit_key)
        if k == 0 and posit_key in Check_key:
            if posit_key not in New_KeyCheck_Value_Dict.keys():
                New_KeyCheck_Value_Dict.setdefault(posit_key, [])#即键不存在于字典中，将会添加键并将值设为默认值
            if Response_dict not in New_KeyCheck_Value_Dict[posit_key]:
                if posit_key not in str(Response_dict):
                    New_list.append(Response_dict)
                else:
                    New_list=New_KeyCheck_Value_Dict[posit_key]
            New_KeyCheck_Value_Dict[posit_key] = New_list
    return New_KeyCheck_Value_Dict



#返回结果跟预期结果完全比较函数
def ExpResultVsResponse_json(ExpResult3,Response3):
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
    if ExpResult==Response:         #如果预期结果与返回值相等则结果完全测试通过
        str0='Pass'
        #print("str0")
    else:
        #dict11=dict(dict1.items()-dict2.items())
        #dict22=dict(dict2.items()-dict1.items())
        #print("dict11",dict11)
        #print("dict22", dict22)
        str0 = 'Fail'
        #键值比较
        for keys1,value1 in ExpResult3.items() :
            for keys2,value2 in Response3.items():
                if keys1==keys2 and value1==value2:  #删除掉相同值，检查出不同项
                    del ExpResult[keys1]
                    del Response[keys1]
        for keys in ExpResult.keys() & Response.keys(): #键值相同，值不同
           #print(keys)
           str1="预期结果的"+keys+"="+str(ExpResult[keys])[0:299]+'\n'+"实际结果的"+keys+"="+str(Response[keys])[0:299]+"或者键值"+keys+"不存在返回结果中"+";"+'\n'
           str2=str2+str1
           #print("str1:",str1)
           #print("str2:", str2)
           del ExpResult[keys]   #删除相同键项
           del Response[keys]
        if ExpResult!={}:#如果预期结果字典为空，则说明预期结果键都存在匹配
            str3 = "预期结果参数" + str(list(ExpResult.keys()))+ "无对应返回参数;" + '\n'
        if Response != {}:#如果返回结果字典为空，则说明返回结果键都存在匹配
            str4 = "返回的参数" + str(list(Response.keys()))+ "无对应预期参数;" + '\n'
        if ExpResult=={} and Response == {}:
            str3="预期结果与返回参数个数、名称完全相同,但"
            #print(ExpResult)
            #print(Response)
            #print(str3)
            #print(str4)
        str5=str3+str4+str2
        #print("str5:",str5)
    #print("str0",str0)
    return str0,str5

#用预期结果做参考标准，去跟返回结果比较，如果预期结果包含于或等于返回结果，则测试通过，否则失败
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


#字符串比较
def ExpResultVsResponse_text(ExpResult3,Response3):
    ExpResult=copy.deepcopy(ExpResult3)#self.ExpResult
    Response = str(Response3)
    result = ""
    reason=""
    if isinstance(ExpResult,dict) and ExpResult!={}:
        for i in ExpResult.values():
            if str(i) in Response:
                reason+=""
            else:
                reason+=","+str(i)
    elif isinstance(ExpResult, list) and ExpResult!=[]:#or isinstance(ExpResult, tuple) :
        for i in ExpResult:
            if str(i) in Response:
                reason += ""
            else:
                reason += ","+str(i)
    elif isinstance(ExpResult, tuple) and ExpResult!=() :
        for i in ExpResult:
            if str(i) in Response:
                reason += ""
            else:
                reason += ","+str(i)
    else:
        ExpResult = str(ExpResult3).split("&&")  # self.ExpResult
        for check_char in ExpResult:
            if check_char in Response:
                reason +=  ""
            else:
                reason += "," + check_char
    if reason=="":
        result='Pass'
    else:
        result = 'Fail'
        reason=reason+"等检查点信息不在返回结果信息中"
    return result,reason