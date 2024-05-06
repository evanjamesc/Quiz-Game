import tkinter as tk
from tkinter import messagebox


class QuizBrain:

    def __init__(self, q_list, window):
        self.score_label = None
        self.false_button = None
        self.true_button = None
        self.question_text = None
        self.canvas = None
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.window = window
        self.setup_ui()

    # GUI setup
    def setup_ui(self):
        self.canvas = tk.Canvas(self.window, width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="",
            fill="#F8F8FF",
            font=('Arial', 20, 'italic')
        )
        self.canvas.pack(pady=20)

        self.true_button = tk.Button(self.window, text="True", command=self.true_pressed, width=20)
        self.true_button.pack()

        self.false_button = tk.Button(self.window, text="False", command=self.false_pressed, width=20)
        self.false_button.pack()

        self.score_label = tk.Label(self.window, text="Score: 0")
        self.score_label.pack()

    # Check if there are questions left, display next question
    def display_question(self):
        if self.still_has_questions():
            q_text = self.question_list[self.question_number].text
            self.canvas.itemconfig(self.question_text, text=f"Q.{self.question_number + 1}: {q_text}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # User clicks "True"
    def true_pressed(self):
        self.check_answer("True")

    # User clicks "False"
    def false_pressed(self):
        self.check_answer("False")

    # Check answer, keep score
    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_number].answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.question_number += 1
        self.display_question()

        # Display alert if no more questions are left
        if not self.still_has_questions():
            self.display_score_alert()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def display_score_alert(self):
        messagebox.showinfo("Quiz Completed",
                            f"You've completed the quiz!\nYour final score was: {self.score}/{len(self.question_list)}")
