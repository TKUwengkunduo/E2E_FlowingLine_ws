import tensorflow as tf
from tensorflow.keras.utils import plot_model

from tensorflow.keras import Model
from tensorflow.keras import Input
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense

import cv2
import numpy as np
import  os

import Load_Data
LoadData = Load_Data.Image_processing


def load_data():
    
    Data_train = []
    Data_train_labe = [(1,2)]

    img = cv2.imread('/home/weng/work/E2E_FlowingLine_ws/test_data/1.jpg')
    # img = LoadData.image_convert_type(img)
    img = LoadData.image_resize(img, (640, 480))

    # img = LoadData.image_reshape_2to1(img)
    img = img.flatten('C')

    print('=========================================')
    print('2', np.shape(img))
    print('=========================================')
    print(img)

    # 重塑 x_train 資料的維度成為 (samples, time_steps, features)
    x_train = np.reshape(img, (1, 1, 921600))  # <-- 特別注意這裡


    # x_train = np.array(Data_train)
    y_train = np.array(Data_train_labe)


    return x_train, y_train


def model_building():
    # model = tf.keras.models.Sequential([
    #     # , input_shape=(1,921600)
    #     # units(LSTM unit number), input_shape(, number of features)
    #     tf.keras.layers.LSTM(units = 10, input_shape=(1,921600), return_sequences=True),
    #     tf.keras.layers.LSTM(units = 100),
    #     # Shape => [batch, time, features]
    #     tf.keras.layers.Dense(1, activation='softmax')
    # ])

    Input_layer     = Input(shape=(1,921600), name='input')
    H1_LSTM         = LSTM(units = 10, return_sequences=True)       (Input_layer)
    H2_LSTM         = LSTM(units = 100, return_sequences=False)     (H1_LSTM)
    Output_layer    = Dense(2, activation='softmax')                (H2_LSTM)

    model = Model(inputs=Input_layer, outputs=Output_layer)

    return model


def train_model(model, x_train, y_train):
    # model.compile(optimizer='adam',
    #             loss='MeanSquaredError',
    #             metrics=['rmsprop'])

    # model.fit(x_train, y_train, epochs=1, batch_size=1)

    # model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=50, batch_size=1, verbose=2)

    return model


def img_read():
    img = "C:/Users/weng/Downloads/S__14540802.jpg"

    img = cv2.imread(img)
    img = cv2.resize(img,(28,28))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(28):
        for j in range(28):
            if img[i][j]>127:
                img[i][j]=0
            else:
                img[i][j]=255
    return img


def save_model(model, path):
    tf.keras.models.save_model(model, path, overwrite=True, save_format=None)

def load_model(path):
    return tf.keras.models.load_model(path, custom_objects=None, compile=True)



if __name__ == '__main__':

    ''' 加載資料 '''
    x_train, y_train = load_data()

    ''' 建立模型 '''
    model = model_building()

    ''' 查看模型架構 '''
    model.summary()
    plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)

    ''' 訓練模型 '''
    model = train_model(model, x_train, y_train)

    ''' 儲存模型 '''
    # save_model(model, 'C:/Users/weng/Downloads/TKU_MNIST/my_model.h5')

    ''' 載入模型 '''
    # model = load_model('C:/Users/weng/Downloads/TKU_MNIST/my_model.h5')

    ''' 測試模型 '''
    scores = model.evaluate(x_train, np.array([(1,2)]), verbose=0)
    print("Model Accuracy: %.2f%%" % (scores[1]*100))
