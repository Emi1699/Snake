print("starting snoyke...\n\n")

import PySimpleGUI as sg

class Window:
    def __init__(self):
        self.width = 600
        self.height = 400

    def show(self):
        sg.Window(title="Hello World", layout=[[]], margins=(self.width, self.height)).read()

window = Window()
window.show()
