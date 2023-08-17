# https://swf.com.tw/?p=1188

import serial  # 引用pySerial模組
from threading import Thread



class FS_i6:
    def __init__(self):
        self.R_speed = 0
        self.L_speed = 0
        pass
    
    def device_initialization(self, usb='/dev/ttyUSB0', baudrate=115200):
        self.ser = serial.Serial(usb, baudrate)   # 初始化序列通訊埠

    def get_data(self):
        # print('R/L speed :', self.R_speed, ' | ',self.L_speed)
        return self.R_speed, self.L_speed

    def _main_loop(self):
        while True:
            while self.ser.in_waiting:          # 若收到序列資料…
                self.data_raw = self.ser.readline()  # 讀取一行
                self.data = self.data_raw.decode()   # 用預設的UTF-8解碼
                # print('接收到的原始資料：', self.data_raw)
                if self.data[-3:-2] == 'R':
                    self.R_speed = int(self.data[:-3])
                else:
                    self.L_speed = int(self.data[:-3])


    def start_main_loop_thread(self):
        self.main_loop_thread = Thread(target=self._main_loop)
        self.main_loop_thread.start()



if __name__ == "__main__":
    stratery = FS_i6()
    stratery.device_setting()
    stratery.start_main_loop_thread()

    while True:
        stratery.get_data()

