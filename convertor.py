from PIL import Image
import numpy as np


def png_to_raw(input_png_path, output_raw_path, mode='RGB'):
    img = Image.open(input_png_path)
    img = img.convert(mode)
    img_data = np.array(img)
    img_data.tofile(output_raw_path)



path = './data_to_convert/'
images = ['img', 'grey_img']

png_to_raw(path + 'img.png', './data/' + 'img.raw')
png_to_raw(path + 'grey_img.png', './data/' + 'grey_img.raw', mode = 'L')



    
    