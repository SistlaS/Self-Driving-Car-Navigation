#PART-1: Finding the blue(starting point) and green(end point) spots, and locating the centre pixel of each of these. These 2 pixels(points) will mark the beginning and end 
# of the path to be drawn on the given map 

import cv2
import numpy as np

img = cv2.imread('Nav.png')
prop = img.shape                                                            # prop is now an array : (breadth, length, 3(for BGR))
sumx1 = 0																	#(x1,y1) are coordinates of centre of blue spot; (x2,y2) are coordinates of centre of green spot 
sumy1 = 0																	# sumx1 is the sum of x-coordinates of all blue pixels, and so on
sumx2 = 0
sumy2 = 0
c = 0
d = 0
for l in range (prop[1]):
    for b in range (prop[0]):
        color = img[b,l]
        if color[0] > 150 and color[1] < 100 and color[2] < 100:		# setting threshold for identifying blue pixels
            sumx1 += l
            sumy1 += b
            c+=1
        if color[0] < 100 and color[1] > 150 and color[2] < 100:		# setting threshold for identifying green pixels
            sumx2 += l
            sumy2 += b
            d+=1

x1 = sumx1/c															
y1 = sumy1/c
x2 = sumx2/d
y2 = sumy2/d
print(x1,y1, x2,y2)
