import tkinter as tk
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    # Setup the window
    window = tk.Tk()
    window.title("Quiz Game")

    # Question bank setup
    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank, window)

    # GUI setup
    quiz.display_question()

    # Start the GUI event loop
    window.mainloop()


if __name__ == "__main__":
    main()
