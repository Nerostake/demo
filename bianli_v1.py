# -*- encoding: utf-8 -*-
#---------------------------------------------
# 程序： 输入路径对本地文件夹里的文件进行排序
# 版本:  v1.0
# 作者： Nerostake
# 时间： 2014-05-29
# 功能： 1. 根据输入统计文件个数 标明哪些为文件夹，哪些为文件
#        2. 根据不同的要求对文件进行排序
#---------------------------------------------

import os,sys,os.path,ctypes

STD_OUTPUT_HANDLE=-11
FOREGROUND_BLACK=0x0
FOREGROUND_RED=0x04
FOREGROUND_GREEN=0x02
FOREGROUND_BLUE=0x01

if os.name != 'nt':
'''检验系统是否为windows'''
	print('This is for windows...')
	sys.exit()

class color:
	'''不同颜色高亮输出'''
	
	std_out_handle=ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	
	def set_color(self, color, handle=std_out_handle):
		'''设置颜色'''
		bool=ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
		return bool
		
	def reset_color(self):
		'''颜色复位'''
		self.set_color(FOREGROUND_GREEN|FOREGROUND_RED|FOREGROUND_BLUE)
		
	def print_blue(self, text):
		self.set_color(FOREGROUND_BLUE)
		print(text)
		self.reset_color()
		
	def print_green(self, text):
		self.set_color(FOREGROUND_GREEN)
		print(text)
		self.reset_color()


		
class travel:
	'''遍历本地文件夹'''
	
	def __init__(self, dir_path):
		self.dir_path=dir_path	
		self.data={x:[0] for x in listdir(dir_path)}
		
	def bianli(self, path):
		'''遍历路径下所有子文件/文件夹,返回总大小'''
		dir_size=0
		for root, dirs, files in os.walk(path):
			dir_size+=sum(os.path.getsize(os.path.join(root, name)) for name in files)
		return dir_size
	
	
	def listitem(self):
		'''列举出路径里的所有文件/文件夹名称，分别高亮'''
		print('There are {0:4d} items in this path.'.format(len(self.data)))
		print('These items are: (green-dir|blue-nondir)')
		clr=color()
		num_dir=0
		for x in listdir(self.dir_path):
			if os.path.isdir(os.path.join(self.dir_path, x)):
				self.data[x][0]=1
				num_dir+=1
				clr.print_green(x)
			else:
				clr.print_blue(x)
		print('Including {0:4d} directories and {1:4d} non-directory files'.format(num_dir, len(self.data)-num_dir))
		
	
	def get_size(self):
		'''获得路径下每一个文件/文件夹的大小'''
		for x in listdir(self.dir_path):
			if self.data[x][0]=0:
				self.data[x].append(os.path.getsize(os.path.join(self.dir_path, x)))
			else:
				path=os.path.join(self.path, x)
				self.data[x].append(self.bianli(path))
				
	def sort_size(self):
		'''按大小排序'''
		print('These items are sorted by size as:')
		
	
	def sort_init(self):
	
	
	
	
		