#convert '*.png[600x]' resized%03d.png
#image magic for terminal to resize montgomery set
# huxwell@huxwell-x230:~/PycharmProjects/lungs/MontgomerySet/crop$ convert '*_0.bmp[x800]' lung%03d_0.bmp
# huxwell@huxwell-x230:~/PycharmProjects/lungs/MontgomerySet/crop$ convert '*_1.bmp[x800]' lung%03d_1.bmp

import numpy as np
import cv2
import os
from itertools import izip
from Preprocessor import Preprocessor


#def process_frame(frame, mask):
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # return frame


size="_800"
#files = ["MontgomerySet/CXR_png"+size+"/" + f for f in os.listdir("MontgomerySet/CXR_png"+size+"/") if ".png" in f or ".PNG" in f]
#r_masks = ["MontgomerySet/ManualMask"+size+"/rightMask/" + f for f in os.listdir("MontgomerySet/ManualMask"+size+"/rightMask/") if ".png" in f or ".PNG" in f]
#l_masks = ["MontgomerySet/ManualMask"+size+"/leftMask/" + f for f in os.listdir("MontgomerySet/ManualMask"+size+"/leftMask/") if ".png" in f or ".PNG" in f]
# processor = Preprocessor(files,l_masks,r_masks)
# processor.process(processor.lungs,processor.l_masks,False,True)
# processor.process(processor.lungs,processor.r_masks,True,True)
files = ["MontgomerySet/crop"+size+"/" + f for f in os.listdir("MontgomerySet/crop"+size+"/") if ".bmp" in f or ".BMP" in f]
print files
processor = Preprocessor(files)
processor.process(files)

#while True:
#    process(files,l_masks,rev=True)
#    process(files,r_masks,rev=False)


