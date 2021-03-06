import numpy as np
import cv2
import os
from itertools import izip

def nothing(*arg, **kw):
    pass
class Preprocessor:
    def __init__(self, lungs, l_masks=None, r_masks=None):
        self.lungs = lungs
        self.l_masks = l_masks
        self.r_masks = r_masks
        self.fast = cv2.FastFeatureDetector_create()
    # def process_all(self):

    def apply_mask(self,img,mask,crop=False):
        img = img * mask
        if crop:
            x,y,w,h = cv2.boundingRect(img)
            img = img[y:y+h,x:x+w]
        return img

    def make_window(self):
        cv2.namedWindow('img')
        cv2.createTrackbar('kernel_size', 'img', 0, 50, self.reprocess)
        cv2.createTrackbar('gauss_kernel_size', 'img', 0, 50, self.reprocess)
        cv2.createTrackbar('threshold', 'img', 0, 255, self.reprocess)
        cv2.createTrackbar('threshold2', 'img', 0, 255, self.reprocess)
        cv2.createTrackbar('FAST', 'img', 100, 100, self.reprocess)


    def read_trackbars(self,val):
        self.kernel_size = cv2.getTrackbarPos('kernel_size', 'img')
        self.gauss_kernel_size = cv2.getTrackbarPos("gauss_kernel_size", 'img')
        self.threshold = cv2.getTrackbarPos('threshold', 'img')
        self.threshold2 = cv2.getTrackbarPos('threshold2', 'img')
        self.fastThr=cv2.getTrackbarPos('FAST', 'img')
        #self.fast = cv2.FastFeatureDetector_create()
        #self.fast = cv2.FastFeatureDetector_create(cv2.getTrackbarPos('FAST', 'img'))


    def reprocess(self,x):
        self.process_img(self.curr_img)
        cv2.imshow("img",self.processed_img)

    def process_img(self,img):
        self.read_trackbars(0)
        kernel_size = self.kernel_size
        gauss_kernel_size = self.gauss_kernel_size
        if kernel_size > 2:
            if kernel_size % 2 == 0:
                kernel_size += 1
            kernel = np.ones((kernel_size,kernel_size),np.uint8)
            img = cv2.erode(img,kernel,iterations = 1)
            img = cv2.dilate(img,kernel, iterations = 1)
        if gauss_kernel_size > 2:
            if gauss_kernel_size % 2 == 0:
                gauss_kernel_size += 1
            img = cv2.GaussianBlur(img, (gauss_kernel_size,gauss_kernel_size), 0)

        if self.threshold > 0:
            val,img = cv2.threshold(img,self.threshold,255,cv2.THRESH_TOZERO)
        if self.threshold2 > 0:
            val,img = cv2.threshold(img,self.threshold2,255,cv2.THRESH_TOZERO_INV )
        if self.fastThr < 100:
            fast = cv2.FastFeatureDetector_create(self.fastThr)
            kp = fast.detect(img,None)
            img = cv2.drawKeypoints(img,kp,img)
        self.processed_img = img
    def process(self,files,masks=None,rev=False, write=False):
        self.make_window()
        if masks:
            for f,m in izip(files,masks):
                try:
                    self.curr_img = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2GRAY)
                    self.curr_img = self.apply_mask(self.curr_img,cv2.imread(m,flags=cv2.IMREAD_GRAYSCALE),True)
                    if rev:
                        self.curr_img=cv2.flip(self.curr_img,1)
                    self.process_img(self.curr_img)
                    if write:
                    #print "MontgomerySet/crop/"+os.path.basename(os.path.normpath(f)).replace(".png",".bmp")
                        cv2.imwrite("MontgomerySet/crop/"+os.path.basename(os.path.normpath(f)).replace(".png",".bmp"),self.curr_img)
                    cv2.imshow("img",self.processed_img)
                    print f
                    print m
                    if cv2.waitKey(0)==27:
                        return
                except:
                    print "Except " + os.path.basename(os.path.normpath(f)) + " " + os.path.basename(os.path.normpath(m))
        else:
            for f in files:
                self.curr_img = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2GRAY)
                self.process_img(self.curr_img)
                cv2.imshow("img",self.processed_img)
                if cv2.waitKey(0)==27:
                    return


    def debug(self):
        print self.l_masks
