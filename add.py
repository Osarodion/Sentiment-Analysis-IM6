# ***************************************** Show test frame ********************************************************

# ************************************** load tweet text for test ***************************
def testTweetText():
    global textfile
    current_path = "./data/"
    textfile = tkFileDialog.askopenfilename(title='Choose text file', initialdir=current_path, filetypes=[("CSV files", "*.csv")])

    tweetTextLabel.config(text=os.path.basename(textfile))
# ************************************** load tweet text for test ***************************



# ****************************** load tweet values for test ***********************************
def testTweetValues():
    global valuefile
    current_path = "./data/"
    valuefile = tkFileDialog.askopenfilename(title='Choose value file', initialdir=current_path, filetypes=[("CSV files", "*.csv")])

    tweetValuesLabel.config(text=os.path.basename(valuefile))
# ****************************** End of load tweet values for test ***********************************


# ***************************** Read files test ****************************************
def test():
    global textFile, valueFile
    if valuefile and textfile is not None:
        try:
            print("\nRunning text evaluation...\n")
            with open(textfile, 'r') as textFile:
                with open(valuefile, 'r') as valueFile:
                    EvaluateText.evaluate(textFile, valueFile)
                    # progressBar()
                    # print (reset, textFile, valueFile)
                    # print(textFile, valueFile)
        except IOError:
            showerror('File not found!', 'Check file')
    else:
        showerror('Error!', 'text file or value file not selected')
        # print "text file or value file not selected!"
        # return
# ***************************** Read files test ****************************************


class Test(tk.Frame):

    def __init__(self, parent, controller):
        # 'parent class' is 'WelcomeWindow'
        tk.Frame.__init__(self, parent, background='gray')
        global testTweetTxtLabel, testTweetValuesLabel

        # ************************** tweet text button and entry *******************
        testTweetTxtBtn = tk.Button(self, text="Tweet text", width=12, command=testTweetText)
        testTweetTxtBtn.grid(row=0, column=0, padx=10, pady=20)
        testTweetTxtBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12))

        testTweetTxtLabel = tk.Label(self, width=25)
        testTweetTxtLabel.grid(row=0, column=1, ipady=5, pady=20)
        testTweetTxtLabel.config(bd=2, font=("Arial ITALIC", 13))
        # ********************End of tweet Text button and label *******************

        # ******************** tweet values button and label *******************
        testTweetValuesBtn = tk.Button(self, text="Tweet values", width=12, command=testTweetValues)
        testTweetValuesBtn.grid(row=3, column=0, pady=25)
        testTweetValuesBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 12))

        testTweetValuesLabel = tk.Label(self, width=25)
        testTweetValuesLabel.grid(row=3, column=1, ipady=5)
        testTweetValuesLabel.config(bd=2, font=("Arial ITALIC", 13))
        # ********************End of tweet values button and label *******************

        # test button
        testBtn = tk.Button(self, text="Test", width=13, command=test)
        testBtn.grid(row=4, column=0)
        testBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13))

        # cancel button
        cancelBtn = tk.Button(self, text="Cancel", width=13, command=lambda: controller.show_frame(StartPage))
        cancelBtn.grid(row=4, column=1)
        cancelBtn.config(bd=3, relief=tk.RAISED, font=("Arial Bold", 13))
# ******************************************** End of test Frame ***************************************************
