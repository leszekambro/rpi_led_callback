#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# GPIO 23 & 24 - inputs

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# threaded callback function
# zostanie to uruchomione w innym watku po wykryciu okreslonego zdarzenia
def my_callback(channel):
    print("Wykryto zbocze opadajace na porcie 24")
    print("w glownym watku dalej czekamy na przycisk na porcie 23\n")


print("***")
print("pkt test 1")
print("***")

raw_input("Wcisnij enter jak bedziesz gotowy \n>")

GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callback)


try:
    print("Czekam na przycisk na porcie 23...")
    GPIO.wait_for_edge(23, GPIO.FALLING)
    print("Przycisk na porcie 23 wciśnięty. Koniec programu.")

except KeyboardInterrupt:
    print("\nProgram przerwany przez użytkownika.")

finally:
    GPIO.cleanup()
    print("GPIO posprzątane")
