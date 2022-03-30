from tkinter import *  # tkinter lib
from tkinter import ttk  # tkinter lib
import os # windows cmd commands lib

### UI Theme Colours
BaseBG  = "grey16"
BG      = "grey30"
FG      = "grey80"
FONT    = "Calibri"
##‽TREY‽NUMA‽##

### Version Numbers (redundant)
VerPre  = "Rev. 0"
VerType = "PreBeta"
VerNum  = "0.0.1"


root = Tk()
root.title("Randamu [{} {}: {}]".format(VerPre,VerType,VerNum)) # window title
root.resizable(False, False) # disable window resizing
root.geometry("720x960") # window size (3:4 aspect-ratio [3]x240,[4]x240)
root.configure(bg=BaseBG) # background colour









root.mainloop() # end of tk
