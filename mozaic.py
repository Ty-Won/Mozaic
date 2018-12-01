import sys
import os
from PIL import Image


class mozaic:

    def __init__(self, target_img, img_collection):
        self.target_image = target_img
        self.img_collection = img_collection

    def makeMozaic(self):
        img = Image.open(self.target_image)
        return 0


if __name__ == '__main__':
    if(len(sys.argv) < 3):
        print("Please provide the following command format: \npython mozaic.py <Image Path to be mozaic> <path to collection of images>")
    else:
        mozaicGenerator = mozaic(sys.argv[1], sys.argv[2])
        mozaicGenerator.makeMozaic()
