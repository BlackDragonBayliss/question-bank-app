from random import shuffle

class QuestionObject:
    def __init__(self):
        self.correctAnswerList = []
        self.answerListComposite = []
        self.randomizedList = []
        self.isAnsweredCorrectly = False

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
    def addCorrectAnswer(self, addCorrectAnswer):
        self.correctAnswerList.append(addCorrectAnswer)
    def getCorrectAnswerList(self):
        return self.correctAnswerList
    def parseAnswer(self, answerString):
        answerList = answerString.split(". ")
        self.answerListComposite.append(answerList)

    def setAnswerListComposite(self, answerListComposite):
        self.answerListComposite = answerListComposite

    def getAnswerListComposite(self):
        return self.answerListComposite

    def getIsAnswered(self):
        return self.isAnswered
    def setIsAnswered(self, isAnswered):
        self.isAnswered = isAnswered

    def getIsAnsweredCorrectly(self):
        return self.isAnsweredCorrectly
    def setIsAnsweredCorrectly(self, isAnsweredCorrectly):
        self.isAnsweredCorrectly = isAnsweredCorrectly
    def randomizeAnswerList(self):
        shuffle(self.answerListComposite)