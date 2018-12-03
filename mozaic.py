import sys
import os
import numpy as np
import cv2 as cv
from .target_processor import TargetProcessor
from .tile_processor import TileProcessor


class Mozaic:

    def __init__(self, target_img_path, img_collection_path):
        self.target_image = target_img_path
        self.img_collection = img_collection_path

    def makeMozaic(self):
        img = cv.imread(self.target_image)
        tile_processor = TileProcessor(self.img_collection)
        
        return 0


if __name__ == '__main__':
    if(len(sys.argv) < 3):
        print("Please provide the following command format: \npython mozaic.py <Image Path to be mozaic> <path to collection of images>")
    else:
        mozaicGenerator = Mozaic(sys.argv[1], sys.argv[2])
        mozaicGenerator.makeMozaic()
