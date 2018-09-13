# coding=utf-8

'''import requests


def test_build_job(self):
    self.url = 'http://172.16.4.70:8081/education_manage/login/login.do?key=key


'
# 以下代码 requests模拟登录后保存的cookie，之后再对系统操作就一直登录状态
conn = requests.session()

postdata = {
    'enName': 'xuecheng',
    'password': '123456'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
rep = conn.post(url, data=postdata, headers=headers)

return conn

r = conn.post(self.test_url, data={'name':'0212','seq':'1',"isApp":"0","enabled":"1"})    最后就一直用这个 conn  来调用Post，就能 往系统里写数据了
【冒泡】北京-星星 2018/2/13 11:42:36
因为这个conn带着返回来的cookie呢。我觉得 他就是 模拟了 登录，然后存了cookie,然后一直用他返回来的对象 就能一直保持 有效链接才能操作平台'''
'''
import math
a= float(input("please input a="))
b= float(input("please input b="))
c= float(input("please input c="))
t1=max(a,b,c)
t2=min(a,b,c)
t4=a+b+c-t1-t2
if a>0and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("area=",area)
        if  max(a,b,c)-min(a,b,c)==0:
            print("等边三角形")
        elif t1!=t2 and t4==t2:
            print("等腰三角形")
        elif t1*t1== t2*t2+t4*t4:
            print("直角三角形")
        else:
            print("任意三角形")
    else:
        print("非三角形")
else:
    print("输入错误,三角形边不能为非正数")
import globalconfig
rr=globalconfig.Global()
db1_cursor=globalconfig.Global().get_db1_conn()
db1_cursor.execute('UPDATE test_result SET result = %s,reason = %s  WHERE case_id = %s', (self.test_data.result,self.test_data.reason, self.test_data.case_id))
db1_cursor().close()
#db1_cursor = db1_conn.cursor()
import copy
a={'a':1,'b':{'b':2},'c':[3,{'c':2}]}
i="b"
p=[]
for i1 in a.keys():
    if i1==i:
        print(i1)
        print(a[i])
        p.append(a[i])
        print(p)
print(p)
print(isinstance(p,list))
def judge_type(key,object1,listzzja):
    k=key
    ob=object1
    listzzj=listzzja
    if isinstance(ob,dict):
        for i in ob.keys() :
            if isinstance(ob[i],dict) or isinstance(ob[i],list) or isinstance(ob[i],tuple) :
                judge_type(key, ob[i],listzzj)
            elif ob[i] not in listzzj and i==key :
                    listzzj.append(ob[i])
    if isinstance(ob,list):
        for i in ob :
            if isinstance(i,dict) or isinstance(i,list) or isinstance(i,tuple) :
                judge_type(key, i,listzzj)
    if isinstance(ob, tuple):
        for i in ob:
            if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
                judge_type(key, i,listzzj)
    print(listzzja)
    return listzzja
    #print(listzzj)
def judge_type(key,object1,listzzja):
    k=key
    ob=object1
    listzzj=listzzja
    if isinstance(ob,dict):
        for i in ob.keys() :
            if isinstance(ob[i],dict) or isinstance(ob[i],list) or isinstance(ob[i],tuple)  :#
                if len(ob[i])==1 and ob[i] not in listzzj and i==key :# isinstance(ob[i][0])=='faul' :
                    listzzj.append(ob[i])
                judge_type(key, ob[i],listzzj)
            elif ob[i] not in listzzj and i==key :
                    listzzj.append(ob[i])
    if isinstance(ob,list):
        for i in ob :
            if isinstance(i,dict) or isinstance(i,list) or isinstance(i,tuple) :
                judge_type(key, i,listzzj)
    if isinstance(ob, tuple):
        for i in ob:
            if isinstance(i, dict) or isinstance(i, list) or isinstance(i, tuple):
                judge_type(key, i,listzzj)
    print(listzzja)
    return listzzj
def lis_change_dict(key,listzzj,dictzzj):
    dictzzj[key]=listzzj
    print(dictzzj)
    return dictzzj
key='c'
object1= {'a':1,'b':{'b':2,'c':({9})},'c':[3,{'b':(5,{'a':6,'d':7},{'c':[({(7,8)})]}),'c':4}]}
#print(object1[1])
listzzja=[]
dictzzj={}
zz1=judge_type(key,object1,listzzja)
zz2=lis_change_dict(key,zz1,dictzzj={})
print(zz1,zz2)'''

