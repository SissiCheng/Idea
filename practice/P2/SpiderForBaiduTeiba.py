# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class Tool:
	removeImg = re.compile('<img.*?>| {7}|')
	removeAddr = re.compile('<a.*?>|</a>')
	replaceLine = re.compile('<tr>|<div>|</div>|</p>')
	replaceTD= re.compile('<td>')
	replacePara = re.compile('<p.*?>')
	replaceBR = re.compile('<br><br>|<br>')
	removeExtraTag = re.compile('<.*?>')
	def replace(self,x):
		x = re.sub(self.removeImg,"",x)
		x = re.sub(self.removeAddr,"",x)
		x = re.sub(self.replaceLine,"\n",x)
		x = re.sub(self.replaceTD,"\t",x)
		x = re.sub(self.replacePara,"\n    ",x)
		x = re.sub(self.replaceBR,"\n",x)
		x = re.sub(self.removeExtraTag,"",x)
		return x.strip()

class BDTB:
	def __init__(self,baseUrl,seeLZ):
		self.baseURL = baseUrl
		self.seeLZ = '?see_lz='+str(seeLZ)
		print 1

	def getPage(self,pageNum):
		try:
			url = self.baseURL +self.seeLZ +'&pn'+str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			print 'get page'
			print response
			return response

		except urllib2.URLError,e:
			if hasatte(e,"reason"):
				print u"Link Baidu Failed,reason",e.reason
				print 3
				return None

	def getTitle(self):
		print 5
		page = self.getPage(1)
		print page
		pattern = re.compile('class="core_title_txt.*style=.*?>(.*?)</',re.S)
		result = re.search(pattern,page)
		print 4
		if result:
			print result.group(1)
			return result.group(1).strip()
			print 5
		else:
			return None

	def getPageNum(self):
		page = self.getPage(1)
		pattern = re.compile('li class="l_reply_num".*?></span.*?<span class=.*?>(.*?)</',re.S)
		result = re.search(pattern,page)
		print 6
		if result:
			print result.group(1)
			return result.group(1).strip()
			print 7
		else:
			return None

	def getContent(self,page):
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		print 10
		items = re.findall(pattern,page)
		print 9
		#for item in items:
		#	print item
		print self.tool.replace(items[1])



baseURL = 'https://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
comtent = bdtb.getPage(1)
#bdtb.getContent(page=comtent)
