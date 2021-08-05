# coding:utf-8

import os
import configparser
# python2 为Configparser  python3 为configparser
cur_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前路径
configpath = os.path.join(cur_path,"config.ini")    #获取配置文件名
conf = configparser.ConfigParser()  # 引用configparser.ConfigParser()
conf.read(configpath)   # 读取路径

# 读取配置文件中内容  email为key  smtp_server 为value
smtp_server = conf.get("email","smtp_server")   # 发件服务器
port = conf.get("email","port")     # 端口
sender = conf.get("email","sender") # 发件人
psw = conf.get("email","psw")   # 授权码
receiver = conf.get("email","receiver") # 收件人

iread_url = conf.get("iread_test","iread_url")


