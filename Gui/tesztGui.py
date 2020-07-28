from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
"""
layout = BoxLayout(padding=10)
button = Button(text='My first button')
layout.add_widget(button)
"""
class Simple( App ):
    def build(self):
        box = BoxLayout( padding = 10 )
        button01 = Button( text = "egyik" )
        button02 = Button( text = "másik")
        box.add_widget( button01 )
        box.add_widget( button02 )
        return box


Simple().run()
