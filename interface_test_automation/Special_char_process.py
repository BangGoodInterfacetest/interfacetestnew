__author__ = 'zuozhijun'
#特殊字符自定义转换
def SpCharReplace(char):
        #char=char
    temp=str(char)
    for i in  temp:
        if '<'==i:
            char= char.replace('<','《')
        if '>' == i:
            char = char.replace('>', '》')
        if '\'' == i:
            char = char.replace('\'', '')#处理单引号
        if '\\' == i:
            char = char.replace('\\', '')#处理反斜杠\
        if '\"' == i:
            char = char.replace('\"', '`')  # 处理双引号"
        if '&' == i:
            char = char.replace('&', '-')  # 处理&号"
        if '|' == i:
            char = char.replace('|', '')
        if '@' == i:
            char = char.replace('@', '.')
        if '%' == i:
            char = char.replace('%', "`")  # 处理单引号
        if '*' == i:
            char = char.replace('*', '`')  # 处理星号
        if '("' == i:
            char = char.replace('("', '`')  # 处理括号号"
        if ')"' == i:
            char = char.replace(')"', '`')
        if '-' == i:
            char = char.replace('-', '`')  # 处理-号"
        if '{' == i:
            char = char.replace('{', '')
        if '}' == i:
            char = char.replace('}', '')
        if '[' == i:
            char = char.replace('[', '')
        if '[' == i:
            char = char.replace(']', '')
        #在后面扩展其他特殊字符
    return char
# import json
# import urllib.parse
# def char_to_json(char):
#     temp = str(char)
#     for i in temp:
#         if '=' == i:
#             char = char.replace('=', '":"')
#         if '&' == i:
#             char = char.replace('&', '","')
#         if '&' == i:
#             char = char.replace('+', ' ')
#     new_char='{'+'"'+char+'"'+'}'
#     print("new_char1",new_char)
#     return new_char
#
# #import HTMLParser
# # from html.parser import HTMLParser
# # html_cont ='&#22995;&#21517;&#65306;'#''pageIndex=1&rowCount=0&orderBy=OperateBarCodeLogId+desc&pageSize=10&search=%60%60op%7CBarCode%60UserName%60OperatedDate%7CA000004746774797979%60%E9%BB%84%E6%98%A5%E5%AE%B9%602018-2-23+0%3A00%7Ceq%60eq%60GreatEq'
# # #html_parser = HTMLParser().unescape()#HTMLParser.HTMLParser()
# # new_cont = HTMLParser().unescape(html_cont)
# # print(new_cont) #new_cont = " asdfg>123<"
#
# # rawurl = "pageIndex=1&rowCount=0&orderBy=OperateBarCodeLogId+desc&pageSize=10&search=%60%60op%7CBarCode%60UserName%60OperatedDate%7CA000004746774797979%60%E9%BB%84%E6%98%A5%E5%AE%B9%602018-2-23+0%3A00%7Ceq%60eq%60GreatEq"
# # url = urllib.parse.unquote(rawurl)
#
# char='pageSize=10&orderBy=OperateBarCodeLogId+desc&rowCount=1&search=%60%60%60%60%60op%60op%7CBarCode%60UserName%60LogType%60OperateType%60SubLogType%60OperatedDate%60ProcessCenterId%7CA000004746774797979%60%E9%BB%84%E6%98%A5%E5%AE%B9%6026%602%601400002%602018-2-23+0%3A00%60722%7Ceq%60eq%60eq%60eq%60eq%60GreatEq%60eq&pageIndex=1'
# url = urllib.parse.unquote(char)
# #data= urllib.parse.urlencode(eval(char))
# print("url",url)
# b=char_to_json(url)
# data1= urllib.parse.urlencode(eval(b))
# print("data1",data1)
# data2= urllib.parse.urlencode(eval(url))
# print("data2",data2)

