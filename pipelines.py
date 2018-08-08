# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  pymongo
from scrapy.conf import settings
import urllib
import os

class DbPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]

        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.sheet = mydb[sheetname]


    def process_item(self, item, spider):
        data = dict(item)
        self.sheet.insert(data)
        a = item['picture']
        bytes = urllib.request.urlopen(a)
        if not os.path.exists("图片"):
           os.makedirs("图片")
        title = item['title'] + '.jpg'
        fp = open("图片"+'/'+title, "wb")
        fp.write(bytes.read())
        fp.flush()
        fp.close()
        return item