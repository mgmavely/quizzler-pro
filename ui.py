from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=("arial", 16, "italic"),
                                                     fill="grey")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", padx=20)
        self.score.grid(row=0, column=1)

        check_img = PhotoImage(file="images/true.png")
        self.true = Button(image=check_img, highlightthickness=0, command=self.ans_true)
        self.true.grid(row=2, column=0)

        x_img = PhotoImage(file="images/false.png")
        self.false = Button(image=x_img, highlightthickness=0, command=self.ans_false)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.question_number < 10:
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score.config(text="")
            self.canvas.itemconfig(self.question_text, text=f"You scored: {self.quiz.score}/10")

    def ans_true(self):
        ans = self.quiz.check_answer("True")
        self.give_feedback(ans)

    def ans_false(self):
        ans = self.quiz.check_answer("False")
        self.give_feedback(ans)

    def give_feedback(self, is_right):
        if self.quiz.question_number <= 10:
            if is_right:
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            self.window.after(400, self.get_next_question)
