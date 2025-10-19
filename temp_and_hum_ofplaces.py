import machine
import network
import urequests
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...\n')
        wlan.connect('Resnie', 'Ressie@1711')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
do_connect()
while True:
    City=input("Enter the City name: ")
    url="https://api.openweathermap.org/data/2.5/weather?q=%s&appid=53c4e3bbd5025f136907d86caf58d7e2"%City
    print(url)
    try:
        r=urequests.get(url)
        s=r.json()
        print(s,"\n")  
        t=s["main"]["temp"]-273.15
        print("temperature: ",t,'°C') 
        h=s["main"]["humidity"]
        print("humidity",h,'%')
        p=s["main"]["pressure"]
        print("pressure",p,'hPa')
        r.close()
    except Exception as e:
        print("Error Fetching Weather Data", e)


