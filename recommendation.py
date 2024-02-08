from tkinter import *
import math
from ttkbootstrap.widgets import Button, Entry, Label, Frame
from ttkbootstrap.widgets import Meter
from PIL import Image, ImageTk
import math
from tkinter import ttk
from ttkbootstrap import Style
import subprocess

# Define the features and properties of the sports
sports = [
    {"name": "Soccer", "type": "team", "difficulty": "easy", "intensity": "high", "equipment": "ball, goal, field"},
    {"name": "Basketball", "type": "team", "difficulty": "medium", "intensity": "high", "equipment": "ball, hoop, court"},
    {"name": "Tennis", "type": "individual", "difficulty": "medium", "intensity": "medium", "equipment": "racket, ball, net, court"},
    {"name": "Swimming", "type": "individual", "difficulty": "easy", "intensity": "medium", "equipment": "swimsuit, goggles, pool"},
    {"name": "Golf", "type": "individual", "difficulty": "hard", "intensity": "low", "equipment": "club, ball, hole, course"},
    {"name": "Chess", "type": "individual", "difficulty": "hard", "intensity": "low", "equipment": "board, pieces"}
]

# Create a profile for each sport, using a vector of numbers
profiles = []
for sport in sports:
    profile = []
    # Type
    if sport["type"] == "team":
        profile.append(0.5)
    else:
        profile.append(0.0)
    # Difficulty
    if sport["difficulty"] == "easy":
        profile.append(0.2)
    elif sport["difficulty"] == "medium":
        profile.append(0.5)
    else:
        profile.append(0.8)
    # Intensity
    if sport["intensity"] == "low":
        profile.append(0.2)
    elif sport["intensity"] == "medium":
        profile.append(0.5)
    else:
        profile.append(1.0)
    # Equipment
    equipment = ["ball", "goal", "field", "hoop", "court", "racket", "net", "swimsuit", "goggles", "pool", "club", "hole", "course", "board", "pieces"]
    for item in equipment:
        if item in sport["equipment"]:
            profile.append(0.05)
        else:
            profile.append(0.0)
    profiles.append(profile)

# Define a function to calculate the cosine similarity between two vectors
def calculate_cosine_similarity(v1, v2):
    dot_product = sum(x * y for x, y in zip(v1, v2))
    magnitude_v1 = math.sqrt(sum(x ** 2 for x in v1))
    magnitude_v2 = math.sqrt(sum(x ** 2 for x in v2))
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0  # Avoid division by zero
    return dot_product / (magnitude_v1 * magnitude_v2)

# Define a function to recommend sports based on an age group
def recommend_sports(selected_age_group):
    preference_weights = {
        "Children (5-12 years)": [0.8, 0.2, 1.0, 0.1],      # high preference for team sports, easy difficulty, high intensity, moderate equipment
        "Teenagers (13-18 years)": [0.7, 0.5, 0.8, 0.2],    # moderate preference for team sports, medium difficulty, high intensity, more equipment
        "Adults (19-64 years)": [0.5, 0.5, 0.5, 0.5],       # equal preference for team and individual sports, medium difficulty, medium intensity, diverse equipment
        "Older Adults (65 years and older)": [0.3, 0.7, 0.3, 0.8]  # high preference for individual sports, high difficulty, low intensity, less equipment
    }
    preference = preference_weights.get(selected_age_group)
    preference += [0] * (len(profiles[0]) - len(preference))  # Adjust the length of preference vector
    similarity_scores = [calculate_cosine_similarity(preference, profile) for profile in profiles]
    top_3_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:3]
    return [sports[i] for i in top_3_indices]

user_course_details = {
    "course_name": "Badminton",
    "instructor": "student 1",
    "duration": "6 weeks"
}

# Create a user interface with tkinter
root = Tk()
root.title("Sports Recommendation System")
root.geometry('925x500+300+200')

# Create a ttkbootstrap style
style = Style(theme="superhero")

# Create a frame to contain all widgets
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=YES)

course_name_label = ttk.Label(main_frame, text="Course Name: " + user_course_details["course_name"], font=("Arial", 14))
course_name_label.pack(pady=5)

instructor_label = ttk.Label(main_frame, text="Instructor: " + user_course_details["instructor"], font=("Arial", 14))
instructor_label.pack(pady=5)

duration_label = ttk.Label(main_frame, text="Duration: " + user_course_details["duration"], font=("Arial", 14))
duration_label.pack(pady=5)

# Define a separator to visually separate the course details from the recommendation section
separator = ttk.Separator(main_frame, orient='horizontal')
separator.pack(fill='x', padx=20, pady=20)

# Create a canvas widget to contain the recommendation widgets
canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=YES)

# Add a scrollbar to the root window
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y, expand=YES)

# Configure the canvas to scroll with the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# Create another frame inside the canvas to contain the recommendation widgets
recommendation_frame = Frame(canvas)
canvas.create_window((0, 0), window=recommendation_frame, anchor='nw')

# Create the meter widget
meter = Meter(
    recommendation_frame,
    metersize=180,
    padding=5,
    amountused=25,
    metertype="semi",
    subtext="miles per hour",
    interactive=True,
)
meter.pack()

# Update the subtext
meter.configure(subtext="Loading...")

# Update the amount used directly
meter.configure(amountused=50)

# Create an entry widget to update the amount used
entry = ttk.Entry(recommendation_frame, textvariable=meter.amountusedvar)
entry.pack(fill='x', pady=10)

# Increment the amount by 10 steps
meter.step(10)

# Decrement the amount by 15 steps
meter.step(-15)

title_label = ttk.Label(recommendation_frame, text="Sports Recommendation System", font=("Arial", 24))
title_label.pack(pady=20)

instruction_label = ttk.Label(recommendation_frame, text="Select an age group to see suitable sports recommended to you.", font=("Arial", 16))
instruction_label.pack(pady=10)

age_group_combobox = ttk.Combobox(recommendation_frame, values=["Children (5-12 years)", "Teenagers (13-18 years)", "Adults (19-64 years)", "Older Adults (65 years and older)"], font=("Arial", 14), state="readonly")
age_group_combobox.pack(pady=10)

recommendation_label = ttk.Label(recommendation_frame, text="", font=("Arial", 14))
recommendation_label.pack(pady=10)

def show_recommendations():
    selected_age_group = age_group_combobox.get()
    if selected_age_group in ["Children (5-12 years)", "Teenagers (13-18 years)", "Adults (19-64 years)", "Older Adults (65 years and older)"]:
        recommended_sports = recommend_sports(selected_age_group)
        recommendation_text = "If you belong to the age group of {}, you may enjoy these sports:\n".format(selected_age_group)
        for sport in recommended_sports:
            recommendation_text += "- {}\n".format(sport["name"])
        recommendation_label.config(text=recommendation_text)
    else:
        recommendation_label.config(text="Please select a valid age group.")

recommend_button = ttk.Button(recommendation_frame, text="Recommend", style="primary.TButton", command=show_recommendations)
recommend_button.pack(pady=10)

# Start the main loop
root.mainloop()
