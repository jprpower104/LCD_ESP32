import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('JULIANPELAEZ', '16929198') 
    while not wlan.isconnected():
        print('.')
print('network config:', wlan.ifconfig())
    
