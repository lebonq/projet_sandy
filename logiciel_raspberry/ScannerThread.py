import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import datetime;
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

        #4min30 de 15 a 380
        ts1 = datetime.datetime.now().timestamp()
        while(GPIO.input(int(17+current_pin_offset)) == GPIO.LOW):
            
            if(GPIO.input(27-current_pin_offset) == GPIO.HIGH):
                self.scanner_obj.warning_pin = True
            else:
                self.scanner_obj.warning_pin = False

            ts2 = datetime.datetime.now().timestamp()
            if(current_pin_offset == 0 and self.scanner_obj.x_aff_barre <= 380):
                self.scanner_obj.x_aff_barre = 1.352*(ts2-ts1) + 15
            elif(self.scanner_obj.x_aff_barre >= 15):
                self.scanner_obj.x_aff_barre = -1.352*(ts2-ts1) + 380

        self.scanner_obj.need_user_input = True
        self.scanner_obj.allere_retour_done += 1
        self.scanner_obj.moteur_a.marche(False)
        self.scanner_obj.y_aff_support += 360/self.scanner_obj.nb_aller_retour

        if(self.scanner_obj.allere_retour_done == self.scanner_obj.nb_aller_retour):#en fois tout les aller retours fait on remte a 0
            self.scanner_obj.allere_retour_done = 0