from StateStore import StateStore
class StateStoreComposite:
    __instance = None
    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.stateStoreInstance = StateStore()
        return self.__instance
    def getState(self):
        return self.stateStoreInstance
    def refreshTestObject(self):
        self.getState().createTest()
        test = self.getState().getTest()
        test.operate()
    def startTest(self):
        test = self.getState().getTest()
        test.operate()