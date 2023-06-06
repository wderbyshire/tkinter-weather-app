import tkinter as tk
import requests
import json
import datetime
from settings import *


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

        self.city_sv = tk.StringVar(value="Type a city here...")
        self.city_input = tk.Entry(
            self,
            font=(FAMILY, LABEL_SIZE),
            foreground=TEXT_INACTIVE_COLOUR,
            textvariable=self.city_sv,
        )
        self.city_input.grid(column=0, row=2, sticky=tk.NSEW, padx=20, pady=5)

        self.city_search_button = tk.Button(
            self,
            font=(FAMILY, LABEL_SIZE),
            text="Search",
            width=10,
        )
        self.city_search_button.grid(column=0, row=3, sticky=tk.NS, padx=5, pady=5)

        self.rowconfigure([0, 1, 2, 3], weight=0)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
