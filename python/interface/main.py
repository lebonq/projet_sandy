# import kivy module
import kivy


# this restricts the kivy version i.e
# below this kivy version you cannot use the app or software
kivy.require("1.9.1")

# modification de la couleur de la fenêtre
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1) # fond blanc


# layout
from kivy.uix.floatlayout import FloatLayout
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
  
# defining the App class
class MyApp(App):
    def build(self):
        # initialisation de la fenêtre
        self.title = "Projet Sandy"
        
        # creation des box layout
        root = BoxLayout(orientation = 'vertical', spacing = 10) # fenetre principale
        middlePart = BoxLayout(orientation = 'horizontal') # fenetre centrale
        description = BoxLayout() # fenetre de description 
     

        # composants de la page
        """ title = Label(text ="Analyse des plages",font_size='125sp',halign = "left",valign = "top",color = (0,0,0))
        test0 = Label(text = "test0",color = (0,0,0))
        test1 = Label(text = "test1",color = (0,0,0))
        test2 = Label(text = "test2",color = (0,0,0)) """

        title = Button(text ="Analyse des plages",font_size='125sp',halign = "left",valign = "top",color = (0,0,0))
        test0 = Button(text = "test0",color = (0,0,0))
        test1 = Button(text = "test1",color = (0,0,0))
        test2 = Button(text = "test2",color = (0,0,0))


        #placement des composants sur la partie centrale
        middlePart.add_widget(test0)
        middlePart.add_widget(test1)

        #placement des composants sur la partie basse (description)
        description.add_widget(test2)

        #placement des composants sur la fenêtre finale
        root.add_widget(title)
        root.add_widget(middlePart)
        root.add_widget(description)
        
        return root


# run the App
if __name__ == "__main__":
    MyApp().run()