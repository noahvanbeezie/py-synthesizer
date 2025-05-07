import tkinter
from tkinter import *

class GUI(tkinter.Tk):
    def __init__(self):
        #Create base window
        super().__init__()
        self.title('Synth Example')
        self.geometry('400x300')

        #Setting base values
        self.padx = 10
        self.pady = 2
        self.starting_value = 50 

        #Setting initial Widget values
        self.slider_val = tkinter.IntVar()
        self.slider_title = tkinter.Label(text="Example Slider")
        self.slider = tkinter.Scale(from_=0, to=100, orient=HORIZONTAL, showvalue=0, tickinterval=0, variable=self.slider_val, command=self.set_label_text)
        self.slider.set(self.starting_value)
        self.slider_variable_value = tkinter.Label(text=self.starting_value)

        #Setting up the display grid
        self.slider_title.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.slider.grid(row=0, column=1, padx=self.padx, pady=self.pady)
        self.slider_variable_value.grid(row=0, column=2, padx=self.padx, pady=self.pady)

    def set_label_text(self, value):
        self.slider_variable_value.config(text=value)