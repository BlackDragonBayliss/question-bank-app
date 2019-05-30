
class FlashCardComposite:
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