import numpy as np
import os
import cv2 as cv
from progress import progress_bar


class TileProcessor:

    def __init__(self, tile_dimension):
        self.tile_dimension = tile_dimension

    # Generates 2 collections, one of rgb values represented by the tiles and
    # the other of reduced img arrays to be used for tiles
    def retrieve_tiles(self, img_collection_path):

        collection_path = img_collection_path
        rgb_collection = {}
        scaled_images = {}

        for root, folders, files in os.walk(collection_path):
            for img_number, img in enumerate(files):

                file_path = os.path.join(root, img)
                img_array = cv.imread(file_path)

                # Non supported image types will result in the image being read to be None
                if(img_array is None):
                    continue
                
                # # Used to view the image if desired
                # cv.namedWindow(img,cv.WINDOW_NORMAL)
                # cv.imshow(img,img_array)
                # cv.waitKey(0)
                # cv.destroyAllWindows()


                progress_bar(img_number, len(files), "Loading Tiles")

                avg_rgb, reduced_img_array = self.process(img_array, self.tile_dimension)

                if avg_rgb in rgb_collection:
                    rgb_collection[avg_rgb].append(img)
                    scaled_images[img] = (reduced_img_array)
                else:
                    rgb_collection[avg_rgb] = [img]
                    scaled_images[img] = (reduced_img_array)

        return (rgb_collection, scaled_images)

    # Separate method to prep the individual image into a tile and collect the average rgb value
    def process(self, img_rgb_array, tile_size):
        reduced_dim_img = downscale(img_rgb_array, tile_size)
        rgb_avg = int(np.array(reduced_dim_img).mean(axis=(0, 1, 2)))
        return (rgb_avg, reduced_dim_img)

    
    #TODO create a more accurate rgb algorithm other than just the rgb average

# Reduces the dimension of the given image to tile size
def downscale(img_array, tile_size):
    return cv.resize(img_array, dsize=(tile_size, tile_size), interpolation=cv.INTER_AREA)


if __name__ == "__main__":
    directory = TileProcessor(50)
    directory.retrieve_tiles("./tiles")
