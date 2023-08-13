'''
    https://hsin-life.com/archives/2328
'''

import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.utils import np_utils
# from keras.preprocessing.sequence import pad_sequences    # Ubuntu
from keras_preprocessing.sequence import pad_sequences      # Jetson Ubuntu

# 給定隨機的種子, 以便讓大家跑起來的結果是相同的
numpy.random.seed(7)


# 定義序列數據集
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 創建字符映射到整數（0 - 25)和反相的查詢字典物件
char_to_int = dict((c, i) for i, c in enumerate(alphabet))
int_to_char = dict((i, c) for i, c in enumerate(alphabet))


seq_length = 3
dataX = []
dataY = []
for i in range(0, len(alphabet) - seq_length, 1):
    seq_in = alphabet[i:i + seq_length]
    seq_out = alphabet[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
    print(seq_in, '->', seq_out)


# 重塑 X 資料的維度成為 (samples, time_steps, features)
X = numpy.reshape(dataX, (len(dataX), seq_length, 1))  # <-- 特別注意這裡

# 歸一化
X = X / float(len(alphabet))

# 使用one hot encode 對Y值進行編碼
y = np_utils.to_categorical(dataY)


# 創建模型
model = Sequential()
model.add(LSTM(32, input_shape=(X.shape[1], X.shape[2]))) # <-- 特別注意這裡
model.add(Dense(y.shape[1], activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=500, batch_size=1, verbose=2)

# 評估模型的性能
scores = model.evaluate(X, y, verbose=0)
print("Model Accuracy: %.2f%%" % (scores[1]*100))

# 讓我們擷取3個字符轉成張量結構 shape:(1,3,1)來進行infer
for pattern in dataX:
    x = numpy.reshape(pattern, (1, len(pattern), 1))
    x = x / float(len(alphabet))
    prediction = model.predict(x, verbose=0)
    index = numpy.argmax(prediction)
    result = int_to_char[index]
    seq_in = [int_to_char[value] for value in pattern]
    print(seq_in, "->", result)