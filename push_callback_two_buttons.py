import time
import RPi.GPIO as GPIO

BUTTON1_PIN = 17
BUTTON2_PIN = 27
LED_PIN = 22

# State variables
button1_pressed = False
button2_pressed = False

# Callback for button 1
def button1_callback(channel):
    global button1_pressed
    button1_pressed = GPIO.input(BUTTON1_PIN)
    check_led_state()

# Callback for button 2
def button2_callback(channel):
    global button2_pressed
    button2_pressed = GPIO.input(BUTTON2_PIN)
    check_led_state()

# Check if both buttons are pressed to light the LED
def check_led_state():
    if button1_pressed and button2_pressed:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

# Event detect
GPIO.add_event_detect(BUTTON1_PIN, GPIO.BOTH, callback=button1_callback, bouncetime=200)
GPIO.add_event_detect(BUTTON2_PIN, GPIO.BOTH, callback=button2_callback, bouncetime=200)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting program")
finally:
    GPIO.cleanup()
