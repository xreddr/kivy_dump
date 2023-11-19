# Kivy Test
# source virt/Scripts/activate 
from kivy.app import App 
from kivy.uix.widget import Widget # For kv design language file
from kivy.properties import ObjectProperty # For kv design language file
from kivy.lang import Builder # To specify design files


Builder.load_file("whatever.kv") # Path to design files
# Builder.load_string("""
#     """) # Used for design language in same file.

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

class AwesomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    AwesomeApp().run()