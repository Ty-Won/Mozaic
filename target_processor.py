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

    #Takes the target image and generates the photoBit through a collection of rgb values
    #associated with a collection of image arrays that are organized by overall rgb value
    def render_target(self, rgb_to_img_dict, reduced_img_arr_dict, tile_size):

        img = cv.imread(self.target_path)
        
        if(img is None):
            print("Error in target image: Invalid path or file")
            return 0
            
        img_height = len(img)
        img_width = len(img[0])
        

        # Reminder that the images are in (height,width,rgb),
        for y_col in range(tile_size, img_width, tile_size):
            for x_row in range(tile_size, img_height, tile_size):

                height_pixel_range = y_col-tile_size
                width_pixel_range = x_row-tile_size
                pixel_arr = img[width_pixel_range:x_row, height_pixel_range:y_col]

                pixel_avg = pixel_arr.mean()
                matching_img = match_rgb_img(pixel_avg, rgb_to_img_dict, reduced_img_arr_dict)
                
                # print(matching_img)
                # print(matching_img.shape)

                img[width_pixel_range:x_row, height_pixel_range:y_col] = matching_img
            progress_bar(y_col*img_height, img_width*img_height, "Rendering Target Image: ")
            
        return img

# Finds the closest rgb average value that our original
# image has so that we can insert the appropriate image
def match_rgb_img(pixel_avg, rgb_to_img_dict, img_arr_collection):

    rgb_values = np.fromiter(rgb_to_img_dict.keys(), dtype=float)
    matching_rgb_index = (np.abs(rgb_values-pixel_avg)).argmin()
    closest_rgb_val = rgb_values[matching_rgb_index]
    rgb_img_name = random.choice(rgb_to_img_dict[closest_rgb_val])
    return img_arr_collection[rgb_img_name]


if __name__ == '__main__':
    if(len(sys.argv)<3):
        print("Please provide the following command format: \npython photoBit.py <target image path> <tile directory path>")
    else:
        tiles = TileProcessor(50).retrieve_tiles(sys.argv[1])
        processor = TargetProcessor(sys.argv[2]).render_target(tiles[0], tiles[1], 50)
