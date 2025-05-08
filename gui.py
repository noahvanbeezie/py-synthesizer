import tkinter
from tkinter import *

class GUI(tkinter.Tk):
    def __init__(self):
        #Create base window
        super().__init__()
        self.title('Synth Example')
        self.geometry('800x600')

        #This will be for setting the color, not sure on what color to use yet
        #self.configure(bg="")

        #Setting base values
        self.padx = 10
        self.pady = 2
        self.slider_starting_value = 50 
        self.slider_entry_width = 5

        
        #Creating sliders
        self.create_slider("Volume", 0)
        self.create_slider("Example", 1)


    def create_slider(self, slider_name, curr_row):
        #Creating initial variables
        self.slider_val = tkinter.IntVar()
        self.slider_title = tkinter.Label(text=slider_name)
        self.slider = tkinter.Scale(from_=0, to=100, orient=HORIZONTAL, showvalue=0, tickinterval=0, variable=self.slider_val)
        self.slider.set(self.slider_starting_value)
        self.slider_input = tkinter.Entry(textvariable=self.slider_val, width=self.slider_entry_width)

        #Setting up the display grid
        self.slider_title.grid(row=curr_row, column=0, padx=self.padx, pady=self.pady)
        self.slider.grid(row=curr_row, column=1, padx=self.padx, pady=self.pady)
        self.slider_input.grid(row=curr_row, column=2, padx=self.padx, pady=self.pady)
