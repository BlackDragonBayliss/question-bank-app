from QuestionObjectManager import QuestionObjectManager
from QuestionObject import QuestionObject
class DisplayManager:
    def __init__(self):
        pass

    def operate(self):
        f = open("demofile.txt", "r")
        stringText = f.read()
        questionObjectManager = QuestionObjectManager()
        questionComposite = self.processParseQuestionBank(stringText)

        # print("question Composite: "+str(questionComposite))
        questionObjectManager.setQuestionList(questionComposite)
        print("question Composite in QOM: " + str(questionObjectManager.getQuestionList()))

        # possibleAnswerList = questionObjectComposite[0].getAnswerListComposite()
        # firstQuestion = questionObjectComposite[0]
        # correctAnswersList = firstQuestion.getCorrectAnswer()
        # questionList = firstQuestion.getAnswerListComposite()
        # print(correctAnswersList)
        # print(questionList)

        #construct question, randomizing answers
        questionObjectManager.createTest(1)




    def parseIntoQuestionObjectsList(self):
        pass
    def instantiateQuestion(self):
        pass
    def randomizeQuestion(self):
        pass

    def processParseQuestionBank(self, str_to_parse):
        data_set_group_0_1 = str_to_parse.split('QUESTION')

        # data_set_group_0_2 = []
        data_set_group_0_1.pop(0)
        questionObjectComposite = []
        intervalIndex = 0
        for val in data_set_group_0_1:
            # if(intervalIndex == 0):
            possibleAnswerIndex = 0
            questionContainer = val.splitlines()
            questionContainer = list(filter(None, questionContainer))
            questionNumber = questionContainer[0].replace(' ','')
            #create data object
            questionObj = QuestionObject()

            # print(questionContainer)

            questionObj.setQuestionNumber(questionNumber)
            questionObj.setProblem(questionContainer[1])
            questionPieceIndex = 0

            # Parse correct answer
            for questionPiece in questionContainer:
                if (questionPiece.find("Correct") == 0):
                    questionObj.setCorrectAnswer(questionPiece)
                questionPieceIndex += 1

            questionObjectComposite.append(questionObj)

            # Parse answer list
            for val in questionContainer:
                if(possibleAnswerIndex > 1):
                    # print(val)
                    if(val.find("Correct") == 0):
                        isContinueCalculating = False
                        break
                    questionObj.parseAnswer(val)
                possibleAnswerIndex += 1

            intervalIndex += 1

        return questionObjectComposite

    def createDisplayList(self, questionList):
        displayContainer = []
        for question in questionList:
            displayObject = "Question "+question[0]

            #associateAnswer with bound correct answer object
            #Append new line questionList attributes
            displayContainer.append(displayObject)
        return displayContainer

