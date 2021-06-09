import RPi.GPIO as GPIO          
from time import sleep

class Moteur: 

    """ marche boolean true or false
        sens boolean true -> forward false -> backward
        vitesse float
         """
    def __init__(self):
        print("Setup motor")
        self.marche_state = False
        self.sens_state = True
        self.vitesse_value = 50

        #Definition des pins
        self.in1 = 24
        self.in2 = 23
        self.ena = 25

        #Setup des pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.ena,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        self.pwm =GPIO.PWM(self.ena,100)
        self.pwm.start(self.vitesse_value)

    #state boolean
    def marche(self, state):
        self.marche_state = state
        if(self.marche_state == True):
            if(self.sens_state == True):
                print("Run forward")
                GPIO.output(self.in1,GPIO.HIGH)
                GPIO.output(self.in2,GPIO.LOW)
            else:
                print("Run backward")
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.HIGH)
        else:
            print("Stop")
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.LOW)

    # permet de changer la vitesse
    def vitesse(self,vitesse):
        self.vitesse_value = vitesse
        print("Vitesse set at ", vitesse)
        self.pwm.ChangeDutyCycle(vitesse)
    
    #Permet de choisir le sens
    def sens(self, state):
        self.sens_state = state
        if(self.sens_state == True):
            print("Set to forward")
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
        else:
            print("Set to backward")
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)

    #Il faut obligatoirement appeler cette fonction a la fin du programme sinon plus rien ne marche
    def exit(self):
        GPIO.cleanup()
        SystemExit.code(1)