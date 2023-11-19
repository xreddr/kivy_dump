# Kivy Test
# source virt/Scripts/activate 
from kivy.app import App 
from kivy.uix.widget import Widget # For kv design language file
from kivy.properties import ObjectProperty # For kv design language file
from kivy.lang import Builder # To specify design files
from kivy.core.window import Window
# from kivy.uix.image import Image
# from kivy.uix.floatlayout import FloatLayout


Builder.load_file("update_label.kv") # Path to design files
# Builder.load_string("""
#     """) # Used for design language in same file.

class MyLayout(Widget):

    def press(self):
        # Create variables for widgets
        name = self.ids.name_input.text
        print(name)

        # Update label
        self.ids.name_label.text = f"Hello {name}!"

        # Clear text box
        self.ids.name_input.text = ""

class AwesomeApp(App):
    def build(self):
        # Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
