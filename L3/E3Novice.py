from microbit import *

def set_leds(brightness):
    for i in range(5):
        for j in range(5):
            display.set_pixel(i, j, brightness)

while True:
    for i in range(2):
        set_leds(9)
        sleep(250)
        display.clear()
        sleep(250)
    
    sleep(500)
    
    for i in range(10):
        set_leds(i)
        sleep(75)
    
    for i in range(9, -1, -1):
        set_leds(i)
        sleep(75)
    
    sleep(500)