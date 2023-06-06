import tkinter as tk
import requests
import json
import datetime
from settings import *
from tkinter import ttk
class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry(GEOMETRY)
        self.title(ROOT_TITLE)
        self.iconbitmap(default="weather.ico")

        self.title_label = tk.Label(
            self,
            font=(FAMILY, TITLE_SIZE, "bold"),
            text="Weather",
            foreground=TEXT_MAIN_COLOUR
        )
        self.title_label.grid(column=0, row=0, sticky=tk.NSEW, pady=5, padx=5)

        self.search_label = tk.Label(
            self,
            font=(FAMILY, LABEL_SIZE, "bold"),
            text="City Search",
            foreground=TEXT_MAIN_COLOUR,
        )
        self.search_label.grid(column=0, row=1, sticky=tk.NSEW, padx=5, pady=5)

        self.default_city_search = "Type a city here..."
        self.city_sv = tk.StringVar()
        self.city_sv.set(self.default_city_search)
        self.city_input = ttk.Entry(
            self,
            font=(FAMILY, LABEL_SIZE),
            foreground=TEXT_INACTIVE_COLOUR,
            textvariable=self.city_sv,
            validate="all",
            validatecommand=(self.register(self.city_search_input), "%P", "%V")
        )
        self.city_input.grid(column=0, row=2, sticky=tk.NSEW, padx=20, pady=5)

        self.city_sv2 = tk.StringVar(value=self.default_city_search)
        self.city_input2 = tk.Entry(
            self,
            font=(FAMILY, LABEL_SIZE),
            foreground=TEXT_INACTIVE_COLOUR,
            textvariable=self.city_sv2,
        )
        self.city_input2.grid(column=0, row=4, sticky=tk.NSEW, padx=20, pady=5)

        self.city_search_button = tk.Button(
            self,
            font=(FAMILY, LABEL_SIZE),
            text="Search",
            width=10,
            state="disabled",
        )
        self.city_search_button.grid(column=0, row=3, sticky=tk.NS, padx=5, pady=5)

        self.rowconfigure([0, 1, 2, 3], weight=0)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)

    def city_search_input(self, value, validation):
        if validation == "focusin" and value == self.default_city_search:
            self.city_sv.set("")
            self.city_input.configure(foreground=TEXT_MAIN_COLOUR)
        elif validation == "focusout" and value == "":
            self.city_sv.set(self.default_city_search)
            self.city_input.configure(foreground=TEXT_INACTIVE_COLOUR)
            self.city_search_button.configure(state="disabled")
        elif validation == "key":
            self.validate_search_button(value)

        return True

    def validate_search_button(self, value):
        allowed_characters = "abcdefghijklmnopqrstuvwxyz- "

        for i in value:
            if i not in allowed_characters:
                self.city_search_button.configure(state="disabled")
                return

        self.city_search_button.configure(state="active")

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
