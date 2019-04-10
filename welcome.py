# -*- coding: utf-8 -*-

import Tkinter as tk
from tkMessageBox import *
import os
import tkFileDialog
from EmotionDetection import WordMap
from EmotionDetection import EvaluateText
from EmotionDetection.WordFilter import WordFilter
from EmotionDetection.EvaluateText import evaluateWord
from EmotionDetection.EvaluateText import guessEmotion
from math import log10

import codecs

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


# initialise text file and value file to empty
textfile = ""
valuefile = ""


class WelcomeWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        # Call to __init__ of super class
        tk.Tk.__init__(self, *args, **kwargs)

        global container

        # change the default tk icon
        tk.Tk.iconbitmap(self, default="emotion.ico")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand="True")

        container.grid_rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # empty list - key & values
        self.frames = {}

        for F in (StartPage, Training, Test, GUI, Evaluate):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # **************** Move movement showing on status bar for frame ****
            frame.bind("<Motion>", self_event)
            # *******************************************************************

        # show current frame
        self.show_frame(StartPage)

    # show_frame function. cont is the key
    def show_frame(self, cont):
        frame =self.frames[cont]
        frame.tkraise()


# ************************************** StartPage ***************************************************
class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        # 'parent class' is 'WelcomeWindow'
        tk.Frame.__init__(self, parent, background='gray')
        global status_bar
        # training button
        trainBtn = tk.Button(self, text="Training", width=13, command=lambda: controller.show_frame(Training))
        trainBtn.grid(row=0, column=0, padx=68, pady=25)
        trainBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')
        trainBtn.bind("<Motion>", train_event)

        # testing button
        testBtn = tk.Button(self, text="Testing", width=13, command=lambda: controller.show_frame(Test))
        testBtn.grid(row=1, column=0, pady=24)
        testBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')
        testBtn.bind("<Motion>", test_event)

        # evaluate text button
        evalTextBtn = tk.Button(self, text="Evaluate Text", width=13, command=lambda: controller.show_frame(Evaluate))
        evalTextBtn.grid(row=2, column=0, pady=25)
        evalTextBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')
        evalTextBtn.bind("<Motion>", eval_text_event)

        # ************************** button to the right ********************************

        # gui evaluation button
        guiEvalBtn = tk.Button(self, text="Word Prediction", width=13, command=lambda: controller.show_frame(GUI))
        guiEvalBtn.grid(row=0, column=1, padx=40)
        guiEvalBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12), activeforeground='gray')
        guiEvalBtn.bind("<Motion>", gui_eval_event)

        # more information evaluation button and function
        def moreInfo():
            text = '''
            °`°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,", "INFORMATION", ",¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°º¤ø
            EmotionDetection v1, sentiment analysis system operating off a multinomial
            Naive Bayes classifier. There are 13 possible labels that text can be
            labelled as, the emotions are :empty, sadness, enthusiasm, neutral, worry,
            surprise, love, fun, hate, happiness, boredom, relief and anger.\n
            1. Training - Generates a WordMap using a text file and emotion value file.
            A word map is required for both testing and evaluation.\n
            2. Testing - Run the system and test its accuracy by supplying correct 
            emotion values. Also produces reports and confusion plot\n
            3. Evaluate Text - Run the system without given values. Used to evaluate input
            file that has not been pre-labelled.
            '''
            showinfo('More Information', text)

        moreInfoBtn = tk.Button(self, text="Information", width=13, command=moreInfo)
        moreInfoBtn.grid(row=1, column=1, padx=40)
        moreInfoBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12), activeforeground='gray')
        moreInfoBtn.bind("<Motion>", info_event)

        # ****************** Close window through exit button *****************

        def exitBtnclose():
            answer = askokcancel("Exit application!", "Are you sure?")

            if answer is True:
                self.quit()
                return
            else:
                return False

        # Exit button
        exitBtn = tk.Button(self, text="Exit", width=13, command=exitBtnclose)
        exitBtn.grid(row=2, column=1, padx=40, pady=24)
        exitBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12), fg='red')
        exitBtn.bind("<Motion>", exit_event)

# ***************************************** End of Start Page **********************************************************

# ******************** Events for All Buttons and Frames and shows on the status bar ***********************************
def train_event(event): status_bar['text'] = 'Click to re-train the model'


def file_train_text_event(event): status_bar['text'] = 'Select text file for training'


