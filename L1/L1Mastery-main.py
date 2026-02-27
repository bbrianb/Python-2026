from microbit import *
import time
lowest = display.read_light_level()
highest = display.read_light_level()
while True:
    light = display.read_light_level()
    display.scroll('L:')
    display.scroll(light)
    if light > 180:
        display.show(Image.HAPPY)
    elif 100 <= light <= 180:
        display.show(Image.MEH)
    else:
        display.show(Image.SAD)
    highest = max(highest, light)
    lowest = min(lowest, light)
    if button_b.is_pressed():
        display.scroll('Min:')
        display.scroll(lowest)
        display.scroll('Max:')
        display.scroll(highest)
    time.sleep(2)