# -*- coding: utf-8 -*-
import json

class TcPipeline(object):
    """ 
    功能：保存item数据 
    """
    def __init__(self):
        self.filename = open("tencent.json", "wb")

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
        #self.log('json-pip: %s' % text)
        self.filename.write(text.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.filename.close()
