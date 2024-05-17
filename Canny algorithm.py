import cv2


image = cv2.imread('E:\\MY FILES\\Wallpapers\\Screenshot_20221014-185651_YouTube.jpg')
grayedImage =cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
Blurredimage = cv2.GaussianBlur(grayedImage , (3 ,3), 0)
Edges = cv2.Canny( Blurredimage ,15 , 35)
cv2.imshow('Image' ,image)
cv2.imshow('the edges' , Edges)
cv2.waitKey(0)