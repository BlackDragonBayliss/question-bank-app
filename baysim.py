from tkinter import *

def main():
    f = open("demofile.txt", "r")
    stringText = f.read()

    questionObjectComposite = processParseQuestionBank(stringText)

    # print(questionObjectComposite[0].getCorrectAnswer())



    # for questionObj in questionObjectComposite:
    #     print(questionObj.getCorrectAnswer())
        # possibleAnswerList = questionObjectComposite[0].getAnswerListComposite()
        # correctAnswer = questionObjectComposite[0].getCorrectAnswer()

    # questionObjectComposite =

    possibleAnswerList = questionObjectComposite[0].getAnswerListComposite()
    correctAnswer = questionObjectComposite[0].getCorrectAnswer()

    # print(correctAnswer)

    initialQuestionObject = questionObjectComposite[0]

    # Radio button. create radiobutton by list entries
    # cb_strings = ['item 1', 'item 2', 'item 3', 'Correct']
    cb_strings = initialQuestionObject.getAnswerListComposite()

    root = Tk()
    root.geometry('1400x800')
    selectedAnswer = StringVar()
    selectedAnswer.set(cb_strings[0])
    def sel():
        print("You selected the option " + str(selectedAnswer.get()))

    questionLabel = Label(text=initialQuestionObject.getProblem()).pack(anchor=W)
    for item in cb_strings:
        textAssociation = item[0]+" "+item[1]
        print(textAssociation)
        radiobutton = Radiobutton(root, text=textAssociation, variable=selectedAnswer, value=textAssociation, command=sel)
        radiobutton.pack(anchor=W)

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

def createDisplayList(questionList):
    displayContainer = []
    for question in questionList:
        displayObject = "Question "+question[0]

        #associateAnswer with bound correct answer object
        #Append new line questionList attributes
        displayContainer.append(displayObject)
    return displayContainer


class QuestionObject:
    def __init__(self):
        self.correctAnswer = 'Error: Check \'Correct\' answer format'
        self.answerListComposite = []
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
