# ********************************************* Show evaluate frame ********************************************************

#  load tweet text for test ***************************************
def evaluateTweetText():
    global textfile
    current_path = "./data/"
    textfile = tkFileDialog.askopenfilename(title='Choose text file for evaluation', initialdir=current_path, filetypes=[("CSV files", "*.csv")])

    testTweetTxtLabel.config(text=os.path.basename(textfile))
# end of load tweet text for test **********************************


#  Read files for text evaluation ************************************************
def evaluate():
    global textFile
    if textfile is not None:
        try:
            print("\nRunning text evaluation...\n")
            with open(textfile, 'r') as textFile:

                EvaluateText.evaluate(textFile)
                progressNotice()
        except IOError:
            showerror('Text File not found!', 'Check file')
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

        evalTweetTxtLabel = tk.Label(self, width=25)
        evalTweetTxtLabel.grid(row=0, column=1, ipady=5, pady=20)
        evalTweetTxtLabel.config(bd=2, font=("Arial ITALIC", 13))
        # ********************End of tweet Text button and label *********************

        # test button
        evaluateBtn = tk.Button(self, text="Evaluate", width=12, command=evaluate)
        evaluateBtn.grid(row=4, column=0)
        evaluateBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='red')

        # back button
        backBtn = tk.Button(self, text="Back", width=10, command=lambda: controller.show_frame(StartPage))
        backBtn.grid(row=4, column=2)
        backBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')

        # clear button for test frame
        def clearEvalText():
            evalTweetTxtLabel['text'] = ""

        clearEvalBtn = tk.Button(self, text="Clear", width=8, command=clearEvalText)
        clearEvalBtn.grid(row=4, column=1)
        clearEvalBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13), activeforeground='gray')

# ********************************************* End of text evaluation Frame *******************************************
