import os
from PIL import Image
 
path = 'supplier-data/images/'
 
for file in os.listdir(path):
    if '.tiff' in file:      
        #Open the image and convert in to RGB
        img = Image.open(path + file).convert("RGB")

        #Get the file name without the extension
        dir, filename = os.path.split(file)
        filename = os.path.splitext(filename)[0]
        
        """
        Convert the image as requested:
        1. Size: Change image resolution from 3000x2000 to 600x400 pixel
        2. Format: Change image format from .TIFF to .JPEG
        """
        img.resize((600, 400)).save(path + filename + '.jpeg' , 'jpeg')