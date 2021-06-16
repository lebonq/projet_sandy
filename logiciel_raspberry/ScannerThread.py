from Moteur import Moteur
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Documentation about sleep with linux and windows kernel https://stackoverflow.com/questions/1133857/how-accurate-is-pythons-time-sleep
import threading

class ScannerThread (threading.Thread):
    def __init__(self, scanner):
        self.scanner_obj = scanner
        threading.Thread.__init__ (self, target=self.run)


    def run(self):
        current_pin_offset = 0

        if(self.scanner_obj.allere_retour_done%2 != 0):
            current_pin_offset = 10
            self.scanner_obj.moteur_a.sens(False)
        else:
            self.scanner_obj.moteur_a.sens(True)

        while(GPIO.input(int(17+current_pin_offset)) == GPIO.LOW):
            if(GPIO.input(27-current_pin_offset) == GPIO.HIGH):
                self.scanner_obj.warning_pin = True
            else:
                self.scanner_obj.warning_pin = False

        self.scanner_obj.need_user_input = True
        self.scanner_obj.allere_retour_done += 1
        self.scanner_obj.moteur_a.marche(False)

        if(self.scanner_obj.allere_retour_done == self.scanner_obj.nb_aller_retour):#en fois tout les aller retours fait on remte a 0
            self.scanner_obj.allere_retour_done = 0
            
            
            

            
            