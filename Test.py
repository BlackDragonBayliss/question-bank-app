
from random import shuffle
from DisplayManager import DisplayManager
from QuestionObjectManager import *
from QuestionObject import QuestionObject

class Test:
    def __init__(self):
        self.randomizedQuestionList = []
        self.questionList = []
        self.completedQuestions = []
        self.currentQuestionIndex = 0
        self.instanceDisplayManager = DisplayManager()
        self.instanceDisplayManager.setup(self)

    # def operate(self):
    #     pass

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



    def confirmAnswer(self):
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


    def operate(self):
        f = open("demofile.txt", "r")
        stringText = f.read()
        questionObjectManager = QuestionObjectManager()


        #Intake feed, process into question bank
        questionComposite = self.processParseQuestionBank(stringText)
        # print("question Composite: "+str(questionComposite))


        #Set question list
        questionObjectManager.setQuestionList(questionComposite)
        print("question Composite in QOM: " + str(questionObjectManager.getQuestionList()))

        # possibleAnswerList = questionObjectComposite[0].getAnswerListComposite()
        # firstQuestion = questionObjectComposite[0]
        # correctAnswersList = firstQuestion.getCorrectAnswer()
        # questionList = firstQuestion.getAnswerListComposite()
        # print(correctAnswersList)
        # print(questionList)


        #Construct question, randomizing answers
        self.createTest(1)


    #
    def processParseQuestionBank(self, str_to_parse):
        data_set_group_0_1 = str_to_parse.split('QUESTION')

        # data_set_group_0_2 = []
        data_set_group_0_1.pop(0)
        questionObjectComposite = []
        intervalIndex = 0
        for val in data_set_group_0_1:
            # if(intervalIndex == 0):
            possibleAnswerIndex = 0
            questionContainer = val.splitlines()
            questionContainer = list(filter(None, questionContainer))
            questionNumber = questionContainer[0].replace(' ','')
            #create data object
            questionObj = QuestionObject()

            # print(questionContainer)

            questionObj.setQuestionNumber(questionNumber)
            questionObj.setProblem(questionContainer[1])
            questionPieceIndex = 0

            # Parse correct answer
            for questionPiece in questionContainer:
                if (questionPiece.find("Correct") == 0):
                    questionObj.setCorrectAnswer(questionPiece)
                questionPieceIndex += 1

            questionObjectComposite.append(questionObj)

            # Parse answer list
            for val in questionContainer:
                if(possibleAnswerIndex > 1):
                    # print(val)
                    if(val.find("Correct") == 0):
                        isContinueCalculating = False
                        break
                    questionObj.parseAnswer(val)
                possibleAnswerIndex += 1
            intervalIndex += 1

        return questionObjectComposite

    def createDisplayList(self, questionList):
        displayContainer = []
        for question in questionList:
            displayObject = "Question "+question[0]

            #associateAnswer with bound correct answer object
            #Append new line questionList attributes
            displayContainer.append(displayObject)
        return displayContainer

    def parseIntoQuestionObjectsList(self):
        pass
    def instantiateQuestion(self):
        pass
    def randomizeQuestion(self):
        pass

    def createTest(self, caseType):
        if(0):
            # Support for sample sized test
            pass
        if (1):
            # print("questionList: "+str(self.getQuestionList()))
            # This is wrong it needs to be one individual question per.... Ah needs to randomize questions first.
            # Set randomized list at another time.
            # print("Question list1 " + str(self.getQuestionList()))


            # self.shuffleQuestionList()

            # testInstance = Test()

            print("Question list1 "+ str(self.getQuestionList()))
            self.setQuestionList(self.getQuestionList())
            #
            print("Question list2 " + str(self.getQuestionList()))
            # self.getQuestionList()


            # testInstance.randomizeQuestionList()
            # testInstance.setCurrentQuestion()



            self.instanceDisplayManager.displayTest()

        if (2):
            # Support for loading test states from previous exams
            pass

            # print("shuffle: " + str(shuffledList))
                # print(question.getAnswerListComposite())
                # question.setRandomizedList(self.randomizeQuestionAnswers(question.getAnswerListComposite()))


            # self.setCurrentQuestion()

                # print(question.getRandomizedList())
                # print(question.getQuestionNumber())

