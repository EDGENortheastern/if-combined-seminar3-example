import tkinter as tk  # GUI framework
from equation_generator import generate_equation  # quiz logic (used later)
import csv  # used to write quiz results to a CSV file
from datetime import datetime  # used to record timestamps

def log_user_start(name):
    """Record the user's name and start time in a CSV file."""
    with open("results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, datetime.now().isoformat()])


class MathQuizApp(tk.Tk):
    """
    A Tkinter application for a simple maths quiz with user tracking.
    """
    def __init__(self):
        super().__init__()

        self.title("Math Quiz")
        self.user_name = None  

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

    def start_quiz(self):
        name = self.name_entry.get().strip()

        if not name:
            self.feedback_label.config(text="Please enter your name", fg="red")
            return

        self.user_name = name
        log_user_start(self.user_name)
        self.feedback_label.config(text=f"Welcome, {self.user_name}", fg="green")



if __name__ == "__main__":
    app = MathQuizApp()
    app.mainloop()
