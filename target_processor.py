import numpy as np
import cv2 as cv
import os
from tile_processor import TileProcessor

class TargetProcessor:
    def __init__(self, target_path, tile_collection):
        self.target_path = target_path

    def render_target(self):
        absolute_target_path = os.path.dirname(os.path.realpath(__file__))
        img = cv.imread(absolute_target_path+"/"+self.target_path)
        print(img)
        img_width = img[0]
        img_height = img[1]

        for x_row in img_width:
            for y_col in img_height:
                np.array(img[x_row][y_col]).mean()
        return 0

if __name__ == '__main__':
    tiles = TileProcessor(50).retrieve_tiles("./tiles")
    processor = TargetProcessor("./mozaic.jpeg",tiles).render_target()
        
