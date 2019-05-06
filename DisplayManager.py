from tkinter import *
from QuestionObjectManager import QuestionObjectManager
from QuestionObject import QuestionObject

class DisplayManager:
    def __init__(self):
        pass

    def setup(self, test):
        self.instanceTest = test

    def displayGUIRadioButtons(self):
        for counter, choiceText in enumerate(questionlist, 1):
            Label(root, text=choiceText).grid(row=counter, column=0)
            var = IntVar()
            for i in range(1, 2):
                textAnswerList.append([str(counter), choiceText])
                # print("I value created: "+str(i))
                button = Radiobutton(root, variable=var, value=i, command=ShowChoice)
                button.grid(row=counter, column=i)
                buttonList.append(button)
                selectedAnswerList.append(var)

    def ShowChoice():
        for selectedAnswer in selectedAnswerList:
            print(selectedAnswer.get())

    correctAnswersList = []  # correctAnswersList
    answerMatchingComposite = []

    def deselectAnswers(self):
        for selectedAnswer in selectedAnswerList:
            selectedAnswer.set(0)

        print(textAnswerList)
        print(str(len(textAnswerList)))

    def displayTest(self):

        root = Tk()
        root.geometry('1400x800')

        questionlist = self.instanceTest.getQuestionList()#["A", "B", "C"]
        selectedAnswerList = []
        textAnswerList = []
        buttonList = []



        # deselectOptionsButton = Button(text="Deselect Answers", command=deselectAnswers)
        # deselectOptionsButton.place(x=70, y=200)

        confirmAnswerButton = Button(text="Confirm Answer", command=self.confirmAnswer)
        confirmAnswerButton.place(x=70, y=150)

        root.mainloop()