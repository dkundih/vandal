import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def hey():
    name = entry.get('1.0', END)
    output.insert(END, name)

root = tk.Tk()
root.title('MyApp')
root.iconbitmap()
root.geometry('350x400')

'''
img = ImageTk.PhotoImage(Image.open(r'.logistics\testimg.jpg'))
panel = Label(root, image = img)
panel.pack()
'''

entry = Text(root, height=2, width=39, bg = 'light green')
entry.insert(END, 'Give me money')
entry.pack()

entrybutton = Button(root, height=2, width= 43, text = 'Pozdravi me!', command= hey)
entrybutton.pack()

output = Text(height=2, width=39, bg = 'light blue')
output.pack()

root.mainloop()