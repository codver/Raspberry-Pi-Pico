''' External LED was connected to Pin 15 of the Raspberry Pi Pico'''
''' A resistor of 100 ohms was used'''


from machine import Pin, Timer
led = Pin(15, Pin.OUT)
timer = Timer()

#function
def blink(timer):
    led.toggle()
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
