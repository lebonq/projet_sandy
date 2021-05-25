# import kivy module
import kivy


# this restricts the kivy version i.e
# below this kivy version you cannot use the app or software
kivy.require("1.9.1")

# modification de la couleur de la fenêtre
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1) # fond blanc


# layout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
  
# if you not import label and use it it through error
from kivy.uix.label import Label

# creates the button in kivy 
# if not imported shows the error 
from kivy.uix.button import Button
  
# Widgets are elements of
# a graphical user interface that
# form part of the User Experience.
from kivy.uix.widget import Widget



#######################################################################

# Creation de la classe App dans lequel
# le fichier .kv doit s'appeler pagePrincipale.kv

#######################################################################

class Plage(BoxLayout):
    def __init__(self, **kwargs):
        super(Plage, self).__init__(**kwargs)

class Spectre(AnchorLayout):
    def __init__(self, **kwargs):
        super(Spectre, self).__init__(**kwargs)

class Description(BoxLayout):
    def __init__(self, **kwargs):
        super(Description, self).__init__(**kwargs)


class analyseDesPlages(BoxLayout):
    def __init__(self, **kwargs):
        super(analyseDesPlages, self).__init__(**kwargs)


# Page principale Kivy
class pagePrincipaleApp(App): 

    def build(self): 
        self.title = "Projet Sandy"

        # Retourne analyseDesPlages
        return analyseDesPlages() 



# Execution de la classe
if __name__ == "__main__":
    pagePrincipaleApp().run()