'''import mysql.connector
try:
    conn = mysql.connector.connect(host='127.0.0.1', port='3306', user='root', password='testdb', database='test', charset='utf8')
    cur=conn.cursor()#buffered=True
    print("cur",cur)
    cur.execute('SELECT * FROM test_data where case_id in(1,2,3)')#.fetchone()
    result2 =cur.fetchall()
    print("result2",result2)
    column_name = cur.description#获取数据表列名
    print("index", column_name)
    a=[]
    b={}
    print
    #for k in index:
       #print("k",k[0])
    #集合数据库中同属性值
    for z in range(0, len(result2[0])):
        for i in range(0, len(result2)):
            a.append(result2[i][z])
    #把同属性值归到属性名下下 组成字典
    p=len(result2)
    for k in column_name:
        b[k[0]]=a[p*(column_name.index(k)+1-1):p*(column_name.index(k)+1)]
        print("b1", b)
    #去掉重复值
    for key in b.keys():        #print("a", a)
        lista=list(set(b[key]))
        b[key]=lista


    print("b", b)
    cur.close()
    conn.close()
except mysql.connector.Error as e:
    print(e)'''
'''import mysql.connector
def query(self, sql):
    connect = self.connect()
    cur = connect.cursor()
    cur.execute(sql)
    index = cur.description
    result = []
    for res in cur.fetchall():
        row = {}
        for i in range(len(index) - 1):
            row[index[i][0]] = res[i]
        result.append(row)
    connect.close()
    return result
sql2='SELECT expectedresults FROM test_data where case_id in(9)'
conn = mysql.connector.connect(host='127.0.0.1', port='3306', user='root', password='testdb', database='test', charset='utf8')
ss=query(conn,sql2)
print|(ss)

print (ss)

import cx_Oracle'''
'''import mysql.connector

def main():
    conn = mysql.connector.connect(host='127.0.0.1', port='3306', user='root', password='testdb', database='test', charset='utf8')
    cur = conn.cursor()

    sql = "SELECT * FROM test_data"# where case_id in(1,2,3)"
    result = cur.execute(sql)

    # 获取数据表的列名，并输出
    title = cur.description
    print(title)

    # 格式化字符串
    g = lambda k: "%-8s" % k
    print("g=",g)
    title = map(g, title)
    print(title)

    for i in title:
        print(i)


    # 输出查询结果
    for i in result.fetchmany(10):
        for k in map(g, i):
            print(k)



if __name__ == '__main__':
    main()

https://knewone.com/?page=1
from bs4 import beatfulsoup
import requests,time'''

# import mysql.connector
# try:
#     conn = mysql.connector.connect(host='127.0.0.1', port='3306', user='root', password='testdb', database='test', charset='utf8')
#     print("conn",conn)
#     cur=conn.cursor()#buffered=True
#     print("cur",cur)
#     cur.execute('SELECT expectedresults FROM test_data where case_id in(9)')#.fetchone()
#     result2 =cur.fetchone()[0]
#     print("result2",result2)
#     cur.execute(result2)
#     result3=cur.fetchall()
#     print("result3", result3)
# except mysql.connector.Error as e:
# #     print(e)
#
# def k(a,b):
#     a=b
#     return a,b
# b=4
# a=''
# d,c,e=k(a,b)
# print(c,d,e)
# !/usr/bin/python
# -*- coding: UTF-8 -*-
#
# class FooParent(object):
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print('Parent')
#
#     def bar(self, message):
#         print("%s from Parent" % message)
#
#
# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
#         super(FooChild, self).__init__()
#         print('Child')
#
#     def bar(self, message):
#         super(FooChild, self).bar(message)
#         print('Child bar fuction')
#         print(self.parent)
#
#
# if __name__ == '__main__':
#     fooChild = FooChild()
#     print("fooChild:",fooChild)
#     fooChild.bar('HelloWorld')

