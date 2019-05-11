from tkinter import *
from QuestionObjectManager import QuestionObjectManager
from QuestionObject import QuestionObject

class DisplayManager:
    def __init__(self):
        self.questionCount = 0
        self.internalRadialIndex = 0
        self.yPositionIndex = 1
        self.yPositionGlobalIterate = self.yPositionIndex * 50

        self.xPositionKey = 10
        self.xPositionRadialButton = 30
        self.xPositionAnswer = 55

        self.xPositionConfirmButton = 10
        self.xPositionDeslectButton = 10

        self.xPositionButtonConfirmQuestionOutcome = 50

        self.displayQuestionCallIndex = 0
        self.resetScreenVariablesCallIndex = 0

        self.root = Tk()
        self.questionListAnswerKeys = []
        self.questionListAnswerTexts = []
        self.keyList = []
        self.keyAnswerList = []

        self.textAnswerList = []
        self.buttonList = []

        self.isInitialClearIndex = True
        self.isQuestionOutcomeScreen = False

    def setup(self, test):
        self.instanceTest = test

    def deselectAnswers(self):
        for selectedAnswer in self.selectedAnswerList:
            selectedAnswer.set(0)

    def showChoice(self):
        print("showChoice")
        # pass

    def startScreen(self):
        self.root.geometry('1400x800')
        self.beginTest1Button = Button(text="Begin Test 1", command=self.instanceTest.testOption1)
        self.beginTest1Button.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()
        self.beginTest2Button = Button(text="Begin Test 2", command=self.instanceTest.testOption2)
        self.beginTest2Button.place(x=self.xPositionDeslectButton, y=self.yPositionGlobalIterate)
        self.root.mainloop()

    def displayQuestion(self):
        self.displayQuestionCallIndex += 1
        # self.resetScreenVariables()
        self.resetScreenVariables()
        self.clearWidgets()

        instanceQuestionObjectManager = self.instanceTest.getInstanceQuestionObjectManager()
        self.questionCount += 1
        questionList = self.instanceTest.getInstanceQuestionObjectManager().getQuestionList()
        self.selectedAnswerList = []
        self.currentQuestion = self.instanceTest.getInstanceQuestionObjectManager().getCurrentQuestionObject()

        self.questionText = self.currentQuestion.getProblem()
        print(str(self.currentQuestion.getAnswerListComposite()))

        for index in self.currentQuestion.getAnswerListComposite():
            # self.questionListAnswerKeys.append(index[0])
            self.questionListAnswerTexts.append(index[1])

        self.questionLabel = Label(text=self.questionText)
        self.questionLabel.place(x=10, y=10)

        self.questionListAnswerKeys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

        self.displayGUIRadioButtons(self.root, self.questionText, self.questionListAnswerKeys, self.questionListAnswerTexts,
                                    self.textAnswerList, self.buttonList, self.selectedAnswerList)

        self.confirmAnswerButton = Button(text="Confirm Answer", command=self.instanceTest.confirmAnswer)
        self.confirmAnswerButton.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()
        self.deselectOptionsButton = Button(text="Deselect Answers", command=self.deselectAnswers)
        self.deselectOptionsButton.place(x=self.xPositionDeslectButton, y=self.yPositionGlobalIterate)

    def displayScoreScreen(self):
        self.resetScreenVariables()
        self.clearWidgets()
        scoreText = self.instanceTest.calculateScore()
        score = Label(self.root, text="Fin")
        score.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)

    def displayGUIRadioButtons(self, root, questionText, questionListAnswerKeys, questionListAnswerTexts, textAnswerList, buttonList, selectedAnswerList):
        radioButtonIndex = 0
        print("questionListAnswerKeys: "+ str(questionListAnswerKeys))
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

    def displayQuestionOutcomeScreen(self):
        self.resetScreenVariables()
        self.clearWidgets()

        self.isQuestionOutcomeScreen = True
        outcomeText = "Incorrect"
        if(self.instanceTest.getIsQuestionCorrectOutcome()):
            outcomeText = "Correct"
        else:
            outcomeText = "Incorrect"

        self.labelQuestionOutcome = Label(self.root, text=outcomeText)
        self.labelQuestionOutcome.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()
        self.buttonConfirmQuestionOutcome = Button(text="Continue", command=self.instanceTest.changeToNextQuestion)
        self.buttonConfirmQuestionOutcome.place(x=self.xPositionButtonConfirmQuestionOutcome, y=self.yPositionGlobalIterate)

    def resetScreenVariables(self):
        self.resetYPositionGlobalIterate()
        self.questionListAnswerKeys = []
        self.questionListAnswerTexts = []
        self.internalRadialIndex = 0
        self.textAnswerList = []

    def updateYPositionGlobalIterate(self):
        self.yPositionIndex += 1
        self.yPositionGlobalIterate = self.yPositionIndex * 50

    def resetYPositionGlobalIterate(self):
        self.yPositionIndex = 1
        self.yPositionGlobalIterate = self.yPositionIndex * 50

    def clearWidgets(self):
        print("displayQuestionCallIndex: "+str(self.displayQuestionCallIndex))
        print("resetScreenVariablesCallIndex: " + str(self.resetScreenVariablesCallIndex))

        if(self.isInitialClearIndex):
            self.isInitialClearIndex = False
            self.beginTest1Button.destroy()
            self.beginTest2Button.destroy()
        else:
            for widget in self.buttonList:
                widget.destroy()

            for widget in self.keyList:
                widget.destroy()

            for widget in self.keyAnswerList:
                widget.destroy()

            self.questionLabel.destroy()
            self.confirmAnswerButton.destroy()
            self.deselectOptionsButton.destroy()

        print("self.isQuestionOutcomeScreen: "+str(self.isQuestionOutcomeScreen))

        # Handle destroy if isOutcomeScreen
        if(self.isQuestionOutcomeScreen):
            self.labelQuestionOutcome.destroy()
            self.buttonConfirmQuestionOutcome.destroy()
            self.isQuestionOutcomeScreen = False
