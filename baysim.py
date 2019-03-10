from tkinter import *

def main():
    # age = input("What is your age? ")
    # print("Your age is: ", age)
    f = open("demofile.txt", "r")
    stringText = f.read()

    questionObjectComposite = processParseQuestionBank(stringText)

    # displayList = createDisplayList(questionList)
    # print(questionList)
    # print(questionObjectComposite[0].getProblem())
    print(questionObjectComposite[0].getCorrectAnswer())
    # print(questionObjectComposite[0].getAnswerListComposite())

    # Radio button. create radiobutton by list entries
    cb_strings = ['item 1', 'item 2', 'item 3', 'Correct']
    # cb_strings = ['item 1', 'item 2', 'item 3', 'Correct']

    def sel():
        print("You selected the option " + str(selectedAnswer.get()))

    root = Tk()
    root.geometry('1400x800')
    selectedAnswer = StringVar()
    selectedAnswer.set(cb_strings[0])

    for item in cb_strings:
        radiobutton = Radiobutton(root, text=item, variable=selectedAnswer, value=item, command=sel)
        radiobutton.pack(anchor=W)

    correctAnswer = 'Error: Check \'Correct\' answer format'
    for val in cb_strings:
        if (val.find("Correct") == 0):
            correctAnswer = val
            break

    def confirmAnswer():
        if (correctAnswer == selectedAnswer.get()):
            print("Correct! selected: " + selectedAnswer.get())
        else:
            print("Answer: " + selectedAnswer.get() + " was incorrect, correct answer is: " + correctAnswer)

    confirmAnswerButton = Button(text="Confirm Answer", command=confirmAnswer)
    confirmAnswerButton.place(x=70, y=150)

    root.mainloop()





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
    questionObjectComposite = []
    intervalIndex = 0
    for val in data_set_group_0_1:
        if(intervalIndex == 0):
            questionContainer = val.splitlines()
            questionContainer = list(filter(None, questionContainer))
            questionNumber = questionContainer[0].replace(' ','')
            # data_set_group_0_2.append(questionContainer)
            # print(questionContainer)
            #create data object
            questionObj = QuestionObject()

            questionObj.setQuestionNumber(questionNumber)
            questionObj.setProblem(questionContainer[1])
            questionObj.setCorrectAnswer(questionContainer[(len(questionContainer)-1)])
            questionObjectComposite.append(questionObj)
            limitIndex = 0
            for val in questionContainer:
                if(limitIndex > 1):
                    # while(isContinueCalculating):
                    print(val)
                        # print(val.find("Correct"))
                    if(val.find("Correct") == 0):
                        isContinueCalculating = False
                        break
                    questionObj.parseAnswer(val)
                limitIndex += 1
            # print(questionObj.getAnswerListComposite())

    return questionObjectComposite

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
        # answerArray = []
        answerList = answerString.split(". ")
        self.appendAnswerList(answerList)
        # print(answerArray)
    def appendAnswerList(self, answerList):
        self.answerListComposite.append(answerList)
    def getAnswerListComposite(self):
        return self.answerListComposite

if __name__ == "__main__": main()
