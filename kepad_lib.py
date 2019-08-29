import keypad
import time 
while True:
    key = keypad.getkey()
    if key!=None:
        print(key)
    time.sleep_ms(150)    