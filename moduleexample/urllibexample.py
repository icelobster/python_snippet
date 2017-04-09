# -*- coding: utf-8 -*-
#urllib是用来从网络上下载内容的

import urllib
import urllib.request


url = "http://www.baidu.com"

request = urllib.request.Request(url)
request.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36}")
# request.add_header("User-Agent", "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9B176 MicroMessenger/4.3.2")
# request.add_header("User-Agent", "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10")
# request.add_header("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)")

request.add_header("Host", "www.baidu.com")
request.add_header("Connection", "keep-alive")
request.add_header("Upgrade-Insecure-Requests", "1")
request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
request.add_header("Referer", "http://www.baidu.com/index.html")
request.add_header("Accept-Language", "zh-CN,zh;q=0.8,en;q=0.6")
request.add_header("Cookie", "__cfduid=de46e9c5fad136c05f7532c70ab18c5841461983592; CNZZDATA950900=cnzz_eid%3D479566610-1461980791-http%253A%252F%252Ft66y.com%252F%26ntime%3D1486561077; 227c9_lastfid=27; 227c9_lastvisit=0%091491706496%09%2Fthread0806.php%3Ffid%3D27%26search%3D%26page%3D59")

#下面这句不能加，加了可能导致网站真的返回压缩形式
# request.add_header("Accept-Encoding", "gzip, deflate, sdch")

content = urllib.request.urlopen(request).read()

print(content.decode('utf-8'))
