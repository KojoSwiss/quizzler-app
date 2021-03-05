from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Questionssss", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        correct_image = PhotoImage(file="images/true.png")
        self.correct_btn = Button(image=correct_image, highlightthickness=0)
        self.correct_btn.grid(column=0, row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_image, highlightthickness=0)
        self.wrong_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
