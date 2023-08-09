from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ('Ariel', 20, 'italic')


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Ariel", 15, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question Goes here",
            fill="black",
            font=QUESTION_FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        # self.true_Button = Button(image=true_img, highlightthickness=0, command=lambda: self.quiz.check_answer(
        # "True")) self.false_button = Button(image=false_img, highlightthickness=0, command=lambda:
        # self.quiz.check_answer("False"))
        self.true_Button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_img, highlightthickness=0,
                                   command=self.false_pressed)
        self.true_Button.grid(row=2, column=1)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_Button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config()
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        # self.window.after_cancel("give_feedback")



