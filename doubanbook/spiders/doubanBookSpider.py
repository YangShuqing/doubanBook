# -*- coding:utf-8 -*-
import scrapy
import re

from scrapy.http import Request
from scrapy.selector import Selector
from doubanbook.items import DoubanbookItem
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# douban books

class DoubanSpider(scrapy.Spider):
    name = "doubanBook"
    allowed_domains = ["douban.com"]
    start_urls = ["https://book.douban.com/tag/%E5%8E%86%E5%8F%B2"]
    url = 'https://book.douban.com'



    def parse(self, response):
        selector = Selector(response)
        books = selector.xpath('//div[@class="info"]/h2/a/@href').extract()
        for book in books:
            print book
            yield Request(book, callback=self.parse_item)

        nextPage = selector.xpath('//span[@class="next"]/a/@href').extract()
        if nextPage:
            print nextPage[0]
            yield Request(self.url+nextPage[0],callback=self.parse)

    def parse_item(self,response):
        item = DoubanbookItem()
        selector = Selector(response)
        name = selector.xpath('//div[@id="wrapper"]/h1/span/text()').extract()[0]
        star = selector.xpath('//strong[@class="ll rating_num "]/text()').extract()[0].strip()
        ratingPeople = selector.xpath('//a[@class="rating_people"]/span/text()').extract()[0]

        #print name + ratingPeople
        #auther = re.findall(u'<span class="pl"> 作者<\/span><a class="" href=".*">(.*)<\/a><\/span>',response)

        # for span in info:
        #     auther = selector.xpath('span/a/@href').extract()[0]
        #     #publish =
        #     print auther
        #print book_info
        bookImg = selector.xpath('//a[@class="nbg"]/@href').extract()[0]
        book_info = selector.xpath('//div[@id="info"]').extract()[0].encode('utf8')
        author = re.findall(r'<a class="" href=".*?">(.*?)</a>', book_info)[0].decode('utf8')
        press = re.search(r'出版社:</span>(.*?)<br', book_info).group(1).strip().decode('utf8')
        try:
            original = re.search(r'原作名:</span>(.*?)<br', book_info).group(1).strip().decode('utf8')
        except Exception, e:
            original = ''
        try:
            translator = re.findall(r'<a class="" href=".*?">(.*?)</a>', book_info)[1].decode('utf8')
        except Exception, e:
            translator = ''
        try:
            publishDate = re.search(r'出版年:</span>(.*?)<br', book_info).group(1).strip().decode('utf8')
        except Exception, e:
            publishDate = ''
        try:
            pages = re.search(r'页数:</span>(.*?)<br', book_info).group(1).decode('utf8')
        except Exception, e:
            pages = ''
        price = re.search(r'定价:</span>(.*?)<br', book_info).group(1).strip().decode('utf8')
        try:
            binding = re.search(r'装帧:</span>(.*?)<br', book_info).group(1).strip().decode('utf8')
        except Exception, e:
            binding = ''
        try:
            series = re.search(r'丛书:.*</span>.*<a href=".*">(.*?)</a>',book_info).group(1).strip().decode('utf8')
        except Exception,e:
            series = ''
        try:
            ISBN = re.search(r'ISBN:</span>(.*?)<br', book_info).group(1).decode('utf8')
        except Exception, e:
            ISBN = ''
        #print author + press + original +translater+ pages+ publishDate + series

        brief = selector.xpath('//div[@id="link-report"]/div/div[@class="intro"]').extract()
        if (not brief):
            brief= selector.xpath('//div[@id="link-report"]/span[@class="all hidden"]/div/div[@class="intro"]').extract()

        authorInfo = selector.xpath('//div[@class="related_info"]/div[@class="indent "]/div/div[@class="intro"]').extract()
        if (not authorInfo):
            authorInfo = selector.xpath('//div[@class="related_info"]/div/span[@class="all hidden "]/div').extract()
        #print authorInfo

        tags = selector.xpath('//div[@id="db-tags-section"]/div/span/a/text()').extract()
        #print tags

        item['name'] = name
        item['bookImg'] = bookImg
        item['press'] = press
        item['author'] = author
        item['star'] = star
        item['ratingPeople'] = ratingPeople
        item['original'] = original
        item['translator']= translator
        item['publishDate'] = publishDate
        item['pages'] = pages
        item['price'] = price
        item['binding'] = binding
        item['series'] = series
        item['ISBN'] = ISBN
        item['brief'] = brief
        item['authorInfo'] = authorInfo
        item['tags'] = tags

        yield item







        

