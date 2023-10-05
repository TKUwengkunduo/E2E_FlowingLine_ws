import numpy as np
import cv2




class Image_processing:
    def __init__(self):
        pass

    def image_convert_type(image):
        return tf.image.convert_image_dtype(image, dtype=tf.float32)

    def image_resize(image, target_size):
        # return tf.image.resize(images=image, size=target_size)
        return cv2.resize(image, target_size)
        
    def image_reshape_2to1(data):
        return tf.reshape(data, [-1])
        
    def test():
        print("dadscsdvdfhbnd")


class Loader(Image_processing):
    def  __init__(self):
        pass

    def search(self):
        data_txt = open('./Data_Collection_Vehicles/Data/data.txt', 'r')


    def image_read(self):
        cv2.imread('./Data_Collection_Vehicles/Data/iclab1004/iclab1004_3.png')


if __name__=='__main__':
    loader = Loader()
    loader.image_read()
    loader.search()