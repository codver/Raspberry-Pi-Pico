'''to control the blinking of an LED based on the input given to the push button switch
LED is connected to the GPIO 15, PUSHBUTTON to GPIO 14
PIN 38 : GROUND, PIN 36 : 3.3V OUT'''

from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.toggle()
        time.sleep(0.5)


	    



















'''from machine import Pin, Timer
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
timer = Timer()

def blink(timer):
    if button.value():
        led.toggle()
        time.sleep(0.5)
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)'''
'''while True:
    if button.value():
        led.toggle()
        time.sleep(0.5)
         '''
         
	   
   
