from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #creating window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #creating canvas
        self.canvas = Canvas(width=300, height=250, bg="white", )
        self.screen_canvas = self.canvas
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #question text
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("arial", 16, "italic"))


        #button true
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0,bd=0,command=self.true_fact)
        self.true_button.grid(row=2, column=0)

        #button false
        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,bd=0, command=self.false_fact)
        self.false_button.grid(row=2, column=1)

        #labels
        self.score_label = Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}", bg=THEME_COLOR, fg="white", font=("arial", 20, "normal"))
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\nYour final score is :{self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_fact(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_fact(self):
        is_wrong = self.quiz.check_answer("False")
        self.give_feedback(is_wrong)

    def give_feedback(self, is_right):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(300, self.get_next_question)





