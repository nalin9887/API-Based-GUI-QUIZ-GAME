THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *
count=0
class QuizInterface:
    def __init__(self,quiz:QuizBrain):
        self.quiz=quiz
        self.window=Tk()

        self.window.title("QuizApp")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)
        self.score=Label(text=f"Score:{count} ",bg=THEME_COLOR,fg="white",font=("Arial",15,"bold"))
        self.score.grid(row=0,column=1)


        self.canvas=Canvas(width=300,height=250)

        self.question_text=self.canvas.create_text(150,125,width=280,text="dsadsadsadsa",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        timages=PhotoImage(file="images/true.png")
        self.true=Button(image=timages,bg=THEME_COLOR,highlightthickness=0,command=self.trues)
        self.true.grid(row=2,column=0)
        fimages=PhotoImage(file="images/false.png")
        self.false=Button(image=fimages,bg=THEME_COLOR,highlightthickness=0,command=self.falses)
        self.false.grid(row=2,column=1)
        self.next_question()
        self.window.mainloop()
    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f"You Have Reached End Of The Quiz  \n \n Your Final Score : {count}")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
    def trues(self):
        is_right=self.quiz.check_answer("True")
        self.feedback(is_right)

    def falses(self):
        is_right=self.quiz.check_answer("false")
        self.feedback(is_right)


    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000,func=self.next_question)
            global count
            count+=1
            self.score.config(text=f"Score:{count}")
        else:
            self.canvas.config(bg="red")
            self.window.after(500,func=self.next_question)


