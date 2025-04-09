import time
import RPi.GPIO as GPIO

BUTTON1_PIN = 5
BUTTON2_PIN = 18
LED_PIN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

button1_pressed = False
button2_pressed = False

# Callback for button 1
def button1_callback(channel):
    global button1_pressed
    button1_pressed = GPIO.input(BUTTON1_PIN) == GPIO.LOW
    print("B1","wcisniety" if button1_pressed else "puszczony")
    check_led_state()

# Callback for button 2
def button2_callback(channel):
    global button2_pressed
    print("B2")
    button2_pressed = GPIO.input(BUTTON2_PIN) == GPIO.LOW
    print("B2","wcisniety" if button2_pressed else "puszczony")
    check_led_state()

# Check if both buttons are pressed to light the LED
def check_led_state():
    if button1_pressed and button2_pressed:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("Led ON")
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        print("Led OFF")


# Event detect
GPIO.add_event_detect(BUTTON1_PIN, GPIO.BOTH, callback=button1_callback, bouncetime=50)
GPIO.add_event_detect(BUTTON2_PIN, GPIO.BOTH, callback=button2_callback,bouncetime=50)


try:
    while True:
        time.sleep(1)
        print("program on")
        #check_led_state()
        print(button1_pressed)
        print(button2_pressed)
        #GPIO.input(BUTTON2_PIN)
except KeyboardInterrupt:
    print("Exiting program")
finally:
    GPIO.cleanup()
