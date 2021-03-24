import time
from pixels import Pixels, pixels
from alexa_led_pattern import AlexaLedPattern
from google_home_led_pattern import GoogleHomeLedPattern

if __name__ == '__main__':

    pixels.pattern = GoogleHomeLedPattern(show=pixels.show)
    
    while True:

        try:
            data =[255,0,0] * 12
            pixels.show(data)
            time.sleep(2)
            data =[0,255,0] * 12
            pixels.show(data)
            time.sleep(2)
            data =[0,0,255] * 12
            pixels.show(data)
            time.sleep(2)
            data =[255,0,255] * 12
            pixels.show(data)
            time.sleep(2)
            
            data =[0,0,0] * 12
            pixels.show(data)
            time.sleep(2)
            pixels.show(data)
            
            
        except KeyboardInterrupt:
            break


    pixels.off()
    time.sleep(1)
