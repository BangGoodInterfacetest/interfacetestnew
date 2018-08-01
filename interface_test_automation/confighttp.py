#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'zuozhijun'

import urllib.request
import http.cookiejar
import urllib.parse
import json
import configparser

# 配置类
class ConfigHttp:
    '''配置要测试接口服务器的ip、端口、域名等信息，封装http请求方法，http头设置'''

    def __init__(self, ini_file):
        config = configparser.ConfigParser()

        # 从配置文件中读取接口服务器IP、域名，端口
        config.read(ini_file)
        self.host = config['HTTP']['host']
        self.port = config['HTTP']['port']
        self.headers = {}  # http 头

        #install cookie
        #cj = http.cookiejar.CookieJar()
        #opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        #urllib.request.install_opener(opener)

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return  self.port

    # 设置http头
    def set_header(self, headers):
        self.headers = headers

    # 封装GET请求方法
    def get(self, url, params):
        # params = urllib.parse.urlencode(eval(params))  # 将参数转为url编码字符串
        url = 'http://' + self.host + ':' + str(self.port)  + url + params
        #print("url",url)
        request = urllib.request.Request(url, headers=self.headers)
        try:
            response = urllib.request.urlopen(request)
            #response = opener.open(request)
            #print("responsecookie",cj)

            response = response.read()#.decode('utf-8')  ## decode函数对获取的字节数据进行解码
            #print("responsecookieGET:", response)
            json_response = response  # 将返回数据转为json格式的数据
            return (json_response,"请求正常")
        except Exception as e:
            print('%s' % e)
            E_response=({},e)
            return E_response

    # 封装POST请求方法
    def post(self, url, data):
        #post提交数据有四种格式json(application/json：{"input1":"xxx","input2":"ooo"}),原生 form 表单格式（application/x-www-form-urlencoded：input1=xxx&input2=ooo），表单格式（multipart/form-data），xml格式（text/xml:这种直接传的xml格式）
        # data = json.dumps(eval(data)) #如果提交数据格式为json格式：{}
        # data= urllib.parse.urlencode(eval(data))#如果提交数据格式为原生form格式
        print("data",data)
        data = data.encode('utf-8')
        url = 'http://' + self.host + ':' + str(self.port)  + url
        try:
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request, data)
            #response = opener.open(request)
            response = response.read().decode('utf-8')
            # print("responsetype1:", type(response))
            # print("responsecookie:",response)
            json_response = (response,"请求正常")
            return json_response
        except Exception as e:
            print('%s' % e)
            E_response = ({}, e)
            return E_response

    # 封装HTTP xxx请求方法
    # 自由扩展
    #def set_Emsg(self):
        #self.erro_msg = erro_msg
        #print(erro_msg&"aa")
        #return self.erro_msg