import numpy as np
import cv2 as cv
import os
from progress import progress_bar
from tile_processor import TileProcessor


class TargetProcessor:
    def __init__(self, target_path):
        self.target_path = target_path

    def render_target(self, rgb_collection, reduced_img_arr_collection):
        img = cv.imread(self.target_path)
        print(img.shape)
        img_height = len(img)
        img_width = len(img[0])
        print(img_height)
        

        for x_row in range(img_height):
            for y_col in range(img_width):
                #print(img[y_col][x_row].mean())
                current_pixel_avg = img[y_col][x_row].mean()
                closest_rgb_value = self.match_rgb(current_pixel_avg, rgb_collection, reduced_img_arr_collection)
                progress_bar((x_row*img_width)/(img_height*img_width),"Processing Target")
        cv.imwrite("mozaic.png",img)
        return 0
    
    #This method is responsible for finding the closest rgb average value that our original
    #image has so that we can insert the appropriate image
    def match_rgb(self,rgb_avg,rgb_collection,img_arr_collection):
        return 0




if __name__ == '__main__':
    tiles = TileProcessor(50).retrieve_tiles("./tiles")
    processor = TargetProcessor("/home/twong/TyDev/Mozaic/us.jpg").render_target(tiles[0],tiles[1])
        
