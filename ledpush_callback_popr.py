#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button GPIO23
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button GPI4

GPIO.setup(18, GPIO.OUT)  # LED GPIO18

global freq
freq = 1


def my_callback1(channel):
    global freq
    freq = 0.5
    print("freq 0.5")


def my_callback2(channel):
    global freq
    freq = 2
    print("freq 2")


GPIO.add_event_detect(23, GPIO.RISING)
GPIO.add_event_detect(24, GPIO.RISING)
GPIO.add_event_callback(23, my_callback1)
GPIO.add_event_callback(24, my_callback2)

raw_input("Nacisnik enter jak bedziesz gotowy\n>")
try:
    while True:
        GPIO.output(18, True)
        print("Led ON: ", freq)
        time.sleep(freq)
        GPIO.output(18, False)
        print("Led OFF: ", freq)
        time.sleep(freq)

except KeyboardInterrupt:
    print("\nZatrzymano program.")
except Exception as e:
    print("Blad:", e)
finally:
    print("Koniec programu.")
    GPIO.cleanup()