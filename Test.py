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
        self.incorrectQuestionStore = []
        self.possibleDuplicantAnswerOnSameLineFaultCorrectedAtIndex = 0
        self.duplicantAnswerOnSameLineFaultCorrectedAtIndex = 0
        self.questionPieceFaultIndex = 0

        self.selectedAnswerIndexTotal = 0
        self.answerListIndex = 0
        self.questionInteration = 0
        self.correctQuestionAnsweredCount = 0
        self.incorrectRetakeCount = 0
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
        self.isIncorrectRetaken = False
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
        stringText = self.pdfText
        questionSplitContainer = []
        stringTextContainer = []
        questionPieceContainer = []
        revisedEmptyStringQuestionPieceContainer = []
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

        # Intake feed, process into question bank
        questionComposite = self.processParseQuestionBank(revisedEmptyStringQuestionPieceContainer)

        # Handle if question problem over a certain length, if so, break with new line, to prevent question being cut off screen.
        questionCompositeRevised = self.handleProblemScreenCutOffFault(questionComposite)

        # Set question list
        self.instanceQuestionObjectManager.setQuestionList(questionCompositeRevised)

        # Randomize question answers
        self.instanceQuestionObjectManager.randomizeQuestionAnswerLists()

    def handleProblemScreenCutOffFault(self, questionComposite):
        splitList = []
        problemResolutionIndexList = []
        questionCompositeRevised = []
        indexOfProblemResolution = 0
        maximumStringScreenSize = 200
        cutScreenIndex = 0
        isCutOff = False
        isSplitProcessing = False

        for question in questionComposite:
            questionRevised = question
            problem = questionRevised.getProblem()
            #iterate through the problem letters to verify if split is needed
            for letterSpace in problem:
                if (cutScreenIndex % maximumStringScreenSize == 0 and cutScreenIndex != 0):
                    isCutOff = True
                if isCutOff:
                    if " " in letterSpace:
                        #append problem prev index of list.
                        split1 = problem[:cutScreenIndex]
                        split2 = problem[cutScreenIndex:]
                        splitList.append(split1)
                        splitList.append(split2)
                        isCutOff = False
                        isSplitProcessing = True
                cutScreenIndex += 1
            #for question problem, if split was performed, correct
            if isSplitProcessing:
                isSplitProcessing = False
                problemResolutionIndexList.append(indexOfProblemResolution)
                problemString = ""
                isInitial = True
                #append splitList pieces.
                for piece in splitList:
                    if isInitial:
                        problemString += piece
                        isInitial =  False
                        continue
                    problemString += "\n" + piece
                questionRevised.setProblem(problemString)
            isCutOff = False
            splitList = []
            cutScreenIndex = 0
            questionCompositeRevised.append(questionRevised)
            indexOfProblemResolution += 1
        return questionCompositeRevised

    def handleVceFault(self, questionList):
        faultIndex = 0
        faultIndexList = []
        for questionPiece in questionList:
            if("www.vceplus.com " in questionPiece):
                faultIndexList.append(faultIndex)
            faultIndex += 1
        questionListRevised = []
        indexProcessing = 0
        faultFoundIndex = 0
        #for each piece, add to revised list, if fault, continue a do not add
        for questionPiece in questionList:
            if(faultFoundIndex <= len(faultIndexList)):
                if(indexProcessing == faultIndexList[faultFoundIndex]):
                    faultFoundIndex += 1
                    indexProcessing += 1
                    continue
            questionListRevised.append(questionPiece)
            indexProcessing += 1
        return questionListRevised

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
            #within questionPiece range "QUESTION" - "A."
            #append question lines into individual lists
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
        #split at question interval store in question set.
        #iterate through question pieces, storing at interval of question found in string.
        currentQuestionSplitIndex = -1
        for questionPiece in questionSplitContainer:
            #if "QUESTION" start new data set
            if "QUESTION" in questionPiece:
                isStartProcessing = True
            if(isStartProcessing):
                if "QUESTION" in questionPiece:
                    currentQuestionSplitIndex += 1
                    questionObjectListContainer.append([])
                    questionObjectListContainer[currentQuestionSplitIndex].append(questionPiece)
                    continue
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
            #parse correct answer
            for questionPiece in objectPieceList:
                if (questionPiece.find("Correct") == 0):
                    answerUnparsed = questionPiece.split(":")
                    self.answerList = answerUnparsed[1].split(" ")
                    del self.answerList[0:1]
                questionPieceIndex += 1

            #reiterate through answers, if matching correct answerList, set text as correct answer in object
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

            #parse answer list
            for val in objectPieceList:
                if(possibleAnswerIndex > 1):
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
            self.faultCorrectedAtIndexContainer = []
            faultQuestionContainer = val.splitlines()
            faultQuestionContainer = list(filter(None, faultQuestionContainer))

            questionNumber = faultQuestionContainer[0].replace(' ', '')
            for questionPiece in faultQuestionContainer:
                self.questionPieceFaultIndex += 1
                if ("A. " in questionPiece or "B. " in questionPiece or "C. " in questionPiece or "D. " in questionPiece
                    or "E. " in questionPiece or "F. " in questionPiece or "G. " in questionPiece or "H. " in questionPiece):
                    #main problems with fault handling
                    self.listResultsDuplicantAnswerOnSameLineFaultCorrected.append(self.handleDuplicantAnswersOnSameLineFault(questionPiece))
                    self.faultCorrectedAtIndexContainer.append(self.possibleDuplicantAnswerOnSameLineFaultCorrectedAtIndex)
                self.possibleDuplicantAnswerOnSameLineFaultCorrectedAtIndex += 1
            #add all pieces to container, if piece is at index of fault corrected, add fault pieces corresponding
            indexAddlistFinalQuestionPieceResults = 0
            self.listFinalQuestionPieceResults = []
            for questionPiece in faultQuestionContainer:
                for faultIndex in self.faultCorrectedAtIndexContainer:
                    if(indexAddlistFinalQuestionPieceResults == faultIndex):
                        if(self.isFaultDuplicantsAppended):
                            for faultCorrected in self.listResultsDuplicantAnswerOnSameLineFaultCorrected:
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
            #handle correct answer spacing faults
            #parse correct answer
            self.spaceFaultQuestionPieceIndex = 0
            self.spaceFaultQuestionPieceList = []
            for questionPiece in self.listFinalQuestionPieceResults:
                if (questionPiece.find("Correct") == 0):
                    answerUnparsed = questionPiece.split(":")
                    self.spaceFaultQuestionPieceList = answerUnparsed[1].split(" ")
                    #remove leading white space index
                    del self.spaceFaultQuestionPieceList[0:1]
                    break
                self.spaceFaultQuestionPieceIndex += 1
            spaceCorrectAnswerFault = self.spaceFaultQuestionPieceList[0]
            if(len(spaceCorrectAnswerFault)):
                lengthIndex = 0
                while(lengthIndex < len(spaceCorrectAnswerFault)):
                    self.strPieceSpaceCorrectAnswerFault += " "+spaceCorrectAnswerFault[lengthIndex]
                    lengthIndex += 1
            #find index where correct answer piece, replace with fixed fault correct answer.
            self.listFinalQuestionPieceResults[self.spaceFaultQuestionPieceIndex] = "Correct Answer:"+self.strPieceSpaceCorrectAnswerFault

    def handleDuplicantAnswersOnSameLineFault(self, questionPiece):
        questionPieceListSplit = []
        questionPieceListSplit = questionPiece.split(" ")
        questionPieceSplitIndex = 0
        filterList1 = []
        newQuestionPieceList = []
        self.nextFilterPieceIndex = 0
        self.faultResolutionQueryStringContainer = []
        for piece in questionPieceListSplit:
            if ("A." in piece or "B." in piece or "C." in piece or "D." in piece
                or "E." in piece or "F." in piece or "G." in piece or "H." in piece):
                filterList1.append(questionPieceSplitIndex)
            questionPieceSplitIndex += 1
        #construct individual questions from split filter
        filterListIterationIndex = 0
        for filterIndex in filterList1:
            self.isFirstRoundStrAddition = True
            currentFilterIndex = filterIndex
            questionString = ""
            if (filterListIterationIndex < (len(filterList1) - 1)):
                self.nextFilterPieceIndex = filterList1[filterListIterationIndex + 1]
                #continue to next stop point adding indexs of the questionPieceListSplit together,
                while (currentFilterIndex < self.nextFilterPieceIndex):
                    strToAdd = questionPieceListSplit[(currentFilterIndex)]
                    questionString += strToAdd
                    if (self.isFirstRoundStrAddition):
                        questionString += " "
                        self.isFirstRoundStrAddition = False
                    currentFilterIndex += 1
            else:
                self.nextFilterPieceIndex = self.nextFilterPieceIndex + 1
                #continue to next stop point adding indexs of the questionPieceListSplit together,
                while (currentFilterIndex <= self.nextFilterPieceIndex):
                    strToAdd = questionPieceListSplit[(currentFilterIndex)]
                    questionString += strToAdd
                    if (self.isFirstRoundStrAddition):
                        questionString += " "
                        self.isFirstRoundStrAddition = False
                    currentFilterIndex += 1
            self.faultResolutionQueryStringContainer.append(questionString)
            filterListIterationIndex += 1
        return self.faultResolutionQueryStringContainer

    def determineParseEntryBatchSizeValueIsValid(self):
        entryList = []
        whiteSpaceClearedList = []
        entryNumberString = self.instanceDisplayManager.entryNumberQuestions.get()
        if("-" in entryNumberString):
            entryList = entryNumberString.split("-")
            #clear extra whitespace for entry index
            for val in entryList:
                whiteSpaceClearedList.append(val.replace(" ", ""))
            #handle two values on either side of "-"
            if(len(whiteSpaceClearedList) == 2):
                #handle values are integers
                isValValidList = []
                for val in whiteSpaceClearedList:
                    isValValidList.append(self.validateIsNumber(val))
                resultsFalseList = []
                for isValValid in isValValidList:
                    if (isValValid == False):
                        resultsFalseList.append(isValValid)
                if(len(resultsFalseList)):
                    self.isEntryBatchSizeValid = False
                else:
                    #handle second value is larger than first
                    val1 = int(whiteSpaceClearedList[0])
                    val2 = int(whiteSpaceClearedList[1])

                    integerTransformedList = [val1,val2]
                    if(val1 < val2 and val1 != 0):
                        #handle if end index is within questionList
                        questionList = self.instanceQuestionObjectManager.getQuestionList()
                        if(val2 <= len(questionList)):
                            #set self.batchRangeList that is used in future processing
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
        batchQuestionList =  []
        startIndex = self.batchRangeList[0]
        endIndex = self.batchRangeList[1]
        #if self.isEntryBatchSizeValid continue questionList to batchQuestionList process
        #else entire list of questions becomes batchQuestionList
        if(self.isEntryBatchSizeValid):
            questionListIndex = 0
            #handle if end index is within questionList
            #if within start index
            while(questionListIndex < len(questionList)):
                if(questionListIndex >= startIndex and questionListIndex <= endIndex):
                    batchQuestionList.append(questionList[questionListIndex-1])
                questionListIndex += 1
        else:
            batchQuestionList = questionList
        self.setQuestionObjectManagerBatchSizeTest(batchQuestionList)

    def setQuestionObjectManagerBatchSizeTest(self, batchQuestionList):
        self.instanceQuestionObjectManager.setBatchSizeQuestionList(batchQuestionList)

    def testMode(self):
        self.isTestMode = True
        self.determineParseEntryBatchSizeValueIsValid()
        if(self.isEntryBatchSizeValid):
            self.batchSizeTest()
            #handle isRandomization of question list selected
            if(self.instanceDisplayManager.isRandomizationCheckBoxIntVar.get() == 1):
                self.instanceQuestionObjectManager.randomizeQuestionList()
            self.instanceQuestionObjectManager.setCurrentQuestionObject(self.instanceQuestionObjectManager.getBatchSizeQuestionList()[0])
            self.instanceDisplayManager.displayQuestion()

    def learnMode(self):
        self.isLearnMode = True
        self.determineParseEntryBatchSizeValueIsValid()
        if (self.isEntryBatchSizeValid):
            self.batchSizeTest()
            #handle isRandomization of question list selected
            if (self.instanceDisplayManager.isRandomizationCheckBoxIntVar.get() == 1):
                self.instanceQuestionObjectManager.randomizeQuestionList()
            self.instanceQuestionObjectManager.setCurrentQuestionObject(self.instanceQuestionObjectManager.getBatchSizeQuestionList()[0])
            self.instanceDisplayManager.displayQuestionLearnMode()

    def createDisplayList(self, questionList):
        displayContainer = []
        for question in questionList:
            displayObject = "Question "+question[0]
            #append new line questionList attributes
            displayContainer.append(displayObject)
        return displayContainer

    def changeToNextQuestion(self):
        self.instanceQuestionObjectManager.getCurrentQuestionObject().setIsAnswered(True)
        #handle on set nextQuestion
        if(self.instanceQuestionObjectManager.processNextQuestion()):
        #handle displayManager paint new question
            self.instanceDisplayManager.displayQuestion()
        else:
            self.instanceDisplayManager.displayScoreScreen()

    def changeToNextQuestionLearnMode(self):
        #handle on set nextQuestion
        self.instanceDisplayManager.showAnswerLearnModeLabelText = ""
        if (self.instanceQuestionObjectManager.processNextQuestion()):
            #handle displayManager paint new question
            self.instanceDisplayManager.displayQuestionLearnMode()
        else:
            self.instanceDisplayManager.displayLearnModeRetakeScreen()

    def confirmAnswer(self):
        #create answerBooleanList to be appended later to textAnswerList
        answerBooleanList = []
        selectedAnswerIndex = 0
        for selectedAnswer in self.instanceDisplayManager.selectedAnswerList:
            if (selectedAnswer.get() == 1):
                answerBooleanList.append("1")
            else:
                answerBooleanList.append("0")
            selectedAnswerIndex += 1
        #append selectedBool to answerList
        appendTrueSelectedValueCount = 0
        for textAnswer in self.instanceDisplayManager.textAnswerList:
            if (len(textAnswer) == 3):
                del textAnswer[2:3]
            textAnswer.append(answerBooleanList[appendTrueSelectedValueCount])
            appendTrueSelectedValueCount += 1
        #instantiate is matching list
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
        #handle if no answers selected, default to answer being incorrect
        if(self.selectedAnswerIndexTotal != 0):
            if(len(self.answerMatchingList) == len(self.correctAnswerList) and self.selectedAnswerIndexTotal == len(self.correctAnswerList)):
                self.isQuestionCorrectOutcome = True
            else:
                self.isQuestionCorrectOutcome = False
                #handle incorrect question store
                self.handleIncorrectQuestionStore(self.instanceQuestionObjectManager.getCurrentQuestionObject())
        else:
            self.isQuestionCorrectOutcome = False
            #handle incorrect question store
            self.handleIncorrectQuestionStore(self.instanceQuestionObjectManager.getCurrentQuestionObject())

        self.instanceQuestionObjectManager.getCurrentQuestionObject().setIsAnsweredCorrectly(self.isQuestionCorrectOutcome)
        self.instanceDisplayManager.displayQuestionOutcomeScreen()
        self.isQuestionCorrectOutcome =  False
        self.answerMatchingList = []
        self.selectedAnswerIndexTotal = 0

    def handleIncorrectQuestionStore(self, question):
        print("appended question problem: "+question.getProblem())
        self.incorrectQuestionStore.append(question)

    def getIncorrectQuestionStore(self):
        return self.incorrectQuestionStore

    def retakeTestCurrentIncorrectQuestions(self):
        #take current incorrect
        self.isIncorrectRetaken = True
        print("isIncorrectRetaken: "+str(self.isIncorrectRetaken))
        print("incorrectQuestionStore: "+str(len(self.incorrectQuestionStore)))

        #retake test params retake
        #process retake, displayQuestions, with questionList set to incorrect question list.
        #go through process again.

        #set questionList
        setQuestionObjectManagerBatchSizeTest = self.incorrectQuestionStore

        #display

    def retakeTestOriginalIncorrectQuestions(self):
        self.incorrectRetakeCount += 1
        print(str(self.incorrectRetakeCount))
        #if initial, set current
        #take original incorrect

    def getIsIncorrectRetaken(self):
        return self.isIncorrectRetaken
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

    def resetGlobalVariablesForIncorrectQuestionRetake(self):
        self.incorrectRetakeCount = 0

    def resetGlobalVariablesForFullTestRetake(self):
        self.incorrectRetakeCount = 0