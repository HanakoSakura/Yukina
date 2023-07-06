import tkinter as tk
import json

score = []

def AddNote(beat:int,pitch:int):
    score.append({'beat':beat,'pitch':pitch})


root = tk.Tk()
root.title('YUKINA Score Maker')

root.geometry('400x300')
root.resizable(0,0)

scl = tk.Scale(
    root,
    from_=-24,
    to=36,
    orient="horizontal",
    resolution=1,
    tickinterval=1,
    length=400,
    label='Pitch'
).pack()

bot = tk.Button(root,text='Close',command=root.quit,width=10).place(x=250,y=250)

root.mainloop()