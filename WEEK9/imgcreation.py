#img consists of matrix of pixels.. pixel is basically a color..colr is defined by 3 attributes.. amt of red,blue,green
#RGB of white(255,255,255) black(0,0,0)
import numpy as np
from PIL import Image
#creating img of particular rgb. take width n heigh
width=200
height=100
array1=np.zeros([height,width,3],dtype=np.uint8)   #np.xeroes makes array of given dimension 3 is for 3 byte values of rgb of pixel
#other parameter is the datatype  here its unsigned int 

# the img thus formed will be black coz zero rgb values so assign new rgb to our im
array1[:,:100]=[255,128,0] #orange in right
array1[:,100:]=[0,0,255]  #blue in left
img=Image.fromarray(array1,'RGB')  #form img from array
img.save('WEEK9/test.jpg')
