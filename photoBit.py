import sys
import os
import numpy as np
import cv2 as cv
from target_processor import TargetProcessor
from tile_processor import TileProcessor

#percentage of tile compression
tile_size = 50


class photoBit:
    

    def __init__(self, target_img_path, img_collection_path):
        self.target_image = target_img_path
        self.img_collection_path = img_collection_path

    def makephotoBit(self):
        tile_processor = TileProcessor(tile_size)
        rgb_to_img_dict, reduced_img_arr_dict = tile_processor.retrieve_tiles(self.img_collection_path)
        photoBit_arr = TargetProcessor(self.target_image).render_target(rgb_to_img_dict, reduced_img_arr_dict, tile_size)
        cv.imwrite("photoBit.png",photoBit_arr)
        return 0


if __name__ == '__main__':
    if(len(sys.argv) < 3):
        print("Please provide the following command format: \npython photoBit.py <photoBit target image path> <path to collection of images>")
    else:
        photoBitGenerator = photoBit(sys.argv[1], sys.argv[2])
        photoBitGenerator.makephotoBit()