def file_train_values_event(event): status_bar['text'] = 'Select value file for training'


def train_btn_event(event): status_bar['text'] = 'Reset  data and train'


def clear_event(event): status_bar['text'] = 'Clear selected file(s) to load another'


def back_welcome_event(event): status_bar['text'] = 'Go back to main menu'


def test_event(event): status_bar['text'] = 'Run the system and test its accuracy'


def file_test_text_event(event): status_bar['text'] = 'Select text file for testing'


def file_test_values_event(event): status_bar['text'] = 'Select the value file for testing'


def test_btn_event(event): status_bar['text'] = 'Runs a test on the selected files'


def eval_text_event(event): status_bar['text'] = "Evaluate input file that hasn't been pre-labelled"


def gui_eval_event(event): status_bar['text'] = 'Click to get emotion from text'


def predict_event(event): status_bar['text'] = 'Predicts the emotion from the inputted text'


def clear_predict_event(event): status_bar['text'] = 'Clears the text'


def file_eval_text_event(event): status_bar['text'] = 'Select a text file to evaluate'


def eval_event(event): status_bar['text'] = 'Evaluates a file that hasn\'t been pre-labelled'


def info_event(event): status_bar['text'] = 'For more information'


def exit_event(event): status_bar['text'] = 'Close application'


def self_event(event): status_bar['text'] = 'Click a button to continue'

# **************************************************** End of mouse movements ******************************************

# *************************************************** load tweet text for training *************************************
def tweetText():
    global textfile
    current_path = "./data/"
    textfile = tkFileDialog.askopenfilename(title='Choose text file',
                                            initialdir=current_path,
                                            filetypes=[("CSV files", "*.csv")])
    tweetTextLabel.config(text=os.path.basename(textfile))
# **************************************************** load tweet values for training **********************************
def tweetValues():
    global valuefile
    current_path = "./data/"
    valuefile = tkFileDialog.askopenfilename(title='Choose value file',
                                             initialdir=current_path,
                                             filetypes=[("CSV files", "*.csv")])

    tweetValuesLabel.config(text=os.path.basename(valuefile))
# ************************************* End of load tweet text and value for training **********************************

# **************************************************** Read files for training *****************************************
def train():
    global textFile, valueFile
    if valuefile and textfile is not None:
        reset = askokcancel("Reset training data", "Are you sure?")
        status_bar['text'] = "Loading input values into WordMap..."
        if reset is True:
            try:
                print("Loading input values into WordMap...\n")
                with codecs.open(textfile, 'rU', encoding='utf-8-sig', errors='ignore') as textFile:
                    with codecs.open(valuefile, 'rU', encoding='utf-8-sig', errors='ignore') as valueFile:

                        # codecs.open('utf8file.csv', 'rU', encoding='utf-8-sig')
                        # with open(textfile, 'r') as textFile:
                        # with open(valuefile, 'r') as valueFile:
                        WordMap.buildWordMap(reset, textFile, valueFile)
                        progressNotice()
            except IOError:
                print("File not found. Returning to main menu...\n")
        else:
            return False

    else:
        showerror('Error!', 'text file or value file not selected')
# ********************************************* End of Read files for training *****************************************


# *************************************************** progressNotice Function ******************************************
def progressNotice():
    showinfo('Info', "Process completed!")
# ************************************************ End of progressNotice ***********************************************


