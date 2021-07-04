from machine import Pin, Timer
led = Pin(15, Pin.OUT)
timer = Timer()

#function
def blink(timer):
    led.toggle()
#timer.init(fre=2.5, mode=Timer.PERIODIC)
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)