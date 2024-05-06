import sys

from kivy.app import App
from kivy.clock import mainthread
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
import threading
import socket

KV = """
MyBL:
        orientation: "vertical"
        size_hint: (0.95, 0.95)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
        Label:  
                font_size: "15sp"
                multiline: True
                text_size: self.width*0.98, None
                size_hint_x: 1.0
                size_hint_y: None
                height: self.texture_size[1] + 15
                text: root.data_label
                markup: True
                
        TextInput:
                id: Inp
                multiline: False
                padding_y: (5,5)
                size_hint: (1, 0.5)
                                
        Button:
                text: "Привет!"
                bold: True
                background_color:'#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback()

        Button:
                text: "Пока!"
                bold: True
                background_color:'#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback_exit()

        Button:
                text: "Здеся был УАСЯ!"
                bold: True
                background_color:'#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback()    

        Button:
                text: "Пыщь пыщь ололо я водитель НЛО!"
                bold: True
                background_color:'#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback()                                             
"""


class MyBL(BoxLayout):
    data_label = StringProperty("Треугольник!")


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        SERVER = "192.168.0.8"
        PORT = 1488

        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((SERVER, PORT))
            self.client.sendall(bytes("979879789", 'UTF-8'))
            self.start_is_ok = True
        except socket.error as e:
            self.start_is_ok = False
            self.data_label += str(e) + "\n"

        threading.Thread(target=self.get_data).start()

    def callback(self):
        print("Поиск по названию")

    def callback_exit(self):
        sys.exit()

    def get_data(self):
        if self.start_is_ok:
            while App.get_running_app().running:
                in_data = self.client.recv(4096)
                receive = in_data.decode()
                print("От сервера: ", receive)
                self.set_data_label(receive)


@mainthread
def set_data_label(self, data):
    self.data_label += "\n" + str(data) + "\n"


class MyApp(App):
    running = True

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False


MyApp().run()
