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


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
