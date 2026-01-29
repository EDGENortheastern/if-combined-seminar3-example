import tkinter as tk  # GUI framework
from equation_generator import generate_equation  # quiz logic (used later)
import csv  # used to write quiz results to a CSV file
from datetime import datetime  # used to record timestamps

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
    """
    A Tkinter application for a simple maths quiz with user tracking.
    """
    def __init__(self):
        super().__init__()

        self.title("Math Quiz")
        self.user_name = None
        self.start_time = None
        self.score = 0
        self.current_question = 0
        self.total_questions = 5

        self.build_name_screen()

    def build_name_screen(self):
        self.title_label = tk.Label(self, text="Enter your name", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.name_entry = tk.Entry(self, font=("Arial", 14))
        self.name_entry.pack(pady=5)

        self.start_button = tk.Button(self, text="Start", command=self.start_quiz)
        self.start_button.pack(pady=10)

        self.feedback_label = tk.Label(self, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=5)
        
    def clear_screen(self):
        """Remove all widgets from the window."""
        for widget in self.winfo_children():
            widget.destroy()

    def start_quiz(self):
        name = self.name_entry.get().strip()

        if not name:
            self.feedback_label.config(text="Please enter your name", fg="red")
            return

        self.user_name = name
        self.start_time = datetime.now()  # store start time in memory

        self.score = 0
        self.current_question = 0

        self.clear_screen()
        # self.build_quiz_screen()
        # self.load_question()
        log_quiz_result(self.user_name, self.start_time, self.score)


if __name__ == "__main__":
    app = MathQuizApp()
    app.mainloop()
