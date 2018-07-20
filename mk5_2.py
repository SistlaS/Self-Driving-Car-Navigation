import cv2
import numpy as np
img = cv2.imread("Nav.png",cv2.IMREAD_COLOR)
k=0
x1 = 479                                                                          #loading the coordinates of points obtained in Part-1
y1 = 793
x2 = 1443
y2 = 101
i = x1
j = y1
path = []                                                                          #list to store coordinates of path-points. Ignore for now
while (i != x2 and j != y2) and k<1000 :                                             #counter (k) added to check progress and prevent infifnite loop in case of faulty  code
   d1 = i - x2                                                                      # sign of d1 and d2 determines the direction of travel 
   d2 = j - y2
   if d1 < 0:
       if img[j, i+1,0] > 0 and img[j, i+1,1] > 0 and img[j, i+1,2]> 0:    # travel till detect black pixels(obstruction) ahead
           path = path + [[j,i]]                                                    #add point coordinates to path list(ignore for now)
           img[j,i] = [0,0,255]                                                     #mark the pixels on which we travel, as red
           i += 1                                                                   # keep moving right
           print('right up to',i,j)
   if d1 >  0:
       if img[j,i-1,0] > 0 and img[j,i-1,1] > 0 and img[j,i-1,2]> 0:
           path = path + [[j,i]]
           img[j,i]= [0,0,255]
           i -= 1                                                                   #keep moving left
           print('left up to',i,j)
   if d2 > 0:
       if img[j-1, i,0] > 0 and img[j-1,i,1] > 0 and img[j-1, i,2]> 0:
           path = path + [[j,i]]
           img[j,i] = [0,0,255]
           j -= 1                                                                   #keep moving up
           print('up till', i,j)
   if d2 < 0:
       if img[j+1,i ,0] > 0 and img[j+1, i ,1] > 0 and img[j+1,i ,2] > 0:
           path = path + [[j,i]]
           img[j,i] = [0,0,255]
           j += 1                                                                   # keep moving down
           print('down till',i,j)
   k+=1

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
