
import scipy.misc
from PIL import Image
import numpy as np
import random
  
img=scipy.misc.imread('WEEK9/test.jpg')
count_pun=0 #dots in punjab region
count_in=0
count=0
while(count<=10000):
    x=random.randint(0,100)
    y=random.randint(0,200) #in python images x is vertical y is horizontol
    z=0
    if(img[x][y][z]==[255,127,0]):
        count_in=count_in+1
        count=count+1
    else:
        if(img[x][y[z]]==[0,0,255]):
            count_pun=count_pun+1
            count=count+1

areapun=(count_pun/count_in)*3287263
print(areapun)
