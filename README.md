# E2E_FlowingLine_ws

## Docker Environment(If you already have an ubuntu environment, oyu can skip this step)
###### 
```js
mkdir weng_ws
cd weng_ws
git clone https://github.com/TKUwengkunduo/ubuntu_docker.git
cd ubuntu_docker/ub22.04_ros2_cu117_cudnn/docker
./build.sh
./run.sh
```

## Download
```js
git clone https://github.com/TKUwengkunduo/E2E_FlowingLine_ws.git
```

## Install Dynamixel SDK
```js
cd E2E_FlowingLine_ws/src/DynamixelSDK/python
sudo python3 setup.py install
```

## Usb access
```js
sudo chmod 777 /dev/ttyUSB0
sudo chmod 777 /dev/ttyUSB1
```

## Use
```js
cd ../..
python3 main
```
