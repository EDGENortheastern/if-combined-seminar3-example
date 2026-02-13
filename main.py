import tkinter as tk # for GUI
import csv # for permanent storage functionality
from datetime import datetime # to get and format the timestamp
from equation_generator import generate_equation # module that generates equations


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
    
    """Math quiz application with score tracking."""

    def __init__(self):
        
        super().__init__()

        self.bg_colour = "#F2D8A7"
        self.primary_colour = "#0D3353"
        self.accent_colour = "#1F6AA5"
        self.correct_colour = "#2E8B57"
        self.error_colour = "#C1121F"
        self.title("Math Quiz")
        self.geometry("1000x750")
        self.resizable(False, False)
        self.configure(bg=self.bg_colour)

        self.logo_image = tk.PhotoImage(file="NU_K100_ring.png")
        self.logo_image = self.logo_image.subsample(3, 3)

        self.user_name = None
        self.start_time = None
        self.score = 0
        self.current_question = 0
        self.total_questions = 5
        self.current_answer = None

        self.build_name_screen()

    def clear_screen(self):
        """Remove all widgets from the window."""
        for widget in self.winfo_children():
            widget.destroy()

    def build_name_screen(self):
        """Build the initial screen explaining the quiz and collecting the user's name."""
        self.clear_screen()

        container = tk.Frame(self, bg=self.bg_colour)
        container.pack(expand=True)

        tk.Label(
            container,
            text="Algebra Skills Challenge",
            font=("Arial", 34, "bold"),
            bg=self.bg_colour,
            fg=self.primary_colour
        ).pack(pady=(40, 10))

        tk.Label(
            container,
            text="You will be given five linear equations.\n"
                 "Enter your answer and press Submit or Return.\n"
                 "Your score will be recorded at the end.",
            font=("Arial", 18),
            justify="center",
            bg=self.bg_colour,
            fg=self.primary_colour
        ).pack(pady=(0, 25))

        tk.Label(
            container,
            image=self.logo_image,
            bg=self.bg_colour
        ).pack(pady=10)

        tk.Label(
            container,
            text="Enter your name",
            font=("Arial", 20),
            bg=self.bg_colour,
            fg=self.primary_colour
        ).pack(pady=(30, 10))

        self.name_entry = tk.Entry(
            container,
            font=("Arial", 20),
            width=18,
            bd=0,
            relief="flat",
            highlightthickness=2,
            highlightbackground=self.primary_colour,
            highlightcolor=self.accent_colour
        )
        self.name_entry.pack(pady=10)
        self.name_entry.focus()

        tk.Button(
            container,
            text="Start Quiz",
            font=("Arial", 18, "bold"),
            width=16,
            height=2,
            bd=0,
            relief="flat",
            bg=self.accent_colour,
            fg="white",
            activebackground=self.primary_colour,
            activeforeground="white",
            command=self.start_quiz
        ).pack(pady=30)

        self.feedback_label = tk.Label(
            container,
            text="",
            font=("Arial", 16),
            bg=self.bg_colour
        )
        self.feedback_label.pack()

    def build_quiz_screen(self):
        """Build the quiz question interface."""
        self.clear_screen()

        container = tk.Frame(self, bg=self.bg_colour)
        container.pack(expand=True)

        self.progress_label = tk.Label(
            container,
            font=("Arial", 18),
            bg=self.bg_colour,
            fg=self.primary_colour
        )
        self.progress_label.pack(pady=(30, 5))

        self.score_label = tk.Label(
            container,
            text=f"Score: {self.score}",
            font=("Arial", 20, "bold"),
            bg=self.bg_colour,
            fg=self.primary_colour
        )
        self.score_label.pack(pady=5)

        self.question_label = tk.Label(
            container,
            font=("Arial", 44, "bold"),
            wraplength=900,
            justify="center",
            bg=self.bg_colour,
            fg=self.primary_colour
        )
        self.question_label.pack(pady=50)

        self.answer_entry = tk.Entry(
            container,
            font=("Arial", 26),
            width=8,
            bd=0,
            relief="flat",
            highlightthickness=2,
            highlightbackground=self.primary_colour,
            highlightcolor=self.accent_colour
        )
        self.answer_entry.pack(pady=20)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        self.answer_entry.focus()

        self.feedback_label = tk.Label(
            container,
            font=("Arial", 20),
            bg=self.bg_colour
        )
        self.feedback_label.pack(pady=20)

        tk.Button(
            container,
            text="Submit",
            font=("Arial", 18, "bold"),
            width=14,
            height=2,
            bd=0,
            relief="flat",
            bg=self.accent_colour,
            fg="white",
            activebackground=self.primary_colour,
            activeforeground="white",
            command=self.check_answer
        ).pack(pady=30)

    def build_result_screen(self):
        """Display the final score screen."""
        self.clear_screen()

        container = tk.Frame(self, bg=self.bg_colour)
        container.pack(expand=True)

        tk.Label(
            container,
            text="Quiz Complete",
            font=("Arial", 36, "bold"),
            bg=self.bg_colour,
            fg=self.primary_colour
        ).pack(pady=50)

        tk.Label(
            container,
            text=f"{self.user_name}, your final score is",
            font=("Arial", 22),
            bg=self.bg_colour,
            fg=self.primary_colour
        ).pack(pady=10)

        tk.Label(
            container,
            text=f"{self.score} / {self.total_questions}",
            font=("Arial", 44, "bold"),
            bg=self.bg_colour,
            fg=self.primary_colour
        ).pack(pady=20)

        tk.Button(
            container,
            text="Restart",
            font=("Arial", 18, "bold"),
            width=14,
            height=2,
            bd=0,
            relief="flat",
            bg=self.accent_colour,
            fg="white",
            activebackground=self.primary_colour,
            activeforeground="white",
            command=self.build_name_screen
        ).pack(pady=40)

    def start_quiz(self):
        """Initialise quiz state and begin."""
        name = self.name_entry.get().strip()

        if not name:
            self.feedback_label.config(
                text="Please enter your name",
                fg=self.error_colour
            )
            return

        self.user_name = name
        self.start_time = datetime.now()
        self.score = 0
        self.current_question = 0

        self.build_quiz_screen()
        self.load_question()

    def load_question(self):
        """Load the next equation question."""
        if self.current_question >= self.total_questions:
            self.end_quiz()
            return

        equation, solution = generate_equation()
        self.current_answer = solution

        self.progress_label.config(
            text=f"Question {self.current_question + 1} of {self.total_questions}"
        )

        self.question_label.config(text=f"Solve: {equation}")
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def check_answer(self):
        """Validate user input and update score."""
        user_input = self.answer_entry.get().strip()

        if not user_input.lstrip("-").isdigit():
            self.feedback_label.config(
                text="Enter a valid number",
                fg=self.error_colour
            )
            return

        if int(user_input) == self.current_answer:
            self.score += 1
            self.feedback_label.config(
                text="Correct",
                fg=self.correct_colour
            )
        else:
            self.feedback_label.config(
                text=f"Incorrect. Answer was {self.current_answer}",
                fg=self.error_colour
            )

        self.score_label.config(text=f"Score: {self.score}")
        self.current_question += 1
        self.after(900, self.load_question)

    def end_quiz(self):
        """Log result and show final screen."""
        log_quiz_result(self.user_name, self.start_time, self.score)
        self.build_result_screen()

if __name__ == "__main__":
    app = MathQuizApp()
    app.mainloop()
