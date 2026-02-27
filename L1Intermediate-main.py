from microbit import *
display.show(Image.HAPPY)
while True:
    if button_a.is_pressed():
        display.scroll('Temp Check!')
    temp = temperature()
    if temp > 25:
        display.show(Image.HAPPY)
    elif 18 <= temp <= 25:
        display.show(Image.MEH)
    else:
        display.show(Image.SAD)