# a={3}
# b={'c':''}
# print("c", type(a))
# if a in b['c']:
#     print("a存在于b")

# import  random
# import itertools
# import math
# a= int (input("please input a="))
# list_a=[]
# list_b=[]
# list_c=[]
# list_d=[]
# list_e=[]
# fm_b=1
# for i in range(1,a+1):
#      list_a.append(i)
#      fm_b=fm_b*i
# print("list_a",list_a,fm_b/24)
# # list_a=(1,2,3,4,5,6,8,9,10,12)
# for i in itertools.combinations(list_a,4):
#     if sum(i)==34:
#         list_b.append(i)
# print("list_b",list_b)
# for i in itertools.combinations(list_b, 8):
#     list_d.append(i)
# print("list_d",list_d)
# # print("list_d",len(list_d))
# i3=()
#
# i5=()
# for i1 in list_d:
#     str = ''
#     k1 = 0
#     for i2 in i1:
#         # print("i2", i2)
#         i3=i3+i2
#         # print("i3",i3)
#     i4=i3
#     i3=()
#     # print("i4", i4)
#     for i in i4:
#         if i4.count(i)==2:
#             # print("i", i)
#             k1=k1+2
#             # print("k1", k1)
#             # zz=math.ceil(i4.index(i)%len(i2))
#             # zz1=math.ceil(i4.rindex(i)%len(i2))
#             # print("zz", zz)
#             # print("zz1", zz1)
#             str=str+'Y'
#     # print("k11", k1)
#     k2=k1/len(i4)
#     # print("k2", k2)
#     # print("str",str)
#     if k2==2:
#         i5=i1
#         list_e.append(i5)
#     # print("i5", i5)
# print("list_e", list_e)
# print("list_e",len(list_e))
# list_f=[]
#
# list_h=[]
# tuple_a=()
# # list_e=[((1, 2, 9, 12), (1, 3, 8, 12), (2, 4, 8, 10), (3, 5, 6, 10), (4, 5, 6, 9)), ((1, 2, 9, 12), (1, 5, 6, 12), (2, 4, 8, 10), (3, 4, 8, 9), (3, 5, 6, 10)), ((1, 2, 9, 12), (1, 5, 8, 10), (2, 4, 6, 12), (3, 4, 8, 9), (3, 5, 6, 10)), ((1, 2, 9, 12), (1, 6, 8, 9), (2, 4, 8, 10), (3, 4, 5, 12), (3, 5, 6, 10)), ((1, 3, 8, 12), (1, 4, 9, 10), (2, 4, 6, 12), (2, 5, 8, 9), (3, 5, 6, 10)), ((1, 3, 8, 12), (1, 5, 6, 12), (2, 3, 9, 10), (2, 4, 8, 10), (4, 5, 6, 9)), ((1, 3, 8, 12), (1, 5, 8, 10), (2, 3, 9, 10), (2, 4, 6, 12), (4, 5, 6, 9)), ((1, 5, 6, 12), (1, 5, 8, 10), (2, 3, 9, 10), (2, 4, 6, 12), (3, 4, 8, 9)), ((1, 5, 6, 12), (1, 6, 8, 9), (2, 3, 9, 10), (2, 4, 8, 10), (3, 4, 5, 12)), ((1, 5, 8, 10), (1, 6, 8, 9), (2, 3, 9, 10), (2, 4, 6, 12), (3, 4, 5, 12))]
# #[((1, 3, 8, 12), (1, 4, 9, 10), (2, 4, 6, 12), (2, 5, 8, 9), (3, 5, 6, 10))]#[((2, 6, 8, 9), (3, 4, 6, 12), (3, 4, 8, 10), (3, 5, 8, 9), (4, 5, 6, 10))]#[((1, 2, 9, 10), (1, 3, 8, 10), (2, 5, 6, 9), (3, 4, 7, 8), (4, 5, 6, 7))]
# for i7 in list_e:
#     tuple_a = i7
#     print("i7",i7)
#     list_g = []
#
#     for i2 in i7:
#         indx=i7.index(i2)
#         list_f = []
#         for i3 in range(0,len(i7)):
#             if indx!=i3:
#                 print("i2[i3]",i7[i3])
#                 list_f.append(i7[i3])
#         print("list_f",len(list_f),list_f)
#         # list_g = []
#         for i5 in range(0,len(list_f)) :
#             # print("i4", i4)
#             k=0
#             for i4 in i2:
#                 print("i4", i4)
#                 for i6 in list_f[i5]:
#                     if i4==i6:
#                         k+=1
#             if k<2:
#                 list_g.append(list_f[i5])
#                 print("list_g", len(list_g), list_g)
#     if len(list_g)==len(list_f)*len(tuple_a):
#         list_h.append(tuple_a)
#         print("list_h", len(list_h), list_h)
# print("list_h",len(list_h),list_h)




