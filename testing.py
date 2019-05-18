# # # # from tkinter import *
# # # #
# # # # root = Tk()
# # # # root.geometry('1400x800')
# # # #
# # # # entry = Entry(root)
# # # # entry.pack()
# # # #
# # # # def getInfo():
# # # #     print("the text is", entry.get())
# # # #
# # # # beginTest1Button = Button(text="Begin Test 1", command=getInfo)
# # # # beginTest1Button.place(x=10, y=100)
# # # #
# # # # root.mainloop()
# # #
# # #
# # #
# # #
# # #
# # # # /Users/CommanderCarr/PycharmProjects/question-bank-app
# # #
# # #
# # # import os, subprocess
# # # SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# # # args = ["/Users/CommanderCarr/PycharmProjects/question-bank-app",
# # #         '-enc',
# # #         'UTF-8',
# # #         "{}/my_pdf.pdf".format(SCRIPT_DIR),
# # #         '-']
# # # res = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # # output = res.stdout.decode('utf-8')
# # #
# # #
# # # import PyPDF2
# # # import os
# # #
# # # ENCRYPTED_FILE_PATH = './my_pdf.pdf'
# # # FILE_OUT_PATH = './my_pdf.pdf'
# # #
# # # PASSWORD=''
# # #
# # # with open(ENCRYPTED_FILE_PATH, mode='rb') as f:
# # #    reader = PyPDF2.PdfFileReader(f)
# # #    if reader.isEncrypted:
# # #        try:
# # #            reader.decrypt(PASSWORD)
# # #        except NotImplementedError:
# # #            command=f"qpdf --password='{PASSWORD}' --decrypt {ENCRYPTED_FILE_PATH} {FILE_OUT_PATH};"
# # #            os.system(command)
# # #            with open(FILE_OUT_PATH, mode='rb') as fp:
# # #                reader = PyPDF2.PdfFileReader(fp)
# # #                print(f"Number of page: {reader.getNumPages()}")
# # #
# # #
# # #
# # #
# # # # import PyPDF2
# # # # pdfFileObject = open('my_pdf.pdf', 'rb')
# # # # pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
# # # # count = pdfReader.numPages
# # # # for i in range(count):
# # # #     page = pdfReader.getPage(i)
# # # #     print(page.extractText())
# # #
# #
# #
# # import pdftotext
# #
# # # Load your PDF
# # with open("my_pdf.pdf", "rb") as f:
# #     pdf = pdftotext.PDF(f)
# #
# # # If it's password-protected
# # # with open("secure.pdf", "rb") as f:
# # #     pdf = pdftotext.PDF(f, "secret")
# #
# # # How many pages?
# # print(len(pdf))
# #
# # # Iterate over all the pages
# # # for page in pdf:
# # #     print(page)
# #
# # # Read some individual pages
# # print(pdf[5])
# # # print(pdf[1])
# #
# # # Read all the text into one string
# # # print("\n\n".join(pdf))
# #
# #
# # #Read all text
#
#
# ""
#
# questionList = []
# questionList.append("Test 1")
# questionList.append("  www.vceplus.com - VCE Exam Simulator - Download A+ VCE (latest) free Open VCE Exams - VCE to PDF Converter - PDF Online")
# questionList.append("Test 2")
#
# faultIndexList = [1]
# faultFoundIndex = 0
# faultInListIndex = 0
# while(faultFoundIndex < len(questionList)):
#     print(str(faultFoundIndex))
#     if(faultFoundIndex == faultIndexList[faultInListIndex]):
#         print("found error: "+questionList[faultFoundIndex])
#         questionList.pop(faultFoundIndex)
#         for piece in questionList:
#             print("Revised: "+piece)
#         faultInListIndex +=1
#         # for questionPiece in faultQuestionContainer:
#             # print("reworked QP: " + questionPiece)
#         # self.isVceFault = False
#
#     faultFoundIndex += 1
# # return questionList
#
#
#     # f = open("demofile.txt", "r")
#     # print(self.pdfText)