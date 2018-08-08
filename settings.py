# -*- coding: utf-8 -*-

# Scrapy settings for db project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'db'

SPIDER_MODULES = ['db.spiders']
NEWSPIDER_MODULE = 'db.spiders'


#LOG_FILE = "douban.log"
#LOG_LEVEL = "DEBUG"

#   设置返回的信息权限 看文件解释

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36;"


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 2.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'db.middlewares.DbSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#   'db.middlewares.RandomUserAgent': 100,#  后面random**可以随机取名子 但是这两个都是要自己去设置的
#    'db.middlewares.RandomProxy':200,      #但是方法的名字也要时后面这个
#}

#   百度获得各种user-agent
#USER_AGENTS=[
#'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
##'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
#'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
#'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1'
#]

#   购买获得代理
#PROXIES = [
    #{ "ip_prot":"121.43.170.207：3128","user_passwd":"aa:qq"},
    # 外面是列表里面是字典 可以有多个代理
    #前面组成是ip：端口
    #后面是账户：密码
    #格式就这样 账户跟密码可以是空的

    #   也可以是下面这样子
#    '58.87.68.189:1080',
#    '58.87.98.112:1080',
#    '125.115.183.169:3128',
#]



# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'db.pipelines.DbPipeline': 300,
}
# MONGODB 主机名
MONGODB_HOST = "localhost"

# MONGODB 端口号
MONGODB_PORT = 27017

# 数据库名称
MONGODB_DBNAME = "Douban"

# 存放数据的表名称
MONGODB_SHEETNAME = "doubanmovies"

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
