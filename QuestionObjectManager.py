from random import shuffle
class QuestionObjectManager:
    def __init__(self):
        self.ranomizedQuestionsList = []
        self.questionList = []
        self.currentQuestionIndex = 0
    def setBatchSizeQuestionList(self, batchSizeQuestionList):
        self.batchSizeQuestionList = batchSizeQuestionList
    def getBatchSizeQuestionList(self):
        return self.batchSizeQuestionList

    def setOriginalIncorrectQuestionList(self, questionList):
        self.questionList = questionList
    def getOriginalIncorrectQuestionList(self):
        return self.questionList

    def setOriginalQuestionList(self, questionList):
        self.questionList = questionList
    def getOriginalQuestionList(self):
        return self.questionList
    def setQuestionList(self, questionList):
        self.questionList = questionList
    def getQuestionList(self):
        return self.questionList

    def getCurrentQuestionObject(self):
        return self.currentQuestionObject
    def setCurrentQuestionObject(self, questionObject):
        self.currentQuestionObject = questionObject
    def processNextQuestion(self):
        self.currentQuestionIndex +=1
        if (self.currentQuestionIndex < len(self.getBatchSizeQuestionList())):
            nextQuestion = self.getBatchSizeQuestionList()[self.currentQuestionIndex]
            self.setCurrentQuestionObject(nextQuestion)
            return True
        else:
            return False
    def setCurrentQuestionIndex(self, index):
        self.currentQuestionIndex = index
    def getCurrentQuestionIndex(self):
        return self.currentQuestionIndex


    def randomizeQuestionList(self):
        shuffle(self.batchSizeQuestionList)
        self.setCurrentQuestionObject(self.batchSizeQuestionList[0])
    def randomizeQuestionAnswerLists(self):
        for questionObject in self.questionList:
            questionObject.randomizeAnswerList()
    def getRandomizedQuestionList(self):
        return self.randomizedQuestionsList
    def setRandomizedQuestionList(self, randomizedQuestionList):
        self.randomizedQuestionList = randomizedQuestionList