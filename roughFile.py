from Tkinter import *


from EmotionDetection.WordFilter import WordFilter
from EmotionDetection.EvaluateText import evaluateWord
from EmotionDetection.EvaluateText import guessEmotion
from math import log10

window = Tk()  # Create instance
window.title("Emotion Detector | Group 6")  # Add a title
window.resizable(False, False)  # This code helps to disable windows from resizing


# ************************* Main Frame *****************************
mainFrame = Frame(window, width=520, height=280, bg='gray', bd=2, relief=GROOVE)
mainFrame.pack(fill=X, side=TOP)
mainFrame.grid_propagate(0)  # don't shrink


# ************************* Status Frame *****************************
# statusFrame = Frame(window, height=50, bd=1, relief=SUNKEN)
# statusFrame.pack(fill=X, side=BOTTOM)
# statusFrame.grid_propagate(0)  # don't shrink


# # ******************************************* show GUI Evaluate frame **************************************************
# inputLabel = Label(mainFrame, text="Input text", bg='gray')
# inputLabel.grid(row=0, column=0, padx=3, pady=20, sticky="W")
# inputLabel.config(font=("Arial", 14))
#
#
# inputStr = Entry(mainFrame, width=46)
# inputStr.grid(row=0, column=1, ipady=6, pady=10)
# inputStr.config(font=("Arial", 13))
#
# predictedLabel = Label(mainFrame, text="Predicted:", bg='gray')
# predictedLabel.grid(row=1, column=0)
# predictedLabel.config(font=("Arial", 14))
#
# v = StringVar()
# output = Label(mainFrame, textvariable=v, font=("Arial", 15), bg='gray')
# output.grid(row=1, column=1, sticky="W",  pady=20)
# output.config(font=("Arial", 14))
#
#
# # predict function************************************************
# def predButton():
#     with open("./data/Priors.csv", "r") as priorFile:
#         priors = priorFile.readline().strip().split(',')[1:]
#         priors = [log10(float(x)) for x in priors]
#     predValues = []
#     unfound = []
#
#     wf = WordFilter()
#     words = inputStr.get()
#     print "Input:", words
#     words = wf.filterWords(words)
#
#     print "Tokens:", words
#     for word in words:
#         try:
#             values = evaluateWord(word)
#         except IOError:
#             print "WordMap not found. Please train system first.\n"
#             raise
#         if values is not None:
#             predValues.append(values)
#         else:
#             unfound.append(word)
#
#     predValues = map(sum, zip(*predValues))
#     predProb = map(sum, zip(priors, predValues))
#     predEmotion = guessEmotion(predProb)
#     v.set(predEmotion)
#     print "Unfound:", unfound
#     print "Prob:", ','.join([('%.2f ') % x for x in predProb])
#     print
#
#
# # predict button *************************************************
# predictBtn = Button(mainFrame, text="Predict", command=predButton)
# predictBtn.grid(row=2, column=1, sticky="nsew", pady=10)
# predictBtn.config(relief=RAISED, font=("Arial Bold", 14), activeforeground='red')
#
# # back button for GUI frame
# backBtn = Button(mainFrame, text="Back to main menu")
# backBtn.grid(row=3, column=1, sticky="nwes")
# backBtn.config(bd=2, relief=RAISED, font=("Arial Bold", 14), activeforeground='gray')
#
#
# # clear button for GUI frame
# def clearTextEntry():
#     v.set("")
#     inputStr.delete(0, 'end')
#
#
# # clear btn for GUI frame
# clearTestBtn = Button(mainFrame, text="Clear", command=clearTextEntry)
# clearTestBtn.grid(row=2, column=0, padx=10)
# clearTestBtn.config(bd=3, relief=RAISED, font=("Arial Bold", 13), activeforeground='gray')
# ******************************************* End of GUI Evaluate frame ************************************************


# ******************** Centralise Window **************************
window_height = 280
window_width = 520
# specifies width and height of window1
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# specifies the co-ordinates for the screen
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))




window.mainloop()
