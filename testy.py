# from tkinter import *
# #
# # top = Tk()
# # # Code to add widgets will go here...
# # top.mainloop()
#
#
# master = Tk()
# Label(master, text='First Name').grid(row=0)
# Label(master, text='Last Name').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
#
# mainloop()
#
#
#
# # from tkinter import *
# #
# #
# # def main():
# #
# #     master = Tk()
# #     Label(master, text='First Name').grid(row=0)
# #     Label(master, text='Last Name').grid(row=1)
# #     e1 = Entry(master)
# #     e2 = Entry(master)
# #     e1.grid(row=0, column=1)
# #     e2.grid(row=1, column=1)
# #
# # if __name__ == "__main__": main()



from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

selected = IntVar()

rad1 = Radiobutton(window, text='First', value=1, variable=selected)

rad2 = Radiobutton(window, text='Second', value=2, variable=selected)

rad3 = Radiobutton(window, text='Third', value=3, variable=selected)


def clicked():
    print(selected.get())


btn = Button(window, text="Click Me", command=clicked)

rad1.grid(column=0, row=0)

rad2.grid(column=1, row=0)

rad3.grid(column=2, row=0)

btn.grid(column=3, row=0)

window.mainloop()