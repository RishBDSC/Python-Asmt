#This is my Final code for the physics quiz
#It combines all the components together and switches the frames

#importing tkinter and messagebox
from tkinter import *

from tkinter import messagebox as mb #importing messagebox for the end of quiz score


#configuring the window (root)
root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("800x500")
root.resizable(0,0)
root.title("Physics Quiz")

#the different frames
user_details = Frame(root)
instructions = Frame(root)
quiz = Frame(root)
play_again = Frame(root)

#making the function for switching frames
for frame in (user_details, instructions, quiz, play_again):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(user_details)

#==================== User details =====================

#configuring the background colour of the user_details frame
user_details.configure(bg = "#88BB92")
class UserDetails:
    def __init__(self):

#the welcome label used at the top (header):
        self.welcome = Label(user_details, text = "Welcome to the Physics Quiz!", bg = "#88BB92", font=("Garamond", "29", "bold"))
        self.welcome.place(x=10, y=20)

#the label to display to the user, to enter their name:
        self.name = Label(user_details, text= "Please Enter your name:", bg="#E6EFE9", font=("Garamond", "20", "bold"))
        self.name.place(x=60, y=100)

#the label to display to the user, instructions1:
        self.name = Label(user_details, text= "This Quiz will include 10 Questions, which will count a point for", bg="#E6EFE9", font=("Garamond", "15", "bold"))
        self.name.place(x=110, y=270)

#the label to display to the user, instructions2:
        self.name = Label(user_details, text= "each question you answer correctly and display your final score at the end!", bg="#E6EFE9", font=("Garamond", "15", "bold"))
        self.name.place(x=75, y=300)

#the label to display to the user, instructions3:
        self.name = Label(user_details, text= "GOOD LUCK!!!", bg="#E6EFE9", font=("Garamond", "15", "bold"))
        self.name.place(x=320, y=350)
       
#The entry box for the user to enter their name:
        self.ent_name = Entry(user_details)
        self.ent_name.place(x=350,y=110)


#The label to display to the user ,to enter their age:
        self.age = Label(user_details, text="Please Enter your age:", bg= "#E6EFE9", font=("Garamond", "20", "bold"))
        self.age.place(x=60, y=175)

#The entry box for the user to enter their age:
        self.ent_age = Entry(user_details)
        self.ent_age.place(x=330,y=186)

#The labels used as a warning, if the user inputs an incorrect value:
        self.warning_name = Label(user_details, text="", bg = "#88BB92", font=("Garamond", "20"))
        self.warning_name.place(x=300, y=135)

        self.warning_age = Label(user_details, text="", bg = "#88BB92", font=("Garamond", "20"))
        self.warning_age.place(x=300, y=205)

#the buttons used (next and quit).
        self.buttons()


    def buttons(self):

#The enter button, for user to input details and move towards next portion of program:
        btn_enter = Button(user_details, text = "ENTER DETAILS", command= self.Check_Entry, highlightbackground = "#E6EFE9", font=("Garamond", "20"))
        btn_enter.place(x=220,y=400)

#The quit button, for user to leave program:
        btn_exit = Button(user_details, text = "QUIT", command=root.destroy, highlightbackground = "#E6EFE9", font=("Garamond", "20")) #root.destroy quits the program
        btn_exit.place(x=500,y=400)


#This function checks for the validity of the user's input in the NAME section:
    def check_name(self):
        self.warning_name.config(text="")

        while len(self.ent_name.get()) >= 1:
            if all(name.isalpha() or name.isspace() for name in self.ent_name.get()):
                self.warning_name.config(text="")

                return True
           
                break
           
           
#isalpha and isspace will check to make sure no numerical or other values have been inputted.
#Checking the length of the entry is important, and having this here will make sure that there has been a value inputted.


            else:
                self.warning_name.config(text="Invalid Name. Please enter using only letters", fg='red')
                self.ent_name.delete(0,END)
               
                return False
                break
           
        else:
            len(self.ent_name.get()) < 1
            self.warning_name.config(text="Please enter your name", fg='blue')
            return False
   
            #if the name is invalid, the entrybox will go blank again.

