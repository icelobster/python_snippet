# -*- coding: utf-8 -*-
#os.path模块，和文件目录操作相关

import os.path

filepath = "/User/aaa/Download/a.html"

# 检查文件是否存在
os.path.exists("/tmp/a.html")

# 路径拼接，会自动选择当前系统的方式来拼接，正反斜线
os.path.join("/tmp", "a.html")
