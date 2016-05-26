# doubanBook
主要用于抓取豆瓣图书，基于Scrapy框架

##特性:
加入UserAgentMiddleware和RandomProxyMiddleware实现每次抓取时自动切换请求头和ip防止被屏蔽

##环境说明：
Python 2.7 
Scrapy 1.10

##使用方法：
1. 安装Scrapy 
`sudo apt-get install scrapy`
2. 切换至本目录
`scrapy crawl doubanBook`

##一些配置选项：
1. 默认抓取的是豆瓣图书关于历史的图书[豆瓣图书历史类](https://book.douban.com/tag/%E5%8E%86%E5%8F%B2),想要抓取全站可以在`doubanBookSpider.py`中`start_urls =[]`中设置更多初始网址[豆瓣图书热门标签](https://book.douban.com/tag/?view=type&icn=index-sorttags-all)
2. 默认不开启代理IP中间件，如需开启可在`setting.py`中`DOWNLOADER_MIDDLEWARES`开启
3. 代理ip默认使用文件，可在`setting.py`中`PROXY_LIST`设置代理文件位置，支持以下格式
```javascript
 http://host1:port
 http://username:password@host2:port
 host3:port
```