#This function checks for the validity of the user's input in the AGE section:      
    def check_age(self):
        self.warning_age.config(text="")

        try:
            while len(self.ent_age.get()) >= 1:
                if int(self.ent_age.get()) >= 12 and int(self.ent_age.get())<= 18:
                    self.warning_age.config(text="")
                    return True
#Will make sure any user using the quiz is for the designated age of 12 - 18
               
                else:
                    self.warning_age.config(text="Sorry! You must be aged 12-18 years old!", fg="red")
                    self.ent_age.delete(0,END)
                    return False

            else:
                len(self.ent_age.get()) < 1
                self.warning_age.config(text="Please enter your age", fg='blue')
                return False
#If the age inputted by the user is not between 12 - 18, the error message will show up, and the entry box will go blank

        except ValueError:
            self.warning_age.config(text="Invalid Age. Please enter using numerical values.", fg="red", )
            self.ent_age.delete(0,END)
            return False
#IF the age inputted is not a numerical value, the error message will show up and the entry box will go blank.


    def Check_Entry(self):

        validate_name = self.check_name()
        validate_age = self.check_age()

        if validate_name == True and validate_age == True:
           show_frame(instructions)
           self.ent_name.delete(0, END)
           self.ent_age.delete(0,END)

#Calling the checking functions, and placing them under one single function, to be called in the "Enter" button.
       
userdetails = UserDetails()

#============ Instructions ==============#

instructions.config(bg = "#88BB92")

instruct_file = open("instructions.txt", "r")
instruct = instruct_file.read()
instruct_file.close()

font_1 = ("Garamond","15","bold")

class Instructions:
    def __init__ (self):

        self.title = Label(instructions, text="Instructions for the Physics Quiz!", font=("Garamond","24","bold"), bg="#E6EFE9")
        self.title.place(x=180, y=20)

        self.instruct = Label(instructions, text = instruct, bg = "#E6EFE9", font= font_1)
        self.instruct.place(x=30,y=150)


        self.play = Button(instructions, text="PLAY QUIZ!", command = lambda: show_frame(quiz), highlightbackground = "#E6EFE9", font = font_1)
        self.play.place(x=250, y=350)

        self.back = Button(instructions, text="GO BACK!", command=lambda: show_frame(user_details), highlightbackground = "#E6EFE9", font = font_1)
        self.back.place(x=450,y=350)

python_image_user_details = PhotoImage(file='user_details.png')

instructs = Instructions()

#================ QUIZ ===============

quiz.config(bg = "#88BB92")

#questions of my program. These are stored in a list variable: "q"

#importing the questions from a file, to make them modifiable by outside users.
q=["Question 1: \nWhich of the following speeds is faster? ",
   "Question 2: \nProtons, neutrons and elections all orbit the ____. ",
   "Question 3: \nAs an ambulance drives past, you notice the pitch of its siren changing. This is caused by the ___ effect. ",
   "Question 4: \nWhat are sounds below 20 Hz known as? ",
   "Question 5: \nWhat does a vector quantity have that a scalar quantity lacks? ",
   "Question 6: \nWhat is the most common unit for measuring pressure? " ,
   "Question 7: \nWhat is the property of an object that can return to its original shape after deformation? ",
   "Question 8: \nLubrication can be used to limit the ____ between two objects. ",
   "Question 9: \nThe dimensions of Planck’s constant are same as____? ",
   "Question 10: \nThe sun is mainly composed of which two elements? ",

   ]

#the multi-choice options of my program. These are stored in the list called: "options"
options=[
    ['speed of light', 'speed of sound', 'speed of electricity'],
    ['nucleus', 'cells', 'monochromes'],
    ['light', 'doppler', 'sound'],
    ['infrasound', 'ultrasound', 'audiblefrequency'],
    ['speed', 'friction', 'sound'],
    ['pascals', 'centemeters', 'meters'],
    ['chromecell', 'elasticity', 'tele'],
    ['speed', 'friction', 'length'],
    ['energy', 'momentum', 'angular momentum'],
    ['hydrogen and helium', 'green house gas and helium', 'helium and gas']
    ]

