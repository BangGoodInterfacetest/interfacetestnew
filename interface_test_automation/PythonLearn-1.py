# 一、Python安装（以win系统为例）
# 1、到官网https://www.python.org/downloads/windows/下载，建议下载适合自己的Python3.X版本程序（同一个系统可以同时安装Python2和python3）
# 2、按照界面提示安装，很简单
# 3、配置环境变量：path 项中添加安装目录即可，注意与其他项用分号;分开（右键点击"计算机"，然后点击"属性"---然后点击"高级系统设置"---选择"系统变量"窗口下面的"Path",双击即可！然后在"Path"行，添加python安装路径即可(我的D:\Python33)，ps：记住，路径直接用分号"；"隔开！）
# 或者直接在运行cmd命令：path=%path%;D:\Python33(我的安装目录)
# 4、如果安装和配置成功，则在cmd命令窗体中输入 python即可显示python相关信息
# 5、 建议安装集成开发工具pycharm 或者 IntelliJ IDEA

# 二、基本语法；
#  1、编码：默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串，也可以指定不同编码如
# # -*- coding: cp-1252 -*-
#
# 2、标识符：
# 2.1第一个字符必须是字母表中字母或下划线 _
# 2.2标识符的其他的部分由字母、数字和下划线组成。
# 2.3标识符对大小写敏感
#
# 3python保留字（关键字）、
# import keyword
# print(keyword.kwlist)

# 4 注释
# 单行注释用# 号
# 多行注释可以用多个 # 号，还有 ''' 和 """   ctr+/

# 5、行与缩进
# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
# if True:
#     print ("Answer")
#     print ("True")
# else:
#     print ("Answer")
#     print ("False")
# prinp
# 建议：1、用四个空格表示层级缩进；2、用tab键进行层级缩进；3、严禁空格跟tab键混用

# 三、主要数据类型；
# 1、Python3 中有六个标准的数据类型：
#     Number（数字）：int、float、bool、complex（复数）
#     String（字符串）
#     List（列表）
#     Tuple（元组）
#     Set（集合）
#     Dictionary（字典）
#1.1.Number（数字）
# print("5 + 4=",5 + 4)  # 加法
# print("4.3 - 2=",4.3 - 2) # 减法
# print("3 * 7=",3 * 7)  # 乘法
# print("2 / 4=",2 / 4)  # 除法，得到一个浮点数
# print("2 // 4=",2 // 4) # 除法，得到一个整数
# print("17 % 3",17 % 3) # 取余
# print("2 ** 5",2 ** 5) # 乘方
# 1.2.String（字符串）
# 字符串用单引号 或双引号  括起来
# 字符串可以用+运算符连接在一起，用*运算符重复。
# Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# Python中的字符串不能改变

# str = 'zzj123'
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始的后的所有字符
# print(str * 2)  # 输出字符串两次
# print(str + "TEST")  # 连接字符串
# str[0]='T'
# print("字符串不能被改变",str[0])

# 1.3List（列表）
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表
# 除了列表值可以被修改，其他特性跟字符串类似，列表值没有任何限制，可以是任何数据类型
# list = ['abcd', 1, 2.34, 'zzj123', 70.2] #此变量命名不规范
# list2 = [123, '123zzj']
# print(list)  # 输出完整列表
# print(list[0])  # 输出列表第一个元素
# print(list[1:3])  # 从第二个开始输出到第三个元素
# print(list[2:])  # 输出从第三个元素开始的所有元素
# print(list2 * 2)  # 输出两次列表
# print(list + list2)  # 连接列表
# print(list)
# print(list2.append(list))
# list2.append(list)# append（obj）方法 添加到列表末尾的对象obj
# print(list2)
# list2.pop(0)#从列表中移除的元素对象，默认为-1
# print(list2)

# # # 1.4Tuple（元组）
# tup1 = ()    # 空元组
# tup2 = (20,) # 一个元素，需要在元素后添加逗号
# tup3 = ( 'abcd', 786 , 2.23, 'runoob', 70.2,786 ,[1,2,3] )
# # tup3[6]=456#tuple的元素不可改变
# tup3[6][1]=4#tuple的元素不可改变，但它可以包含可变的对象
# print(tup3)

