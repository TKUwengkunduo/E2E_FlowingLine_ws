import time

T = time.localtime(time.time())
print(time.strftime('%Y_%m_%d__%H_%M',T))

data_file = open('./'+str(time.strftime('%Y_%m_%d__%H_%M',T))+'.txt', 'w')

start_time = time.time()
while True:
    now_time = time.time()-start_time
    now_time = str(round(now_time, 2))
    now_time = now_time.replace('.','_')
    print(now_time)

    data_file.write(now_time)


