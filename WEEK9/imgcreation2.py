#fabs() return modulus of given number
#finding rgb from img (of dominant colors)

from PIL import Image
im=Image.open('WEEK9/test.jpg')
#convert to a rgb img
rgb_im=im.convert('RGB')
#now calc rgb values from rgb img
r,g,b=rgb_im.getpixel((150,1)) #arguments are x,y the locn where u want to find rgb
print(r,g,b)