# # 1.5 Set（集合）
# 一个无序不重复元素的序列
# 使用大括号 { } 或者 set() 函数创建集合
# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
# 常用最大的功能就是去重复
# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print(student)  # 输出集合，重复的元素被自动去掉
# # 成员测试
# if 'Rose' in student:
#     print('Rose 在集合中')
# else:
#     print('Rose 不在集合中')
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(a - b)  # a和b的差集
# print(a | b)  # a和b的并集
# print(a & b)  # a和b的交集
# print(a ^ b)  # a和b中不同时存在的元素
# # print(student[0])#因无序，所以不能用索引访问
# # for i in student: #遍历集合
# #     print(i)
# lists=[1,2,2,3] #去重复
# print(lists)
# newset=set(lists)
# print(newset)
# lists=list(newset)
# print(lists)
#
# 1.6 Dictionary（字典）
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
# 键(key)必须使用不可变类型
# dict1 ={} #创建空字典
# dict1['key1'] = "value1"    #给空字典创建项：键为key1，值为value1
# dict1[2] = "value2"  ##给空字典创建项：键为2，值为value2
# dict2 = {'name': 'zzj', 'code': 1, 'site': '20107'}
# print(dict1)
# print(dict1['key1'])  # 输出键为 'key1' 的值
# print(dict1[2])  # 输出键为 value2的值
# print(dict2)  # 输出完整的字典
# print(dict2.keys())  # 输出所有键
# print(dict2.values())  # 输出所有值
# print(dict2.items())#返回可遍历的(键, 值) 元组数组
# for key,values in  dict2.items():# 遍历字典列表
#     print(key,values)
# for key in  dict2.keys():# 按键遍历字典列表
#     print(key,values)
# del dict2['name']
# print(dict2)

# 1.7 数据类型转换
# int(x[, base])#将x转换为一个整数
# float(x)#将x转换到一个浮点数
# complex(real[, imag])#创建一个复数
# str(x)#将对象x转换为字符串
# repr(x)#将对象x转换为表达式字符串
# eval(str)#用来计算在字符串中的有效Python表达式, 并返回一个对象
# tuple(s)#将序列s转换为一个元组
# list(s)#将序列s转换为一个列表
# set(s)#转换为可变集合
# dict(d)#创建一个字典。d必须是一个序列(key, value)元组。
# frozenset(s)#转换为不可变集合
# chr(x)#将一个整数转换为一个字符
# ord(x)#将一个字符转换为它的整数值
# hex(x)#将一个整数转换为一个十六进制字符串
# oct(x)#将一个整数转换为一个八进制字符串

# 四、类、函数、方法、对象
# 类（class）：用来描述具有相同的属性和方法的对象的集合，可以简单用“模板概念”理解
# 函数（def）：用来实现单一、或者相关联功能的代码段
# 方法：类中定义的函数
# 对象：通过类定义的数据结构实例。
# class house:
#     # h,w=0,1
#
#     def __init__(self,height,width):
#         self.h=height
#         self.w=width
#
#     def wall_area(self):
#         area=self.h * self.w
#         print("area=",area)
#         return area
#
# def shadow_area(ware,angle):#创建函数
#     shadow_areas=ware*angle
#     return shadow_areas
# # # 1234r
# #
# hours1=house() #创建对象过程 ，过程实例化
# hours2=house(30,40)
# hours2.h=20
# hours2.w=30
# hours2.y=21
# hours2.z=22
#以下两种方式调用结果一样，但是实质不一样
# hours2.wall_area()#方法调用，优用方法
# house.wall_area(hours2)#函数调用
# hours2.wall_area()
# print(shadow_area(hours2.wall_area(),0.1))


# 五、常用模块函数方法；
# import unittest
# import mysql.connector
# 连接数据库
# 创建游标
# 游标执行sql
# 关闭游标
# 关闭连接
# import urllib.request
# r=requests.get(‘https://github.com/timeline.json’) #GET请求
# requests.post(“http://httpbin.org/post”) #POST请求
# requests.put(“http://httpbin.org/put”) #PUT请求
# requests.delete(“http://httpbin.org/delete”) #DELETE请求
# requests.head(“http://httpbin.org/get”) #HEAD请求
# requests.options(“http://httpbin.org/get”) #OPTIONS请求
# 响应
# r.status_code #响应状态码
# r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
# r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
# r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
# r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# #*特殊方法*#
# r.json() #Requests中内置的JSON解码器
# r.raise_for_status() #失败请求(非200响应)抛出异常

# import re 正则表达式
#

# 六： 异常调试；
# 1：语法错误 ：SyntaxError
#   检查是否核语句或者创建函数、类的行尾缺少：
# 检查引号  括号是否匹配
# 检查缩进是否规范
# 检查条件判断‘==’是否写成‘=’
# 2、异常： nameerro ：一般是变量超出范围
# typeerro：使用类型错误、传参个数、传错格式
# attrbuteerro：一般是不存在的属性或者方法
# indexerro：一般使用的索引超出范围
# keyerro：一般使用字典不存在的键值

# 推荐：入门：《项计算机科学家一样思考Python》、廖雪峰官方网站学习python；进阶：Python核心编程

#