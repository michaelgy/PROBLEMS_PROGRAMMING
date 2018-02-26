#This code was used for debug the 554 uva problem (my 100th problem)
from tkinter import *

root = Tk()
frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

#b rows, w columns
b,w = (10,11)
matrix = []
for x in range(b):
    matrix.append([int(e) for e in input()])

#example values
for x in range(w):
    for y in range(b):
        if matrix[y][x] == 1:
            v = -1
        elif matrix[y][x] >1:
            v = matrix[y][x]-1
        else:
            v = 0
        #text is the text on each button in the button array, and bg is the background button color
        btn = Button(frame,text=str(v),bg="#000" if v == -1 else "#{}".format("{}".format(hex(15-2*v)[2:]*3)))
        btn.grid(column=x, row=y, sticky=N+S+E+W)

for x in range(b):
  Grid.columnconfigure(frame, x, weight=1)

for y in range(w):
  Grid.rowconfigure(frame, y, weight=1)

root.mainloop()
