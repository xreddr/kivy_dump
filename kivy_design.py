# Kivy Test
# source virt/Scripts/activate 

import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget # For kv design language file
from kivy.properties import ObjectProperty # For kv design language file


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    
    def action(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # Print to screen
        # self.msg = Label(text=f"Hello {name}, you like {pizza} pizza, and your favorite color is {color}")
        # self.add_widget(self.msg)
        # self.remove_widget(self.msg)
        print(f"Hello {name}, you like {pizza} pizza, and your favorite color is {color}")

        # Clear input
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()