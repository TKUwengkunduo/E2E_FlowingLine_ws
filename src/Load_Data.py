import numpy as np
import tensorflow as tf
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