from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp32_i2c_lcd import I2cLcd
import keypad
import time 

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.clear()
    count = 0
    while 1:
#---------------------------------------------------------------------------------------------------------------
# Lee el primer valor
        time.sleep_ms(100)  
        lcd.move_to(0, 0)
        lcd.putstr("1er. valor")
        c1=0
        num1=' '
        key=None
        while True:
            lcd.move_to(c1, 1)
            lcd.putstr("              ")
            key = keypad.getkey_(timeout=500)
            if key!=None and key!='D' and key!='A' and key!='B' and key!='C' and key!='*' and key!='#':
                lcd.move_to(c1, 1)
                lcd.putstr(key)
                num1+=key
                c1+=1
            if key == 'D':
                break
            time.sleep_ms(250)    
#---------------------------------------------------------------------------------------------------------------
# Lee el segundo valor
        time.sleep_ms(100)  
        lcd.move_to(0, 0)
        lcd.putstr("2do. valor")
        c1=0
        num2=' '
        key=None
        while True:
            lcd.move_to(c1, 1)
            lcd.putstr("              ")
            key = keypad.getkey_(timeout=500)
            if key!=None and key!='D' and key!='A' and key!='B' and key!='C' and key!='*' and key!='#':
                lcd.move_to(c1, 1)
                lcd.putstr(key)
                num2+=key
                c1+=1
            if key == 'D':
                key=None
                break
            time.sleep_ms(250)    
#---------------------------------------------------------------------------------------------------------------
# Lee la operacion
        time.sleep_ms(100)  
        lcd.move_to(0, 0)
        lcd.putstr("             ")
        lcd.move_to(0, 0)
        lcd.putstr("Operacion")
        op='   '
        key=None
        while True:
            lcd.move_to(0, 1)
            lcd.putstr("             ")
            key = keypad.getkey_(timeout=500)
            if key!=None and key!='D' and key!='A' and key!='1' and key!='2' and key!='3' and key!='4' and key!='5' and key!='6' and key!='7' and key!='8' and key!='9' and key!='0':
                lcd.move_to(0, 1)
                op=key
                if op == '*':
                    lcd.putstr('*')
                    break
                if op == '#':
                    lcd.putstr('+')
                    break
                if op == 'A':
                    lcd.putstr('-')
                    break
                if op == 'B':
                    lcd.putstr('/')
                    break
                if op == 'C':
                    lcd.putstr('-')
                    break
            if key == 'D':
                break
            time.sleep_ms(250)    
#---------------------------------------------------------------------------------------------------------------
# Muestra resultado
        key=None
        while True:
            key = keypad.getkey_(timeout=500)
            if key!='D' and key!='A' and key!='B' and key!='C' and key!='1' and key!='2' and key!='3' and key!='4' and key!='5' and key!='6' and key!='7' and key!='8' and key!='9' and key!='0':
                lcd.move_to(0, 0)
                if op == '#':
                    lcd.putstr("la suma es:")
                    num=int(int(num1)+int(num2))
                    lcd.move_to(0, 1)
                    lcd.putstr(str(num))
                if op == '*':
                    lcd.putstr("la multi. es:")
                    num=int(int(num1)*int(num2))
                    lcd.move_to(0, 1)
                    lcd.putstr(str(num))
                if op == 'C':
                    lcd.putstr("la resta es:")
                    num=int(int(num1)-int(num2))
                    lcd.move_to(0, 1)
                    lcd.putstr(str(num))
                if op == 'B':
                    lcd.putstr("la div. es:")
                    num=int(num1)/int(num2)
                    lcd.move_to(0, 1)
                    lcd.putstr(str(num))
#                if op == 'C':
#                    lcd.putstr("la pot. es:")
#                    num=int(num1)**int(num2)
#                    lcd.move_to(0, 1)
#                    lcd.putstr(str(num))
            if key == 'D':
                break
            #time.sleep_ms(250)    

test_main()