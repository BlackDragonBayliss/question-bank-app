from tkinter import *
from QuestionObjectManager import QuestionObjectManager
from QuestionObject import QuestionObject

class DisplayManager:
    def __init__(self):
        pass

    def setup(self, test):
        self.instanceTest = test

    def showChoice(self):
        for selectedAnswer in self.selectedAnswerList:
            pass
            # print(selectedAnswer.get())

        correctAnswersList = []  # correctAnswersList
        answerMatchingComposite = []

    def deselectAnswers(self):
        for selectedAnswer in self.selectedAnswerList:
            selectedAnswer.set(0)

        # print(self.textAnswerList)
        # print(str(len(self.textAnswerList)))

    def displayTest(self):

        root = Tk()
        root.geometry('1400x800')

        questionList = self.instanceTest.getQuestionObjectManager().getQuestionList()#["A", "B", "C"]
        self.selectedAnswerList = []
        self.questionListAnswers = questionList[0].getAnswerListComposite()#["ok","hi"]
        self.textAnswerList = []
        self.buttonList = []


        # print("answers: "+str(questionList[1].getAnswerListComposite()))
        self.displayGUIRadioButtons(root,self.questionListAnswers,self.textAnswerList,self.buttonList,self.selectedAnswerList)
        deselectOptionsButton = Button(text="Deselect Answers", command=self.deselectAnswers)
        deselectOptionsButton.place(x=70, y=200)

        confirmAnswerButton = Button(text="Confirm Answer", command=self.instanceTest.confirmAnswer)
        confirmAnswerButton.place(x=70, y=150)

        root.mainloop()

    def displayGUIRadioButtons(self, root, questionList, textAnswerList, buttonList, selectedAnswerList):
        for counter, choiceText in enumerate(questionList, 1):
            Label(root, text=choiceText).grid(row=counter, column=0)
            var = IntVar()
            for i in range(1, 2):
                textAnswerList.append([str(counter), choiceText])
                # print("I value created: "+str(i))
                button = Radiobutton(root, variable=var, value=i, command=self.showChoice)
                button.grid(row=counter, column=i)
                buttonList.append(button)
                selectedAnswerList.append(var)