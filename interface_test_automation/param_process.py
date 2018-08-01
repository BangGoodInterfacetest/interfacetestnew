import mysql.connector
from globalconfig import Global

global_config = Global()
db1_conn = global_config.get_db1_conn()

#预期结果为sql语句查询情况时，对查询结果进行字典化：查询字段属性名为字典键，查询值组成列表为字典值
def Param_Sql_process(Param_Sql):
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
        print("Query_Result", Query_Result)
        column_name = db1_cursor.description  # 获取数据表列名
        db1_cursor.close()
        db1_conn.close()
        print("column_name", column_name)
        column_name_temp_list = []
        Query_Result_dict = {}
        # 集合数据库中同属性值
        for z in range(0, len(Query_Result[0])):
            for i in range(0, len(Query_Result)):
                column_name_temp_list.append(Query_Result[i][z])
        # 把同属性值归到属性名下并组成字典
        p = len(Query_Result)
        for k in column_name:
            Query_Result_dict[k[0]] = column_name_temp_list[p * (column_name.index(k) + 1 - 1):p * (column_name.index(k) + 1)]
            print("Query_Result_dict1", Query_Result_dict)
        # 字典去掉重复值
        for key in Query_Result_dict.keys():  # print("a", a)
            lista = list(set(Query_Result_dict[key]))
            Query_Result_dict[key] = lista

        print("Query_Result_dict", Query_Result_dict)
        for listkey in Query_Result_dict.keys():
            bbv=Query_Result_dict[listkey]#[0:len(Query_Result_dict[listkey])]
            bbb2 = str(bbv)[1:len(str(bbv)) - 1]#去掉list的[]符号
            Query_Result_dict[listkey]=bbb2

        return Query_Result_dict
    except mysql.connector.Error as e:
        print(e)
sqlchar='select case_id,request_name from test_data'
zzzz=Param_Sql_process(sqlchar)
print("zzzz",zzzz)
