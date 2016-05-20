# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from  scrapy import Item,Field


class DoubanbookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #bookNum = Field()
    name = Field()
    bookImg = Field()
    press = Field() #出版社
    star = Field()
    ratingPeople = Field()
    tags = Field()
    author = Field()
    translator = Field()
    original = Field() #原作名
    publishDate = Field()
    pages = Field()
    price = Field()
    binding = Field() #装帧
    series = Field() #系列
    ISBN = Field()

    brief = Field()
    authorInfo = Field()
    directory = Field()