# t=list(itertools.combinations(list_a, 4))
# print(t)

# for i in range(1,int(fm_b/24)+1):
#     list_b=random.sample(list_a, 4)
#     if  list_b not in list_c:
#         list_c.append(random.sample(list_a, 4))
# print("list_c",list_c)
# # listb=list(set(list_b))
# listb={}.fromkeys(list_b).keys()
# print("list_b",list_b)
    # if sum(list_b)==22:
    #     print("list_b",list_b,sum(list_b))
# a=2
# b=3
# print(2%2)

# import  random
# import itertools
# import math
# a= int (input("please input a="))
# list_a=[]
# list_b=[]
# list_c=[]
# list_d=[]
# list_e=[]
# fm_b=1
# for i in range(1,a+1):
#      list_a.append(i)
#      fm_b=fm_b*i
# print("list_a",list_a,fm_b/24)
# # list_a=(1,2,3,4,5,6,8,9,10,12)
# for i in itertools.combinations(list_a,3):
#     if sum(i)==15:
#         list_b.append(i)
# print("list_b",len(list_b),list_b)
# for za in itertools.combinations(list_b, 6):
#     # print("za",za)
#     # list_d.append(za)
#     # print("list_d",list_d)
#     # print("len(za)",len(za))
#     i3=()
#
#     i5=()
#     for i1 in za:
#         str = ''
#         k1 = 0
#         # print("i1", i1)
#         # for i2 in i1:
#         # print("i2", i2)
#         i3=i3+i1
#             # print("i3",i3)
#     i4=i3
#     i3=()
#     # print("i4", i4)
#     for i in i4:
#         if i4.count(i)==2:
#                 # print("i", i)
#             k1=k1+2
#                 # print("k1", k1)
#                 # zz=math.ceil(i4.index(i)%len(i2))
#                 # zz1=math.ceil(i4.rindex(i)%len(i2))
#                 # print("zz", zz)
#                 # print("zz1", zz1)
#             str=str+'Y'
#         # print("k11", k1)
#     k2=k1/len(i4)
#         # print("k2", k2)
#         # print("str",str)
#     if k2==2:
#         i5=za
#         list_e.append(i5)
#         # print("i5", i5)
#     # print("list_e", list_e)
#     # print("list_e",len(list_e))
#     list_f=[]
#
#     list_h=[]
#     tuple_a=()
#     # list_e=[((1, 2, 9, 12), (1, 3, 8, 12), (2, 4, 8, 10), (3, 5, 6, 10), (4, 5, 6, 9)), ((1, 2, 9, 12), (1, 5, 6, 12), (2, 4, 8, 10), (3, 4, 8, 9), (3, 5, 6, 10)), ((1, 2, 9, 12), (1, 5, 8, 10), (2, 4, 6, 12), (3, 4, 8, 9), (3, 5, 6, 10)), ((1, 2, 9, 12), (1, 6, 8, 9), (2, 4, 8, 10), (3, 4, 5, 12), (3, 5, 6, 10)), ((1, 3, 8, 12), (1, 4, 9, 10), (2, 4, 6, 12), (2, 5, 8, 9), (3, 5, 6, 10)), ((1, 3, 8, 12), (1, 5, 6, 12), (2, 3, 9, 10), (2, 4, 8, 10), (4, 5, 6, 9)), ((1, 3, 8, 12), (1, 5, 8, 10), (2, 3, 9, 10), (2, 4, 6, 12), (4, 5, 6, 9)), ((1, 5, 6, 12), (1, 5, 8, 10), (2, 3, 9, 10), (2, 4, 6, 12), (3, 4, 8, 9)), ((1, 5, 6, 12), (1, 6, 8, 9), (2, 3, 9, 10), (2, 4, 8, 10), (3, 4, 5, 12)), ((1, 5, 8, 10), (1, 6, 8, 9), (2, 3, 9, 10), (2, 4, 6, 12), (3, 4, 5, 12))]
#     #[((1, 3, 8, 12), (1, 4, 9, 10), (2, 4, 6, 12), (2, 5, 8, 9), (3, 5, 6, 10))]#[((2, 6, 8, 9), (3, 4, 6, 12), (3, 4, 8, 10), (3, 5, 8, 9), (4, 5, 6, 10))]#[((1, 2, 9, 10), (1, 3, 8, 10), (2, 5, 6, 9), (3, 4, 7, 8), (4, 5, 6, 7))]
#     for i7 in list_e:
#         tuple_a = i7
#         # print("i7",i7)
#         list_g = []
#
#         for i9 in i7:
#             indx=i7.index(i9)
#             list_f = []
#             for i10 in range(0,len(i7)):
#                 if indx!=i10:
#                     # print("i7[i10]",i7[i10])
#                     list_f.append(i7[i10])
#             # print("list_f",len(list_f),list_f)
#             # list_g = []
#             for i5 in range(0,len(list_f)) :
#                 # print("i4", i4)
#                 k=0
#                 for i8 in i9:
#                     # print("i8", i8)
#                     for i6 in list_f[i5]:
#                         if i8==i6:
#                             k+=1
#                 if k<2:
#                     list_g.append(list_f[i5])
#                     # print("list_g", len(list_g), list_g)
#         if len(list_g)==len(list_f)*len(tuple_a):
#             list_h.append(tuple_a)
#             # print("list_h", len(list_h), list_h)
# print("list_h",len(list_h),list_h)

