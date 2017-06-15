import csv
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage
import numpy as np
import math
import os
from skimage import transform
from skimage import color,io


set_dir="/home/mahesh/VOC2010/ImageSets/Main"
cat_name="car"
dataset="train"
filename = os.path.join(set_dir, cat_name + "_" + dataset + ".txt")

_file=open(filename, 'rb')
datareader=csv.reader(_file, delimiter=' ', quotechar='|')
for row in datareader:
	print row[1]
	if row[1].find("-1")>-1:
		continue
	print "Copying "+row[0]
	image=mpimg.imread("/home/mahesh/VOC2010/JPEGImages/"+row[0]+".jpg")
	gray=color.rgb2gray(image)
	io.imsave("/home/mahesh/compression/category1/"+row[0]+".jpg",gray)
