import cv2 as cv 
 


def rescaleFrame(frame, scale=0.75):
  width = int(frame.shape[1]*scale)
  height = int(frame.shape[0]*scale)
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('images/frame2.jpg')
#cv.imshow('astronaut', img)

	
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('grey', grayImage)




blur = cv.blur(grayImage, (4,4)) 
#cv.imshow('bnw', blur)



	
(thresh, blackAndWhiteImage) = cv.threshold(blur, 127, 255, cv.THRESH_BINARY)
#cv.imshow('bnw', blackAndWhiteImage)

resized_org = rescaleFrame(img, scale=.5)
resized_image = rescaleFrame(blackAndWhiteImage, scale=.5)
cv.imshow('org scaled', resized_org)
cv.imshow('scaled', resized_image)

cv.imwrite("images\irame2-bnw.jpg", blackAndWhiteImage) 


cv.waitKey(0)