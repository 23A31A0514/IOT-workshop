import machine
import utime
rpin=machine.Pin(2,machine.Pin.OUT)
gpin=machine.Pin(4,machine.Pin.OUT)
bpin=machine.Pin(14 ,machine.Pin.OUT)
def setcolor(r,g,b):
    rpin.value(r)
    gpin.value(g)
    bpin.value(b)
while (True):
      x=input("Enter which light to ON likki:RED\nyashu:Green\n harsha:Blue\nsowji:Pink\ndeepu:Cyan\nsrija:Yellow\ntanuja:null\nimmu:White")
      if x=='likki':
          setcolor(0,1,1)
          print("RED led is ON")
          utime.sleep(1)
      elif x=='yashu':
          setcolor(1,0,1)
          print("Green led is ON")
          utime.sleep(1)
      elif x=='harsha':
          setcolor(1,1,0)
          print("Blue led is ON")
          utime.sleep(1)
      elif x=='sowji':
          setcolor(0,1,0)
          print("Pink led is ON")
          utime.sleep(1)
      elif x=='deepu':
          setcolor(1,0,0)
          print("Cyan led is ON")
          utime.sleep(1)
      elif x=='srija':
          setcolor(1,1,0)
          print("Yellow led is ON")
          utime.sleep(1)
      elif x=='tanuja':
          setcolor(1,1,0)
          print("No led is ON")
          utime.sleep(1)
      elif x=='immu':
          setcolor(1,1,0)
          print("White led is ON")
          utime.sleep(1)
      else:
          print("Enter valid value:")
      utime.sleep(5)
          
          

