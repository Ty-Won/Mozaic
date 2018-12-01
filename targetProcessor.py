from PIL import Image


class TargetProcessor:
    def targetProcess(self, target_path):
        self.target_path = target_path

    def process(self):
        img = Image.open(self.target_path)
        img_width = img.size[0]
        img_height = img.size[1]

        
