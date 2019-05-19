from tkinter import *
from QuestionObjectManager import QuestionObjectManager
from QuestionObject import QuestionObject

class DisplayManager:
    def __init__(self):
        self.questionCount = 0
        self.internalRadialIndex = 0
        self.yPositionIndex = 1
        self.yPositionGlobalIterate = self.yPositionIndex * 50
        self.yPositionContinueButton = 250
        self.xPositionKey = 10
        self.xPositionRadialButton = 30
        self.xPositionAnswer = 55
        self.xPositionConfirmButton = 10
        self.xPositionDeslectButton = 10
        self.xPositionButtonConfirmQuestionOutcome = 50

        self.root = Tk()
        self.questionListAnswerKeys = []
        self.questionListAnswerTexts = []
        self.keyList = []
        self.keyAnswerList = []

        self.textAnswerList = []
        self.buttonList = []

        self.isInitialClearIndex = True
        self.isQuestionOutcomeScreen = False
        self.isShowAnswerLearnMode = False

        self.showAnswerTestModeOutomeText = ""
        self.showAnswerLearnModeLabelText = ""

    def setup(self, test):
        self.instanceTest = test

    def deselectAnswers(self):
        for selectedAnswer in self.selectedAnswerList:
            selectedAnswer.set(0)

    def showChoice(self):
        pass

    def displayEntry(self):
        print(str(self.entryNumberQuestions.get()))

    def startScreen(self):
        self.root.geometry('1400x800')
        self.root.configure(background='blue')

        self.labelInfoNumberQuestions = Label(self.root, text="Enter number of questions for test")
        self.labelInfoNumberQuestions.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        # label prompt user enter question range seperated by ","
        self.labelInfoNumberInstructionForQuestions = Label(self.root, text="If question range, enter question range seperated by \"-\", for example enter: 1 - 10")
        self.labelInfoNumberInstructionForQuestions.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.entryNumberQuestions = Entry(self.root)
        self.entryNumberQuestions.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.isRandomizationCheckBoxIntVar = IntVar()
        self.isRandomizationCheckBox = Checkbutton(self.root, text='Randomize questions?', variable=self.isRandomizationCheckBoxIntVar)
        self.isRandomizationCheckBox.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.testModeButton = Button(text="Test mode", command=self.instanceTest.testMode)
        self.testModeButton.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()
        self.learnModeButton = Button(text="Learn mode", command=self.instanceTest.learnMode)
        self.learnModeButton.place(x=self.xPositionDeslectButton, y=self.yPositionGlobalIterate)

        self.root.mainloop()

    def displayQuestion(self):
        self.resetScreenVariables()
        self.clearWidgets()
        instanceQuestionObjectManager = self.instanceTest.getInstanceQuestionObjectManager()
        self.questionCount += 1
        questionList = self.instanceTest.getInstanceQuestionObjectManager().getBatchSizeQuestionList()
        self.selectedAnswerList = []

        self.currentQuestion = self.instanceTest.getInstanceQuestionObjectManager().getCurrentQuestionObject()

        self.questionText = self.currentQuestion.getProblem()

        for index in self.currentQuestion.getAnswerListComposite():
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

    def displayQuestionLearnMode(self):
        self.resetScreenVariables()
        self.clearWidgets()
        instanceQuestionObjectManager = self.instanceTest.getInstanceQuestionObjectManager()
        self.questionCount += 1
        questionList = self.instanceTest.getInstanceQuestionObjectManager().getBatchSizeQuestionList()
        self.selectedAnswerList = []

        self.currentQuestion = self.instanceTest.getInstanceQuestionObjectManager().getCurrentQuestionObject()
        self.questionText = self.currentQuestion.getProblem()

        for index in self.currentQuestion.getAnswerListComposite():
            self.questionListAnswerTexts.append(index[1])

        self.questionLabel = Label(text=self.questionText)
        self.questionLabel.place(x=10, y=10)
        answerIndex = 0
        for counter, choiceText in enumerate(self.questionListAnswerTexts, 1):
            key = Label(self.root, text=self.questionListAnswerTexts[answerIndex])
            key.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
            self.keyList.append(key)
            self.updateYPositionGlobalIterate()
            answerIndex += 1

        self.showAnswerLabel = Label(self.root, text=self.showAnswerLearnModeLabelText)
        self.showAnswerLabel.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.showAnswerButton = Button(text="Show answer", command=self.showAnswerLearnMode)
        self.showAnswerButton.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.nextQuestionButton = Button(text="Next question", command=self.instanceTest.changeToNextQuestionLearnMode)
        self.nextQuestionButton.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

    def populateShowAnswerTestModeOutomeText(self):
        correctAnswerString = ""
        index = 0
        for correctAnswer in self.currentQuestion.getCorrectAnswerList():
            if((index + 1) == len(self.currentQuestion.getCorrectAnswerList())):
                correctAnswerString += str(correctAnswer)
                break
            correctAnswerString += str(correctAnswer) + "\n"
        if(len(self.currentQuestion.getCorrectAnswerList()) == 1):
            self.showAnswerTestModeOutomeText = "Correct answer: " + correctAnswerString
        else:
            self.showAnswerTestModeOutomeText = "Correct answers: " + correctAnswerString

    def populateShowAnswerLearnModeLabelText(self):
        correctAnswerString = ""
        index = 0
        for correctAnswer in self.currentQuestion.getCorrectAnswerList():
            if((index + 1) == len(self.currentQuestion.getCorrectAnswerList())):
                correctAnswerString += str(correctAnswer)
                break
            correctAnswerString += str(correctAnswer) + "\n"
        if(len(self.currentQuestion.getCorrectAnswerList()) == 1):
            self.showAnswerLearnModeLabelText = "Correct answer: " + correctAnswerString
        else:
            self.showAnswerLearnModeLabelText = "Correct answers: " + correctAnswerString

    def showAnswerLearnMode(self):
        self.isShowAnswerLearnMode = True
        self.populateShowAnswerLearnModeLabelText()
        self.resetScreenVariables()
        self.clearWidgets()
        self.displayQuestionLearnMode()

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

        self.populateShowAnswerTestModeOutomeText()

        self.labelQuestionOutcomeCorrectAnswer = Label(self.root, text=self.showAnswerTestModeOutomeText)
        self.labelQuestionOutcomeCorrectAnswer.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.buttonConfirmQuestionOutcome = Button(text="Continue", command=self.instanceTest.changeToNextQuestion)
        self.buttonConfirmQuestionOutcome.place(x=self.xPositionButtonConfirmQuestionOutcome, y=self.yPositionContinueButton)

    def displayScoreScreen(self):
        self.resetScreenVariables()
        self.clearWidgets()
        scoreText = str(round(self.instanceTest.calculateScore(), 1))

        score = Label(self.root, text="Total correct: "+str(scoreText)+"%")
        score.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)

    def displayLearnModeRetakeScreen(self):
        self.resetScreenVariables()
        self.clearWidgets()
        learnModeEndScreenLabel = Label(self.root, text="End")
        learnModeEndScreenLabel.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)

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
        # Initial screen widgets
        if(self.isInitialClearIndex):
            self.isInitialClearIndex = False
            self.labelInfoNumberQuestions.destroy()
            self.labelInfoNumberInstructionForQuestions.destroy()
            self.entryNumberQuestions.destroy()
            self.isRandomizationCheckBox.destroy()
            self.testModeButton.destroy()
            self.learnModeButton.destroy()
            return

        # Handle destroy if isOutcomeScreen
        if (self.isQuestionOutcomeScreen):
            self.labelQuestionOutcome.destroy()
            self.labelQuestionOutcomeCorrectAnswer.destroy()
            self.buttonConfirmQuestionOutcome.destroy()
            self.isQuestionOutcomeScreen = False
            return

        # Learn mode widgets
        if(self.instanceTest.isLearnMode):
            for widget in self.keyList:
                widget.destroy()
            self.questionLabel.destroy()
            self.showAnswerLabel.destroy()
            self.showAnswerButton.destroy()
            self.nextQuestionButton.destroy()
            return
        # Test mode widgets
        if(self.instanceTest.isTestMode):
            for widget in self.buttonList:
                widget.destroy()
            for widget in self.keyList:
                widget.destroy()
            for widget in self.keyAnswerList:
                widget.destroy()
            self.questionLabel.destroy()
            self.confirmAnswerButton.destroy()
            self.deselectOptionsButton.destroy()
            return


