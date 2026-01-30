from machine import Pin
import utime
button=Pin(2,Pin.IN)
rpin=Pin(4,Pin.OUT)
buzzer=Pin(18,Pin.OUT)
while(True):
    if button.value()==0:
        print("Button press")
        rpin.on()
        buzzer.on()
        print("Buttonn State:",button.value())
    else:
        print("Not pressed")
        rpin.off()
        buzzer.off()
    utime.sleep(0.3)
    
