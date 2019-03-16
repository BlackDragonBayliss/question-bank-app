from tkinter import *
from random import shuffle

def main():
    f = open("demofile.txt", "r")
    stringText = f.read()

    questionObjectManager = QuestionObjectManager()
    questionComposite = processParseQuestionBank(stringText)

    print("question Composite: "+str(questionComposite))
    questionObjectManager.setQuestionList(questionComposite)

    # possibleAnswerList = questionObjectComposite[0].getAnswerListComposite()
    # firstQuestion = questionObjectComposite[0]
    # correctAnswersList = firstQuestion.getCorrectAnswer()
    # questionList = firstQuestion.getAnswerListComposite()
    # print(correctAnswersList)
    # print(questionList)

    #construct question, randomizing answers
    questionObjectManager.createTest(False)"

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
            # print("I value created: "+str(i))
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


    # def isCorrectAnswerListSubmited(self, questionList, answerList):


class QuestionObjectManager:
    def __init__(self):
        ranomizedQuestionsList = []
        questionList = []

    #start on first question or randomize questions.
    #saving state of test completed
    #sampling or entirety
    #I want a 50 queston sample

    #I want to iterate through entire list,
    def createTest(self, isSample):
        if(isSample):
            pass
        else:
            print("questionList: "+str(self.getQuestionList()))
            for question in self.getQuestionList():
                print(question.getAnswerListComposite())

                question.setRandomizedList(self.randomizeQuestionAnswers(question.getAnswerListComposite()))
                # print(question.getRandomizedList())
                # print(question.getQuestionNumber())

    def createQuestion(self):
        pass

    def setQuestionList(self, questionList):
        self.questionList = questionList
    def getQuestionList(self):
        return self.questionList
    def setCurrentQuestion(self, questionObject):
        pass
    def randomizeQuestions(self):
        # getOriginalAnswerFormation()
        pass
    def randomizeQuestionAnswers(self, answerList):
        shuffledList = shuffle(answerList)
        print("shuffle: "+ str(shuffledList))
        return shuffledList
    def getOriginalAnswerFormation(self):
        pass

    def getRanomizedQuestionsList(self):
        return self.ranomizedQuestionsList
    def setOriginalQuestionList(self, question):

        pass
    def getOriginalQuestionList():
        pass
if __name__ == "__main__": main()
