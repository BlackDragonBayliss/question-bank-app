class FlashCard:
    def __init__(self, problem, answer):
        self.correctAnswerList = []
        self.answerListComposite = []
        self.isAnsweredCorrectly = False
        self.problem = problem
        self.answer = answer
    def setQuestionNumber(self, questionNumber):
        self.questionNumber = questionNumber
    def getQuestionNumber(self):
        return self.questionNumber
    def setProblem(self, problem):
        self.problem = problem
    def getProblem(self):
        return self.problem
    def setAnswer(self, answer):
        self.answer = answer
    def getAnswer(self):
        return self.answer
    def getIsAnswered(self):
        return self.isAnswered
    def setIsAnswered(self, isAnswered):
        self.isAnswered = isAnswered
    def getIsAnsweredCorrectly(self):
        return self.isAnsweredCorrectly
    def setIsAnsweredCorrectly(self, isAnsweredCorrectly):
        self.isAnsweredCorrectly = isAnsweredCorrectly