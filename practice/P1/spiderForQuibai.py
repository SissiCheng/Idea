# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
 
page = 1
url = 'https://www.qiushibaike.com/'
#url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    #print content
    pattern = re.compile(
	'<div class="author.*?<a.*?<img.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    #print items
    for item in items:
    	print item[0],item[1],item[2],item[3]
    	print "\n\n\n\n\n"
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason