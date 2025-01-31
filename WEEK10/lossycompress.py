#take a gray scale img 
# pixels are from 0 10 255.. 2^8-1.. we will map the values of 0-255 to 0-8. 
# earlier it was 8 bits now it will be 3 bits
from PIL import Image
import numpy as np


##replace imgopen by img.. img by pixelmap and new by newpixelmap
imgopen=Image.open("WEEK8\enh.jpg")
img=imgopen.load()   #pixel map
arr=np.asanyarray(img)   #img as matrix
#print(arr)

newimg=Image.new(imgopen.mode,imgopen.size) #a new img of same type(gray scale) and same size a blank img
new=newimg.load()  #new pixmap
'''
2^8-->2^3 means 2^5=32 number  to be mapped to 1 number
0-31=0
32-63=1
64-95=2
128-159=4
160-191=5
192-223=6
224-255=7
'''
for i in range(imgopen.size[0]):  #remeber size mode these can be used with image only
    for j in range(imgopen.size[1]):
        if img[i,j]>=0 and img[i,j]<32:  #these are on pixel maps
            new[i,j]=0
        elif img[i,j]>=32 and img[i,j]<64:
            new[i,j]=1
        elif img[i,j]>=64 and img[i,j]<96:
            new[i,j]=2
        elif img[i,j]>=96 and img[i,j]<128:
            new[i,j]=3
        elif img[i,j]>=128 and img[i,j]<160:
            new[i,j]=4
        elif img[i,j]>=160 and img[i,j]<192:
            new[i,j]=5
        elif img[i,j]>=192 and img[i,j]<224:
            new[i,j]=6
        elif img[i,j]>=224 and img[i,j]<255:
            new[i,j]=7

newimg.save('WEEK10/compressed.jpg')
j=np.asanyarray(Image.open('WEEK10/compressed.jpg'))
print(j)