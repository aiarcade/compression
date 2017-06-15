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


		self.imgInepisode=60

		self.epsIndex=0

		self.maxEps=10
		self.currEps=0		
		
		for file in os.listdir("category1"):
    			if file.endswith(""):
        			self.pdataList.append(os.path.join("category1", file))
		
		for file in os.listdir("category2"):
    			if file.endswith(""):

        			self.ndataList.append(os.path.join("category2", file))	
		self.pN=len(self.pdataList)
		self.nN=len(self.ndataList)

	def reset(self):
		#self.dataIndex=0
		self.readImg(0)
		return self.observation

	def readImg(self,label):
		if label==-1:
			image=transform.resize(mpimg.imread(self.pdataList[self.pdIndex]),(128,128))
			self.pdIndex=self.pdIndex+1
			if self.pdIndex<self.pN:
				self.pdIndex=0
		else:	
			image=transform.resize(mpimg.imread(self.ndataList[self.ndIndex]),(128,128))
			self.ndIndex=self.ndIndex+1
			if self.ndIndex<self.nN:
				self.ndIndex=0
		return image
	
	def step(self,action):
		#print "action is",action,self.lastLabel
		if action==2 and self.lastLabel==-1:
			reward=-1.0
		elif action==3 and self.lastLabel!=-1:
			reward=-1.0		
		else:
			reward=0.0
		
		self.lastLabel=random.choice([-1,1])
		self.observation=self.readImg(self.lastLabel)
		
		terminate=False
		if self.epsIndex==self.imgInepisode:
			self.epsIndex=0
			self.currEps=self.currEps+1
			self.done=True
		else:
			self.epsIndex=self.epsIndex+1
			self.done=False
		if self.currEps==self.maxEps:
			terminate=True
		
				
		return self.observation,reward,self.done,self.info,terminate
			
		

