from tkinter import *
import os
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

#Creates GUI window
root = Tk()

#Sets title of the window to Weather App
root.title("Weather App")

#Sets the window geometry
root.geometry("800x470+300+200")

#Sets background color of the window
root.configure(bg="#57adff")

#Avoids resizing of the window
root.resizable(False,False)

#icon

image_icon = PhotoImage(file="Assets/icon.png")
root.iconphoto(False,image_icon)

root.mainloop()
