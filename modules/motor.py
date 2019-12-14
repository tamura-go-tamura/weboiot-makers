import Fabo_PCA9685
import time
import pkg_resources
SMBUS='smbus'
for dist in pkg_resources.working_set:
    #print(dist.project_name, dist.version)
    if dist.project_name == 'smbus':
        break
    if dist.project_name == 'smbus2':
        SMBUS='smbus2'
        break
if SMBUS == 'smbus':
    import smbus
elif SMBUS == 'smbus2':
    import smbus2 as smbus

def motor(order):
    for i in range(6):
        BUSNUM=1
        SERVO_HZ=50
        # set value
        if order=="open":
            INITIAL_VALUE=120
            bus = smbus.SMBus(BUSNUM)
            PCA9685 = Fabo_PCA9685.PCA9685(bus,INITIAL_VALUE)
            PCA9685.set_hz(SERVO_HZ)
            value = 540

        if order=="close":
            INITIAL_VALUE=330
            bus = smbus.SMBus(BUSNUM)
            PCA9685 = Fabo_PCA9685.PCA9685(bus,INITIAL_VALUE)
            PCA9685.set_hz(SERVO_HZ)
            value = 120
        
        channel = 0 # PWM0
        PCA9685.set_channel_value(channel,value)

        # get value(Get chip register's value. This value may not be equal to the actual position.)
        #value = PCA9685.get_channel_value(channel)
        #print(value)
