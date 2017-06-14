import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage
import numpy as np
import math
import os
from skimage import transform

import random

class CompressorEnv():
	def __init__(self):
		self.observation = mpimg.imread('lena4.bmp')
		self.reward=0.0
		self.done=False
		self.info="?"
		self.state=0

		self.pdataList=[]
		self.pdIndex=0
		self.pN=0
		self.ndataList=[]
		self.ndIndex=0
		self.nN=0
		
		self.lastLabel=-1


		self.imgInpisode=10

		self.epsIndex=0		
		
		for file in os.listdir("data"):
    			if file.endswith(""):
        			self.pdataList.append(os.path.join("data", file))
		
		for file in os.listdir("data2"):
    			if file.endswith(""):
        			self.ndataList.append(os.path.join("data2", file))	
		self.pN=len(self.pdataList)
		self.nN=len(self.ndataList)

	def reset(self):
		#self.dataIndex=0
		self.readImg(0)
		return self.observation

	def readImg(self,label):
		if label=-1:
			image=transform.resize(mpimg.imread(self.pdataList[self.pdIndex]),(128,128))
			self.pdIndex=self.pdIndex+1
			if self.pdIndex<self.pN:
				self.pdIndex=0
		else:	
			image=transform.resize(mpimg.imread(self.ndataList[self.ndIndex]),(128,128))
			self.ndIndex=self.ndIndex+1
			if self.ndIndex<self.nN:
				self.ndIndex=0
	
	def step(self,action):
		if action==2 and self.lastLabel==-1:
			reward=-1
		elif action==3 and self.lastLabel!=-1:
			reward=-1		
		else:
			reward=0
		self.observation=readImg(random.choice([-1,1])
		
		if self.epsIndex==self.imgInpisode:
			self.epsIndex=0
			self.done=True
		else:
			self.epsIndex=self.epsIndex+1
			self.done=False
		return self.observation,self.reward,self.done,self.info,False

