from microbit import *

lights = []

for i in range(20):
    lights.append(display.read_light_level())
    sleep(500)

average = sum(lights)/len(lights)

temp = temperature()

message = "Avg Light: " + str(average) + " Temp: " + str(temp)
display.scroll(message)

if average > 100:
    display.scroll('Day')
else:
    display.scroll('Night')