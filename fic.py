import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage
import numpy as np
import math
import os
from skimage import transform

class CompressorEnv():
	def __init__(self):
		self.observation = mpimg.imread('lena4.bmp')
		self.reward=0.0
		self.done=False
		self.info="?"
		self.state=0
		self.dataList=[]
		self.dataIndex=0
		self.eps=0
		for file in os.listdir("data"):
    			if file.endswith(".pgm"):
        			self.dataList.append(os.path.join("data", file))
	

	def reset(self):
		return self.observation

	def readImg(self,index):
		try:
			self.observation = transform.resize(mpimg.imread(self.dataList[index]),(128,128))
		except:
			print "Unable to open",self.dataList[index]

	def step(self,action):
		
		if self.dataIndex<len(self.dataList):
			self.readImg(self.dataIndex)			
			
			self.dataIndex=self.dataIndex+1
		else:
			self.eps=0			 
			return self.observation,self.reward,True,self.info,True
		if self.eps==50:
			self.done=True
			self.eps=0
		else:
			self.eps=self.eps+1 	
			
		print "action is ",action		
		if action==2:
			self.reward=-1.0
		else:
			self.reward=0.0
							
		return self.observation,self.reward,self.done,self.info,False

