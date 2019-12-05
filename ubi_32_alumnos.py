'''
This Example sends harcoded data to Ubidots using the request HTTP
library.
Please install the library using pip install requests
Made by Jose García @https://github.com/jotathebest/
'''
import urequests as requests 
import dht
import time
import network
import machine as m
import socket
import time
'''
global variables
'''
ENDPOINT = "industrial.api.ubidots.com"
DEVICE_LABEL = "esp32"
VARIABLE_LABEL1 = "temperature"
VARIABLE_LABEL2 = "humedad"
VARIABLE_LABEL3 = "suiche"
TOKEN = "BBFF-Wo1hpM74XXXXnTQ9Xxxxxx82bTxxk"
DELAY = 100  # Delay in seconds
sensor = dht.DHT11(m.Pin(13,m.Pin.IN,m.Pin.PULL_UP))
led = m.Pin(2,m.Pin.OUT)
def connect():
#    SSID = "WIFI-ITM"
#    PASSWORD = ""
    SSID = "JULIANPELAEZ"
    PASSWORD = "16929198"
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID,PASSWORD)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def get_var(url=ENDPOINT, device=DEVICE_LABEL, variable=VARIABLE_LABEL3,
            token=TOKEN):
    try:
        url = "http://{}/api/v1.6/devices/{}/{}/?page_size=2".format(url,
                                                        device,
                                                        variable)

        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400

        while status_code >= 400 and attempts < 5:
            print("[INFO] Retrieving data, attempt number: {}".format(attempts))
            req = requests.get(url=url, headers=headers)
            status_code = req.status_code
            attempts += 1
            time.sleep_ms(DELAY)

        #print("[INFO] Results:")
        #print(req.text)
        val=int(req.text[req.text.find('"value": ')+len('"value": ')])
        return val
    except Exception as e:
        print("[ERROR] Error getting, details: {}".format(e))

def post_var(payload, url=ENDPOINT, device=DEVICE_LABEL, token=TOKEN):
    try:
        url = "http://{}/api/v1.6/devices/{}".format(url, device)
        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400

        while status_code >= 400 and attempts < 5:
            print("[INFO] Sending data, attempt number: {}".format(attempts))
            req = requests.post(url=url, headers=headers,
                                json=payload)
            status_code = req.status_code
            attempts += 1
            time.sleep_ms(DELAY)

        #print("[INFO] Results:")
        #print(req.text)
        
    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))

def main():
    connect()
    #time.sleep(DELAY)
    valLed=0
    while True:
        # Simulates sensor values
        sensor.measure()
        time.sleep_ms(250)
        sensor_value1 = sensor.temperature() # eg. 23.6 (°C)
        sensor_value2 = sensor.humidity()    # eg. 41.3 (% RH)
        print("La temperatura: {} ºC y la humedad es: {} % y el suiche es: {}".format(sensor_value1,sensor_value2, valLed))
        # Builds Payload and topíc
        payload = {VARIABLE_LABEL1: sensor_value1, VARIABLE_LABEL2: sensor_value2}
        #             "temperatura: 75,            humedad: 90" 
        # Sends data
        post_var(payload)
        valLed=get_var()
        led.value(valLed)
        time.sleep_ms(DELAY)


main()