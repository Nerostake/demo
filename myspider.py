# -*- coding utf-8 -*-
#--------------------------------------------
# 程序：百度贴吧爬虫
# 版本：V1.0
# 作者：Enzo
# 更新时间：2014-05-28
# 功能：将百度贴吧的文章下载并保存的本地文件
#--------------------------------------------

import re, string
from request import urllib

class baidu_spider:
	
	#申明属性
	def __init__(self, url):
		self.myurl=url+'?see_lz=1'
		data=[]
		
	#爬虫函数
	def baidu_tieba(self):
		#打开初始页面
		mypage=request.urlopen(self.myurl).read().decode('GBK')
		#找到标题并输出
		title=findtitle(mypage)
		print('小说名称为：{0}'.format(title))
		#找到页数并输出
		endpage=pagecounter(mypage)
		print('该小说一共有{0:2d}页'.format(endpage))
		#将文章保存的到本地文件
		self.save_data(self.myurl,title,endpage)
		
	def findtitle(self, mypage):
		mymatch=re.search(r'<h1.?*>(.*?)</h1>',mypage,re.S)
		if mymatch:
			title=mymatch.group(1)
		else：			
			title='无法找到标题'
		return title
		
	def pagecounter(self,mypage):
		mymatch=re.search(r'class="red">(\d+?)</span>',mypage,re.S)
		if mymatch:
			endpage=mymatch.group(1)
		else:
			endpage=0
			print('无法计算有多少页')
		return endpage
		
	def save_data(self, url, title, endpage):
		self.getdata(url, endpage)
		f=open(title+'.txt',mode='w+')
		f.write(self.data)
		f.close()
		print('文件已下载到本地')
		print('按任意键退出')
		raw_input()
		
	def getdata(self, url, endpage):
		url=url+'&pn='
		for i in range(1,endpage+1):
			print('报告：爬虫{0:2d}号正在工作中.....'.format(i))
			mypage=request.urlopen(url+str(i)).read().decode('GBK')
			self.deal_data(mypage)
			
	def deal_data(self, mypage)；
		myitems=re.findall(r'class="d_post_content j_d_post_content ">(.*?)</div>',mypage,re.S)
		for item in myitems:
			self.da\ta.append(item+'\n')
	
print('''
#--------------------------------------------
# 程序：百度贴吧爬虫
# 版本：V1.0
# 作者：Enzo
# 更新时间：2014-05-28
# 功能：将百度贴吧的文章下载并保存的本地文件
#--------------------------------------------
''')
 
 bdurl='http://tieba.baidu.com/p/2945353489'
 myspider=baidu_spider(bdurl)
 myspider.baidu_tieba()
 
 
			
		
		
		
		