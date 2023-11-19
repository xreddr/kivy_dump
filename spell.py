from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.spelling import Spelling # for spell check



Builder.load_file("spell.kv")

class MyLayout(Widget):

    def press(self):
        # Create instance of Spelling
        s = Spelling()
        # Select language
        s.select_language("en_US")
        # s.list_languages()
        # Grab word from textbox
        word = self.ids.word_input.text
        options = s.suggest(word)
        x = ""
        for item in options:
            x = f"{x} {item},"
        # Update label
        self.ids.word_label.text = f"{x}"

class AweseomApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AweseomApp().run()
