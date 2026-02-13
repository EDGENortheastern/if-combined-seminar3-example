import tkinter as tk
from equation_generator import generate_equation
import csv
from datetime import datetime


def log_quiz_result(name, start_time, score):
    """Record the user's quiz result in a CSV file."""
    with open("results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            name,
            start_time.isoformat(),
            datetime.now().isoformat(),
            score
        ])


class MathQuizApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Math Quiz")

        self.user_name = None
        self.start_time = None
        self.score = 0
        self.current_question = 0
        self.total_questions = 5

        self.current_answer = None

        self.build_name_screen()

    def build_name_screen(self):
        self.clear_screen()

        tk.Label(self, text="Enter your name", font=("Arial", 16)).pack(pady=10)

        self.name_entry = tk.Entry(self, font=("Arial", 14))
        self.name_entry.pack(pady=5)

        tk.Button(self, text="Start", command=self.start_quiz).pack(pady=10)

        self.feedback_label = tk.Label(self, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=5)

    def build_quiz_screen(self):
        self.clear_screen()

        self.question_label = tk.Label(self, text="", font=("Arial", 16))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self, font=("Arial", 14))
        self.answer_entry.pack(pady=5)

        self.feedback_label = tk.Label(self, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=5)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

    def build_result_screen(self):
        self.clear_screen()

        tk.Label(
            self,
            text=f"Quiz complete, {self.user_name}!",
            font=("Arial", 16)
        ).pack(pady=10)

        tk.Label(
            self,
            text=f"Your final score: {self.score}/{self.total_questions}",
            font=("Arial", 14)
        ).pack(pady=10)

        tk.Button(self, text="Restart", command=self.build_name_screen).pack(pady=10)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def start_quiz(self):
        name = self.name_entry.get().strip()

        if not name:
            self.feedback_label.config(text="Please enter your name", fg="red")
            return

        self.user_name = name
        self.start_time = datetime.now()
        self.score = 0
        self.current_question = 0

        self.build_quiz_screen()
        self.load_question()

    def load_question(self):
        if self.current_question >= self.total_questions:
            self.end_quiz()
            return

        equation, solution = generate_equation()
        self.current_answer = solution

        self.question_label.config(
            text=f"Question {self.current_question + 1}: Solve {equation}"
        )

        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def check_answer(self):
        user_input = self.answer_entry.get().strip()

        if not user_input.isdigit():
            self.feedback_label.config(text="Enter a valid number", fg="red")
            return

        if int(user_input) == self.current_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(
                text=f"Incorrect. Answer was {self.current_answer}",
                fg="red"
            )

        self.current_question += 1
        self.after(1000, self.load_question)

    def end_quiz(self):
        log_quiz_result(self.user_name, self.start_time, self.score)
        self.build_result_screen()


if __name__ == "__main__":
    app = MathQuizApp()
    app.mainloop()
