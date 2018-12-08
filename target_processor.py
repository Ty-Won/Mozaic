import numpy as np
import cv2 as cv
import os
from tile_processor import TileProcessor

class TargetProcessor:
    def __init__(self, target_path, tile_collection):
        self.target_path = target_path

    def render_target(self):
        img = cv.imread(self.target_path)
        print(img.shape)
        img_height = len(img)
        img_width = len(img[0])
        print(img_height)
        

        for x_row in range(img_width):
            for y_col in range(img_height):
                print(img[y_col][x_row].mean())
        return 0

if __name__ == '__main__':
    tiles = TileProcessor(50).retrieve_tiles("./tiles")
    processor = TargetProcessor("/home/twong/TyDev/Mozaic/mosaic.jpeg",tiles).render_target()
        
