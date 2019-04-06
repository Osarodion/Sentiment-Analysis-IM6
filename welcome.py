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

        for F in (StartPage):
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

        # testing button
        testBtn = tk.Button(self, text="Testing", width=13)
        testBtn.grid(row=1, column=0, padx=40, pady=24)
        testBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13))

        # evaluate text button
        evalTextBtn = tk.Button(self, text="Evaluate Text", width=13)
        evalTextBtn.grid(row=2, column=0, pady=15)
        evalTextBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13))

        # ************************** button to the right ********************************

        # gui evaluation button
        guiEvalBtn = tk.Button(self, text="GUI Evaluation", width=13)
        guiEvalBtn.grid(row=0, column=1, padx=40)
        guiEvalBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12))

        # more information evaluation button
        moreInfoBtn = tk.Button(self, text="Information", width=13)
        moreInfoBtn.grid(row=1, column=1, padx=40)
        moreInfoBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12))

        # ****************** Close window through exit button *****************
        # Exit button
        exitBtn = tk.Button(self, text="Exit", width=13)
        exitBtn.grid(row=2, column=1, padx=40, pady=24)
        exitBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12), fg='red')

        # ************************* status bar *****************************
        status_bar_frame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        status_bar_frame.grid(row=4, column=0, columnspan=6, sticky="we")

        status_bar = tk.Label(status_bar_frame, text="status bar", bg="#dfdfdf")

        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        status_bar.config(anchor=tk.W, font=("Times", 11))
        status_bar.grid_propagate(0)
# ******************** End of Start Page *************************************

# ***************** Mouse movement(StartPage) for status bar **********************
# ********************************** End of mouse movements *********************************

# ************************************* load tweet text ************************************

# ************************************* End of load tweet text and value ************************************


# ************************ Read files from tweettext and tweetvalues file ****************

# ***************************** End of Read files from tweettext and tweetvalues file ****************


# *************************** Progress Bar Function ********************************

# *******************************************************************************************


# ******************************** Show training frame ****************************
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