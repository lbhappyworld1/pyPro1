# -*- coding: utf-8 -*-
import scrapy
from ..items import TcItem
#from scrapy.linkextractors import LinkExtractor

class TencentpositionSpider(scrapy.Spider):
    """
    功能：爬取腾讯社招信息
    """
    # 爬虫名
    name = "tc"
    # 爬虫作用范围
    allowed_domains = ["tencent.com"]

    url = "http://hr.tencent.com/position.php?&start="
    offset = 0
    # 起始url
    start_urls = [url + str(offset)]

    def parse(self, response):
        items = []
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            item = TcItem()
            # 职位名称
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            ptype = each.xpath("./td[2]/text()").extract()
            if not len(ptype):
                item['positionType'] = ' '
            else:
                item['positionType'] = ptype[0]
            # 招聘人数
            item['peopleNum'] =  each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]
            items.append(item)
            yield item

        if self.offset < 20:
            self.offset += 10
            
        #self.log(items.len()) 
        for item in items:
            yield scrapy.Request('http://hr.tencent.com/'+item['positionlink'], callback=self.detail_parse)
        #filename = 'tc-%s.html' % self.offset
        #拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html
        #with open(filename, 'wb') as f:
             #python文件操作，不多说了；
             #f.write(response.body)
        #刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
        #self.log('保存文件: %s' % filename)

        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
    
    def detail_parse(self, response):
        self.log('this...22222222222')
        item = TcItem()
        item['positionname'] = response.body
        yield item
        filename = 'tc-%s.html' % self.offset
        #拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html
        with open(filename, 'wb') as f:
             #python文件操作，不多说了；
             f.write(response.body)
        #刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
        self.log('保存文件: %s' % filename)

            
