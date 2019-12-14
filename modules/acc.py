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

from .AXIS345 import ADXL345
import time
import sys
from . import motor


def Sensing_acceleration():
    #諸初期化
    adxl345 = ADXL345()
    open_ = 1
    close = 1
    y_p = 100
    diff_y = 100

    try:
        #door oprn and close ,door stop,  exit the loop
        while diff_y+open_+close != 0 :
            print(diff_y+open_+close != 0 )
            axes = adxl345.read()

            x_n = axes["x"]
            y_n = axes["y"]

            
            if x_n + y_n >= 30:#detect door open
                open_ = 0
                print("opening!")

            if x_n + y_n <= -30:#detect door close
                close = 0
                print("closing!")

            #一つ前のyの加速度との差を計算
            diff_y = y_n - y_p
            print(diff_y)

            y_p = y_n

            print("x = " , (axes['x']))
            print("y = " , (axes['y']))
            print("z = " , (axes['z']))
            print("open_",open_)
            print("close",close)
            print()

            time.sleep(0.50)

        #here start motor_function 
        print("diff_y",diff_y,"  open",open_,"  close",close)
        print("motor start!")
        motor.motor("close")


    except KeyboardInterrupt:
        sys.exit()