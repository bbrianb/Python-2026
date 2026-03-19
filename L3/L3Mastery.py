from microbit import *

lights = []
frozen = False
while True:
    current = display.read_light_level()
    lights.append(current)

    if len(lights) > 10:
        lights.pop(0)

    average = sum(lights)/len(lights)
    min_light = min(lights)
    max_light = max(lights)

    data = 'Current: ' + str(current)+ ' Average: ' + str(average) + ' Min: ' + str(min_light) + ' Max: ' + str(max_light) + '\r\n'
    uart.write(data)

    if button_a.was_pressed():
        frozen = not frozen

    if button_b.was_pressed():
        output = 'Min: ' + str(min_light) + ' Max: ' + max_light + 'Average: ' + average
        display.scroll(output)

    if (not frozen):
        display.clear()
        if max_light > 0:
            leds = int(lights[-1] / max_light * 25)
            for i in range(leds):
                display.set_pixel(i % 5, i // 5, 9)

    sleep(110)