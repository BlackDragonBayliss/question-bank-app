from tkinter import *
from QuestionObjectManager import QuestionObjectManager
from QuestionObject import QuestionObject

class DisplayManager:
    def __init__(self):
        self.internalRadialIndex = 0
        self.yPositionIndex = 1
        self.yPositionGlobalIterate = self.yPositionIndex * 50

        self.xPositionKey = 10
        self.xPositionRadialButton = 30
        self.xPositionAnswer = 55

        self.xPositionConfirmButton = 10
        self.xPositionDeslectButton = 10


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

    def displayTest(self):

        root = Tk()
        root.geometry('1400x800')


        questionList = self.instanceTest.getQuestionObjectManager().getQuestionList()#["A", "B", "C"]
        self.selectedAnswerList = []
        self.questionText = questionList[0].getProblem()
        self.questionListAnswerKeys = ["A","B"] #questionList[0].getAnswerListComposite()#["ok","hi"]
        self.questionListAnswerTexts = ["Groovy","Not groovy"]

        self.textAnswerList = []
        self.buttonList = []

        questionLabel = Label(text=self.questionText)
        questionLabel.place(x=10, y=10)

        self.displayGUIRadioButtons(root, self.questionText, self.questionListAnswerKeys, self.questionListAnswerTexts, self.textAnswerList,self.buttonList,self.selectedAnswerList)

        confirmAnswerButton = Button(text="Confirm Answer", command=self.instanceTest.confirmAnswer)
        confirmAnswerButton.place(x=self.xPositionConfirmButton, y=150)

        deselectOptionsButton = Button(text="Deselect Answers", command=self.deselectAnswers)
        deselectOptionsButton.place(x=self.xPositionDeslectButton, y=200)

        root.mainloop()

    def displayGUIRadioButtons(self, root, questionText, questionListAnswerKeys, questionListAnswerTexts, textAnswerList, buttonList, selectedAnswerList):


        for counter, choiceText in enumerate(questionListAnswerKeys, 1):

            key = Label(root, text=choiceText).place(x=self.xPositionKey, y=self.yPositionGlobalIterate)#grid(row=counter+1, column=0)
            answer = Label(root, text=questionListAnswerTexts[self.internalRadialIndex]).place(x=self.xPositionAnswer, y=self.yPositionGlobalIterate)#grid(row=counter+1, column=2)

            var = IntVar()
            for i in range(1, 2):
                textAnswerList.append([str(counter), choiceText])
                # print("I value created: "+str(i))
                button = Radiobutton(root, variable=var, value=i, command=self.showChoice)
                button.place(x=self.xPositionRadialButton, y=self.yPositionGlobalIterate)#grid(row=counter+1, column=i)
                buttonList.append(button)
                selectedAnswerList.append(var)

                self.internalRadialIndex += 1
                self.updateYPositionGlobalIterate()
                # self.yPositionIndex += 1
                # answerBoxLabel.place(x=30, y=50)

    def updateYPositionGlobalIterate(self):
        self.yPositionIndex += 1
        self.yPositionGlobalIterate = self.yPositionIndex * 50