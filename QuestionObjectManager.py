# from Test import Test
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

    # def processNextQuestionLearnMode(self):
    #     self.currentQuestionIndex += 1
    #     # Clear show label text
    #     self.showAnswerLearnModeLabelText = ""
    #     if (self.currentQuestionIndex < len(self.getBatchSizeQuestionList())):
    #         nextQuestion = self.getBatchSizeQuestionList()[self.currentQuestionIndex]
    #         self.setCurrentQuestionObject(nextQuestion)
    #         return True
    #     else:
    #         return False

    def randomizeQuestionList(self):
        shuffle(self.questionList)
        self.setCurrentQuestionObject(self.getQuestionList()[0])
    def randomizeQuestionAnswerLists(self):
        for questionObject in self.questionList:
            questionObject.randomizeAnswerList()

    def getRandomizedQuestionList(self):
        return self.randomizedQuestionsList
    def setRandomizedQuestionList(self, randomizedQuestionList):
        self.randomizedQuestionList = randomizedQuestionList
    def getOriginalAnswerFormation(self):
        pass
    def setOriginalQuestionList(self, question):
        pass
    def getOriginalQuestionList(self):
        pass
