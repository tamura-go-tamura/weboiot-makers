# coding: utf-8
## @package 3axis
#  This is a library for the FaBo 3AXIS I2C Brick.
#
#  http://fabo.io/201.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBo3Axis_ADXL345
import time
import sys
import motor


def Sensing_acceleration():
    #諸初期化
    adxl345 = FaBo3Axis_ADXL345.ADXL345()
    open_ = 0
    close = 0
    y_p = 100
    diff_y = 0

    try:
        #door oprn and close ,door stop,  exit the loop
        while diff_y == 0 and open_*close == 0:
            axes = adxl345.read()

            x_n = axes["x"]
            y_n = axes["y"]

            #一つ前のyの加速度との差を計算
            diff_y = y_n - y_p

            if x_n + y_n >= 10:#detect door open
                open_ = 1
                print("opening!")

            if x_n + y_n <= -10:#detect door close
                close = 1
                print("closing!")

            
            y_p = axes["y"]

            print("x = " , (axes['x']))
            print("y = " , (axes['y']))
            print("z = " , (axes['z']))
            print()

            time.sleep(0.25)

        #here start motor_function 
        print("motor start!")
        motor.motor("close")


    except KeyboardInterrupt:
        sys.exit()