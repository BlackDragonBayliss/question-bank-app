
class Test:
    def __init__(self):
        self.randomizedQuestionList = []
        self.questionList = []
        self.completedQuestions = []
        self.currentQuestionIndex = 0

    def randomizeQuestionList(self):
        self.randomizedQuestionList = shuffle(self.getQuestionList())

    def setQuestionList(self, questionList):
         self.questionList = questionList
    def getQuestionList(self):
        return self.questionList

    def changeToNextQuestion(self):
        # Handled elsewhere to give functionality to go back to previous questions without adding to completed list issues.
        self.handleCompletedQuestionChange()
        #Set current question isAnswered
        self.getCurrentQuestion().setIsAnswered(1)

        # self.setCurrentQuestion()
    def handleCompletedQuestionChange(self):
        # If currentQuestion has already been added,
        pass
        # for questionObject
        # currentQuestionIndex

    def setCurrentQuestion(self, currentQuestion):
        self.currentQuestion = currentQuestion
    def getCurrentQuestion(self):
        return self.currentQuestion

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

    def confirmAnswer():
        # create answerBooleanList to be appended later to textAnswerList
        answerBooleanList = []
        selectedAnswerIndex = 0
        for selectedAnswer in selectedAnswerList:
            # print("hit "+str(selectedAnswer))
            # for each selected answer, if case met return true, continue
            # else return false
            if (selectedAnswer.get() == 1):
                # print("true at index: "+str(selectedAnswerIndex))
                answerBooleanList.append("1")
            else:
                answerBooleanList.append("0")
            selectedAnswerIndex += 1

        # append is selected
        appendTrueSelectedValueCount = 0
        for textAnswer in textAnswerList:
            if (len(textAnswer) == 3):
                print("I'm at index 3")
                del textAnswer[2:3]
            textAnswer.append(answerBooleanList[appendTrueSelectedValueCount])
            appendTrueSelectedValueCount += 1
        # print(selectedAnswerList)
        print(textAnswerList)
        print(str(len(textAnswerList)))

        # instantiate is matching list
        for textAnswer in textAnswerList:
            correctAnswerIndex = 0
            answerMatchingList = [textAnswer]
            answerMatchingComposite.append(answerMatchingList)
            selectedAnswerText = textAnswer[1]

            for correctAnswer in correctAnswerList:
                if (selectedAnswerText == correctAnswer):
                    isAnswerMatching = True
                else:
                    isAnswerMatching = False
                answerMatchingList.append(isAnswerMatching)
        print(textAnswerList)
        print(answerMatchingComposite)

        # calculate are answers correct


        # filter isAnswerMatchingList, if isNotTrue found then tag answer as incorrect.
        # Case in which success? Case in which fail?
        # Given that all answers in correct answer list criteria need to be met, or wrong.
        # Also not too many answers given, or wrong answers selected.
        # Perhaps finding where criteria is not met, and if found then wrong.

        # iterate through corr
        # print(correctAnswer)

        selectedChoices = []
        for selectedAnswer in selectedAnswerList:
            # print(selectedAnswer.get())
            selectedChoices.append(selectedAnswer.get())
        print(selectedChoices)

        # selectedChoices = [0,0,0,0,1,1,0,0]
        answersList = [1, 1, 1, 0, 0, 0, 0, 0]

        # index = 0
        # while(index < len(selectedChoices)):
        #     if(selectedChoices[index] == answersList[index]):
        #         print("true")
        #     else:
        #         print("false")
        #     index += 1

    def deselectAnswers(self):
        for selectedAnswer in selectedAnswerList:
            selectedAnswer.set(0)

        print(textAnswerList)
        print(str(len(textAnswerList)))

    def startTest(self):

        root = Tk()
        root.geometry('1400x800')

        questionlist = self.getQuestionList()#["A", "B", "C"]
        selectedAnswerList = []
        textAnswerList = []
        buttonList = []



        deselectOptionsButton = Button(text="Deselect Answers", command=deselectAnswers)
        deselectOptionsButton.place(x=70, y=200)

        confirmAnswerButton = Button(text="Confirm Answer", command=confirmAnswer)
        confirmAnswerButton.place(x=70, y=150)

        root.mainloop()