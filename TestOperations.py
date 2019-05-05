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




# progressbar

# from tkinter import *
#
# from tkinter.ttk import Progressbar
#
# from tkinter import ttk
#
# window = Tk()
#
# window.title("Welcome to LikeGeeks app")
#
# window.geometry('350x200')
#
# style = ttk.Style()
#
# style.theme_use('default')
#
# style.configure("black.Horizontal.TProgressbar", background='black')
#
# bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
#
# bar['value'] = 70
#
# bar.grid(column=0, row=0)
#
# window.mainloop()




# age = input("What is your age? ")
# print("Your age is: ", age)




# from tkinter import *
#
# from tkinter.ttk import *
#
# window = Tk()
#
# window.title("Baysim")
#
# window.geometry('1400x800')
#
# selected = IntVar()
# var1 = IntVar()
# var2 = IntVar()
#
# def clicked():
#     print(selected.get())
#
# def toggle():
#     if mylabel.visible:
#         # btnToggle["text"] = "Show Example"
#         # print("Now you don't")
#         mylabel.place_forget()
#     else:
#         mylabel.place(mylabel.pi)
#         # print("Now you see it")
#         # btnToggle["text"] = "Hide Example"
#     mylabel.visible = not mylabel.visible
#
# # root = tk.Tk()
# #
# #
# # mylabel = tk.Label(text="Example")
# # mylabel.visible = True
# # mylabel.place(x=20, y=50)
# # mylabel.pi = mylabel.place_info()
# #
# # btnToggle = tk.Button(text="Hide Example", command=toggle)
# # btnToggle.place(x=70, y=150)
#
#
# # v = IntVar()
# # Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
# # Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
#
#
# questionLabel = Label(window, text="Question Question Question Question Question Question Question Question Question Question")
# answerLabel = Label(window, text="")
#
# Checkbutton(window, text='male', variable=var1).grid(row=1, sticky=W)
# Checkbutton(window, text='female', variable=var2).grid(row=2, sticky=W)
#
# # rad1 = Radiobutton(window, text='Awesome answer 1 wow', value=1, variable=selected)
# #
# # rad2 = Radiobutton(window, text='Awesome answer 2 wow Awesome answer 2 wow Awesome answer 2 wow', value=2, variable=selected)
# #
# # rad3 = Radiobutton(window, text='Awesome answer 3 wow Awesome answer 3 wow Awesome answer 3 wow', value=3, variable=selected)
#
# btn = Button(window, text="Submit answer", command=clicked)
#
# questionLabel.grid(column=0, row=0)
#
# answerLabel.grid(column=0, row=6)
# # rad1.grid(column=0, row=3)
# #
# # rad2.grid(column=0, row=4)
# #
# # rad3.grid(column=0, row=5)
#
# btn.grid(column=0, row=6)
#
# window.mainloop()








# from tkinter import *
#
# from tkinter.ttk import *
#
# window = Tk()
#
# window.title("Baysim")
#
# window.geometry('1400x800')
#
# def toggle():
#     if radial1.visible:
#         # btnToggle["text"] = "Show Example"
#         # print("Now you don't")
#         radial1.place_forget()
#     else:
#         radial1.place(radial1.pi)
#         # print("Now you see it")
#         # btnToggle["text"] = "Hide Example"
#     radial1.visible = not radial1.visible
#
# listAnswers = []
#
# mylabel = Label(text="test1")
# # radial1 =
#
#
# v = IntVar()
# radial1 = Radiobutton(window, text='GfG', variable=v, value=1).pack(anchor=W)
# # Radiobutton(window, text='MIT', variable=v, value=2).pack(anchor=W)
#
# print(len(listAnswers))
#
# radial1.visible = True
# # mylabel.place(x=20, y=50)
# radial1.pi = mylabel.place_info()
#
# mylabel.visible = True
# mylabel.place(x=20, y=50)
# mylabel.pi = mylabel.place_info()
#
# btnToggle = Button(text="Hide Example", command=toggle)
# btnToggle.place(x=70, y=150)
#
# if(len(listAnswers) < 1):
#     if mylabel.visible:
#         # btnToggle["text"] = "Show Example"
#         # print("Now you don't")
#         mylabel.place_forget()
#     else:
#         mylabel.place(radial1.pi)
#         # print("Now you see it")
#         # btnToggle["text"] = "Hide Example"
#     mylabel.visible = not mylabel.visible

# mainloop()






# from tkinter import *
# def main():
#     root = Tk()
#     questionlist = ["room quality", "food quality", "value for money", "value for money"]
#     answers = []
#
#     def ShowChoice():
#         for v in answers:
#             print(v.get())
#
#     for counter, question in enumerate(questionlist, 1):
#         Label(root, text=question).grid(row=counter, column = 0)
#         var = IntVar()
#         for i in range(1,2):
#             button = Radiobutton(root, variable = var, value = i, command = ShowChoice)
#             button.grid(row = counter, column = i)
#         answers.append(var)
#
#     root.mainloop()
#
# if __name__ == "__main__": main()


# questionObjectComposite
# randomizeQuestions
# getOriginalAnswerFormation()
# self.ranomizedAnswersList = mixed answers
# getRanomizedQuestionsList():
# return self.ranomizedQuestionsList
# setOriginalQuestionList()
# getOriginalQuestionList()
#
#
# questionObject
#
# setOriginalAnswerFormation()
# # Intake [0,0,0]
# getOriginalAnswerFormation()
# # Intake [0,0,0]
# setCurrentAnswerFormation()
# # Intake [0,0,0]
# getCurrentAnswerFormation()
# # Intake [0,0,0]
#
# setCorrectAnswersFormation()
# # Intake [0,1,0]
# randomizeAnswers():
# getOriginalAnswerFormation()
# self.ranomizedAnswersList = mixed answers
# getRanomizedAnswersList():
# return self.ranomizedAnswersList
#
# calculateCorrectAnswersFormation()
# # Intake [correctAnswerText]
# # Return [[correctAnswers]]
# # Further parse correct answers.
# # Find if correctAnswer equates to currentAnswerFormation.index
# # if true, place "1", else 0
# setCorrectAnswersFormation(returnedValue)