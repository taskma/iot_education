import blynklib
import random
import time
#global blynk

BLYNK_AUTH = ''
blynk = blynklib.Blynk(BLYNK_AUTH)
tempPin = 1 
humidityPin = 2

def main():
    value = 1
    while True:
        value = value + 1
        if value % 30 == 0:
            #print(value)
            temp = random.randint(0,50)
            blynk.virtual_write(tempPin, str(temp))
            hum = random.randint(0, 50)
            blynk.virtual_write(humidityPin, str(hum))
        blynk.run()

@blynk.handle_event('write V*')
def write_handler(pin, value):
    print("pin" + str(pin))
    button_state = value
    print(button_state)

if __name__ == "__main__": main()
