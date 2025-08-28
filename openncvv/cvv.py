import cv2 as cv
img=cv.imread('photos/cat.jpg') # read the file 
cv.imshow('Cat',img) #  cat ismein new file ka name hai aur img variable ka
cv.waitKey(0) # wait for keyboard key press 
