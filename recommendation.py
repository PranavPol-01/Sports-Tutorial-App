import tkinter as tk
from tkinter import ttk
from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine_similarity
import ttkbootstrap as ttkb

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
    return sklearn_cosine_similarity([v1], [v2])[0][0]

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

    

# Create a user interface with tkinter
root = tk.Tk()
root.title("Sports Recommendation System")
root.geometry("600x400")

# Create a ttkbootstrap style
style = ttkb.Style(theme="darkly")

title_label = tk.Label(root, text="Sports Recommendation System", font=("Arial", 24))
title_label.pack(pady=20)

instruction_label = tk.Label(root, text="Select an age group to see suitable sports recommended to you.", font=("Arial", 16))
instruction_label.pack(pady=10)

age_group_combobox = ttk.Combobox(root, values=["Children (5-12 years)", "Teenagers (13-18 years)", "Adults (19-64 years)", "Older Adults (65 years and older)"], font=("Arial", 14), state="readonly")
age_group_combobox.pack(pady=10)

recommendation_label = tk.Label(root, text="", font=("Arial", 14))
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

recommend_button = tk.Button(root, text="Recommend", font=("Arial", 14), command=show_recommendations)
recommend_button.pack(pady=10)

# Start the main loop
root.mainloop()
