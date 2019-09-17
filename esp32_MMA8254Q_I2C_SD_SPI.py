from machine import I2C, Pin, SPI
from time import time, sleep_ms
import math
from sdcard import SDCard
import os

MMA8254Q_ADDR=0x1D

#classmachine.SDCard(slot=1, width=1, cd=None, wp=None, sck=None, miso=None, mosi=None, cs=None)
#SDCard(slot=1, width=1, cd=None, wp=None, sck=None, miso=None, mosi=None, cs=None)
Acelx = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
Acelx.writeto_mem(MMA8254Q_ADDR,0x2A, b'\x00')
Acelx.writeto_mem(MMA8254Q_ADDR,0x2A, b'\x01')
Acelx.writeto_mem(MMA8254Q_ADDR,0x0E, b'\x00')
Acelx.writeto_mem(MMA8254Q_ADDR,0x0F, b'\x30')


SD1 = SPI(1, 1000000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
sleep_ms(500)
SD1.init()  # Ensure right baudrate
sd = SDCard(SD1,Pin(05)) # Compatible with PCB
vfs = os.VfsFat(sd)
os.mount(vfs,'/fc')


in_xAcc1=0
in_yAcc1=0
in_zAcc1=0

xAcc1=0
yAcc1=0
zAcc1=0

in_in_xAcc1=0
in_in_yAcc1=0
in_in_zAcc1=0

current_time_a=0
current_time_b=0
n=1
while True:
    current_time_a = time()
    data = Acelx.readfrom_mem(MMA8254Q_ADDR, 0x00, 7)
    # Convert the data
    xAccl = (data[1] *256 + data[2])/16.0 
    if xAccl >= 2048 :
        xAccl -= 4096

    yAccl = (data[3]*256 + data[4]) / 16.0
    if yAccl >= 2048 :
        yAccl -= 4096

    zAccl = (data[5]*256 + data[6]) / 16.0
    if zAccl >= 2048 :
        zAccl -= 4096
    

    xAccl = xAccl/2048.0
    yAccl = yAccl/2048.0
    zAccl = zAccl/2048.0
    current_time_b = time()
    dt  = current_time_b-current_time_a
    
    in_xAcc1 += xAccl*dt
    in_yAcc1 += yAccl*dt
    in_zAcc1 += zAccl*dt
    
    in_in_xAcc1 += in_xAcc1*dt
    in_in_yAcc1 += in_yAcc1*dt
    in_in_zAcc1 += in_zAcc1*dt
    
    # Output data to screen
    print("Acceleration in X-Axis : %1.5f" %(in_in_xAcc1))
    print("Acceleration in Y-Axis : %1.5f" %(in_in_yAcc1))
    print("Acceleration in Z-Axis : %1.5f" %(in_in_zAcc1))
    print("                           ")
    print("                           ")
    print("                           ")
    f = open('accel.txt', 'a')
    f.write('\n' + str(in_in_xAcc1) + ',' + str(in_in_yAcc1) + ',' + str(in_in_zAcc1) + ',')
    f.close()