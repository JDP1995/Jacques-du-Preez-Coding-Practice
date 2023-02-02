# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, a

import requests
import tkinter as tk
from tkinter import ttk

response = requests.get("https://randomfox.ca/floof")
fox = response.json()


root = tk.Tk()

foxlabel = tk.Label(text = fox)
foxlabel.pack()




root.mainloop()













