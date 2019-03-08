
def main():
    # age = input("What is your age? ")
    # print("Your age is: ", age)
    f = open("demofile.txt", "r")
    stringText = f.read()

    questionList = processParseQuestionBank(stringText)

    displayList = createDisplayList(questionList)
    print(displayList)


def parseIntoQuestionObjectsList():
    pass
def instantiateQuestion():
    pass
def randomizeQuestion():
    pass

def processParseQuestionBank(str_to_parse):
    data_set_group_0_1 = str_to_parse.split('QUESTION')

    data_set_group_0_2 = []
    data_set_group_0_1.pop(0)
    intervalIndex = 0
    for val in data_set_group_0_1:
        if(intervalIndex == 0):
            questionContainer = val.splitlines()
            questionContainer = list(filter(None, questionContainer))
            data_set_group_0_2.append(questionContainer)
            print(questionContainer)
        #create data object
            questionObj = QuestionObject()
            internalIndex = 2
            limitIndex = 0
            for val in questionContainer:
                if(limitIndex > 1):
                    # while(isContinueCalculating):
                    questionObj.parseAnswer(val)
                    print(val)
                        # print(val.find("Correct"))
                    if(val.find("Correct") == 0):
                        isContinueCalculating = False
                        break
                limitIndex += 1
                intervalIndex += 1
            print(questionObj.getAnswerListComposite())

    return data_set_group_0_2

def createDisplayList(questionList):
    displayContainer = []
    for question in questionList:
        displayObject = "Question "+question[0]

        #associateAnswer with bound correct answer object
        #Append new line questionList attributes
        displayContainer.append(displayObject)
    return displayContainer


class QuestionObject:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.answerListComposite = []
        return self.__instance

    def setQuestionNumber(self, problem):
        self.problem = problem
    def getQuestionNumber(self):
        return self.problem
    def setProblem(self, problem):
        self.problem = problem
    def getProblem(self):
        return self.problem
    def parseAnswer(self, answerString):
        # answerArray = []
        answerList = answerString.split(". ")
        self.appendAnswerList(answerList)
        # print(answerArray)
    def appendAnswerList(self, answerList):
        self.answerListComposite.append(answerList)
    def getAnswerListComposite(self):
        return self.answerListComposite
    def print(self):
        print("hey hey")

if __name__ == "__main__": main()
