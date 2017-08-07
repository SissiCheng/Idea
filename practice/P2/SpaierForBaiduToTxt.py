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
 
    def __init__(self,baseUrl,seeLZ,floorTag):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = Tool()
        self.file = None
        self.floor = 1
        self.defaultTitle = u"百度贴吧"
        self.floorTag = floorTag
 
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print "Linking Baidu Failed ,Failed reason",e.reason
                return None
 
    #获取帖子标题
    def getTitle(self,page):

        #pattern = re.compile('class="core_title_txt.*style=.*?>(.*?)</',re.S)
        pattern = re.compile(' class="core_title_txt.*?>(.*?)<',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None
 
    def getPageNum(self,page):

       # pattern = re.compile('li class="l_reply_num".*?></span.*?<span class=.*?>(.*?)</',re.S)
        pattern = re.compile('li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None
 
    def getContent(self,page):

        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            content = "\n"+self.tool.replace(item)+"\n"
            contents.append(content.encode('utf-8'))
        return contents
 
    def setFileTitle(self,title):
        #如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt","w+")
        else:
            self.file = open(self.defaultTitle + ".txt","w+")
 
    def writeData(self,contents):
        #向文件写入每一楼的信息
        for item in contents:
            if self.floorTag == '1':
                #楼之间的分隔符
                floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1
 
    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print "URLFail,try again "
            return
        try:
            print "Page name " + str(pageNum) + "page"
            for i in range(1,int(pageNum)+1):
                print "Writing Page" + str(i) + "data "
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        #出现写入异常
        except IOError,e:
            print "Writing Error，reason" + e.message
        finally:
            print "Writing ending"
 
 
 
print u"please enter the number"
baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ = raw_input("if you want to see louzhang only ? \n")
floorTag = raw_input("if you want the floor info?\n")
bdtb = BDTB(baseURL,seeLZ,floorTag)
bdtb.start()