#convert '*.png[600x]' resized%03d.png
#image magic for terminal to resize montgomery set
import numpy as np
import cv2
import os
from itertools import izip
def nothing(*arg, **kw):
    pass
def process_frame(frame, mask):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = frame * mask

        kernel_size = cv2.getTrackbarPos('kernel_size', 'img')
        gauss_kernel_size = cv2.getTrackbarPos("gauss_kernel_size", 'img')
        if kernel_size > 2:
            if kernel_size % 2 == 0:
                kernel_size += 1
            kernel = np.ones((kernel_size,kernel_size),np.uint8)
            frame = cv2.erode(frame,kernel,iterations = 1)
            frame = cv2.dilate(frame,kernel, iterations = 1)
        if gauss_kernel_size > 2:
            if gauss_kernel_size % 2 == 0:
                gauss_kernel_size += 1
                frame = cv2.GaussianBlur(frame, (gauss_kernel_size,gauss_kernel_size), 0)

        threshold = cv2.getTrackbarPos('threshold', 'img')
        threshold2 = cv2.getTrackbarPos('threshold2', 'img')
        if(threshold > 0):
            val,frame = cv2.threshold(frame,threshold,255,cv2.THRESH_TOZERO)

        if(threshold2 > 0):
            val,frame = cv2.threshold(frame,threshold2,255,cv2.THRESH_TOZERO_INV )
        #frame = cv2.cornerHarris(frame,2,3,0.04)
        #frame = cv2.Canny(frame,100,200)
        cv2.imshow("img",frame)
        cv2.waitKey(0)

def process(files,masks):
    cv2.namedWindow('img')
    cv2.createTrackbar('kernel_size', 'img', 0, 50, nothing)
    cv2.createTrackbar('gauss_kernel_size', 'img', 0, 50, nothing)
    cv2.createTrackbar('threshold', 'img', 0, 255, nothing)
    cv2.createTrackbar('threshold2', 'img', 0, 255, nothing)
    for f,m in izip(files,masks):
        try:
            process_frame(cv2.imread(f),cv2.imread(m,flags=cv2.IMREAD_GRAYSCALE))
        except:
            pass
def list1(files):
    cv2.namedWindow('img')
    cv2.createTrackbar('brightness', 'img', 0, 100, nothing)
    cv2.createTrackbar('contrast', 'img', 1.0, 400, nothing)
    #cv2.createTrackbar('kernel_size', 'img', 0, 50, nothing)
    #cv2.createTrackbar('gauss_kernel_size', 'img', 0, 50, nothing)
    #cv2.createTrackbar('threshold', 'img', 0, 255, nothing)
    #cv2.createTrackbar('threshold2', 'img', 0, 255, nothing)
    while True:
        for f in files:
            list1_process_frame(cv2.imread(f))
def list1_process_frame(frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        alpha = cv2.getTrackbarPos('contrast in %', 'img')
        beta = cv2.getTrackbarPos('brightness', 'img')
        frame = cv2.multiply(frame,np.array([float(alpha)/100]))                    # mul_img = img*alpha
        #frame = cv2.add(frame,np.array([beta]))
        #frame = cv2.add(frame,np.uint8([10]))
        cv2.imshow("img",frame)
        cv2.waitKey(0)

files = ["MontgomerySet/CXR_png_600/" + f for f in os.listdir("MontgomerySet/CXR_png_600/") if ".png" in f or ".PNG" in f]
r_masks = ["MontgomerySet/ManualMask_600/rightMask/" + f for f in os.listdir("MontgomerySet/ManualMask_600/rightMask/") if ".png" in f or ".PNG" in f]
l_masks = ["MontgomerySet/ManualMask_600/leftMask/" + f for f in os.listdir("MontgomerySet/ManualMask_600/leftMask/") if ".png" in f or ".PNG" in f]
while True:
    process(files,l_masks)
    process(files,r_masks)


