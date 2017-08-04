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
		self.headers={'User-Agent':self.user_agent}
		self.stories=[]
		self.enable=False

	def getPage(self,pageIndex):
		try:
			url = 'https://www.qiushibaike.com/'
			#url = 'https://www.qiushibaike.com/8hr/page/'+str(pageIndex)
			request = urllib2.Request(url,headers = self.headers)
			response = urllib2.urlopen(request)
			pageCode = response.read().decode('utf-8')
			return pageCode

		except urllib2.URLError,e:
			if hasattr(e,"reason"):
				print "connect failed ",e.reason
				return None

	def getPageItems(self,pageIndex):
		content = self.getPage(pageIndex)
		if not content:
			print "Load Failed...."
			return None
		pattern = re.compile(
	'<div class="author.*?<a.*?<img.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
		items = re.findall(pattern,content)
		pageStories = []
		for item in items:
			#print item[0],item[1],item[2],item[3]
			#print "\n\n\n\n\n"
			#print 668
			pageStories.append([item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip()])
		return pageStories

	def loadPage(self):
		if self.enable == True:
			if len(self.stories) <2:
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex +=1

	def getOneStory(self,pageStories,page):
		for story in pageStories:
			input = raw_input()
			self.loadPage()
			if input =="Q":
				self.enable = False
				return
			print "Author:%s" % (story[0])
			print "Story:"
			print story[1]
			print "Comment: %s Like: %s" % (story[2],story[3])
			print "-------------------------------I'm  the boundary line---------------------------"

	def start(self):
		print u"Reading...Press enter for new one ,press Q to quit"
		self.enable = True
		self.loadPage()
		nowPage= 0
		while self.enable:
			if len(self.stories)>0:
				pageStories = self.stories[0]
				nowPage +=1
				del self.stories[0]
				self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()


