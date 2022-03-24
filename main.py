from view.Home import Home
from tkinter import *
from tkinter import messagebox
from models import *
from models.db import DB
from public.validation import Validate_Data
ws = Tk()
ws.geometry("940x500")
Vd = Validate_Data(ws)
db = DB(ws)
f = ('Times', 14)

frame_1 = Home(ws)
frame_1.display()
