# _*_ coding:utf-8 _*_
import mysql.connector
import time

# mysql数据库连接配置
# conn = mysql.connector.connect(
#     host = "172.16.11.40",
#     port = 13307,   # 07子库
#     user = "wspuser",
#     password = "wsppass",
#     database = "ews",
#     charset = "utf8",
#     )#cursorclass = pymysql.cursors.DictCursor
# cur=conn.cursor()

# try:
#    # with conn.cursor() as cursor:
#         cursor = conn.cursor()
#
#         i = 1
#         values = []
#         values_data = []
#         sql = """CREATE TABLE `sync_test_targer%s` (
#                 `Id` int(11) NOT NULL AUTO_INCREMENT,
#                 `Name` varchar(50) NOT NULL,
#                 `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
#                 PRIMARY KEY (`Id`),
#                 KEY `timestamp`(`timestamp`)
#                 ) ENGINE=InnoDB AUTO_INCREMENT=2147483647 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;"""
#         sql_drop = "DROP TABLE `sync_test_targer%s`;"
#         # sql_data = "INSERT INTO `sync_test_targer%s`  VALUES (%s, %s, %s)"
#         for i in range(1,10):
#                 values.append(i)
#                 ticks = time.time()
#                 ticks = ticks + 1
#                 time_local = time.localtime(ticks)
#                 dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
#                 values_data.append((i, i, dt))
#         print(values)
#         values=tuple(values)
#         print(values)
#         cursor.executemany(sql,values)
#         # cursor.executemany(sql_data, values_data)
#         # cursor.executemany(sql_drop,values)
#         conn.commit()
#
# finally:
#     conn.close()


# print(ticks)
# time_local = time.localtime(ticks)
# print(time_local)
# dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
# print(dt)

# for i in range(1,10):
#     type(ticks)
#     ticks = ticks + i
#     # print(ticks)
#     time_local = time.localtime(ticks)
#     # print(time_local)
#     dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
#     print(dt)

# try:
#     # with conn.cursor() as cursor:
#         ticks = time.time()
#         values = []
#         i = 1
#
#         for i in range(1, 10):
#             ticks = ticks + 1
#             time_local = time.localtime(ticks)
#             dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
#             # print(dt)
#             # sql_data = "INSERT INTO sync_test_targer%s   VALUES (%s, %s,%s)"
#             values.append((i,i,dt))
#             # print(values)
#             # cur.executemany(sql_data, values)
#         print("values=",values)
#         print(sql_data)
#         for a in range(1, 10):
#             sync_test_targer=''
#             sync_test_targer="sync_test_targer"+str(a)
#             print(sync_test_targer)
#             sql_data='INSERT INTO '+ sync_test_targer +' VALUES (%s,%s,%s)'
#             print(sql_data)
#             cur.executemany(sql_data, values)
#             conn.commit()
# finally:
#     conn.close()

# try:
#     with conn.cursor() as cursor:
#         ticks = time.time()
#         values = []
#         i = 1
#         j = 1
#         for i in range(1,3 ):
#             for j in range(1,3):
#                 ticks = ticks + 1
#                 time_local = time.localtime(ticks)
#                 dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
#                 sql_data = "INSERT INTO sync_test_targer{}  VALUES (%s ,%s ,%s );".format(i)
#                 values.append((j,j,dt))
#                 # print(values)
#             print(values)
#             # cur.executemany(sql_data,values)
#             # conn.commit()
#
# finally:
#     conn.close()