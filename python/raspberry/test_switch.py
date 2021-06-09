import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
from Moteur import *

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

my_motor = Moteur()

while True: # Run forever
    if GPIO.input(17) == GPIO.HIGH:
        #print("Button was pushed!")
        if(my_motor.marche_state == False):
            my_motor.marche(True)
    else:
        #print("Button was not pushed!")
        if(my_motor.marche_state == True):
            my_motor.marche(False)