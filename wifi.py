import network
import socket
import machine

# === 1️⃣ Configure LED pin ===
# Change pin number if using external LED:
led = machine.Pin(2, machine.Pin.OUT)  # ESP32/ESP8266 built-in LED

# === 2️⃣ Create Access Point ===
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='yashu', password='1234567890')  # password 8+ chars required
print('Access Point created')
print('Network config:', ap.ifconfig())

# Wait until AP is active
while ap.active() == False:
    pass

print('AP Active. Connect to:', ap.config('essid'))
print('Then open browser at http://' + ap.ifconfig()[0])

# === 3️⃣ Simple Web Page ===
def web_page():
    led_state = "ON" if led.value() == 1 else "OFF"
    html = f"""<!DOCTYPE html>
<html>
<head>
<title>Huebits LED Control</title>
<style>
body {{
  font-family: Arial; text-align: center; margin-top: 40px;
  background-color: #f2f2f2;
}}
button {{
  font-size: 20px; padding: 10px 20px; margin: 10px;
}}
</style>
</head>
<body>
<h2>ESP Access Point LED Control</h2>
<p>LED is currently <strong>{led_state}</strong></p>
<a href="/?led=on"><button>Turn ON</button></a>
<a href="/?led=off"><button>Turn OFF</button></a>
</body>
</html>
"""
    return html

# === 4️⃣ Start Socket Web Server ===
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('Web server running on http://', ap.ifconfig()[0])

# === 5️⃣ Main Loop: Serve requests ===
while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024)
    request = str(request)
    print('Request:', request)

    # Parse query
    if '/?led=on' in request:
        print("LED ON command")
        led.value(1)
    if '/?led=off' in request:
        print("LED OFF command")
        led.value(0)

    # Send web page
    response = web_page()
    cl.send('HTTP/1.1 200 OK\n')
    cl.send('Content-Type: text/html\n')
    cl.send('Connection: close\n\n')
    cl.sendall(response)
    cl.close()
