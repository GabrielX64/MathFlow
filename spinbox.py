import customtkinter
import tkinter as tk
from typing import Union, Callable
from CTkMessagebox import CTkMessagebox

def show_error(num: int):
    if num == 1:
        CTkMessagebox(title="Error", message='"n" no puede ser menor de 5!', icon="cancel", topmost=False)
    elif num == 2:
        CTkMessagebox(title="Error", message='"n" no puede ser mayor de 15!', icon="cancel", topmost=False)

class IntSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: int = 1,  
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28")) 
        self.grid_columnconfigure((0, 2), weight=0) 
        self.grid_columnconfigure(1, weight=1)  

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        
        self.entry.insert(5, "5")
        self.entry.configure(state= "readonly")


    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            self.entry.configure(state= "normal")
            value = int(self.entry.get()) + self.step_size
            if value > 15:
                show_error(2)
                return
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
            self.entry.configure(state= "readonly")
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            self.entry.configure(state= "normal")
            value = int(self.entry.get()) - self.step_size
            if value < 5:
                show_error(1)
                return
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
            self.entry.configure(state= "readonly")
        except ValueError:
            return

    def get(self) -> Union[int, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))
