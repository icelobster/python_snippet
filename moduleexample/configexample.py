# -*- coding: utf-8 -*-
#配置文件使用

import configparser

config = configparser.ConfigParser()

#读取配置文件
config.read("config.ini")

encoding = config["DEFAULT"]["encoding"]

print(encoding)

