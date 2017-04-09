# -*- coding: utf-8 -*-
#requests是一个网络下载模块，和urllib类似

import requests

url = "http://www.baidu.com"

get = requests.get(url)

#指定编码
get.encoding = "utf-8"

#获得网页内容
content = get.text

print(content)
