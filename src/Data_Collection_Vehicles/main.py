import motor_controller
import communication

motor = motor_controller.MOTOR_2_WHEEL_MODE()
motor.usb_initialization(usb='/dev/ttyUSB0', baudrate=1000000, protocol_version=2.0)
motor.motor_initialization(m1_id=1, m2_id=2)
motor.ping()


stratery = communication.FS_i6()
stratery.device_initialization(usb='/dev/ttyUSB1', baudrate=115200)
stratery.start_main_loop_thread()

while True:
    R_speed, L_speed = stratery.get_data()
    # print(R_speed, ' | ', L_speed)

    motor.setSpeed(L_speed, R_speed)