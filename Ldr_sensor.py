from machine import ADC,Pin
import utime
ldr=ADC(Pin(33))
led=Pin(2,Pin.OUT)
buzzer=Pin(5,Pin.OUT)
while True:
    ldr_value=ldr.read()
    ldr_voltage=(ldr_value*3.3)/4095.0
    lightIntensity=100.0-(ldr_voltage/3.3)*100.0
    print("Light Intensity",lightIntensity)
    if(lightIntensity<=40):
        led.on()
        buzzer.on()
    else:
        led.off()
        buzzer.off()
    utime.sleep(1)