# ***************************************** Show training frame ********************************************************
class Training(tk.Frame):

    def __init__(self, parent, controller):
        # 'parent class' is 'WelcomeWindow'
        tk.Frame.__init__(self, parent, background='gray')
        global tweetTextLabel, tweetValuesLabel

        # ************************** tweet text button and entry *******************
        tweetTextBtn = tk.Button(self, text="Tweet text", width=12, command=tweetText)
        tweetTextBtn.grid(row=0, column=0, padx=5, pady=30)
        tweetTextBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12), activeforeground='gray')
        tweetTextBtn.bind("<Motion>", file_train_text_event)

        tweetTextLabel = tk.Label(self, width=25)
        tweetTextLabel.grid(row=0, column=1, ipady=5, pady=20)
        tweetTextLabel.config(bd=2, font=("Arial ITALIC", 13))
        # ********************End of tweet Text button and entry *******************

        # ******************** tweet values button and entry *******************
        tweetValuesBtn = tk.Button(self, text="Tweet values", width=12, command=tweetValues)
        tweetValuesBtn.grid(row=3, column=0, pady=28)
        tweetValuesBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12), activeforeground='gray')
        tweetValuesBtn.bind("<Motion>", file_train_values_event)

        tweetValuesLabel = tk.Label(self, width=25)
        tweetValuesLabel.grid(row=3, column=1, ipady=5)
        tweetValuesLabel.config(bd=2, font=("Arial ITALIC", 13))
        # ********************************End of tweet values button and entry *************************

        # training button
        trainBtn = tk.Button(self, text="Train", width=12, command=train)
        trainBtn.grid(row=4, column=0)
        trainBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), fg='red')
        trainBtn.bind("<Motion>", train_event)


        # testing button
        backBtn = tk.Button(self, text="Back", width=10, command=lambda: controller.show_frame(StartPage))
        backBtn.grid(row=4, column=2)
        backBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')
        backBtn.bind("<Motion>", back_welcome_event)

        # clear button for training frame
        def clearTraining():
            tweetTextLabel['text'] = ""
            tweetValuesLabel['text'] = ""

        clearTrainBtn = tk.Button(self, text="Clear", width=10, command=clearTraining)
        clearTrainBtn.grid(row=4, column=1)
        clearTrainBtn.config(bd=4, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')
        clearTrainBtn.bind("<Motion>", clear_event)
# ******************************************** End of Training Frame ***************************************************


# ********************************************* Show test frame ********************************************************

#  load tweet text for test ***************************************
def testTweetText():
    global textfile
    current_path = "./data/"
    textfile = tkFileDialog.askopenfilename(title='Choose text file', initialdir=current_path, filetypes=[("CSV files", "*.csv")])

    testTweetTxtLabel.config(text=os.path.basename(textfile))
# end of load tweet text for test **********************************


#  load tweet values for test **************************************
def testTweetValues():
    global valuefile
    current_path = "./data/"
    valuefile = tkFileDialog.askopenfilename(title='Choose value file', initialdir=current_path, filetypes=[("CSV files", "*.csv")])

    testTweetValuesLabel.config(text=os.path.basename(valuefile))
# end of load tweet values for test ***********************************


#  Read files for testing ************************************************
def test():
    global textFile, valueFile
    if valuefile and textfile is not None:
        try:
            print("\nRunning text evaluation...\n")
            with codecs.open(textfile, 'rU', encoding='utf-8-sig', errors='ignore') as textFile:
                with codecs.open(valuefile, 'rU', encoding='utf-8-sig', errors='ignore') as valueFile:
                    # codecs.open('utf8file.csv', 'rU', encoding='utf-8-sig')
                    # with open(textfile, 'r') as textFile:
                    # with open(valuefile, 'r') as valueFile:
                    EvaluateText.evaluate(textFile, valueFile)
                    progressNotice()
                    # print (reset, textFile, valueFile)
                    # print(textFile, valueFile)
        except IOError:
            showerror('File not found!', 'Check file')
    else:
        showerror('Error!', 'text file or value file not selected')
        # print "text file or value file not selected!"
        # return
# end of Read files for test ********************************************


class Test(tk.Frame):

    def __init__(self, parent, controller):
        # 'parent class' is 'WelcomeWindow'
        tk.Frame.__init__(self, parent, background='gray')
        global testTweetTxtLabel, testTweetValuesLabel

        # ************************** tweet text button and entry *******************
        testTweetTxtBtn = tk.Button(self, text="Tweet text", width=12, command=testTweetText)
        testTweetTxtBtn.grid(row=0, column=0, padx=5, pady=35)
        testTweetTxtBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12), activeforeground='gray')
        testTweetTxtBtn.bind("<Motion>", file_test_text_event)

        testTweetTxtLabel = tk.Label(self, width=25)
        testTweetTxtLabel.grid(row=0, column=1, ipady=5, pady=20)
        testTweetTxtLabel.config(bd=2, font=("Arial ITALIC", 13))
        # ********************End of tweet Text button and label *******************

        # *********************** tweet values button and label ********************
        testTweetValuesBtn = tk.Button(self, text="Tweet values", width=12, command=testTweetValues)
        testTweetValuesBtn.grid(row=3, column=0, pady=30)
        testTweetValuesBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12), activeforeground='gray')
        testTweetValuesBtn.bind("<Motion>", file_test_values_event)

        testTweetValuesLabel = tk.Label(self, width=25)
        testTweetValuesLabel.grid(row=3, column=1, ipady=5)
        testTweetValuesLabel.config(bd=2, font=("Arial ITALIC", 13))
        # ********************End of tweet values button and label *******************

        # test button
        testBtn = tk.Button(self, text="Test", width=12, command=test)
        testBtn.grid(row=4, column=0)
        testBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), fg='red')
        testBtn.bind("<Motion>", test_btn_event)

        # back button
        backBtn = tk.Button(self, text="Back", width=10, command=lambda: controller.show_frame(StartPage))
        backBtn.grid(row=4, column=2)
        backBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')
        backBtn.bind("<Motion>", back_welcome_event)

        # clear button for test frame
        def clearTest():
            testTweetTxtLabel['text'] = ""
            testTweetValuesLabel['text'] = ""

        clearTestBtn = tk.Button(self, text="Clear", width=8, command=clearTest)
        clearTestBtn.grid(row=4, column=1)
        clearTestBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')
        clearTestBtn.bind("<Motion>", clear_event)
