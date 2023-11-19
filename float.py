# Kivy Test
# source virt/Scripts/activate 
from kivy.app import App 
from kivy.uix.widget import Widget # For kv design language file
from kivy.properties import ObjectProperty # For kv design language file
from kivy.lang import Builder # To specify design files
from kivy.core.window import Window
# from kivy.uix.image import Image
# from kivy.uix.floatlayout import FloatLayout


Builder.load_file("calc.kv") # Path to design files
# Builder.load_string("""
#     """) # Used for design language in same file.

class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        # Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
