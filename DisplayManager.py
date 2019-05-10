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

        self.root = Tk()
        self.questionListAnswerKeys = []
        self.questionListAnswerTexts = []
        self.keyList = []
        self.keyAnswerList = []

        self.isInitialClearIndex = True


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
        # self.root.destroy()


    def displayTest(self):
        self.root.geometry('1400x800')

        self.displayQuestion()


        self.root.mainloop()

    def displayQuestion(self):
        self.clearWidgets()
        self.resetYPositionGlobalIterate()
        self.questionListAnswerKeys = []
        self.questionListAnswerTexts = []
        self.internalRadialIndex = 0
        # self.xPositionRadialButton

        questionList = self.instanceTest.getQuestionObjectManager().getQuestionList()  # ["A", "B", "C"]
        self.selectedAnswerList = []
        self.currentQuestion = self.instanceTest.getQuestionObjectManager().getCurrentQuestionObject()

        self.questionText = self.currentQuestion.getProblem()
        print(str(self.currentQuestion.getAnswerListComposite()))

        for index in self.currentQuestion.getAnswerListComposite():
            self.questionListAnswerKeys.append(index[0])#["ok","hi"]
            self.questionListAnswerTexts.append(index[1])


        self.textAnswerList = []
        self.buttonList = []

        self.questionLabel = Label(text=self.questionText)
        self.questionLabel.place(x=10, y=10)

        self.displayGUIRadioButtons(self.root, self.questionText, self.questionListAnswerKeys, self.questionListAnswerTexts,
                                    self.textAnswerList, self.buttonList, self.selectedAnswerList)

        self.confirmAnswerButton = Button(text="Confirm Answer", command=self.instanceTest.confirmAnswer)
        self.confirmAnswerButton.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()
        self.deselectOptionsButton = Button(text="Deselect Answers", command=self.deselectAnswers)
        self.deselectOptionsButton.place(x=self.xPositionDeslectButton, y=self.yPositionGlobalIterate)



    def displayGUIRadioButtons(self, root, questionText, questionListAnswerKeys, questionListAnswerTexts, textAnswerList, buttonList, selectedAnswerList):
        radioButtonIndex = 0
        for counter, choiceText in enumerate(questionListAnswerTexts, 1):
            key = Label(root, text=questionListAnswerKeys[radioButtonIndex])
            key.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
            self.keyList.append(key)

            keyAnswer = Label(root, text=questionListAnswerTexts[self.internalRadialIndex])
            keyAnswer.place(x=self.xPositionAnswer, y=self.yPositionGlobalIterate)
            self.keyAnswerList.append(keyAnswer)

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
            radioButtonIndex += 1

    def updateYPositionGlobalIterate(self):
        self.yPositionIndex += 1
        self.yPositionGlobalIterate = self.yPositionIndex * 50

    def resetYPositionGlobalIterate(self):
        self.yPositionIndex = 1
        self.yPositionGlobalIterate = self.yPositionIndex * 50

    def clearWidgets(self):
        if(self.isInitialClearIndex):
            self.isInitialClearIndex = False
        else:
            for widget in self.buttonList:
                widget.destroy()

            for widget in self.keyList:
                widget.destroy()

            for widget in self.keyAnswerList:
                widget.destroy()

            # self.key.destroy()
            # self.answer.destroy()
            self.questionLabel.destroy()
            self.confirmAnswerButton.destroy()
            self.deselectOptionsButton.destroy()