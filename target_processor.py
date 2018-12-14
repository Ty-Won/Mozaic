import numpy as np
import cv2 as cv
import os
import sys
import random
from time import sleep
from progress import progress_bar
from tile_processor import TileProcessor


class TargetProcessor:
    def __init__(self, target_path):
        self.target_path = target_path

    def render_target(self, rgb_to_img_dict, reduced_img_arr_dict, tile_size):
        img = cv.imread(self.target_path)
        print(img.shape)
        img_height = len(img)
        img_width = len(img[0])
        print(img_height)
        
        rgb_values = np.fromiter(rgb_to_img_dict.keys(), dtype=float)
        

        for x_row in range(tile_size,img_height,tile_size):
            for y_col in range(tile_size,img_width,tile_size):
                print(img[y_col][x_row].mean())
                pixel_avg = img[y_col-tile_size:y_col][x_row-tile_size:x_row].mean()
                matching_img = match_rgb_img( pixel_avg, rgb_values, rgb_to_img_dict, reduced_img_arr_dict)


                percent_done= 100*(x_row*img_width)/(img_height*img_width)
                progress_bar(percent_done,"testing")
        

        return 0
    
#This method is responsible for finding the closest rgb average value that our original
#image has so that we can insert the appropriate image
def match_rgb_img(pixel_avg, rgb_values, rgb_to_img_dict, img_arr_collection):
    matching_rgb_index = (np.abs(rgb_values-pixel_avg)).argmin()
    closest_rgb_val = rgb_values[matching_rgb_index]
    rgb_img_name = random.choice(rgb_to_img_dict[closest_rgb_val])
    return img_arr_collection[rgb_img_name]
        



if __name__ == '__main__':
    tiles = TileProcessor(50).retrieve_tiles("./tiles")
    processor = TargetProcessor("/home/twong/TyDev/Mozaic/us.jpg").render_target(tiles[0],tiles[1],50)
        