#
# import  random
# import itertools
# import math
# a= int (input("please input a="))
# list_a=[]
# list_b=[]
# list_c=[]
# list_d=[]
# list_e=[]
# fm_b=1
# for i in range(1,a+1):
#      list_a.append(i)
#      fm_b=fm_b*i
# print("list_a",list_a,fm_b/24)
# # list_a=(1,2,3,4,5,6,8,9,10,12)
# for i in itertools.combinations(list_a,3):
#     if sum(i)==15:
#         list_b.append(i)
# print("list_b",len(list_b),list_b)
# for za in itertools.combinations(list_b, 6):
#     # print("za",za)
#     # list_d.append(za)
#     # print("list_d",list_d)
#     # print("len(za)",len(za))
#     i3=()
#
#     i5=()
#     for i1 in za:
#         str = ''
#         k1 = 0
#         # print("i1", i1)
#         # for i2 in i1:
#         # print("i2", i2)
#         i3=i3+i1
#             # print("i3",i3)
#     i4=i3
#     i3=()
#     # print("i4", i4)
#     for i in i4:
#         if i4.count(i)==2:
#                 # print("i", i)
#             k1=k1+2
#                 # print("k1", k1)
#                 # zz=math.ceil(i4.index(i)%len(i2))
#                 # zz1=math.ceil(i4.rindex(i)%len(i2))
#                 # print("zz", zz)
#                 # print("zz1", zz1)
#             str=str+'Y'
#         # print("k11", k1)
#     k2=k1/len(i4)
#         # print("k2", k2)
#         # print("str",str)
#     if k2==2:
#         i5=za
#         list_e.append(i5)
#         # print("i5", i5)
#     # print("list_e", list_e)
#     # print("list_e",len(list_e))
#     list_f=[]
#
#     list_h=[]
#     tuple_a=()
#     # list_e=[((1, 2, 9, 12), (1, 3, 8, 12), (2, 4, 8, 10), (3, 5, 6, 10), (4, 5, 6, 9)), ((1, 2, 9, 12), (1, 5, 6, 12), (2, 4, 8, 10), (3, 4, 8, 9), (3, 5, 6, 10)), ((1, 2, 9, 12), (1, 5, 8, 10), (2, 4, 6, 12), (3, 4, 8, 9), (3, 5, 6, 10)), ((1, 2, 9, 12), (1, 6, 8, 9), (2, 4, 8, 10), (3, 4, 5, 12), (3, 5, 6, 10)), ((1, 3, 8, 12), (1, 4, 9, 10), (2, 4, 6, 12), (2, 5, 8, 9), (3, 5, 6, 10)), ((1, 3, 8, 12), (1, 5, 6, 12), (2, 3, 9, 10), (2, 4, 8, 10), (4, 5, 6, 9)), ((1, 3, 8, 12), (1, 5, 8, 10), (2, 3, 9, 10), (2, 4, 6, 12), (4, 5, 6, 9)), ((1, 5, 6, 12), (1, 5, 8, 10), (2, 3, 9, 10), (2, 4, 6, 12), (3, 4, 8, 9)), ((1, 5, 6, 12), (1, 6, 8, 9), (2, 3, 9, 10), (2, 4, 8, 10), (3, 4, 5, 12)), ((1, 5, 8, 10), (1, 6, 8, 9), (2, 3, 9, 10), (2, 4, 6, 12), (3, 4, 5, 12))]
#     #[((1, 3, 8, 12), (1, 4, 9, 10), (2, 4, 6, 12), (2, 5, 8, 9), (3, 5, 6, 10))]#[((2, 6, 8, 9), (3, 4, 6, 12), (3, 4, 8, 10), (3, 5, 8, 9), (4, 5, 6, 10))]#[((1, 2, 9, 10), (1, 3, 8, 10), (2, 5, 6, 9), (3, 4, 7, 8), (4, 5, 6, 7))]
#     for i7 in list_e:
#         tuple_a = i7
#         # print("i7",i7)
#         list_g = []
#
#         for i9 in i7:
#             indx=i7.index(i9)
#             list_f = []
#             for i10 in range(0,len(i7)):
#                 if indx!=i10:
#                     # print("i7[i10]",i7[i10])
#                     list_f.append(i7[i10])
#             # print("list_f",len(list_f),list_f)
#             # list_g = []
#             for i5 in range(0,len(list_f)) :
#                 # print("i4", i4)
#                 k=0
#                 for i8 in i9:
#                     # print("i8", i8)
#                     for i6 in list_f[i5]:
#                         if i8==i6:
#                             k+=1
#                 if k<2:
#                     list_g.append(list_f[i5])
#                     # print("list_g", len(list_g), list_g)
#         if len(list_g)==len(list_f)*len(tuple_a):
#             list_h.append(tuple_a)
#             # print("list_h", len(list_h), list_h)
# print("list_h",len(list_h),list_h)


#!/usr/bin/python3

# Function definition is here
from selenium import webdriver
# import selenium
# help(selenium)
webdriver.Firefox()