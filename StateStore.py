from Test import Test
class StateStore:
    def __init__(self):
        self.ranomizedQuestionsList = []
        self.testInstance = Test(self)
        self.testInstance.operate()
    def createTest(self):
        self.testInstance = Test(self)
        self.testInstance.operate()
    def getTest(self):
        return self.testInstance