__author__='CQC'
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import thread
import time


class QSBK:
	def __init__(self):
		self.pageIndex = 1
		self.user_agent ='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
		self.headers={'User-Agent':self.uaer_agent}
		self.stories=[]
		self.enable=False

	def getPage(self,pageIndex):
		try:
			url = 'https://www.qiushibaike.com/8hr/page/'+str(pageIndex)
			request = urllib2.Request(url,headers = self.headers)
			response = urllib2.urlopen(request)
			pageCode = response.read().decode('utf-8')
			return pageCode

		except urllib2.IRLError,r:
			if hasattr(e,"reason"):
				print u"链接失败",e.reason
				return None

	def getPageItems(self,pageIndex):
		pagecode= self.getPage(pageIndex)
		if not pageCode:
			print u"页面加载失败。。。"
			return None
		pattern = re.compile('<div class="author.*?<a.*?<img.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
		items=re.findall(pattern,pagecode)
		pageStories =[]
		for item in items:
			pageStories.append(item[0],item[1],item[2],item[3])
		return pageStories

	def loadPage(self):