#the answers to the questions. These are stored in the list called: "a"

a = [1,1,2,1,2,1,2,2,3,1]

class App(Tk):
    def __init__(self):
        super().__init__()
        

#calling the functions
class Quiz:

    def __init__(self):


        self.qn = 0

        self.ques = self.question(self.qn)

#IntVar() holds an integer value
        self.opt_selected = IntVar()

        self.opts = self.radiobtns()

        self.display_options(self.qn)

        self.buttons()

        self.correct = 0

        self.warning_select = Label(quiz, text="", bg = "#C6A9FB")
        self.warning_select.place(x=40,y=200)



    def question(self, qn):

        t = Label(quiz, text=" ~~~~ Physics Quiz ~~~~ ", bg = "#E6EFE9", font = ("Helvetica", "25","bold"))

        t.place(x=265, y=15)

        qn = Label(quiz, text = q[qn], bg = "#E6EFE9", font = ("Helvetica", "15","bold"))

        qn.place(x=55, y=80)

        label = Label(user_details, image=python_image_user_details)
        label.place(x=510,y=40)

        return qn

#the radio buttons on the questions.

    def radiobtns(self):

        val = 0

        b = []

        yp = 180

        while val < 3:

            btn = Radiobutton(quiz, text="", variable=self.opt_selected, value=val + 1, bg = "#E6EFE9")

            b.append(btn)

            btn.place(x=300, y=yp)

            val += 1

            yp += 45

        return b

    def display_options(self, qn):

        val = 0

        self.opt_selected.set(0)
   

        self.ques['text'] = q[qn]

        for op in options[qn]:

              self.opts[val]['text'] = op

              val += 1

    def buttons(self):

        backbutton = Button(quiz, text = "PREVIOUS QUESTION", command=self.backbtn, highlightbackground = "#E6EFE9", font = ("Garamond", "15", "bold"))

        backbutton.place(x=70,y=380)
       
        nextbutton = Button(quiz, text = "NEXT QUESTION", command=self.nextbtn, highlightbackground = "#E6EFE9", font = ("Garamond", "15", "bold"))
       
        nextbutton.place(x=370,y=380)
        quitbutton = Button(quiz, text = "QUIT", command = lambda: show_frame(user_details), highlightbackground = "#E6EFE9", font = ("Garamond", "15", "bold"))
       
        #root.destroy means end the program.

        quitbutton.place(x=630,y=380)

    def checkans(self, qn):

        if self.opt_selected.get() == a[qn]:

             return True

    def checkselected(self):
       
        if self.opt_selected.get() >= 1:
            self.warning_select.configure(text="")
            return True

        elif self.opt_selected.get() == 0:
           
            self.warning_select.configure(text="Please select an answer!", fg='red', font = ("Garamond", "18", "bold", "italic"))
           
    def nextbtn(self):

        x = self.checkselected()

        while x == True:

            if self.checkans(self.qn):

                self.correct += 1

            self.qn += 1

            if self.qn == len(q):

                self.display_result()
                break
    
            else:

                self.display_options(self.qn)      
                break

    def backbtn(self):

        while self.qn <= 10:
   
            self.qn -= 1

            if self.qn == len(q):
           
                self.display_result()

            else:
                self.display_options(self.qn)
                break
            
    def display_result(self):

        #if self.qn == 10:
            #self.answer = Button(quiz, text = "Show Results!", command = lambda: show_frame(play_again))
            #self.answer.place(x=350, y=200)
           
        score = int(self.correct / len(q) * 100)

        result = "Your Score: " + str(score) + "%"

        wc = len(q) - self.correct

        correct = "The number of correct answers you had: " + str(self.correct)
     
        wrong = "The number of incorrect answers you had: " + str(wc)

        mb.showinfo("Your Result", "\n".join([result, correct, wrong]))

quiz_bot=Quiz()

#===========Play Again ==============

#=========== End ==============
root.mainloop()
