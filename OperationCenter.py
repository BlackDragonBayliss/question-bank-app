# import aiohttp
# import asyncio
# from time import sleep
# from threading import Timer
# from HTTP_Utility import HTTP_Utility
# from Top_Stock_Monument_Composite import Top_Stock_Monument_Composite
# from Stock_Composite import Stock_Composite
# from Request_Factory import Request_Factory
# from TypeConverter import TypeConverter
# from Task_Master import Task_Master
# from Thread_Factory import Thread_Factory
# from Perpetual_Timer import Perpetual_Timer
# from Thread_Manager import Thread_Manager
# from Stock_Composite_Manager import Stock_Composite_Manager
# from Data_Manager_Action import Data_Manager_Action
# from Time_Manager import Time_Manager
# from Time_Data_Set_Manager import Time_Data_Set_Manager
# from Node_Manager import Node_Manager
# from Day_Decision_Process_Action_Manager import Day_Decision_Process_Action_Manager
# from Stock_Statistics_Composite import Stock_Statistics_Composite
# from Trade_Manager import Trade_Manager
# from Odin_Algorithm import Odin_Algorithm
# from Data_Manager_Request_Bundler import Data_Manager_Request_Bundler
# from Scraper_Manager import Scraper_Manager


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
    internalIndex = 0
    for val in data_set_group_0_1:
        questionContainer = val.splitlines()
        data_set_group_0_2.append(questionContainer)
        internalIndex += 1

    return data_set_group_0_2

def createDisplayList(questionList):
    displayContainer = []
    for question in questionList:
        displayObject = "Question "+question[0]
        #Append new line questionList attributes
        displayContainer.append(displayObject)
    return displayContainer

if __name__ == "__main__": main()





# class OperationCenter:
#     list_stock_composite = []
#     list_top_stock_symbols = []
#     list_top_stock_composite = []
#     list_data_managers = []
#     list_extended_data_manager = []
#     list_chosen_data_manager = []
#     list_bought_data_manager = []
#
#     stock_composite_generation_iteration = 0
#     top_stock_chosen = 0
#     __instance = None
#
#     def __new__(self):
#         if self.__instance == None:
#             self.__instance = object.__new__(self)
#             self.typeConverter = TypeConverter()
#         return self.__instance
#
#     def process_main_process_loop(self):
#         print("start")
#         self.time_data_set_manager.init_time_monitoring(self)
#         self.data_manager_request_bundler.setup_data_manager_request_bundler(self, self.get_time_data_set_manager())
#
#         self.main_process_loop()
#     def main_process_loop(self):
#         self.perpetual_timer_main_process_loop.setup_timer_stock(1, 1000000, self.main_loop, 'main_process_loop')
#
#     def main_loop(self):
#         if (self.is_start_yet_to_be_initiated and self.calculate_time_delimiter_start()):
#             self.process_async_top_stock_phase1_internal()
#             self.is_start_yet_to_be_initiated = False
#
#         if(self.is_scrape_yet_to_be_initiated and self.calculate_time_delimiter_process_scrape_top_stock_list_dow_volume_industry()):
#             self.initiate_process_top_stocks_scrape()
#             self.is_scrape_yet_to_be_initiated = False
#
#         if (self.is_top_stock_bird_yet_to_be_initiated and self.calculate_time_delimiter_top_stock_bird()):
#             self.initiate_process_top_stock_bird()
#             self.is_top_stock_bird_yet_to_be_initiated = False
#
#     def intakeUserInput(self, input):
#         # loop = asyncio.new_event_loop()
#         # asyncio.set_event_loop(loop)
#         # response = loop.run_until_complete(self.node_manager.async_bird_messenger_top_stock_process_complete());
#         self.typeConverter.processParseQuestionBank()
#         print(input)
#
#     def processParseQuestionBank(self, str_to_parse, operationCenter):
#         data_set_group_0_1 = str_to_parse.split('</quotetype>')
#         data_set_group_0_2 = data_set_group_0_1[1].split('</quotetype>')
#         data_set_group_0_3 = data_set_group_0_2[0].split('</quotes>')
#         data_set_group_0_4 = data_set_group_0_3[0].split('</quote>')
#         for val in data_set_group_0_4:
#             data_set_group_1_2 = val.split('<symbol>');
#             data_set_group_2_2 = val.split('<pchg>');
#             data_set_group_3_2 = val.split('<pcls>');
#             data_set_group_4_2 = val.split('<last>');
#             data_set_group_5_2 = val.split('<bid>');
#             data_set_group_6_2 = val.split('<ask>');
#
#             data_set_group_1_3 = data_set_group_1_2[1].split('</symbol');
#             data_set_group_2_3 = data_set_group_2_2[1].split('</pchg');
#             data_set_group_3_3 = data_set_group_3_2[1].split('</pcls');
#             data_set_group_4_3 = data_set_group_4_2[1].split('</last');
#             data_set_group_5_3 = data_set_group_5_2[1].split('</bid');
#             data_set_group_6_3 = data_set_group_6_2[1].split('</ask');
#             stock_created = Stock()
#             stock_created.set_sym(str(data_set_group_1_3[0]))
#             stock_created.set_pchg(float(data_set_group_2_3[0]))
#             stock_created.set_pcls(float(data_set_group_3_3[0]))
#             stock_created.set_last(float(data_set_group_4_3[0]))
#             stock_created.set_bid(float(data_set_group_5_3[0]))
#             stock_created.set_ask(float(data_set_group_6_3[0]))

