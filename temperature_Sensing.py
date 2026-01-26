import network
import urequests
import dht
from machine import ADC, Pin
import utime
dht11 = dht.DHT11(Pin(13))
ldr = ADC(Pin(34))
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('fountain','12345678')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
do_connect()
while True:
    dht11.measure()
    t = dht11.temperature()
    h = dht11.humidity()
    ldr_value = ldr.read()
    ldr_voltage = (ldr_value * 3.3) / 4095.0;
    lightIntensity = 100.0 - (ldr_voltage / 3.3) * 100.0
    print(f"ldr: {lightIntensity:.2f} %")
    print('temperature : ',t, '°C', 'humidity :', h,'%')
    url="https://api.thingspeak.com/update?api_key=73VLLUHBBLEPLIUQ&field1=%d&field2=%d&field3=%d"%(t,h,lightIntensity)
    print(url)
    r=urequests.get(url)
    r.close()
    utime.sleep(1)
