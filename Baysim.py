from tkinter import *
from random import shuffle
from DisplayManager import DisplayManager
from QuestionObjectManager import QuestionObjectManager
from QuestionObject import QuestionObject
from Test import Test

def main():
    print("Operating")
    instanceTest = Test()
    instanceTest.operate()

if __name__ == "__main__": main()
