# -*- encoding: utf-8 -*-
#---------------------------------------------
# 程序： 输入路径对本地文件夹里的文件进行排序
# 版本:  v1.0
# 作者： Nerostake
# 时间： 2014-05-29
# 功能： 1. 根据输入统计文件个数 标明哪些为文件夹，哪些为文件
#        2. 根据不同的要求对文件进行排序
#---------------------------------------------

import os,sys,os.path

class travel:
	
	def __init__(self, dir_path):
		self.dir_path=dir_path	
		self.data={}
		
	def bianli(self):
		