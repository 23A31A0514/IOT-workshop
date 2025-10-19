import machine
import utime
led=machine.Pin(2,machine.Pin.OUT)
led1=machine.Pin(4,machine.Pin.OUT)
while(True):
    led.on()
    print("Red is ON")
    utime.sleep(1)
    led.off()
    print("Red is OFF")
    utime.sleep(1)
    led1.on()
    print("Yellow is ON")
    utime.sleep(1)
    led1.off()
    print("Yellow is OFF")
    utime.sleep(1)