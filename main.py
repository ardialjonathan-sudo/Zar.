from kivy.core.audio import SoundLoader
import json
import os
from kivy.animation import Animation
import threading
import ast
import webbrowser
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.screenmanager import NoTransition, ScreenManager
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import (
    MDFlatButton,
    MDFloatingActionButton,
    MDIconButton,
    MDRaisedButton,
    MDRectangleFlatButton,
)
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDIcon, MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
import random 
import math
from kivy.uix.button import Button

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "360")
Config.set("graphics", "height", "640")
Window.softinput_mode = "below_target"

class win(MDScreen):
    def calc(self, instance):
        if self.t.text != "":
            try:
                expression = self.t.text
                expression = expression.replace("×", "*")
                expression = expression.replace("sin(", "math.sin(math.radians(")
                expression = expression.replace("cos(", "math.cos(math.radians(")
                expression = expression.replace("÷", "/")
                
                nb_ouvrantes = expression.count("(")
                nb_fermantes = expression.count(")")
                expression += ")" * (nb_ouvrantes - nb_fermantes)
    
                résultats = eval(expression)
                self.t.text = str(résultats)
                self.lb.text = "=" + str(résultats)
            except Exception:
                sd = MDDialog(title="Erreur", text="Erreur de syntaxe")
                sd.open()

    def ef(self, instance):
        self.t.text = ""
        self.lb.text = ""

    def ajou(self, instance):
        self.t.text += instance.text

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.bar = MDTopAppBar(
            title="X -zar",
            orientation="vertical",
            pos_hint={"center_x": 0.5, "y": 0.91}
        )
        self.add_widget(self.bar)
        self.lb = MDLabel(text="", font_style="H3", pos_hint={"center_y": 0.83}, theme_text_color='Custom', text_color="blue")
        self.add_widget(self.lb)
        
        box = MDBoxLayout(orientation="vertical", size_hint_x=1, size_hint_y=0.75)
        
        box1 = MDBoxLayout(orientation="horizontal", size_hint=(1, 0.15))
        b = Button(text="0", size_hint=(0.25, 1), on_release=self.ajou)
        b1 = Button(text=".", size_hint=(0.25, 1), on_release=self.ajou)
        b2 = Button(text="÷", size_hint=(0.25, 1), on_release=self.ajou)
        b3 = Button(text="=", size_hint=(0.25, 1), color="blue", on_release=self.calc)
        box1.add_widget(b)
        box1.add_widget(b1)
        box1.add_widget(b2)
        box1.add_widget(b3)
        
        box2 = MDBoxLayout(orientation="horizontal", size_hint_x=1, size_hint_y=0.15)
        b4 = Button(text="1", size_hint=(0.25, 1), on_release=self.ajou)
        b5 = Button(text="2", size_hint=(0.25, 1), on_release=self.ajou)
        b6 = Button(text="3", size_hint=(0.25, 1), on_release=self.ajou)
        b7 = Button(text="–", size_hint=(0.25, 1), on_release=self.ajou)
        box2.add_widget(b4)
        box2.add_widget(b5)
        box2.add_widget(b6)
        box2.add_widget(b7)
        
        box3 = MDBoxLayout(orientation="horizontal", size_hint_x=1, size_hint_y=0.15)
        b8 = Button(text="4", size_hint=(0.25, 1), on_release=self.ajou)
        b9 = Button(text="5", size_hint=(0.25, 1), on_release=self.ajou)
        b10 = Button(text="6", size_hint=(0.25, 1), on_release=self.ajou)
        b11 = Button(text="+", size_hint=(0.25, 1), on_release=self.ajou)
        box3.add_widget(b8)
        box3.add_widget(b9)
        box3.add_widget(b10)
        box3.add_widget(b11)
        
        box4 = MDBoxLayout(orientation="horizontal", size_hint_x=1, size_hint_y=0.15)
        b12 = Button(text="7", size_hint=(0.25, 1), on_release=self.ajou)
        b13 = Button(text="8", size_hint=(0.25, 1), on_release=self.ajou)
        b14 = Button(text="9", size_hint=(0.25, 1), on_release=self.ajou)
        b15 = Button(text="×", size_hint=(0.25, 1), on_release=self.ajou)
        box4.add_widget(b12)
        box4.add_widget(b13)
        box4.add_widget(b14)
        box4.add_widget(b15)
        
        box5 = MDBoxLayout(orientation="horizontal", size_hint_x=1, size_hint_y=0.15)
        b16 = Button(text="cos(", size_hint=(0.25, 1), on_release=self.ajou)
        b17 = Button(text="sin(", size_hint=(0.25, 1), on_release=self.ajou)
        b18 = Button(text=")", size_hint=(0.25, 1), on_release=self.ajou)
        b19 = Button(text="EF", size_hint=(0.25, 1), on_release=self.ef)
        box5.add_widget(b16)
        box5.add_widget(b17)
        box5.add_widget(b18)
        box5.add_widget(b19)
        
        box6 = MDBoxLayout(orientation="horizontal", size_hint_x=1, size_hint_y=0.15)
        self.t = MDTextField(mode="rectangle", readonly=True, halign="right", size_hint_y=1, size_hint_x=1)
        box6.add_widget(self.t)
        
        box.add_widget(box6)
        box.add_widget(box5)        
        box.add_widget(box4)
        box.add_widget(box3)        
        box.add_widget(box2)     
        box.add_widget(box1)
        self.add_widget(box)

class MainApp(MDApp):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(win(name="win"))
        return sm

if __name__ == "__main__":
    MainApp().run()
