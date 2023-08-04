import tensorflow as tf
import cv2
import numpy as np
import  os

import Load_Data
LoadData = Load_Data.Image_processing


def load_data():
    
    Data_train = []
    Data_train_labe = [1]

    img = cv2.imread('/home/weng/weng_ws/E2E_FlowingLine_ws/test_data/1.jpg')
    # img = LoadData.image_convert_type(img)
    img = LoadData.image_resize(img, (640, 480))
    print('=========================================')
    print(np.shape(img))
    print('=========================================')
    img = LoadData.image_reshape_2to1(img)
    Data_train.append(np.array(img/255.0))
    print('=========================================')
    print(np.shape(Data_train))
    print('=========================================')

    # img = cv2.imread('/home/weng/weng_ws/E2E_FlowingLine_ws/test_data/2.jpg')
    # img = LoadData.image_convert_type(img)
    # img = LoadData.image_resize(img, (640, 480))
    # img = LoadData.image_reshape_2to1(img)
    # Data_train.append(np.array(img/255.0))

    x_train = np.array(Data_train)
    y_train = np.array(Data_train_labe)

    return x_train, y_train


def model_building():
    model = tf.keras.models.Sequential([
        # units(LSTM unit number), input_shape(, number of features)
        tf.keras.layers.LSTM(units = 1, input_shape=(1,921600),return_sequences=True),
        # Shape => [batch, time, features]
        tf.keras.layers.Dense(1, activation='softmax')
    ])

    return model


def train_model(model, x_train, y_train):
    model.compile(optimizer='adam',
                loss='MeanSquaredError',
                metrics=['rmsprop'])

    model.fit(x_train, y_train, epochs=1, batch_size=1)

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

    ''' 訓練模型 '''
    model = train_model(model, x_train, y_train)

    ''' 儲存模型 '''
    # save_model(model, 'C:/Users/weng/Downloads/TKU_MNIST/my_model.h5')

    ''' 載入模型 '''
    # model = load_model('C:/Users/weng/Downloads/TKU_MNIST/my_model.h5')

    ''' 測試模型 '''
    # model.evaluate(x_test, y_test, verbose=2)