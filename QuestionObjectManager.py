
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


    def createTest(self, caseType):
        if(0):
            # Support for sample sized test
            pass
        if (1):
            # print("questionList: "+str(self.getQuestionList()))
            # This is wrong it needs to be one individual question per.... Ah needs to randomize questions first.
            # Set randomized list at another time.
            # print("Question list1 " + str(self.getQuestionList()))
            self.shuffleQuestionList()

            testInstance = Test()

            print("Question list1 "+ str(self.getQuestionList()))
            testInstance.setQuestionList(self.getQuestionList())
            #
            print("Question list2 " + str(testInstance.getQuestionList()))
            testInstance.getQuestionList()


            testInstance.randomizeQuestionList()
            # testInstance.setCurrentQuestion()
            testInstance.startTest()



        if (2):
            # Support for loading test states from previous exams
            pass






            # print("shuffle: " + str(shuffledList))
                # print(question.getAnswerListComposite())
                # question.setRandomizedList(self.randomizeQuestionAnswers(question.getAnswerListComposite()))





            # self.setCurrentQuestion()

                # print(question.getRandomizedList())
                # print(question.getQuestionNumber())



    def shuffleQuestionList(self):
        list = self.getQuestionList()#[20, 16, 10, 5];
        shuffle(list)
        print("Reshuffled list : ", list)
        self.setQuestionList(list)

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


    def setCurrentQuestion(self, questionObject):
        pass
    def randomizeQuestionList(self):
        shuffledList = shuffle(self.getRandomizedQuestionList())
        print("shuffle: " + str(shuffledList))
        return shuffledList

    def getRandomizedQuestionList(self):
        return self.randomizedQuestionsList
    def setRandomizedQuestionList(self, randomizedQuestionList):
        self.randomizedQuestionList = randomizedQuestionList

    def randomizeQuestionAnswers(self, answerList):
        shuffledList = shuffle(answerList)
        print("shuffle: "+ str(shuffledList))
        return shuffledList
    def getOriginalAnswerFormation(self):
        pass


    def setOriginalQuestionList(self, question):
        pass
    def getOriginalQuestionList(self):
        pass
