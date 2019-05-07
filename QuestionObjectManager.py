# from Test import Test

class QuestionObjectManager:
    def __init__(self):
        self.ranomizedQuestionsList = []
        self.questionList = []

    #start on first question or randomize questions.
    #saving state of test completed
    #sampling or entirety
    #I want a 50 queston sample
    #I want to iterate through entire list

    def setQuestionList(self, questionList):
        self.questionList = questionList
    def getQuestionList(self):
        return self.questionList




    # def shuffleQuestionList(self):
    #     list = self.getQuestionList()#[20, 16, 10, 5];
    #     shuffle(list)
    #     print("Reshuffled list : ", list)
    #     self.setQuestionList(list)

    def calculateQuestionSuccess(self):
        self.associateQuestionAnswersWithRandomizedResults()




    def associateQuestionAnswersWithRandomizedResults(self):
        # It knows the current question, randomized question list, answer list,
        # Need selected answer positioning.

        self.getRanomizedQuestionList()

        #associate placement?
        #Or... check if match, check if match
            # position selected equates to answer list,
               # check if answerList selected matches currently selected.
                # currently selected returned as a list.



    def getCurrentQuestionObject(self):
        return self.currentQuestionObject
    def setCurrentQuestionObject(self, questionObject):
        self.currentQuestionObject = questionObject

    def randomizeQuestionList(self):
        shuffledList = shuffle(self.getRandomizedQuestionList())
        print("shuffle: " + str(shuffledList))
        return shuffledList
    def getRandomizedQuestionList(self):
        return self.randomizedQuestionsList
    def setRandomizedQuestionList(self, randomizedQuestionList):
        self.randomizedQuestionList = randomizedQuestionList

    # def randomizeQuestionAnswers(self, answerList):
    #     shuffledList = shuffle(answerList)
    #     print("shuffle: "+ str(shuffledList))
    #     return shuffledList
    def getOriginalAnswerFormation(self):
        pass


    def setOriginalQuestionList(self, question):
        pass
    def getOriginalQuestionList(self):
        pass
