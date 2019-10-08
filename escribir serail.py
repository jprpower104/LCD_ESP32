from machine import UART
import time
from machine import ADC, Pin

def run():
    print('demo UART')
    adc = ADC(Pin(32))
    uart = UART(2, baudrate=9600)# tx2 rx2
    T = 0
    while 1:
        T = (24*(adc.read())*3.3/4096)
        uart.write('La temperatura es: '+ str(T) + ' C' + '\r\n')
        string=uart.read()
        print("%s"%(string))
        time.sleep(2)
run()