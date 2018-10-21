from tkinter import *
from tkinter import filedialog as fd
import tkinter.font

from PIL import ImageTk, Image

import RUN



master = Tk()

def open_file_explorer():
	filename = fd.askopenfilename()
	RUN.run_me(filename)
	output = open("output.txt", "r").read()
	output = "As we think about comprehension and response today, I'd like you to First think about the essential comprehension strategies for me to send important starting place because one of the things I think that happens to watch these teachers that we end up with his very large collection of comprehension strategies there so many things that we want children to do if we book in a scope and sequence there are often, you know, 20 or 25 different skills listed in a typical scope and sequence for curriculum guide or something of that sort. In fact, when you compare it to the behaviors are Core Reader's researchers have found essentially five behaviors differentiate good readers from for readers and they are these good readers Focus attention and set purpose in some way. You can think of this in terms of taking strategies that are so common in our classroom II strategy that differentiates a good reader for Reader's ability to organize and comeDuring and after reading I think that the process of sorting and categorizing knowing what to keep and what to throw away. Good readers, don't try to remember everything they read good readers. Don't meet a 25 or 20 or 25 page chapter and try to remember it all they have some way to prioritize information have some weight to decide. This is important. I'll keep it information. I'll throw it away organize and sort in some way."
	S = Scrollbar(master)
	T = Text(master, height=15, width=100, font = tkinter.font.Font(family = "Calibri"))
	S.pack(side=RIGHT, fill=Y)
	T.pack(side=LEFT, fill=Y)
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set)
	quote = output
	T.insert(END, quote)


img = ImageTk.PhotoImage(Image.open("logo350x350.png"))
panel = Label(master, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

b = Button(master, text="Select your .wav file", command=open_file_explorer)
b.pack()


mainloop()

