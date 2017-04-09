# -*- coding: utf-8 -*-
#re是正则表达式模块

import re

plain = "http://www.baidu.com?sid=3&pid=101"

#取出sid的值，group(0)表示整个匹配，group(1)表示第一个括号里的匹配
sid = re.match(".+sid=(\d+).+", plain).group(1)

print(sid)
