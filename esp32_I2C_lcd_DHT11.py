from time import sleep_ms
from machine import I2C, Pin
from esp32_i2c_lcd import I2cLcd
import dht

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27
d = dht.DHT11(Pin(4))

def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
    lcd = I2cLcd(i2c,DEFAULT_I2C_ADDR,2,16)
    lcd.putstr("Esto Trabaja!\nAja!!!")
    sleep_ms(500)
    lcd.clear()
    while True:
        d.measure()
        temp = d.temperature()
        humd = d.humidity()
        print(temp)
        print(humd)
        print(type(temp))
        lcd.move_to(0, 0)
        lcd.putstr("Temp = ")
        lcd.move_to(8, 0)
        lcd.putstr(str(temp))
        lcd.move_to(0, 1)
        lcd.putstr("Humd = ")
        lcd.move_to(8, 1)
        lcd.putstr(str(humd))
        sleep_ms(1000)
        
test_main()