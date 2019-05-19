
from random import shuffle
import pdftotext
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
        self.batchRangeList = []
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
        self.isEntryBatchSizeValid = False
        self.isFirstRoundStrAddition = True
        self.isFaultDuplicantsAppended = True
        self.isTestMode = False
        self.isLearnMode = False
        self.instanceDisplayManager = DisplayManager()
        self.instanceQuestionObjectManager = QuestionObjectManager()

    def operate(self):
        self.readPDF()
        self.readQuestionBank()
        self.instanceDisplayManager.setup(self)
        self.instanceDisplayManager.startScreen()

    def readPDF(self):
        # Load your PDF
        with open("my_pdf.pdf", "rb") as f:
            pdf = pdftotext.PDF(f)
        self.pdfText = "\n\n".join(pdf)

    def readQuestionBank(self):
        stringText = self.pdfText #f.read()
        questionSplitContainer = []
        stringTextContainer = []
        #Iterate through first question, followed by consec four.
        questionPieceContainer = []
        revisedProblemLengthFaultQuestionPieceContainer = []
        stringTextContainer = stringText.splitlines()
        tempContainer = []
        strToAppend = ""
        isBeginTextAppend = False
        isOperationNormal = True
        index = 0

        vceTestList = []
        vceIndex = 0
        for text in stringTextContainer:
            vceTestList.append(text)
            vceIndex += 1
        vceTestList = self.handleVceFault(vceTestList)
        revisedEmptyStringAtIndexFaultList = self.handleEmptyStringAtIndexFault(vceTestList)

        # Handle problem concatenation fault
        revisedEmptyStringQuestionPieceContainer = self.handleProblemConcatenationFault(revisedEmptyStringAtIndexFaultList)

        # Handle if question problem over a certain length, if so, break with new line, to prevent question being cut off screen.
        revisedProblemLengthFaultQuestionPieceContainer = self.parseProblemLengthFault(revisedEmptyStringQuestionPieceContainer)

        # Intake feed, process into question bank
        questionComposite = self.processParseQuestionBank(questionPieceContainer)

        # Set question list
        self.instanceQuestionObjectManager.setQuestionList(questionComposite)
        # self.instanceQuestionObjectManager.setCurrentQuestionObject(questionComposite[0])
        # # Randomize question answers
        self.instanceQuestionObjectManager.randomizeQuestionAnswerLists()

    def handleVceFault(self, questionList):
        faultIndex = 0
        faultIndexList = []
        for questionPiece in questionList:
            # print("questionPiece: "+questionPiece)
            if("www.vceplus.com " in questionPiece):
                # print("hit")
                # self.vceFaultIndex = faultIndex
                faultIndexList.append(faultIndex)
                # self.isVceFault = True
            faultIndex += 1
        # print("vceFault in faultQuestionContainer: "+questionList[self.vceFaultIndex])
        # if(self.isVceFault):
        questionListRevised = []
        indexProcessing = 0
        faultFoundIndex = 0
        # for each piece, add to revised list, if fault, continue a do not add
        for questionPiece in questionList:
            if(faultFoundIndex <= len(faultIndexList)):
                if(indexProcessing == faultIndexList[faultFoundIndex]):
                    faultFoundIndex += 1
                    indexProcessing += 1
                    continue
            questionListRevised.append(questionPiece)
            indexProcessing += 1
        return questionListRevised

    def parseProblemLengthFault(self, questionList):
        # Handle if question problem over a certain length, if so, break with new line, to prevent question being cut off screen.
        pass

    def handleEmptyStringAtIndexFault(self, questionList):
        emptyStringAtIndexFaultIndex = 0
        newList = []
        for piece in questionList:
            if(len(piece)==0):
                continue
            newList.append(piece)
            emptyStringAtIndexFaultIndex +=1
        return newList

    def handleProblemConcatenationFault(self, questionPieceList):
        index = 0
        questionPieceContainer = []
        isBeginTextAppend = False
        strToAppend = ""
        for text in questionPieceList:
            # Within questionPiece range"QUESTION" - "A."
            # append question lines into individual lists
            if "A." in text:
                questionPieceContainer.append(strToAppend)
                strToAppend = ""
                isBeginTextAppend = False
                isOperationNormal = True
            if (isBeginTextAppend):
                strToAppend += text
            if "QUESTION" in text:
                isBeginTextAppend = True
                isOperationNormal = False
                questionPieceContainer.append(text)
            if(isOperationNormal):
                questionPieceContainer.append(text)
            index += 1
        return questionPieceContainer

    def processParseQuestionBank(self, questionSplitContainer):
        questionObjectComposite = []
        intervalIndex = 0
        isBeginAddQuestionObject = True
        isStartProcessing = False
        questionObjectListContainer = []
        questionObjectList = []
        # Split at question interval store in question set.
        # Iterate through question pieces, storing at interval of question found in string.
        currentQuestionSplitIndex = -1
        for questionPiece in questionSplitContainer:
            #If "QUESTION" start new data set
            if "QUESTION" in questionPiece:
                isStartProcessing = True
            if(isStartProcessing):
                if "QUESTION" in questionPiece:
                    # if(currentQuestionSplitIndex == -1):
                    currentQuestionSplitIndex += 1
                    questionObjectListContainer.append([])
                    # print("currentQuestionSplitIndex: " + str(currentQuestionSplitIndex))
                    # print("questionObjectListContainer: " + str(questionObjectListContainer))
                    questionObjectListContainer[currentQuestionSplitIndex].append(questionPiece)
                    continue
                    # if(isBeginAddQuestionObject):
                    # questionObjectList = []
                        # isBeginAddQuestionObject = False
                # print("currentQuestionSplitIndex: "+str(currentQuestionSplitIndex))
                questionObjectListContainer[(currentQuestionSplitIndex)].append(questionPiece)
        questionContainer =[]
        testIndex = 0
        for objectPieceList in questionObjectListContainer:
            possibleAnswerIndex = 0
            questionNumber = objectPieceList[0].split(' ')
            #create data object
            questionObj = QuestionObject()

            questionObj.setQuestionNumber(questionNumber[1])
            questionObj.setProblem(objectPieceList[1])
            questionPieceIndex = 0
            # Parse correct answer
            for questionPiece in objectPieceList:
                if (questionPiece.find("Correct") == 0):
                    answerUnparsed = questionPiece.split(":")
                    self.answerList = answerUnparsed[1].split(" ")
                    del self.answerList[0:1]
                questionPieceIndex += 1

            #Reiterate through answers, if matching correct answerList, set text as correct answer in object
            for answer in self.answerList:
                for questionPiece in objectPieceList:
                    questionPieceKey = self.answerList[self.answerListIndex] + "."
                    if (questionPiece.find(questionPieceKey) == 0):
                        answerListSplit = questionPiece.split(". ")
                        correctAnswerToAppend = answerListSplit[1]
                        questionObj.addCorrectAnswer(correctAnswerToAppend)
                self.answerListIndex +=1
            self.answerListIndex = 0
            questionObjectComposite.append(questionObj)

            # Parse answer list
            for val in objectPieceList:
                if(possibleAnswerIndex > 1):
                    # print(val)
                    if(val.find("Correct") == 0):
                        isContinueCalculating = False
                        break
                    questionObj.parseAnswer(val)
                possibleAnswerIndex += 1
            intervalIndex += 1
            testIndex += 1
            self.questionInteration += 1
        return questionObjectComposite

    def parseQuestionBankToCorrectFormat(self):
        f = open("testfile.txt", "r")
        stringText = f.read()
        self.parseForFaults(stringText)

    def parseForFaults(self, stringText):
        data_set_group_0_1 = stringText.split('QUESTION')
        data_set_group_0_1.pop(0)
        for val in data_set_group_0_1:
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
            self.isFaultDuplicantsAppended = True
        #     possibleAnswerIndex = 0
            self.faultCorrectedAtIndexContainer = []
            faultQuestionContainer = val.splitlines()
            faultQuestionContainer = list(filter(None, faultQuestionContainer))

            questionNumber = faultQuestionContainer[0].replace(' ', '')
            for questionPiece in faultQuestionContainer:
                self.questionPieceFaultIndex += 1
                if ("A. " in questionPiece or "B. " in questionPiece or "C. " in questionPiece or "D. " in questionPiece
                    or "E. " in questionPiece or "F. " in questionPiece or "G. " in questionPiece or "H. " in questionPiece):
                    # print("Possible duplicantAnswerOnSameLineFault at questionPieceFaultIndex: "+str(self.questionPieceFaultIndex))

                    #Main problems with fault handling
                    # if(self.listResultsDuplicantAnswerOnSameLineFaultCorrected)
                    self.listResultsDuplicantAnswerOnSameLineFaultCorrected.append(self.handleDuplicantAnswersOnSameLineFault(questionPiece))
                    # self.listResultsDuplicantAnswerOnSameLineFaultCorrected =
                    # print("listResultsDuplicantAnswerOnSameLineFaultCorrected: "+str(self.listResultsDuplicantAnswerOnSameLineFaultCorrected))
                    # faultCorrectedAtIndex

                    self.faultCorrectedAtIndexContainer.append(self.possibleDuplicantAnswerOnSameLineFaultCorrectedAtIndex)
                self.possibleDuplicantAnswerOnSameLineFaultCorrectedAtIndex += 1

            # print("faultCorrectedAtIndexContainer: "+str(self.faultCorrectedAtIndexContainer))
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
                        # print("self.isFaultDuplicantsAppended: "+str(self.isFaultDuplicantsAppended))

                        if(self.isFaultDuplicantsAppended):
                            for faultCorrected in self.listResultsDuplicantAnswerOnSameLineFaultCorrected:
                                # print("appending faultCorrected: "+str(faultCorrected))
                                for fault in faultCorrected:
                                    self.listFinalQuestionPieceResults.append(fault)
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
            # print(self.strPieceSpaceCorrectAnswerFault)

            #find index where correct answer piece, replace with fixed fault correct answer.
            self.listFinalQuestionPieceResults[self.spaceFaultQuestionPieceIndex] = "Correct Answer:"+self.strPieceSpaceCorrectAnswerFault
            # print("self.listFinalQuestionPieceResults"+str(self.listFinalQuestionPieceResults))

    def handleDuplicantAnswersOnSameLineFault(self, questionPiece):
        questionPieceListSplit = []
        questionPieceListSplit = questionPiece.split(" ")
        # # print("fixing duplicantAnswersOnSameLineFault: "+str(questionPiece))
        questionPieceSplitIndex = 0
        filterList1 = []
        newQuestionPieceList = []
        self.nextFilterPieceIndex = 0
        self.faultResolutionQueryStringContainer = []
        # self.nextFilterPieceIndex = 0
        for piece in questionPieceListSplit:
            # print("piece: " + piece)
            if ("A." in piece or "B." in piece or "C." in piece or "D." in piece
                or "E." in piece or "F." in piece or "G." in piece or "H." in piece):
                filterList1.append(questionPieceSplitIndex)
                # print("hit piece: " + piece)
            questionPieceSplitIndex += 1

        # print("filterList1: " + str(filterList1))
        # construct individual questions from split filter
        filterListIterationIndex = 0
        for filterIndex in filterList1:
            # print("SECOND INTERATION")
            self.isFirstRoundStrAddition = True
            currentFilterIndex = filterIndex
            questionString = ""
            # questionString = self.questionPieceListSplit[filterIndex]
            # print(questionString)
            # print("currentFilterIndex: " + str(currentFilterIndex))
            # print("filterListIterationIndex: " + str(filterListIterationIndex))
            # print("len(self.filterList1): " + str(len(self.filterList1)))

            if (filterListIterationIndex < (len(filterList1) - 1)):
                self.nextFilterPieceIndex = filterList1[filterListIterationIndex + 1]
                # print("nextFilterPieceIndex: " + str(nextFilterPieceIndex))

                # print("self.questionPieceListSplit: " + str(self.questionPieceListSplit))
                # print("currentFilterIndex: " + str(currentFilterIndex))
                # print("nextFilterPieceIndex: " + str(self.nextFilterPieceIndex))

                # continue to next stop point adding indexs of the questionPieceListSplit together,
                while (currentFilterIndex < self.nextFilterPieceIndex):
                    strToAdd = questionPieceListSplit[(currentFilterIndex)]
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
                    strToAdd = questionPieceListSplit[(currentFilterIndex)]
                    questionString += strToAdd
                    if (self.isFirstRoundStrAddition):
                        questionString += " "
                        self.isFirstRoundStrAddition = False
                    # print("questionString: " + str(questionString))
                    # print("currentFilterIndex: " + str(currentFilterIndex))
                    currentFilterIndex += 1

            self.faultResolutionQueryStringContainer.append(questionString)
            filterListIterationIndex += 1
            # print("Check test: "+str(self.faultResolutionQueryStringContainer))
        return self.faultResolutionQueryStringContainer


    def determineParseEntryBatchSizeValueIsValid(self):
        entryList = []
        whiteSpaceClearedList = []
        entryNumberString = self.instanceDisplayManager.entryNumberQuestions.get()
        # print(entryNumberString)
        if("-" in entryNumberString):
            entryList = entryNumberString.split("-")
            # Clear extra whitespace for entry index
            for val in entryList:
                whiteSpaceClearedList.append(val.replace(" ", ""))
            # print("lenwhiteSpaceClearedList: "+str(len(whiteSpaceClearedList)))
            # Handle two values on either side of "-"
            if(len(whiteSpaceClearedList) == 2):
                # Handle values are integers
                isValValidList = []
                for val in whiteSpaceClearedList:
                    isValValidList.append(self.validateIsNumber(val))
                # print(str(isValValidList))
                resultsFalseList = []
                for isValValid in isValValidList:
                    if (isValValid == False):
                        resultsFalseList.append(isValValid)
                if(len(resultsFalseList)):
                    # print("results false")
                    self.isEntryBatchSizeValid = False
                else:
                    # print("results are good: "+str(whiteSpaceClearedList))
                    # Handle second value is larger than first
                    val1 = int(whiteSpaceClearedList[0])
                    val2 = int(whiteSpaceClearedList[1])

                    integerTransformedList = [val1,val2]
                    if(val1 < val2 and val1 != 0):
                        # Handle if end index is within questionList
                        questionList = self.instanceQuestionObjectManager.getQuestionList()
                        if(val2 <= len(questionList)):
                            # Set self.batchRangeList that is used in future processing
                            self.batchRangeList = integerTransformedList
                            self.isEntryBatchSizeValid = True
                        else:
                            self.isEntryBatchSizeValid = False
                    else:
                        self.isEntryBatchSizeValid = False
            else:
                self.isEntryBatchSizeValid = False
        else:
            self.isEntryBatchSizeValid = False

    def validateIsNumber(self, val):
        try:
            int(val)
            return True
        except ValueError:
            return False

    def batchSizeTest(self):
        questionList = self.instanceQuestionObjectManager.getQuestionList()
        self.batchQuestionList =  []
        startIndex = self.batchRangeList[0]
        endIndex = self.batchRangeList[1]
        # If self.isEntryBatchSizeValid continue questionList to batchQuestionList process
        # Else entire list of questions becomes batchQuestionList
        if(self.isEntryBatchSizeValid):
            questionListIndex = 0
            # handle if end index is within questionList
            # if within start index
            while(questionListIndex < len(questionList)):
                if(questionListIndex >= startIndex and questionListIndex <= endIndex):
                    self.batchQuestionList.append(questionList[questionListIndex-1])
                questionListIndex += 1
        else:
            self.batchQuestionList = questionList
        # print("self.batchQuestionList: "+str(len(self.batchQuestionList)))
        # for questionObj in self.batchQuestionList:
        #     print(questionObj.getProblem())
        self.instanceQuestionObjectManager.setBatchSizeQuestionList(self.batchQuestionList)

    def testMode(self):
        self.isTestMode = True
        self.determineParseEntryBatchSizeValueIsValid()
        if(self.isEntryBatchSizeValid):
            self.batchSizeTest()
            # Handle isRandomization of question list selected
            if(self.instanceDisplayManager.isRandomizationCheckBoxIntVar.get() == 1):
                self.instanceQuestionObjectManager.randomizeQuestionList()
            self.instanceQuestionObjectManager.setCurrentQuestionObject(self.instanceQuestionObjectManager.getBatchSizeQuestionList()[0])
            self.instanceDisplayManager.displayQuestion()

    def learnMode(self):
        self.isLearnMode = True
        self.determineParseEntryBatchSizeValueIsValid()
        if (self.isEntryBatchSizeValid):
            self.batchSizeTest()
            # Handle isRandomization of question list selected
            if (self.instanceDisplayManager.isRandomizationCheckBoxIntVar.get() == 1):
                self.instanceQuestionObjectManager.randomizeQuestionList()
            self.instanceQuestionObjectManager.setCurrentQuestionObject(self.instanceQuestionObjectManager.getBatchSizeQuestionList()[0])
            self.instanceDisplayManager.displayQuestionLearnMode()

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

    def changeToNextQuestionLearnMode(self):
        # Handle on set nextQuestion
        self.instanceDisplayManager.showAnswerLearnModeLabelText = ""
        if (self.instanceQuestionObjectManager.processNextQuestion()):
            # Handle displayManager paint new question
            self.instanceDisplayManager.displayQuestionLearnMode()
        else:
            self.instanceDisplayManager.displayLearnModeRetakeScreen()

    def confirmAnswer(self):
        # Create answerBooleanList to be appended later to textAnswerList
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
        questionList = self.instanceQuestionObjectManager.getBatchSizeQuestionList()
        totalCountQuestions = len(questionList)
        for question in questionList:
            if(question.getIsAnsweredCorrectly()):
                self.correctQuestionAnsweredCount += 1
        percentageCorrect = (self.correctQuestionAnsweredCount / totalCountQuestions) * 100
        return percentageCorrect

    def getIsQuestionCorrectOutcome(self):
        return self.isQuestionCorrectOutcome

    def getInstanceQuestionObjectManager(self):
        return self.instanceQuestionObjectManager