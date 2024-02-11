import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
from tkinter import messagebox


# Define the quiz questions and answers
quiz_questions = [
    {
        "question": "All badminton matched are played to best of how many games?",
        "choices": ["1", "2", "3", "4"],
        "answer": "3"
    },
    {
        "question": "All singles and doubles games are played to how many points?",
        "choices": [ "21 ", "23", "27","30"],
        "answer": "21"
    },
    {
        "question": "Does Badminton uses net?",
        "choices": [ "No","Yes, Of course", "Sometimes", "None of the above"],
        "answer": "Yes, Of course"
    },
    {
        "question": "Is Badminton a Indoor or Outdoor sport?",
        "choices": [ "Indoor","Outdoor", "Both", "None of the above"],
        "answer": "Yes"
    },
    {
        "question": "when serving in badminton, the birdie must be hit below the waist.",
        "choices": ["True ", "False", "Maybe", "I don't know"],
        "answer": "P.V Sindhu"
    }
]

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sports Quiz for Badminton")
        self.style = Style(theme='flatly')
        self.geometry("400x300")
        self.question_label = tk.Label(self, text="Question")
        self.question_label.pack(pady=10)
        self.choices = tk.StringVar()
        self.choice_buttons = [tk.Radiobutton(self, text="", variable=self.choices, value=choice) for choice in range(4)]
        for btn in self.choice_buttons:
            btn.pack(pady=5)
        self.submit_button = tk.Button(text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=5)
        self.questions = quiz_questions
        self.count = 0
        self.next_question()

    def next_question(self):
        
        # total = len(self.questions)
        # print(total)
        if self.questions:
            self.current_question = self.questions.pop(0)
            self.question_label.config(text=self.current_question["question"])
            for i, choice in enumerate(self.current_question["choices"]):
                self.choice_buttons[i]['text'] = choice
                self.choice_buttons[i]['value'] = choice
        else:
            messagebox.showinfo("Quiz Finished", f"Congratulations! You have completed the quiz. You scored {self.count} out of 5 questions correctly.")
            self.destroy()

    def check_answer(self):
        user_answer = self.choices.get()
        
        if user_answer == self.current_question["answer"]:
            self.count+=1
        else:
            pass
        self.next_question()

# if __name__ == "__main__":
#     app = QuizApp()
#     app.mainloop()

