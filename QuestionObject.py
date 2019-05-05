
class QuestionObject:
    def __init__(self):
        self.correctAnswer = 'Error: Check \'Correct\' answer format'
        self.answerListComposite = []
        self.randomizedList = []

    def setRandomizedList(self, randomizedList):
        self.randomizedList = randomizedList
    def getRandomizedList(self):
        return self.randomizedList
    def setQuestionNumber(self, questionNumber):
        self.questionNumber = questionNumber
    def getQuestionNumber(self):
        return self.questionNumber
    def setProblem(self, problem):
        self.problem = problem
    def getProblem(self):
        return self.problem
    def setCorrectAnswer(self, correctAnswer):
        self.correctAnswer = correctAnswer
    def getCorrectAnswer(self):
        return self.correctAnswer
    def parseAnswer(self, answerString):
        answerList = answerString.split(". ")
        self.answerListComposite.append(answerList)
    def getAnswerListComposite(self):
        return self.answerListComposite

    def getIsAnswered(self):
        return self.isAnswered
    def setIsAnswered(self, isAnswered):
        self.isAnswered = isAnswered
    # def isCorrectAnswerListSubmited(self, questionList, answerList):
