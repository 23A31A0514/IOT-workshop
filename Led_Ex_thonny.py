import machine
import utime
led=machine.Pin(2,machine.Pin.OUT)
while(True):
    led.on()
    utime.sleep(1)
    led.off()
    utime.sleep(1)