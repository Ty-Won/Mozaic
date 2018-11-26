import sys
import os
from PIL import Image


class mozaic:

    def __init__(self, target_img,img_collection):
        self.target_image = target_img
        self.img_collection = img_collection

    def makeMozaic(self):
        #TODO


if __name__ =='__main__':
    picture = mozaic(sys.argv[0],sys.argv[1])

