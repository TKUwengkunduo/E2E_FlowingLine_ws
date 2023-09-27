import time
import cv2
from threading import Thread



class WRITE_DATA():
    def __init__(self, proj_name='test'):
        self.proj_name = proj_name
        self.num = 0

        # time.sleep(0.5)
        self.data_file = open('./Data/' + proj_name + '.txt', 'w')
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()

    def recode(self, L_speed, R_speed):
        file_name = self.proj_name + '_' + str(self.num)
        print('write file : ' + file_name)
        self.data_file.write(file_name + '_' + str(L_speed) + '_' + str(R_speed) + '\n')
        for i in range(10):
            self.cap.read()
        ret, frame = self.cap.read()
        cv2.imwrite('./Data/' + self.proj_name + '/' + file_name + '.png', frame)
        cv2.imshow('img', frame)
        cv2.waitKey(1)
        self.num+=1


    # def _main_loop(self):
    #     while True:
    #         ret, self.frame = self.cap.read()
    #         cv2.imshow('img', self.frame)
    #         cv2.waitKey(1)

    # def start_main_loop_thread(self):
    #     self.main_loop_thread = Thread(target=self._main_loop)
    #     self.main_loop_thread.start()




if __name__=='__main__':
    recorder = WRITE_DATA('test', 1)
    # recorder.start_main_loop_thread()

    recorder.recode()