# *********************************************** End of test Frame ****************************************************


# ********************************************* Show evaluate frame ****************************************************

#  load tweet text for test ***************************************
def evaluateTweetText():
    global textfile
    current_path = "./data/"
    textfile = tkFileDialog.askopenfilename(title='Choose text file for evaluation', initialdir=current_path, filetypes=[("CSV files", "*.csv")])

    evalTweetTxtLabel.config(text=os.path.basename(textfile))
# end of load tweet text for test **********************************


#  Read files for text evaluation ************************************************
def evaluate():
    global textFile
    if textfile is not None:
        try:
            print("\nRunning text evaluation...\n")
            with codecs.open(textfile, 'rU', encoding='utf-8-sig', errors='ignore') as textFile:
                # codecs.open('utf8file.csv', 'rU', encoding='utf-8-sig')
                # with open(textfile, 'r') as textFile:

                EvaluateText.evaluate(textFile)
                progressNotice()
        except IOError:
            showerror('TextFile not found!', 'Check file')
    else:
        showerror('Error!', 'text file not selected')

# end of Read files for evaluate ********************************************


class Evaluate(tk.Frame):

    def __init__(self, parent, controller):
        # 'parent class' is 'WelcomeWindow'
        tk.Frame.__init__(self, parent, background='gray')
        global evalTweetTxtLabel
        # ************************** tweet text button and entry *******************
        evalTweetTxtBtn = tk.Button(self, text="Text Evaluate", width=12, command=evaluateTweetText)
        evalTweetTxtBtn.grid(row=0, column=0, padx=5, pady=35)
        evalTweetTxtBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12), activeforeground='gray')
        evalTweetTxtBtn.bind("<Motion>", file_eval_text_event)

        evalTweetTxtLabel = tk.Label(self, width=25)
        evalTweetTxtLabel.grid(row=0, column=1, ipady=5, pady=20)
        evalTweetTxtLabel.config(bd=2, font=("Arial ITALIC", 13))
        # ********************End of tweet Text button and label *********************

        # test button
        evaluateBtn = tk.Button(self, text="Evaluate", width=12, command=evaluate)
        evaluateBtn.grid(row=4, column=0)
        evaluateBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), fg='red')
        evaluateBtn.bind("<Motion>", eval_event)

        # back button
        backBtn = tk.Button(self, text="Back", width=10, command=lambda: controller.show_frame(StartPage))
        backBtn.grid(row=4, column=2)
        backBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')
        backBtn.bind("<Motion>", back_welcome_event)

        # clear button for test frame
        def clearEvalText(): 
            evalTweetTxtLabel['text'] = ""

        clearEvalBtn = tk.Button(self, text="Clear", width=8, command=clearEvalText)
        clearEvalBtn.grid(row=4, column=1)
        clearEvalBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')
        clearEvalBtn.bind("<Motion>", clear_event)
# ********************************************* End of text evaluation Frame *******************************************


