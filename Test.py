
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
        self.questionPieceContainer = []
        # Fault fixing variables
        self.faultResolutionQueryStringContainer = []
        self.filterList1 = []
        self.listResultsDuplicantAnswerOnSameLineFaultCorrected = []
        self.faultCorrectedAtIndexContainer = []
        self.possibleDuplicantAnswerOnSameLineFaultCorrectedAtIndex = 0
        self.duplicantAnswerOnSameLineFaultCorrectedAtIndex = 0
        self.questionPieceFaultIndex = 0

        self.selectedAnswerIndexTotal = 0
        self.answerListIndex = 0
        self.questionInteration = 0
        self.correctQuestionAnsweredCount = 0
        self.vceFaultIndex = 0
        self.strPieceSpaceCorrectAnswerFault = ""
        self.isQuestionCorrectOutcome = False
        self.isVceFault = False
        self.isFaultAppended = False
        self.isFirstRoundStrAddition = True
        self.isFaultDuplicantsAppended = True
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
        self.vceFaultIndex = 0
        self.questionPieceFaultIndex = 0
        self.listResultsDuplicantAnswerOnSameLineFaultCorrected = []
        self.faultCorrectedAtIndexContainer = []
        self.listResultsDuplicantAnswerOnSameLineFaultCorrected = []
        self.listFinalQuestionPieceResults = []
        self.possibleDuplicantAnswerOnSameLineFaultCorrectedAtIndex = 0
        self.spaceFaultQuestionPieceList = []
        self.strPieceSpaceCorrectAnswerFault = ""
        # self.listFinalQuestionPieceResults = []

        for val in data_set_group_0_1:
        #     possibleAnswerIndex = 0
            self.faultCorrectedAtIndexContainer = []
            faultQuestionContainer = val.splitlines()
            faultQuestionContainer = list(filter(None, faultQuestionContainer))

            questionNumber = faultQuestionContainer[0].replace(' ', '')

            # Handle VCE faults
            faultIndex = 0
            for questionPiece in faultQuestionContainer:
                # print("questionPiece: "+questionPiece)
                if("www.vceplus.com " in questionPiece):
                    # print("hit")
                    self.vceFaultIndex = faultIndex
                    self.isVceFault = True
                faultIndex += 1
            # print("vceFaultIndex: " + str(self.vceFaultIndex))
            # print("vceFault in faultQuestionContainer: "+faultQuestionContainer[self.vceFaultIndex])
            if(self.isVceFault):
                faultQuestionContainer.pop(self.vceFaultIndex)
                # for questionPiece in faultQuestionContainer:
                    # print("reworked QP: " + questionPiece)
                self.isVceFault = False
            self.vceFaultIndex = 0

            # Handle duplicant answers on same line faults
            # print("faultQuestionContainer: "+str(faultQuestionContainer))
            for questionPiece in faultQuestionContainer:
                self.questionPieceFaultIndex += 1
                if ("A. " in questionPiece or "B. " in questionPiece or "C. " in questionPiece or "D. " in questionPiece
                    or "E. " in questionPiece or "F. " in questionPiece or "G. " in questionPiece or "H. " in questionPiece):
                    # print("Possible duplicantAnswerOnSameLineFault at questionPieceFaultIndex: "+str(self.questionPieceFaultIndex))
                    self.listResultsDuplicantAnswerOnSameLineFaultCorrected = self.handleDuplicantAnswersOnSameLineFault(questionPiece)
                    # print("listResultsDuplicantAnswerOnSameLineFaultCorrected: "+str(self.listResultsDuplicantAnswerOnSameLineFaultCorrected))
                    # faultCorrectedAtIndex
                    self.faultCorrectedAtIndexContainer.append(self.possibleDuplicantAnswerOnSameLineFaultCorrectedAtIndex)
                self.possibleDuplicantAnswerOnSameLineFaultCorrectedAtIndex += 1

            print("faultCorrectedAtIndexContainer: "+str(self.faultCorrectedAtIndexContainer))
            # Handle if answers added twice, handle at index
            # print(self.listResultsDuplicantAnswerOnSameLineFaultCorrected)
            # add all pieces to container, if piece is at index of fault corrected, add fault pieces corresponding
            indexAddlistFinalQuestionPieceResults = 0
            self.listFinalQuestionPieceResults = []
            # print("faultQuestionContainer: "+str(faultQuestionContainer))

            for questionPiece in faultQuestionContainer:
                for faultIndex in self.faultCorrectedAtIndexContainer:
                    if(indexAddlistFinalQuestionPieceResults == faultIndex):
                        # print("Fault fixing at: "+str(indexAddlistFinalQuestionPieceResults))
                        # print("self.listResultsDuplicantAnswerOnSameLineFaultCorrected: "+str(self.listResultsDuplicantAnswerOnSameLineFaultCorrected))
                        if(self.isFaultDuplicantsAppended):
                            for faultCorrected in self.listResultsDuplicantAnswerOnSameLineFaultCorrected:
                                # print("appending faultCorrected: "+faultCorrected)
                                self.listFinalQuestionPieceResults.append(faultCorrected)
                                self.isFaultDuplicantsAppended = False
                        self.isFaultAppended = True
                        continue
                indexAddlistFinalQuestionPieceResults += 1
                if(self.isFaultAppended):
                    self.isFaultAppended = False
                    continue
                self.listFinalQuestionPieceResults.append(questionPiece)
                # indexAddlistFinalQuestionPieceResults += 1
            # print("self.listFinalQuestionPieceResults: "+str(self.listFinalQuestionPieceResults))


            # Handle correct answer spacing faults
            # Parse correct answer
            self.spaceFaultQuestionPieceIndex = 0
            self.spaceFaultQuestionPieceList = []
            for questionPiece in self.listFinalQuestionPieceResults:
                if (questionPiece.find("Correct") == 0):
                    answerUnparsed = questionPiece.split(":")
                    self.spaceFaultQuestionPieceList = answerUnparsed[1].split(" ")
                    # Remove leading white space index
                    del self.spaceFaultQuestionPieceList[0:1]
                    break
                self.spaceFaultQuestionPieceIndex += 1
            # print("self.spaceFaultQuestionPieceList: "+str(self.spaceFaultQuestionPieceList[0]))
            # print(len(self.spaceFaultQuestionPieceList[0]))
            spaceCorrectAnswerFault = self.spaceFaultQuestionPieceList[0]
            if(len(spaceCorrectAnswerFault)):
                lengthIndex = 0
                while(lengthIndex < len(spaceCorrectAnswerFault)):
                    self.strPieceSpaceCorrectAnswerFault += " "+spaceCorrectAnswerFault[lengthIndex]
                    lengthIndex += 1
            print(self.strPieceSpaceCorrectAnswerFault)

            #find index where correct answer piece, replace with fixed fault correct answer.
            self.listFinalQuestionPieceResults[self.spaceFaultQuestionPieceIndex] = "Correct Answer:"+self.strPieceSpaceCorrectAnswerFault
            print(str(self.listFinalQuestionPieceResults))

    def handleDuplicantAnswersOnSameLineFault(self, questionPiece):
        self.questionPieceListSplit = []
        self.questionPieceListSplit = questionPiece.split(" ")
        # print("fixing duplicantAnswersOnSameLineFault: "+str(questionPiece))
        self.questionPieceSplitIndex = 0
        self.filterList1 = []
        self.faultResolutionQueryStringContainer = []
        self.nextFilterPieceIndex = 0
        for piece in self.questionPieceListSplit:
            # print("piece: " + piece)
            if ("A." in piece or "B." in piece or "C." in piece or "D." in piece
                or "E." in piece or "F." in piece or "G." in piece or "H." in piece):
                self.filterList1.append(self.questionPieceSplitIndex)
                # print("hit piece: " + piece)
            self.questionPieceSplitIndex += 1

        print("filterList1: " + str(self.filterList1))
        newQuestionPieceList = []
        self.nextFilterPieceIndex = 0
        # construct individual questions from split filter
        filterListIterationIndex = 0
        for filterIndex in self.filterList1:
            # print("SECOND INTERATION")
            self.isFirstRoundStrAddition = True
            currentFilterIndex = filterIndex
            questionString = ""
            # questionString = self.questionPieceListSplit[filterIndex]
            # print(questionString)
            # print("currentFilterIndex: " + str(currentFilterIndex))
            # print("filterListIterationIndex: " + str(filterListIterationIndex))
            # print("len(self.filterList1): " + str(len(self.filterList1)))

            if (filterListIterationIndex < (len(self.filterList1) - 1)):
                self.nextFilterPieceIndex = self.filterList1[filterListIterationIndex + 1]
                # print("nextFilterPieceIndex: " + str(nextFilterPieceIndex))

                # print("self.questionPieceListSplit: " + str(self.questionPieceListSplit))
                # print("currentFilterIndex: " + str(currentFilterIndex))
                # print("nextFilterPieceIndex: " + str(self.nextFilterPieceIndex))

                # continue to next stop point adding indexs of the questionPieceListSplit together,
                while (currentFilterIndex < self.nextFilterPieceIndex):
                    strToAdd = self.questionPieceListSplit[(currentFilterIndex)]
                    questionString += strToAdd
                    if (self.isFirstRoundStrAddition):
                        questionString += " "
                        self.isFirstRoundStrAddition = False
                    # print("questionString: " + str(questionString))
                    # print("currentFilterIndex: " + str(currentFilterIndex))
                    currentFilterIndex += 1
            else:
                self.nextFilterPieceIndex = self.nextFilterPieceIndex + 1

                # print("self.questionPieceListSplit: " + str(self.questionPieceListSplit))
                # print("currentFilterIndex: " + str(currentFilterIndex))
                # print("nextFilterPieceIndex: " + str(self.nextFilterPieceIndex))

                # continue to next stop point adding indexs of the questionPieceListSplit together,
                while (currentFilterIndex <= self.nextFilterPieceIndex):
                    strToAdd = self.questionPieceListSplit[(currentFilterIndex)]
                    questionString += strToAdd
                    if (self.isFirstRoundStrAddition):
                        questionString += " "
                        self.isFirstRoundStrAddition = False
                    # print("questionString: " + str(questionString))
                    # print("currentFilterIndex: " + str(currentFilterIndex))
                    currentFilterIndex += 1

            self.faultResolutionQueryStringContainer.append(questionString)
            filterListIterationIndex += 1
            print("POOP: "+str(self.faultResolutionQueryStringContainer))
        return self.faultResolutionQueryStringContainer




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