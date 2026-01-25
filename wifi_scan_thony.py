import network
wlan=network.WLAN(network.STA_IF)
wlan.active(True)
networks=wlan.scan()
print("Found networks:")
for net in networks:
    ssid=net[0].decode('utf-8')
    bssid=':'.join('%02x' % b for b in net[1])
    channel=net[2]
    rssi=net[3]
    authmode=net[4]
    hidden=net[5]
    print(f"SSID: {ssid}, BSSID: {bssid}, CH: {channel},  RSSI: {rssi}, AUTH: {authmode}, Hidden: {hidden}")
