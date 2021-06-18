from Moteur import Moteur
from ScannerThread import ScannerThread
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

class Scanner ():
    def __init__(self):
        self.moteur_a = Moteur()

        self.moteur_a.vitesse(100)

        self.nb_aller_retour = 6 #Nombre d'aller retour
        self.allere_retour_done = 0

        #On a donc un tableau de donnée de n_x * n_y spectres

        #Toute ces variables sont relatives a l'affichage sur l'interface web
        self.x_aff_barre = 15

        self.y_aff_support = 20

        self.warning_pin = False

        self.need_user_input = True

        self.y_state_input = False #tells us if the user moves on y axis the spectrometer
        #If True we can do the scan

        #Initilisation pin 
        self.pin_17 = 17 #Le plus proche du moteur
        self.pin_27 = 27 

        #Setup gpio
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
        GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)


    def launch(self):
        my_thread = ScannerThread(self)
        my_thread.start()