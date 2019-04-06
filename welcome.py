# -*- coding: utf-8 -*-
import Tkinter as tk
from tkMessageBox import *
import os
import tkFileDialog
from EmotionDetection import WordMap

# initialise text file and value file to empty
textfile = ""
valuefile = ""

class WelcomeWindow(tk.Tk):

    def __init__(self, *args, **kwargs):


        # Call to __init__ of super class
        tk.Tk.__init__(self, *args, **kwargs)
        # change the default tk icon
        tk.Tk.iconbitmap(self, default="emotion.ico")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand="True")

        container.grid_rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # empty list - key & values
        self.frames = {}

        for F in (StartPage, Training):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # **************** Move movement showing on status bar for frame ****
            # frame.bind("<Motion>", mainframe_event)
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
        trainBtn = tk.Button(self, text="Training", width=13)
        trainBtn.grid(row=0, column=0, padx=40, pady=15)
        trainBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13))
        trainBtn.bind("<Motion>", train_event)

        # testing button
        testBtn = tk.Button(self, text="Testing", width=13)
        testBtn.grid(row=1, column=0, padx=40, pady=24)
        testBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13))
        testBtn.bind("<Motion>", test_event)

        # evaluate text button
        evalTextBtn = tk.Button(self, text="Evaluate Text", width=13)
        evalTextBtn.grid(row=2, column=0, pady=15)
        evalTextBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13))
        evalTextBtn.bind("<Motion>", eval_text_event)

        # ************************** button to the right ********************************

        # gui evaluation button
        guiEvalBtn = tk.Button(self, text="GUI Evaluation", width=13)
        guiEvalBtn.grid(row=0, column=1, padx=40)
        guiEvalBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12))
        guiEvalBtn.bind("<Motion>", gui_eval_event)

        # more information evaluation button
        moreInfoBtn = tk.Button(self, text="Information", width=13)
        moreInfoBtn.grid(row=1, column=1, padx=40)
        moreInfoBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12))
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

        # ************************* status bar *****************************
        status_bar_frame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        status_bar_frame.grid(row=4, column=0, columnspan=6, sticky="we")

        status_bar = tk.Label(status_bar_frame, text="status bar", bg="#dfdfdf")

        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        status_bar.config(anchor=tk.W, font=("Times", 11))
        status_bar.grid_propagate(0)
# ******************** End of Start Page *************************************

# ***************** Mouse movement(StartPage) for status bar **********************
def train_event(event): status_bar['text'] = 'Click to re-train the model'


def test_event(event): status_bar['text'] = 'Run the system and test its accuracy'


def eval_text_event(event): status_bar['text'] = "Evaluate input file that hasn't been pre-labelled"


def gui_eval_event(event): status_bar['text'] = 'Click to get emotion from text'


def info_event(event): status_bar['text'] = 'For more information'


def exit_event(event): status_bar['text'] = 'Close application'


def mainframe_event(event): status_bar['text'] = 'Click a button to continue'

# ********************************** End of mouse movements *********************************

# ************************************* load tweet text ************************************

# ************************************* End of load tweet text and value ************************************


# ************************ Read files from tweettext and tweetvalues file ****************
def train():
    global textFile, valueFile
    if valuefile and textfile is not None:
        reset = askokcancel("Reset training data", "Are you sure?")
        if reset is True:
            try:
                print("Loading input values into WordMap...\n")
                with open(textfile, 'r') as textFile:
                    with open(valuefile, 'r') as valueFile:
                        WordMap.buildWordMap(reset, textFile, valueFile)
                        progressBar()
            except IOError:
                print("File not found. Returning to main menu...\n")
        else:
            return False

    else:
        showerror('Error!', 'text file or value file not selected')

# ***************************** End of Read files from tweettext and tweetvalues file ****************


# *************************** Progress Bar Function ********************************

# *******************************************************************************************


# ******************************** Show training frame ****************************
class Training(tk.Frame):

    def __init__(self, parent, controller):
        # 'parent class' is 'WelcomeWindow'
        tk.Frame.__init__(self, parent, background='gray')
        global tweetTextLabel, tweetValuesLabel

        # ******************** tweet text button and entry *******************
        tweetTextBtn = tk.Button(self, text="Tweet text", width=12, command=tweetText)
        tweetTextBtn.grid(row=0, column=0, padx=10, pady=20)
        tweetTextBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12))

        tweetTextLabel = tk.Label(self, width=25)
        tweetTextLabel.grid(row=0, column=1, ipady=5, pady=20)
        tweetTextLabel.config(bd=2, font=("Arial ITALIC", 13))
        # ********************End of tweet Text button and entry *******************

        # ******************** tweet values button and entry *******************
        tweetValuesBtn = tk.Button(self, text="Tweet values", width=12, command=tweetValues)
        tweetValuesBtn.grid(row=3, column=0, pady=25)
        tweetValuesBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12))

        tweetValuesLabel = tk.Label(self, width=25)
        tweetValuesLabel.grid(row=3, column=1, ipady=5)
        tweetValuesLabel.config(bd=2, font=("Arial ITALIC", 13))
        # ********************************End of tweet values button and entry *************************

        # training button
        trainBtn = tk.Button(self, text="Train", width=13, command=train)
        trainBtn.grid(row=4, column=0)
        trainBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13))

        # testing button
        cancelBtn = tk.Button(self, text="Back", width=13, command=lambda: controller.show_frame(StartPage))
        cancelBtn.grid(row=4, column=1)
        cancelBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13))


# ******************************************** End of Training Frame ***************************************************

# ******************************** Show Testing frame ******************************************************************
# ********************************************* End of Testing Frame ***************************************************

# ********************************************* More Information message box *******************************************

# ********************************************* End of More Information ************************************************



# running the main class
root = WelcomeWindow()

# *********************** Menu Bar *********************************
# Insert a menu bar on the main window
menubar = tk.Menu(root)

# ************************ Create a menu button labeled "File" that brings up a menu *******************
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Quit', command=root.quit)

# ************* Event to show on status bar ************************
def print_event(): status_bar['text'] = 'Now Printing..........'


def save_event(): status_bar['text'] = 'Saving files...........'


# ******************** Creates  "File" Sub-menus ***************************
printStatus = filemenu.add_command(label='Print', command=print_event)
saveStatus = filemenu.add_command(label='Save', command=save_event)

# ************************* End of menu ************************************************************



# ********************* Centralise the window ****************************
window_height = 259
window_width = 445
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
