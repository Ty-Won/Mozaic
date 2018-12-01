from PIL import Image
import os

class processTiles:

    def __init__(self,img_collection_path):
        self.img_collection_path=img_collection_path


    def retrieve_tiles(self, tile_collection):
        collection_path=self.img_collection_path

        for root, folders, files in os.walk(collection_path):
            for file_name in folders:
                print(file_name)
                file_path = os.path.join(root,file_name)


    
    def process(self):
        tiles = []
                


if __name__=="__main__":
    # img = Image.open("./mosaic.jpeg")
    # img.convert('RGB')
    directory = processTiles("./")
    directory.process()
    
        
    