# ******************************************* show GUI Evaluate frame **************************************************
class GUI(tk.Frame):
    def __init__(self, parent, controller):

        # 'parent class' is 'WelcomeWindow'
        tk.Frame.__init__(self, parent, background='gray')
        inputLabel = tk.Label(self, text="Input text", bg='gray')
        inputLabel.grid(row=0, column=0, padx=3, pady=20, sticky="W")
        inputLabel.config(font=("Arial", 14))
        
        inputStr = tk.Entry(self, width=46)
        inputStr.grid(row=0, column=1, ipady=6, pady=10)
        inputStr.config(font=("Arial", 13))
        
        predictedLabel = tk.Label(self, text="Predicted:", bg='gray')
        predictedLabel.grid(row=1, column=0)
        predictedLabel.config(font=("Arial", 14))
        
        v = tk.StringVar()
        output = tk.Label(self, textvariable=v, font=("Arial", 15), bg='gray')
        output.grid(row=1, column=1, sticky="W",  pady=20)
        output.config(font=("Arial", 14))
        
        # predict function for predict button ************************************************
        def predButton():
            with open("./data/Priors.csv", "r") as priorFile:
                priors = priorFile.readline().strip().split(',')[1:]
                priors = [log10(float(x)) for x in priors]
            predValues = []
            unfound = []
        
            wf = WordFilter()
            words = inputStr.get()
            print "Input:", words
            words = wf.filterWords(words)
        
            print "Tokens:", words
            for word in words:
                try:
                    values = evaluateWord(word)
                except IOError:
                    print "WordMap not found. Please train system first.\n"
                    raise
                if values is not None:
                    predValues.append(values)
                else:
                    unfound.append(word)
        
            predValues = map(sum, zip(*predValues))
            predProb = map(sum, zip(priors, predValues))
            predEmotion = guessEmotion(predProb)
            v.set(predEmotion)
            print "Unfound:", unfound
            print "Prob:", ','.join(['%.2f ' % x for x in predProb])
            print
        
        # predict button *************************************************
        predictBtn = tk.Button(self, text="Predict", command=predButton)
        predictBtn.grid(row=2, column=1, sticky="nsew", pady=10)
        predictBtn.config(relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='red')
        predictBtn.bind("<Motion>", predict_event)

        # back button for GUI frame
        backBtn = tk.Button(self, text="Back to main menu", command=lambda: controller.show_frame(StartPage))
        backBtn.grid(row=3, column=1, sticky="nwes")
        backBtn.config(bd=2, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')
        backBtn.bind("<Motion>", back_welcome_event)

        # clear button for GUI frame
        def clearTextEntry():
            v.set("")
            inputStr.delete(0, 'end')
        
        # clear btn for GUI frame
        clearTestBtn = tk.Button(self, text="Clear", command=clearTextEntry)
        clearTestBtn.grid(row=2, column=0, padx=10)
        clearTestBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')
        clearTestBtn.bind("<Motion>", clear_predict_event)
# ******************************************* End of GUI Evaluate frame ************************************************


# ********************************************* running the main class *************************************************
root = WelcomeWindow()

# ******************************************************* Menu Bar *****************************************************
# Insert a menu bar on the main window
menubar = tk.Menu(root)

# ********************************* Creates a menu button labeled "File" and "Quit" ************************************
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Quit', command=root.quit)


# *************************************** Event to show on status bar **************************************************
def print_event(): status_bar['text'] = 'Now Printing................................'


def save_event(): status_bar['text'] = 'Saving files..................................'


# ********************************************* Creates  "File" Sub-menus **********************************************
printStatus = filemenu.add_command(label='Print', command=print_event)
saveStatus = filemenu.add_command(label='Save', command=save_event)

# ************************************************ End of menu *********************************************************

# ******************************************************** status bar **************************************************
status_bar_frame = tk.Frame(container, bd=1, relief=tk.SUNKEN)
status_bar_frame.grid(row=4, column=0, columnspan=6, sticky="we")

status_bar = tk.Label(status_bar_frame, text="Welcome", bg="#dfdfdf", anchor=tk.W)

status_bar.pack(side=tk.BOTTOM, fill=tk.X)
# status_bar.config(anchor=tk.W, font=("Times", 11))
status_bar.config(font=("Times", 11))
status_bar.grid_propagate(0)
# ********************************************* End of status bar ******************************************************

# ************************************************** Centralise the window *********************************************
window_height = 280
window_width = 520
# specifies width and height of window1
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# specifies the co-ordinates for the screen
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
root.title("Emotion Detector | Group 6")  # Add a title
root.resizable(False, False)  # This code helps to disable windows from resizing
root.config(menu=menubar)
root.mainloop()
