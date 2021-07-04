''' This code is used to blink the inbuild LED Pin-25 on the Raspberry Pi Pico'''


from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

