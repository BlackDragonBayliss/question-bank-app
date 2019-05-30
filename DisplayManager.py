from tkinter import *
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
        self.isScoreScreen = False
        self.isShowAnswerLearnMode = False

        self.showAnswerTestModeOutomeText = ""
        self.showAnswerLearnModeLabelText = ""

    def setup(self, test):
        self.instanceTest = test

    def deselectAnswers(self):
        for selectedAnswer in self.selectedAnswerList:
            selectedAnswer.set(0)

    def startScreen(self):
        self.root.geometry('1400x800')
        self.root.configure(background='red')

        self.labelInfoNumberQuestions = Label(self.root, text="Enter number of questions for test")
        self.labelInfoNumberQuestions.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        #label prompt user enter question range seperated by ","
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
        self.updateYPositionGlobalIterate()

        self.flashCardModeButton = Button(text="Flash card mode", command=self.instanceTest.flashCardMode)
        self.flashCardModeButton.place(x=self.xPositionDeslectButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.root.mainloop()

    def flashCardMode(self):
        f = open("flash_card.txt", "r")
        if f.mode == 'r':
            contents = f.read()




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

        self.currentQuestionLabel = Label(self.root, text="Current question: " + str(self.instanceTest.getQuestionObjectManagerCurrentQuestionIndex()))
        self.currentQuestionLabel.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.instanceTest.isRevisitQuestion = IntVar()
        self.isRevisitCheckBox = Checkbutton(self.root, text='Revisit question',variable=self.instanceTest.isRevisitQuestion)
        self.isRevisitCheckBox.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()


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
                button = Radiobutton(root, variable=var, value=i)
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
        if (self.isShowAnswerLearnMode):
            self.showAnswerLabel.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
            self.isShowAnswerLearnMode = False

        self.updateYPositionGlobalIterate()

        self.showAnswerButton = Button(text="Show answer", command=self.showAnswerLearnMode)
        self.showAnswerButton.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.nextQuestionButton = Button(text="Next question", command=self.instanceTest.changeToNextQuestionLearnMode)
        self.nextQuestionButton.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        # print(str(self.instanceTest.getQuestionObjectManagerCurrentQuestionIndex()))
        if(self.instanceTest.getQuestionObjectManagerCurrentQuestionIndex() != 0):
            self.instanceTest.isShowPreviousQuestion = True
            self.previousQuestionButton = Button(text="Previous question",command=self.instanceTest.changeToPreviousQuestionLearnMode)
            self.previousQuestionButton.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.currentQuestionLabel = Label(self.root, text="Current question: "+str(self.instanceTest.getQuestionObjectManagerCurrentQuestionIndex()))
        self.currentQuestionLabel.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        # testRevisitMarkedQuestionsButton
        # self.markedQuestionsButton = Button(text="Test Revisit Questions",command=self.instanceTest.testMarkedRevisitQuestions)
        # self.testRevisitMarkedQuestionsButton.place(x=self.xPositionButtonConfirmQuestionOutcome,y=self.yPositionGlobalIterate)
        # self.updateYPositionGlobalIterate()

        self.instanceTest.isRevisitQuestion = IntVar()
        self.isRevisitCheckBox = Checkbutton(self.root, text='Revisit question', variable=self.instanceTest.isRevisitQuestion)
        self.isRevisitCheckBox.place(x=self.xPositionConfirmButton, y=self.yPositionGlobalIterate)
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
        # self.resetScreenVariables()
        # self.clearWidgets()
        self.populateShowAnswerLearnModeLabelText()
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
        self.score = Label(self.root, text="Total correct: "+str(scoreText)+"%")
        self.score.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        #retake incorrect questions widgets
        #retake current incorrect label
        self.retakeCurrentIncorrectLabel = Label(self.root, text="Number of incorrect questions: "+ "Retake incorrect questions?")
        self.retakeCurrentIncorrectLabel.place(x=self.xPositionButtonConfirmQuestionOutcome, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        #retake current incorrect button.
        self.retakeCurrentIncorrectButton = Button(text="Retake Incorrect Questions", command=self.instanceTest.retakeTestCurrentIncorrectQuestions)
        self.retakeCurrentIncorrectButton.place(x=self.xPositionButtonConfirmQuestionOutcome, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        #retake full test button
        self.retakeFullTestButton = Button(text="Retake Full Test",command=self.instanceTest.retakeFullTest)
        self.retakeFullTestButton.place(x=self.xPositionButtonConfirmQuestionOutcome,y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        #if incorrect retake already taken, display widgets to retake original incorrect questions.
        if(self.instanceTest.isIncorrectOriginalPathOpen):
            print("out isIncorrectOriginalPathOpen: " + str(self.instanceTest.isIncorrectOriginalPathOpen))
            print("out isIncorrectOriginalClearOpen: " + str(self.instanceTest.isIncorrectOriginalClearOpen))
            #retake original incorrect label
            self.retakeOriginalIncorrectLabel = Label(self.root, text="Retake original incorrect questions: "+str(len(self.instanceTest.getOriginalIncorrectList())))
            self.retakeOriginalIncorrectLabel.place(x=self.xPositionKey, y=self.yPositionGlobalIterate)
            self.updateYPositionGlobalIterate()
            #retake original incorrect button.
            self.retakeOriginalIncorrectButton = Button(text="Retake Original Incorrect Questions", command=self.instanceTest.retakeTestOriginalIncorrectQuestions)
            self.retakeOriginalIncorrectButton.place(x=self.xPositionButtonConfirmQuestionOutcome,y=self.yPositionGlobalIterate)
            self.updateYPositionGlobalIterate()
            self.instanceTest.isIncorrectOriginalClearOpen = True

        #retake full test button
        self.startScreenButton = Button(text="Home Screen", command=self.instanceTest.returnHome)
        self.startScreenButton.place(x=self.xPositionButtonConfirmQuestionOutcome, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()


        self.retakeCurrentIncorrectLabel = Label(self.root, text="Number of revisit questions: " +self.instanceTest.getQuestionObjectManagerRevisitQuestionList())
        self.retakeCurrentIncorrectLabel.place(x=self.xPositionButtonConfirmQuestionOutcome, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        #testRevisitMarkedQuestionsButton
        self.testRevisitMarkedQuestionsButton = Button(text="Test Revisit Questions", command=self.instanceTest.testMarkedRevisitQuestions)
        self.testRevisitMarkedQuestionsButton.place(x=self.xPositionButtonConfirmQuestionOutcome, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.instanceTest.isIncorrectOriginalPathOpen = True
        self.isScoreScreen = True

    def displayLearnModeEndScreen(self):
        self.resetScreenVariables()
        self.clearWidgets()
        self.instanceTest.isLearnModeEndScreen = True

        self.updateYPositionGlobalIterate()
        self.startScreenButton = Button(text="Home Screen", command=self.instanceTest.returnHome)
        self.startScreenButton.place(x=self.xPositionButtonConfirmQuestionOutcome, y=self.yPositionGlobalIterate)

        self.updateYPositionGlobalIterate()
        self.retakeCurrentIncorrectLabel = Label(self.root,text="Number of revisit questions: " + self.instanceTest.getQuestionObjectManagerRevisitQuestionList())
        self.retakeCurrentIncorrectLabel.place(x=self.xPositionButtonConfirmQuestionOutcome,y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()

        self.testRevisitMarkedQuestionsButton = Button(text="Test Revisit Questions", command=self.instanceTest.testMarkedRevisitQuestionList)
        self.testRevisitMarkedQuestionsButton.place(x=self.xPositionButtonConfirmQuestionOutcome, y=self.yPositionGlobalIterate)
        self.updateYPositionGlobalIterate()



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
        #initial screen widgets
        if(self.isInitialClearIndex):
            self.isInitialClearIndex = False
            self.labelInfoNumberQuestions.destroy()
            self.labelInfoNumberInstructionForQuestions.destroy()
            self.entryNumberQuestions.destroy()
            self.isRandomizationCheckBox.destroy()
            self.testModeButton.destroy()
            self.learnModeButton.destroy()
            self.flashCardModeButton.destroy()
            return
        #handle destroy if isScoreScreen
        if (self.isScoreScreen):
            self.score.destroy()
            self.retakeCurrentIncorrectLabel.destroy()
            self.retakeCurrentIncorrectButton.destroy()
            self.retakeFullTestButton.destroy()
            self.startScreenButton.destroy()
            print("inside isIncorrectOriginalPathOpen: " + str(self.instanceTest.isIncorrectOriginalPathOpen))
            print("inside isIncorrectOriginalClearOpen: "+str(self.instanceTest.isIncorrectOriginalClearOpen))
            if (self.instanceTest.isIncorrectOriginalClearOpen):
                self.retakeOriginalIncorrectLabel.destroy()
                self.retakeOriginalIncorrectButton.destroy()
                self.instanceTest.isIncorrectOriginalClearOpen = False
            self.isScoreScreen = False
            return
        #handle destroy if isOutcomeScreen
        if (self.isQuestionOutcomeScreen):
            self.labelQuestionOutcome.destroy()
            self.labelQuestionOutcomeCorrectAnswer.destroy()
            self.buttonConfirmQuestionOutcome.destroy()
            self.isQuestionOutcomeScreen = False
            return

        if (self.instanceTest.getIsLearnModeEndScreen()):
            self.startScreenButton.destroy()
            self.retakeCurrentIncorrectLabel.destroy()
            self.testRevisitMarkedQuestionsButton.destroy()
            self.instanceTest.isLearnModeEndScreen = False
            return

        #learn mode widgets
        if(self.instanceTest.getIsLearnMode()):
            for widget in self.keyList:
                widget.destroy()
            self.questionLabel.destroy()
            self.showAnswerLabel.destroy()
            self.showAnswerButton.destroy()
            self.nextQuestionButton.destroy()
            if(self.instanceTest.isShowPreviousQuestion):
                self.previousQuestionButton.destroy()
            self.currentQuestionLabel.destroy()
            self.isRevisitCheckBox.destroy()
            return

        #test mode widgets
        if(self.instanceTest.getIsTestMode()):
            for widget in self.buttonList:
                widget.destroy()
            for widget in self.keyList:
                widget.destroy()
            for widget in self.keyAnswerList:
                widget.destroy()
            self.questionLabel.destroy()
            self.confirmAnswerButton.destroy()
            self.deselectOptionsButton.destroy()
            self.currentQuestionLabel.destroy()
            self.isRevisitCheckBox.destroy()
            return