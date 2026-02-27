from microbit import *
#show a smiley face when the board starts
#endless while loop
while True:
    display.show(Image.HAPPY)
#scroll your name if button A is pressed
    if button_a.was_pressed():
        display.scroll("Brian")