# -*- coding:utf-8 -*-
import datetime

#获取今天的日期
today = datetime.date.today()

#获取昨天的日期
yesterday = (today - datetime.timedelta(days=1))

#日期装换成字符串
print(today.strftime("%Y-%m-%d"))
