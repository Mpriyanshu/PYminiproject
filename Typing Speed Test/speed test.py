import tkinter as tk
from time import time
import random

# Sample text list
texts = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a versatile and powerful programming language",
    "Typing speed tests are a fun way to improve your skills"
]

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        self.sample_text = random.choice(texts)
        self.start_time = None

        # UI Elements
        tk.Label(root, text="Type the text below:", font=("Arial", 15)).pack(pady=10)

        self.text_label = tk.Label(root, text=self.sample_text, font=("Arial", 13), wraplength=500)
        self.text_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 13), width=60)
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.start_timer)
        self.entry.bind("<Return>", self.check_result)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time()

    def check_result(self, event):
        end_time = time()
        typed_text = self.entry.get()
        time_taken = end_time - self.start_time

        words = len(typed_text.split())
        wpm = words / (time_taken / 60)

        # Calculate accuracy
        correct_chars = sum(1 for a, b in zip(typed_text, self.sample_text) if a == b)
        accuracy = (correct_chars / len(self.sample_text)) * 100

        self.result_label.config(
            text=f"WPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%\nTime: {time_taken:.2f}s"
        )

    def reset(self):
        self.sample_text = random.choice(texts)
        self.text_label.config(text=self.sample_text)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
