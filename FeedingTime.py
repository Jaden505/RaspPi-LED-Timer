import RPi.GPIO as g
from gpiozero import Button
from threading import Thread
import time

pins = [0, 5, 6]

for p in pins:
    g.setmode(g.BCM)
    g.setwarnings(False)
    g.setup(p, g.OUT)
    g.output(p, False)

button = Button(18)

g.setmode(g.BCM)
g.setwarnings(False)
g.setup(5, g.OUT)
g.output(5, True)

def onOffLED(off, off2, on):
    g.setup(off, g.OUT)
    g.output(off, False)
    
    g.setup(off2, g.OUT)
    g.output(off2, False)
    
    g.setup(on, g.OUT)
    g.output(on, True)

def waitLEDChange():
    time.sleep(7200)
    onOffLED(5, 6, 0)
    
    time.sleep(10800)
    onOffLED(5, 0, 6)
    
while True:
    Thread(target=waitLEDChange).start()
    
    button.wait_for_press()
    
    print('Pressed')
    
    onOffLED(0, 6, 5)

    time.sleep(1)

