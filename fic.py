import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage
import numpy as np
import math


class CompressorEnv():
	def __init__(self):
		self.observation = mpimg.imread('lena4.bmp')
		self.reward=0
		self.done=False
		self.info="?"
		self.state=0
	

	def reset(self):
		return self.observation

	def step(self,action):

		if self.state%2==0:
			self.reward=0.0
		else:
			self.reward=-1.0	
		self.state=self.state+1
		if self.state==20:
			self.done=True
			self.state=0
		else:
			self.done=False
		return self.observation,self.reward,self.done,self.info 

