import machine
import utime

temp_sensor = machine.ADC(4) #internal temperature sensor
conversion_factor = 3.3 / (65535)

while True:
    reading = temp_sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0706)/0.001721
    print("Current temperature : ", temperature)
    utime.sleep(2)
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
 # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per detemperature = 27 - (reading - 0.706)/0.001721


