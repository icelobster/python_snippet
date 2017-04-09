# -*- coding: utf-8 -*-
# beautifulsoap是一个html和xml解析模块
# 依赖解析模块html5lib
# 依赖模块：cssselect，lxml
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import bs4
import requests
import urllib

#用requests模块来下载内容来解析
def downloadByRequests():
    get = requests.get("http://www.baidu.com")
    get.encoding = 'utf-8'
    content = get.text
    soap = bs4.BeautifulSoup(content, "html5lib")

    #这个是beautifulsoap对html格式化和标签修复
    print(soap.prettify())

#用urllib木块来下载内容来解析
def downloadByUrllib():
    rawContent = urllib.request.urlopen("http://www.baidu.com").read()

    #这种方式，beautifulsoap会自动合适的编码方式来解码网页，比如gbk或utf-8
    soap = bs4.BeautifulSoup(rawContent, "html5lib")

    print(soap.prettify())

rawContent = urllib.request.urlopen("http://www.baidu.com").read()
soap = bs4.BeautifulSoup(rawContent, "html5lib")

#find可以根据标签名，和里面的一些属性来找标签，find是找到第一个，find_all就是找出所有符合条件的标签
aTag = soap.find(name="a", id="setf")

#这是获取标签里的属性信息
print(aTag["href"])

#属性比较多的时候，也可以这么写，class_其实就是class，因为关键字不能冲突所以这么写
aTag = soap.find(name="a", attrs={"id": "setf", "target": "_blank"}, class_="f10")

#获取标签中间的内容
aTag.string

#网页在文件里的话，可以这么写
soap = bs4.BeautifulSoup(open("/tmp/a.html"), "html5lib")
