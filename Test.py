
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
        self.correctQuestionAnsweredCount = 0
        self.vceFaultIndex = 0
        self.isQuestionCorrectOutcome = False
        self.isVceFault = False
        self.instanceDisplayManager = DisplayManager()
        self.instanceQuestionObjectManager = QuestionObjectManager()

    def operate(self):
        self.parseQuestionBankToCorrectFormat()
        # self.readQuestionBank()
        # self.instanceDisplayManager.setup(self)
        # self.instanceDisplayManager.startScreen()

    def parseQuestionBankToCorrectFormat(self):
        # file = open("testfile.txt", "w")
        # file.write("Hello World")
        # file.close()

        f = open("testfile.txt", "r")
        # f = open("demofile.txt", "r")
        stringText = f.read()

        self.parseForFaults(stringText)
        # print(stringText)

    def parseForFaults(self, stringText):
        data_set_group_0_1 = stringText.split('QUESTION')
        data_set_group_0_1.pop(0)
        # questionObjectComposite = []
        # intervalIndex = 0
        valIndex = 0
        for val in data_set_group_0_1:
        #     possibleAnswerIndex = 0
            faultQuestionContainer = val.splitlines()
            faultQuestionContainer = list(filter(None, faultQuestionContainer))

            questionNumber = faultQuestionContainer[0].replace(' ', '')

            # Handle VCE faults
            # faultIndex = 0
            # for questionPiece in faultQuestionContainer:
            #     print("questionPiece: "+questionPiece)
            #     if("www.vceplus.com " in questionPiece):
            #         print("hit")
            #         self.vceFaultIndex = faultIndex
            #         self.isVceFault = True
            #     faultIndex += 1
            # print("vceFaultIndex: " + str(self.vceFaultIndex))
            # # print("vceFault in faultQuestionContainer: "+faultQuestionContainer[self.vceFaultIndex])
            # if(self.isVceFault):
            #     faultQuestionContainer.pop(self.vceFaultIndex)
            #     for questionPiece in faultQuestionContainer:
            #         print("reworked QP: " + questionPiece)
            #     self.isVceFault = False
            # self.vceFaultIndex = 0

            sampleTest1 = ["A. asko. dsak B. odsokdsod"]
            sampleTest2 = ["C. askodsak D. odsokdsod"]
            # Handle duplicant answers on same line faults
            faultIndex = 0
            # for questionPiece in faultQuestionContainer:
            for questionPiece in sampleTest1:
                print("questionPiece: " + questionPiece)
                if ("A. " in questionPiece or "B. " in questionPiece or "C. " in questionPiece or "D. " in questionPiece
                    or "E. " in questionPiece or "F. " in questionPiece or "G. " in questionPiece or "H. " in questionPiece):

                    print("hit duplicantAnswerOnSameLineFault")
                    self.questionPieceListSplit = questionPiece.split(" ")
                    print(str(questionPiece))
                    self.questionPieceSplitIndex = 0
                    self.filterList1 = []
                    for piece in self.questionPieceListSplit:
                        print("piece: "+piece)
                        if ("A." in piece or "B." in piece or "C." in piece or "D." in piece
                                or "E." in piece or "F." in piece or "G." in piece or "H." in piece):
                            self.filterList1.append(self.questionPieceSplitIndex)
                            print("hit piece: "+piece)
                        self.questionPieceSplitIndex += 1

                    print("filterList1: "+str(self.filterList1))
                newQuestionPieceList = []

                # construct individual questions from split filter
                filterListIterationIndex = 0
                for filterIndex in self.filterList1:
                    currentFilterIndex = filterIndex
                    questionString = self.questionPieceListSplit[filterIndex]
                    print(questionString)
                    # stopPoint = self.filterList1[currentFilterIndex+1]
                    print("currentFilterIndex: "+str(currentFilterIndex))
                    print("self.filterList1[filterListIterationIndex]: " + str(self.filterList1[filterListIterationIndex+1]))
                    while(currentFilterIndex < self.filterList1[filterListIterationIndex+1]):
                        questionString += self.questionPieceListSplit[currentFilterIndex]
                        currentFilterIndex += 1
                    print("questionString: "+questionString)
                    filterListIterationIndex += 1

            # Handle correct answer spacing faults


            #     if ("www.vceplus.com " in questionPiece):
            #         print("hit")
            #         self.vceFaultIndex = faultIndex
            #         self.isVceFault = True
            #     faultIndex += 1
            # print("vceFaultIndex: " + str(self.vceFaultIndex))
            # # print("vceFault in faultQuestionContainer: "+faultQuestionContainer[self.vceFaultIndex])
            # if (self.isVceFault):
            #     faultQuestionContainer.pop(self.vceFaultIndex)
            #     for questionPiece in faultQuestionContainer:
            #         print("reworked QP: " + questionPiece)
            #     self.isVceFault = False
            # self.vceFaultIndex = 0


        # questionNumber = questionContainer[0].replace(' ', '')
            # create data object
            # questionObj = QuestionObject()

            # questionObj.setQuestionNumber(questionNumber)
            # questionObj.setProblem(questionContainer[1])
        # print(str(self.faultQuestionContainer))

        # Parse correct answer
        # for questionPiece in questionContainer:
        #     if (questionPiece.find("Correct") == 0):
        #         answerUnparsed = questionPiece.split(":")
        #         # print(answerUnparsed[1])
        #
        #         self.answerList = answerUnparsed[1].split(" ")
        #         # Remove leading white space index
        #         del self.answerList[0:1]
        #
        #     questionPieceIndex += 1
        #
        # # Reiterate through answers, if matching correct answerList, set text as correct answer in object
        # for answer in self.answerList:
        #     for questionPiece in questionContainer:
        #         questionPieceKey = self.answerList[self.answerListIndex] + "."
        #         if (questionPiece.find(questionPieceKey) == 0):
        #             answerListSplit = questionPiece.split(". ")
        #             correctAnswerToAppend = answerListSplit[1]
        #             questionObj.addCorrectAnswer(correctAnswerToAppend)
        #     self.answerListIndex += 1
        # self.answerListIndex = 0
        # questionObjectComposite.append(questionObj)
        #
        # # Parse answer list
        # for val in questionContainer:
        #     if (possibleAnswerIndex > 1):
        #         # print(val)
        #         if (val.find("Correct") == 0):
        #             isContinueCalculating = False
        #             break
        #         questionObj.parseAnswer(val)
        #     possibleAnswerIndex += 1
        # intervalIndex += 1


    def batchSizeTest(self):
        batchSize = int(self.instanceDisplayManager.entryNumberQuestions.get())
        print(str(batchSize))
        questionList = self.instanceQuestionObjectManager.getQuestionList()
        self.batchQuestionList =  []
        if(batchSize <= len(questionList)):
            index = 0
            while(index < batchSize):
                self.batchQuestionList.append(questionList[index])
                index += 1
        else:
            self.batchQuestionList = questionList
        print("length of batchQuestionList: "+str(len(self.batchQuestionList)))
        self.instanceQuestionObjectManager.setBatchSizeQuestionList(self.batchQuestionList)

    def testOption1(self):
        self.batchSizeTest()
        self.instanceDisplayManager.displayQuestion()

    def testOption2(self):
        self.instanceQuestionObjectManager.randomizeQuestionList()
        self.instanceDisplayManager.displayQuestion()
        self.batchSizeTest()

    def readQuestionBank(self):
        f = open("demofile.txt", "r")
        stringText = f.read()
        # Intake feed, process into question bank
        questionComposite = self.processParseQuestionBank(stringText)
        # Set question list
        self.instanceQuestionObjectManager.setQuestionList(questionComposite)
        self.instanceQuestionObjectManager.setCurrentQuestionObject(questionComposite[0])
        # Randomize question answers
        self.instanceQuestionObjectManager.randomizeQuestionAnswerLists()


    def processParseQuestionBank(self, str_to_parse):
        data_set_group_0_1 = str_to_parse.split('QUESTION')

        data_set_group_0_1.pop(0)
        questionObjectComposite = []
        intervalIndex = 0
        for val in data_set_group_0_1:
            possibleAnswerIndex = 0
            questionContainer = val.splitlines()
            questionContainer = list(filter(None, questionContainer))
            questionNumber = questionContainer[0].replace(' ','')
            #create data object
            questionObj = QuestionObject()

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
            for answer in self.answerList:
                for questionPiece in questionContainer:
                    questionPieceKey = self.answerList[self.answerListIndex] + "."
                    if (questionPiece.find(questionPieceKey) == 0):
                        answerListSplit = questionPiece.split(". ")
                        correctAnswerToAppend = answerListSplit[1]
                        questionObj.addCorrectAnswer(correctAnswerToAppend)
                self.answerListIndex +=1
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
            #Append new line questionList attributes
            displayContainer.append(displayObject)
        return displayContainer

    def changeToNextQuestion(self):
        self.instanceQuestionObjectManager.getCurrentQuestionObject().setIsAnswered(True)
        #Handle on set nextQuestion
        if(self.instanceQuestionObjectManager.processNextQuestion()):
        # Handle displayManager paint new question
            self.instanceDisplayManager.displayQuestion()
        else:
            self.instanceDisplayManager.displayScoreScreen()

    def confirmAnswer(self):
        # create answerBooleanList to be appended later to textAnswerList
        answerBooleanList = []
        selectedAnswerIndex = 0
        for selectedAnswer in self.instanceDisplayManager.selectedAnswerList:
            if (selectedAnswer.get() == 1):
                answerBooleanList.append("1")
            else:
                answerBooleanList.append("0")
            selectedAnswerIndex += 1
        # Append selectedBool to answerList
        appendTrueSelectedValueCount = 0
        for textAnswer in self.instanceDisplayManager.textAnswerList:
            if (len(textAnswer) == 3):
                del textAnswer[2:3]
            textAnswer.append(answerBooleanList[appendTrueSelectedValueCount])
            appendTrueSelectedValueCount += 1
        # Instantiate is matching list
        for selectedAnswer in self.instanceDisplayManager.textAnswerList:
            correctAnswerIndex = 0
            selectedAnswerKey = selectedAnswer
            if(selectedAnswerKey[2] == "1"):
                currentQuestionObject = self.instanceQuestionObjectManager.getCurrentQuestionObject()
                self.correctAnswerList = currentQuestionObject.getCorrectAnswerList()
                for correctAnswer in self.correctAnswerList:
                    if (selectedAnswerKey[1] == correctAnswer):
                        self.answerMatchingList.append(selectedAnswerKey)
                    else:
                        pass
                self.selectedAnswerIndexTotal += 1

        # Handle if no answers selected, default to answer being incorrect
        if(self.selectedAnswerIndexTotal != 0):
            if(len(self.answerMatchingList) == len(self.correctAnswerList) and self.selectedAnswerIndexTotal == len(self.correctAnswerList)):
                self.isQuestionCorrectOutcome = True
            else:
                self.isQuestionCorrectOutcome = False

        self.instanceQuestionObjectManager.getCurrentQuestionObject().setIsAnsweredCorrectly(self.isQuestionCorrectOutcome)
        self.instanceDisplayManager.displayQuestionOutcomeScreen()
        self.isQuestionCorrectOutcome =  False
        self.answerMatchingList = []
        self.selectedAnswerIndexTotal = 0

    def calculateScore(self):
        questionList = self.instanceQuestionObjectManager.questionList
        totalCountQuestions = len(questionList)
        # self.instanceQuestionObjectManager.getCurrentQuestionObject().setIsAnsweredCorrectly(True)
        for question in questionList:
            if(question.getIsAnsweredCorrectly()):
                self.correctQuestionAnsweredCount += 1
        percentageCorrect = (self.correctQuestionAnsweredCount / totalCountQuestions) * 100
        return percentageCorrect


    def getIsQuestionCorrectOutcome(self):
        return self.isQuestionCorrectOutcome

    def getInstanceQuestionObjectManager(self):
        return self.instanceQuestionObjectManager