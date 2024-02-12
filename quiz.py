# import tkinter as tk
# from tkinter import messagebox
# from ttkbootstrap import Style
# from tkinter import messagebox
# from tkinter import ttk


# # Define the quiz questions and answers
# quiz_questions = [
#     {
#         "question": "All badminton matched are played to best of how many games?",
#         "choices": ["1", "2", "3", "4"],
#         "answer": "3"
#     },
#     {
#         "question": "All singles and doubles games are played to how many points?",
#         "choices": [ "21 ", "23", "27","30"],
#         "answer": "21"
#     },
#     {
#         "question": "Does Badminton uses net?",
#         "choices": [ "No","Yes, Of course", "Sometimes", "None of the above"],
#         "answer": "Yes, Of course"
#     },
#     {
#         "question": "Is Badminton a Indoor or Outdoor sport?",
#         "choices": [ "Indoor","Outdoor", "Both", "None of the above"],
#         "answer": "Indoor"
#     },
#     {
#         "question": "when serving in badminton, the birdie must be hit below the waist.",
#         "choices": ["True ", "False", "Maybe", "I don't know"],
#         "answer": "True"
#     }
# ]

# class QuizApp(tk.Tk):
    

#     def __init__(self):
#         super().__init__()
#         self.title("Sports Quiz for Badminton")
#         self.style = Style(theme='lumen')
#         self.geometry("600x400")
      

# # Set the geometry of the root window to fill the screen
# #root.geometry("%dx%d" % (width, height))
#         self.question_label = tk.Label(self, text="Question")
#         self.question_label.pack(pady=10)

#         self.choices = tk.StringVar()
#         self.choice_buttons = [ttk.Radiobutton(self, text="", variable=self.choices, value=choice, style='Large.TRadiobutton', padding= 20) for choice in range(4)]
#         for btn in self.choice_buttons:
#             btn.pack(side=tk.LEFT, padx=5)

#         # Create a new style
#         style = ttk.Style()
#         style.configure('Large.TRadiobutton', font=('TkDefaultFont', 20))  # Adjust the font size as needed

        
#         # self.choice_buttons = [ttk.Radiobutton(self, text="", variable=self.choices, value=choice, style='Large.TRadiobutton') for choice in range(4)]
#         # for btn in self.choice_buttons:
#         #     btn.pack(pady=5)

        


#         # self.choices = tk.StringVar()
#         # self.choice_buttons = [ttk.Radiobutton(self, text="", variable=self.choices, value=choice, ) for choice in range(4)]
#         # for btn in self.choice_buttons:
#         #     btn.pack(pady=5, expand=True)
#         self.submit_button = ttk.Button(text="Submit", command=self.check_answer, padding=5)
#         self.submit_button.pack(side=tk.bottom,pady=5)
#         self.questions = quiz_questions
#         self.count = 0
#         self.next_question()
        
# #         def on_frame_resized(event):
# #     # Calculate new font size based on frame width
# #             new_font_size = int(event.width / 4)  # Adjust the divisor to get the desired font size

# #     # Update font size of question_label
# #             self.question_label.configure(font=("TkDefaultFont", new_font_size))

# # # Bind on_frame_resized to <Configure> event of the frame
# #         self.bind("<Configure>", on_frame_resized)    

#     def next_question(self):
        
#         # total = len(self.questions)
#         # print(total)
#         if self.questions:
#             self.current_question = self.questions.pop(0)
#             self.question_label.config(text=self.current_question["question"],pady=80, font=("Helvetica", 20))
#             for i, choice in enumerate(self.current_question["choices"]):
#                 self.choice_buttons[i]['text'] = choice
#                 self.choice_buttons[i]['value'] = choice
#         else:
#             messagebox.showinfo("Quiz Finished", f"Congratulations! You have completed the quiz. You scored {self.count} out of 5 questions correctly.")
#             self.destroy()

#     def check_answer(self):
#         user_answer = self.choices.get()
#         count = 0
#         if user_answer == self.current_question["answer"]:
#             self.count+=1
#         else:
#             pass
#         self.next_question()

# if __name__ == "__main__":
#     app = QuizApp()
#     app.mainloop()



import tkinter as tk
from tkinter import messagebox
from ttkbootstrap.widgets import *

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
        "answer": "Indoor"
    },
    {
        "question": "when serving in badminton, the birdie must be hit below the waist.",
        "choices": ["True ", "False", "Maybe", "I don't know"],
        "answer": "True"
    }
]

def next_question():
    global questions, count
    if questions:
        current_question = questions.pop(0)
        question_label.config(text=current_question["question"], pady=80, font=("Helvetica", 14))
        for i, choice in enumerate(current_question["choices"]):
            choice_buttons[i]['text'] = choice
            choice_buttons[i]['value'] = choice
    else:
        messagebox.showinfo("Quiz Finished", f"Congratulations! You have completed the quiz. You scored {count} out of 5 questions correctly.")
        root.destroy()

def check_answer():
    global count
    user_answer = choices.get()
    if user_answer == questions[0]["answer"]:
        count += 1
    next_question()

root = tk.Tk()
root.title("Sports Quiz for Badminton")
root.geometry("1000x800")

# Set the geometry of the root window to fill the screen
root.geometry("600x400")

question_label = tk.Label(root, text="Question")
question_label.pack(pady=10)

option_frame = Frame(root, width=350, height=350)
option_frame.place(relx=0.5, rely=0.5, anchor= tk.CENTER)

choices = tk.StringVar()
choice_buttons = [ttk.Radiobutton(option_frame, text="", variable=choices, value=choice) for choice in range(4)]
for btn in choice_buttons:
    btn.pack(side=tk.LEFT, padx=15)

submit_button = ttk.Button(option_frame, text="Submit", command=check_answer, padding=5)
submit_button.pack(side=tk.BOTTOM, pady=5,  expand=True, anchor='center')

questions = quiz_questions
count = 0
next_question()


#     def next_question(self):
        
#         # total = len(self.questions)
#         # print(total)
#         if self.questions:
#             self.current_question = self.questions.pop(0)
#             self.question_label.config(text=self.current_question["question"],pady=80, font=("Helvetica", 20))
#             for i, choice in enumerate(self.current_question["choices"]):
#                 self.choice_buttons[i]['text'] = choice
#                 self.choice_buttons[i]['value'] = choice
#         else:
#             messagebox.showinfo("Quiz Finished", f"Congratulations! You have completed the quiz. You scored {self.count} out of 5 questions correctly.")
#             self.destroy()

#     def check_answer(self):
#         user_answer = self.choices.get()
#         count = 0
#         if user_answer == self.current_question["answer"]:
#             self.count+=1
#         else:
#             pass
#         self.next_question()

# root.mainloop()
