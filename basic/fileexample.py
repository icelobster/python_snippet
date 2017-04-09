# -*- coding: utf-8 -*-
#文件操作

#这种写法，不需要自己关闭文件和处理异常
with open("/tmp/a.html", "r") as f:
    content = f.read()
    print(content)

#写文件
with open("/tmp/a.html", "w") as f:
    f.write("a lot content")
