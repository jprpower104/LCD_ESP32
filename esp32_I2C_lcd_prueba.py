from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp32_i2c_lcd import I2cLcd

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.putstr("Esto Trabaja!\nAja!!!")
    sleep_ms(3000)
    lcd.clear()
    count = 0
    while 1:
        lcd.move_to(0, 0)
        lcd.putstr("1er. linea")
        sleep_ms(500)
        lcd.move_to(0, 1)
        lcd.putstr("2da. linea")
        sleep_ms(500)
        lcd.move_to(13, 1)
        lcd.putstr("%d"%count)
        lcd.move_to(13, 0)
        lcd.putstr("%d"%(100-count))
        lcd.putstr(" ")
        count +=1
        if count>=100:
            count=0

test_main()