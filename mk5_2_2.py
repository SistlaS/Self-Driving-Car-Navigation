import cv2
import numpy as np
img = cv2.imread("Nav.png",cv2.IMREAD_COLOR)
k=0
x1 = 479                                                                          
y1 = 790
x2 = 1443
y2 = 101

def trace (x1,y1, x2, y2):
    i = x1
    j = y1
    d1 = i - x2                                                                      
    d2 = j - y2
    if i == x2 or j == y2:
        return 0
    else:
        if d1 < 0:
         while d1<0 and img[j, i+10,0] > 0 and img[j, i+10,1] > 0 and img[j, i+10,2]> 0:    
                                                                                
           img[j,i] = [0,0,255]                                                     
           i += 1                                                                   
           print('right up to',i,j)
           d1 = i - x2
        if d1 >  0:
         while d1<0 and img[j,i-10,0] > 0 and img[j,i-10,1] > 0 and img[j,i-10,2]> 0:
           img[j,i]= [0,0,255]
           i -= 1                                                                   
           print('left up to',i,j)
           d1 = i - x2
        if d2 > 0:
         while d2 > 0 and img[j-10, i,0] > 0 and img[j-10,i,1] > 0 and img[j-10, i,2]> 0:
           img[j,i] = [0,0,255]
           j -= 1                                                                   
           print('up till', i,j)
           d2 = j - y2
        if d2 < 0:
         while d2<0 and img[j+10,i ,0] > 0 and img[j+1, i ,1] > 0 and img[j+10,i ,2] > 0:
           img[j,i] = [0,0,255]
           j += 1                                                                   
           print('down till',i,j)
           d2 = j - y2
        return trace(i,j, x2,y2)
def bty(x1, x2, y):
    i = x1
    j = y
    d1 = i-x2
    if i==x2 and j == y:
        return 0
    else:
        if d1< 0:  
    
trace( x1, y1, x2,y2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
