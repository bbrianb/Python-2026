import log
from microbit import *
import time

log.set_labels('light', 'temperature')
while not button_a.is_pressed():
    pass
while not button_b.is_pressed():
    display.show(Image.HAPPY)
    log.add({
        'light': display.read_light_level(),
        'temperature': temperature()
    })
    time.sleep(0.5)