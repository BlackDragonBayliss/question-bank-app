from tkinter import *

root = Tk()
root.geometry('1400x800')

entry = Entry(root)
entry.pack()

def getInfo():
    print("the text is", entry.get())

beginTest1Button = Button(text="Begin Test 1", command=getInfo)
beginTest1Button.place(x=10, y=100)

root.mainloop()