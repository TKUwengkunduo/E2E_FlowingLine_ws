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

# 打印看一下
print("字母對應到數字編號: \n", char_to_int)
print("\n")

print("數字編號對應到字母: \n", int_to_char)


# 準備輸入數據集
seq_length = 1
dataX = []
dataY = []
for i in range(0, len(alphabet) - seq_length, 1):
    seq_in = alphabet[i:i + seq_length]
    seq_out = alphabet[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
    print(seq_in, '->', seq_out)


# 重塑 X 資料的維度成為 (samples, time_steps, features)
X = numpy.reshape(dataX, (len(dataX), seq_length, 1))

# 歸一化
X = X / float(len(alphabet))

# one-hot 編碼輸出變量
y = np_utils.to_categorical(dataY)

print("X shape: ", X.shape) # (25筆samples, "1"個時間步長, 1個feature)
print("y shape: ", y.shape)


# 創建模型
model = Sequential()
model.add(LSTM(32, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(y.shape[1], activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=500, batch_size=1, verbose=2)

scores = model.evaluate(X, y, verbose=0)
print("Model Accuracy: %.2f%%" % (scores[1]*100))


# 展示模型預測能力
for pattern in dataX:
    # 把26個字母一個個拿進模型來預測會出現的字母
    x = numpy.reshape(pattern, (1, len(pattern), 1))
    x = x / float(len(alphabet))
    
    prediction = model.predict(x, verbose=0)
    index = numpy.argmax(prediction) # 機率最大的idx
    result = int_to_char[index] # 看看預測出來的是那一個字母
    seq_in = [int_to_char[value] for value in pattern]
    print(seq_in, "->", result) # 打印結果