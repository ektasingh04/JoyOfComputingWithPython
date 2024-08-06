#flippin the img

from PIL import Image

#open img
img=Image.open('img.jpg')
#cmp generally process img in terms of matrix format
#transposing the matrix--- mirroring of image
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT) #inbuilt fn

#convert back to human understable form
transposed_img.save('new.jpg')  #inbuilt fn save

print("done flipping")


#enhancement of img---contrast limited adaptive histogram equalisation or clahe-- cv2 package

import cv2

#read img
img=cv2.imread('img.jpg')
#prep for clahe
clahe=cv2.createCLAHE()

#works best in b&w img so convert to bw or gre scale
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#apply enhancemet
enh_img=clahe.apply(gray_img)

#save to file
cv2.imwrite('enh.jpg',enh_img)


