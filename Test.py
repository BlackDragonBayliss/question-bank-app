
from random import shuffle
from DisplayManager import DisplayManager
from QuestionObjectManager import *
from QuestionObject import QuestionObject

class Test:
    def __init__(self):
        self.randomizedQuestionList = []
        self.questionList = []
        self.completedQuestions = []
        self.answerMatchingList = []
        self.answerMatchingComposite = []
        self.correctAnswerList = []
        self.selectedAnswerIndexTotal = 0
        self.answerListIndex = 0
        self.questionInteration = 0
        self.instanceDisplayManager = DisplayManager()
        self.instanceQuestionObjectManager = QuestionObjectManager()

    def randomizeQuestionList(self):
        self.randomizedQuestionList = shuffle(self.getQuestionList())

    def setQuestionList(self, questionList):
         self.questionList = questionList
    def getQuestionList(self):
        return self.questionList

    def changeToNextQuestion(self):
        # Set current question isAnswered
        self.instanceQuestionObjectManager.getCurrentQuestionObject().setIsAnswered("1")
        #Handle on set nextQuestion
        # self.instanceQuestionObjectManager.setCurrentQuestionObject(nextQuestion)
        self.instanceQuestionObjectManager.processNextQuestion()
        # #Handle displayManager paint new question
        self.instanceDisplayManager.displayTest()


    def confirmAnswer(self):
        # create answerBooleanList to be appended later to textAnswerList
        answerBooleanList = []
        selectedAnswerIndex = 0
        for selectedAnswer in self.instanceDisplayManager.selectedAnswerList:
            if (selectedAnswer.get() == 1):
                # print("true at index: "+str(selectedAnswerIndex))
                answerBooleanList.append("1")
            else:
                answerBooleanList.append("0")
            selectedAnswerIndex += 1
        # print(str(answerBooleanList))

        # append selectedBool to answerList
        appendTrueSelectedValueCount = 0
        for textAnswer in self.instanceDisplayManager.textAnswerList:

            if (len(textAnswer) == 3):
                # print("I'm at index 3")
                del textAnswer[2:3]
            textAnswer.append(answerBooleanList[appendTrueSelectedValueCount])
            appendTrueSelectedValueCount += 1
        #
        # # print(selectedAnswerList)
        print("textAnswerList: "+str(self.instanceDisplayManager.textAnswerList))
        # print(str(len(self.instanceDisplayManager.textAnswerList)))
        #
        #
        # # instantiate is matching list
        for selectedAnswer in self.instanceDisplayManager.textAnswerList:
            correctAnswerIndex = 0
            selectedAnswerKey = selectedAnswer#textAnswer[1][0]

            if(selectedAnswerKey[2] == "1"):
                print("1 at: " + str(selectedAnswerKey))
                currentQuestionObject = self.instanceQuestionObjectManager.getCurrentQuestionObject()
                self.correctAnswerList = currentQuestionObject.getCorrectAnswerList()
                print("selectedAnswerKey: "+str(selectedAnswerKey))


                for correctAnswer in self.correctAnswerList:
                    print("correctAnswer: "+correctAnswer)
                    print("selectedAnswerKey[1]: " + selectedAnswerKey[1])
                    if (selectedAnswerKey[1] == correctAnswer):
                        self.answerMatchingList.append(selectedAnswerKey)
                    else:
                        pass
                self.selectedAnswerIndexTotal += 1

        print("selectedAnswerIndexTotal: "+str(self.selectedAnswerIndexTotal))
        print("answerMatch: "+str(self.answerMatchingList))
        print("correctAnswerList: " + str(len(self.correctAnswerList)))
        if(len(self.answerMatchingList) == len(self.correctAnswerList) and self.selectedAnswerIndexTotal == len(self.correctAnswerList)):
            print("CORRECT")
        else:
            print("INCORRECT")

        self.answerMatchingList = []
        self.selectedAnswerIndexTotal = 0
        self.changeToNextQuestion()



    def operate(self):
        self.readQuestionBank()
        self.instanceDisplayManager.setup(self)
        self.createTest(1)


    def readQuestionBank(self):
        f = open("demofile.txt", "r")
        stringText = f.read()

        # Intake feed, process into question bank
        questionComposite = self.processParseQuestionBank(stringText)
        # print("question Composite: "+str(questionComposite))

        # Set question list
        self.instanceQuestionObjectManager.setQuestionList(questionComposite)
        self.instanceQuestionObjectManager.setCurrentQuestionObject(questionComposite[0])

        # Randomize question answers
        self.instanceQuestionObjectManager.randomizeQuestionList()


        # print("question Composite in QOM: " + str(self.questionObjectManager.getQuestionList()))

    def createTest(self, caseType):
        if(0):
            # Support for sample sized test
            pass
        if (1):
            # testInstance.randomizeQuestionList()
            # self.instanceQuestionObjectManager.randomizeQuestionList()
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

    def processParseQuestionBank(self, str_to_parse):


        data_set_group_0_1 = str_to_parse.split('QUESTION')

        # data_set_group_0_2 = []
        data_set_group_0_1.pop(0)
        questionObjectComposite = []
        intervalIndex = 0
        for val in data_set_group_0_1:
            print(self.questionInteration)
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

                    answerUnparsed = questionPiece.split(":")
                    # print(answerUnparsed[1])

                    self.answerList = answerUnparsed[1].split(" ")
                    # Remove leading white space index
                    del self.answerList[0:1]

                questionPieceIndex += 1






            #Reiterate through answers, if matching correct answerList, set text as correct answer in object
            print("Incoming answerList: "+str(self.answerList))
            for answer in self.answerList:
                for questionPiece in questionContainer:
                    print("Parsing questionPiece: "+questionPiece)
                    questionPieceKey = self.answerList[self.answerListIndex] + "."
                    # print("KEYuestionPiece: "+questionPieceKey)
                    if (questionPiece.find(questionPieceKey) == 0):
                        answerListSplit = questionPiece.split(". ")
                        # print("Internal answerListSplit: "+str(answerListSplit))
                        correctAnswerToAppend = answerListSplit[1]
                        # print("Process questionPiece: "+correctAnswerToAppend)

                        questionObj.addCorrectAnswer(correctAnswerToAppend)
                self.answerListIndex +=1
                print("correct answer: "+str(questionObj.getCorrectAnswerList()))

            self.answerListIndex = 0
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

            self.questionInteration += 1
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
    def getQuestionObjectManager(self):
        return self.instanceQuestionObjectManager

