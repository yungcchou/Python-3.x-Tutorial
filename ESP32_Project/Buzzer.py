from machine import Pin, PWM
import time

buzzer = PWM(Pin(0, Pin.OUT), freq=440, duty=100)
buzzer.duty(100)
buzzer.freq(500)
time.sleep(1)
buzzer.duty(0)
time.sleep(3)
buzzer.duty(512)
buzzer.freq(899)
time.sleep(1)
buzzer.duty(512)
buzzer.freq(525)
time.sleep(1)
buzzer.duty(0)
time.sleep(1)

print("buzzer done!")