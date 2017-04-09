# -*- coding: utf-8 -*-
#解析json

import json

class Topic:
    def __init__(self, title="", url="", dateStr=""):
        self.title = title
        self.url = url
        self.dateStr = dateStr

    def fromDict(self, d):
        self.title = d["title"]
        self.url = d["url"]
        self.dateStr = d["date"]

        return self

    def toDict(self):
        return {"title": self.title,
                "url": self.url,
                "date": self.dateStr}


class TopicJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Topic):
            # 对于dict对象，json可以直接转换，所以先把topic转换成dict对象
            return o.toDict()
        else:
            return json.JSONEncoder.default(self, o)

oriJsonStr ='''
[
    {
        "title": "apple",
        "date" : "2017-04-08",
        "url"  : "http://www.apple.com"
    },
    {
        "title": "orange",
        "date" : "2017-04-09",
        "url"  : "http://www.orange.com"
    }
]
'''

# 这个是把字符串转换成json格式的对象，里面其实是list套着dict，获得dict后就可以根据一个一个的键值把内容取出来了
l = json.loads(oriJsonStr)
for d in l:
    topic = Topic()
    topic.title = d["title"]
    topic.dateStr = d["date"]
    topic.url = d["url"]

# 把对象转换成json格式的字符串
l = [Topic("apple", "http://www.apple.com", "2017-04-08"),
     Topic("orange", "http://www.orange.com", "2017-04-09")]

# cls表示用什么编码器，因为Topic是自定义的对象，所以也自定义了一个编码器
# ensure_ascii表示是否强制保持ascii编码，如果中文的话会有问题，所以设置成false
# sort_keys和indent是格式化用的
print(json.dumps(l, cls=TopicJsonEncoder, ensure_ascii=False, sort_keys=True, indent=4))
