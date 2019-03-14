from tkinter import *

def main():
    f = open("demofile.txt", "r")
    stringText = f.read()

    questionObjectComposite = processParseQuestionBank(stringText)
    #
    # possibleAnswerList = questionObjectComposite[0].getAnswerListComposite()
    correctAnswersList = questionObjectComposite[0].getCorrectAnswer()
    # correctAnswerList = ["A","B","C"]
    # initialQuestionObject = questionObjectComposite[0]
    #
    # # Radio button. create radiobutton by list entries
    # # cb_strings = ['item 1', 'item 2', 'item 3', 'Correct']
    # cb_strings = initialQuestionObject.getAnswerListComposite()

    root = Tk()
    root.geometry('1400x800')

    questionlist = ["A", "B", "C"]
    selectedAnswerList = []
    textAnswerList = []
    buttonList = []
    def ShowChoice():
        # pass
        for selectedAnswer in selectedAnswerList:
            print(selectedAnswer.get())

    for counter, choiceText in enumerate(questionlist, 1):
        Label(root, text=choiceText).grid(row=counter, column=0)
        var = IntVar()
        for i in range(1, 2):
            textAnswerList.append([str(counter),choiceText])
            print("I value created: "+str(i))
            button = Radiobutton(root, variable=var, value=i, command=ShowChoice)
            button.grid(row=counter, column=i)
            buttonList.append(button)
            selectedAnswerList.append(var)





    correctAnswersList =  []# correctAnswersList


    answerMatchingComposite = []
    def confirmAnswer():
        # create answerBooleanList to be appended later to textAnswerList
        answerBooleanList = []
        selectedAnswerIndex = 0
        for selectedAnswer in selectedAnswerList:
            # print("hit "+str(selectedAnswer))
            # for each selected answer, if case met return true, continue
            # else return false
            if(selectedAnswer.get() == 1):
                # print("true at index: "+str(selectedAnswerIndex))
                answerBooleanList.append("1")
            else:
                answerBooleanList.append("0")
            selectedAnswerIndex += 1



        #append is selected
        appendTrueSelectedValueCount = 0
        for textAnswer in textAnswerList:
            if (len(textAnswer) == 3):
                print("I'm at index 3")
                del textAnswer[2:3]
            textAnswer.append(answerBooleanList[appendTrueSelectedValueCount])
            appendTrueSelectedValueCount += 1
        # print(selectedAnswerList)
        print(textAnswerList)
        print(str(len(textAnswerList)))





        # instantiate is matching list
        for textAnswer in textAnswerList:
            correctAnswerIndex = 0
            answerMatchingList = [textAnswer]
            answerMatchingComposite.append(answerMatchingList)
            selectedAnswerText = textAnswer[1]

            for correctAnswer in correctAnswerList:
                if(selectedAnswerText == correctAnswer):
                    isAnswerMatching = True
                else:
                    isAnswerMatching = False
                answerMatchingList.append(isAnswerMatching)
        print(textAnswerList)
        print(answerMatchingComposite)

        # calculate are answers correct


        # filter isAnswerMatchingList, if isNotTrue found then tag answer as incorrect.
        # Case in which success? Case in which fail?
        # Given that all answers in correct answer list criteria need to be met, or wrong.
            # Also not too many answers given, or wrong answers selected.
            # Perhaps finding where criteria is not met, and if found then wrong.

            # iterate through corr
                # print(correctAnswer)

        selectedChoices = []
        for selectedAnswer in selectedAnswerList:
            # print(selectedAnswer.get())
            selectedChoices.append(selectedAnswer.get())
        print(selectedChoices)


        # selectedChoices = [0,0,0,0,1,1,0,0]
        answersList = [1,1,1,0,0,0,0,0]

        # index = 0
        # while(index < len(selectedChoices)):
        #     if(selectedChoices[index] == answersList[index]):
        #         print("true")
        #     else:
        #         print("false")
        #     index += 1



    def deselectAnswers():
        for selectedAnswer in selectedAnswerList:
            selectedAnswer.set(0)

        print(textAnswerList)
        print(str(len(textAnswerList)))

    deselectOptionsButton = Button(text="Deselect Answers", command=deselectAnswers)
    deselectOptionsButton.place(x=70, y=200)

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

class QuestionObjectComposite:
    def __init__(self):
        ranomizedQuestionsList = []

    def randomizeQuestions(self):
        # getOriginalAnswerFormation()
        pass
    def getOriginalAnswerFormation(self):
        pass

    # self.ranomizedAnswersList = mixed
    # answers

    def getRanomizedQuestionsList(self):
        return self.ranomizedQuestionsList
    def setOriginalQuestionList(self, question):

        pass
    def getOriginalQuestionList():
        pass
if __name__ == "__main__": main()
