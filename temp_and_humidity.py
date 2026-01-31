import machine
import dht
import utime
dht11=dht.DHT11(machine.Pin(2))
while True:
    dht11.measure()
    t=dht11.temperature()
    h=dht11.humidity()
    print('temperature:',t, '°C','humidity:',h,'%')
    utime.sleep(2)
