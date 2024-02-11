
# import tkinter as tk
# import math
# from ttkbootstrap.widgets import Button, Entry, Label, Frame
# from ttkbootstrap.widgets import Meter
# from PIL import Image, ImageTk
# import math
# from tkinter import ttk
# from ttkbootstrap import Style
# import subprocess
# from ttkbootstrap.scrolled import ScrolledFrame

# # Define the features and properties of the sports
# sports = [
#     {"name": "Soccer", "type": "team", "difficulty": "easy", "intensity": "high", "equipment": "ball, goal, field"},
#     {"name": "Basketball", "type": "team", "difficulty": "medium", "intensity": "high", "equipment": "ball, hoop, court"},
#     {"name": "Tennis", "type": "individual", "difficulty": "medium", "intensity": "medium", "equipment": "racket, ball, net, court"},
#     {"name": "Swimming", "type": "individual", "difficulty": "easy", "intensity": "medium", "equipment": "swimsuit, goggles, pool"},
#     {"name": "Golf", "type": "individual", "difficulty": "hard", "intensity": "low", "equipment": "club, ball, hole, course"},
#     {"name": "Chess", "type": "individual", "difficulty": "hard", "intensity": "low", "equipment": "board, pieces"}
# ]

# # Create a profile for each sport, using a vector of numbers
# profiles = []
# for sport in sports:
#     profile = []
#     # Type
#     if sport["type"] == "team":
#         profile.append(0.5)
#     else:
#         profile.append(0.0)
#     # Difficulty
#     if sport["difficulty"] == "easy":
#         profile.append(0.2)
#     elif sport["difficulty"] == "medium":
#         profile.append(0.5)
#     else:
#         profile.append(0.8)
#     # Intensity
#     if sport["intensity"] == "low":
#         profile.append(0.2)
#     elif sport["intensity"] == "medium":
#         profile.append(0.5)
#     else:
#         profile.append(1.0)
#     # Equipment
#     equipment = ["ball", "goal", "field", "hoop", "court", "racket", "net", "swimsuit", "goggles", "pool", "club", "hole", "course", "board", "pieces"]
#     for item in equipment:
#         if item in sport["equipment"]:
#             profile.append(0.05)
#         else:
#             profile.append(0.0)
#     profiles.append(profile)

# # Define a function to calculate the cosine similarity between two vectors
# def calculate_cosine_similarity(v1, v2):
#     dot_product = sum(x * y for x, y in zip(v1, v2))
#     magnitude_v1 = math.sqrt(sum(x ** 2 for x in v1))
#     magnitude_v2 = math.sqrt(sum(x ** 2 for x in v2))
#     if magnitude_v1 == 0 or magnitude_v2 == 0:
#         return 0  # Avoid division by zero
#     return dot_product / (magnitude_v1 * magnitude_v2)

# # Define a function to recommend sports based on an age group
# def recommend_sports(selected_age_group):
#     preference_weights = {
#         "Children (5-12 years)": [0.8, 0.2, 1.0, 0.1],      # high preference for team sports, easy difficulty, high intensity, moderate equipment
#         "Teenagers (13-18 years)": [0.7, 0.5, 0.8, 0.2],    # moderate preference for team sports, medium difficulty, high intensity, more equipment
#         "Adults (19-64 years)": [0.5, 0.5, 0.5, 0.5],       # equal preference for team and individual sports, medium difficulty, medium intensity, diverse equipment
#         "Older Adults (65 years and older)": [0.3, 0.7, 0.3, 0.8]  # high preference for individual sports, high difficulty, low intensity, less equipment
#     }
#     preference = preference_weights.get(selected_age_group)
#     preference += [0] * (len(profiles[0]) - len(preference))  # Adjust the length of preference vector
#     similarity_scores = [calculate_cosine_similarity(preference, profile) for profile in profiles]
#     top_3_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:3]
#     return [sports[i] for i in top_3_indices]

# user_course_details = {
#     "course_name": "Badminton",
#     "instructor": "student 1",
#     "duration": "6 weeks"
# }

# # Create a user interface with tkinter
# root = tk.Tk()
# root.title("Sports Recommendation System")
# root.geometry('925x500+300+200')

# # Create a ttkbootstrap style
# style = Style(theme="superhero")

# # Create a frame to contain all widgets
# main_frame = ScrolledFrame(root)
# main_frame.pack(fill=tk.BOTH, expand=tk.YES)

# course_name_label = ttk.Label(main_frame, text="Course Name: " + user_course_details["course_name"], font=("Arial", 14))
# course_name_label.pack(pady=5)

# instructor_label = ttk.Label(main_frame, text="Instructor: " + user_course_details["instructor"], font=("Arial", 14))
# instructor_label.pack(pady=5)

# duration_label = ttk.Label(main_frame, text="Duration: " + user_course_details["duration"], font=("Arial", 14))
# duration_label.pack(pady=5)

# # Define a separator to visually separate the course details from the recommendation section
# separator = ttk.Separator(main_frame, orient='horizontal')
# separator.pack(fill='x', padx=20, pady=20)

# # Create another frame to contain the recommendation widgets
# recommendation_frame = Frame(main_frame)
# recommendation_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

# # add a large number of checkbuttons into the scrolled frame
# # sf = ScrolledFrame(recommendation_frame, autohide=True)
# # sf.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

# # for x in range(20):
# #     ttk.Checkbutton(sf, text=f"Checkbutton {x}").pack(anchor=tk.W)

# # Create the meter widget
# meter = Meter(
#     recommendation_frame,
#     metersize=180,
#     padding=5,
#     amountused=25,
#     metertype="semi",
#     subtext="miles per hour",
#     interactive=True,
# )
# meter.pack()

# # Update the subtext
# meter.configure(subtext="Loading...")

# # Update the amount used directly
# meter.configure(amountused=50)

# # Create an entry widget to update the amount used
# entry = ttk.Entry(recommendation_frame, textvariable=meter.amountusedvar)
# entry.pack(fill='x', pady=10)

# # Increment the amount by 10 steps
# meter.step(10)

# # Decrement the amount by 15 steps
# meter.step(-15)

# title_label = ttk.Label(recommendation_frame, text="Sports Recommendation System", font=("Arial", 24))
# title_label.pack(pady=20)

# instruction_label = ttk.Label(recommendation_frame, text="Select an age group to see suitable sports recommended to you.", font=("Arial", 16))
# instruction_label.pack(pady=10)

# age_group_combobox = ttk.Combobox(recommendation_frame, values=["Children (5-12 years)", "Teenagers (13-18 years)", "Adults (19-64 years)", "Older Adults (65 years and older)"], font=("Arial", 14), state="readonly")
# age_group_combobox.pack(pady=10)

# recommendation_label = ttk.Label(recommendation_frame, text="", font=("Arial", 14))
# recommendation_label.pack(pady=10)

# def show_recommendations():
#     selected_age_group = age_group_combobox.get()
#     if selected_age_group in ["Children (5-12 years)", "Teenagers (13-18 years)", "Adults (19-64 years)", "Older Adults (65 years and older)"]:
#         recommended_sports = recommend_sports(selected_age_group)
#         recommendation_text = "If you belong to the age group of {}, you may enjoy these sports:\n".format(selected_age_group)
#         for sport in recommended_sports:
#             recommendation_text += "- {}\n".format(sport["name"])
#         recommendation_label.config(text=recommendation_text)
#     else:
#         recommendation_label.config(text="Please select a valid age group.")

# recommend_button = ttk.Button(recommendation_frame, text="Recommend", style="primary.TButton", command=show_recommendations)
# recommend_button.pack(pady=10)

# # Start the main loop
# root.mainloop()


#--------------------------------------------------------------------------------------------------------------------------------------------
# import tkinter as tk
# import math
# from ttkbootstrap.widgets import Button, Entry, Label, Frame
# from ttkbootstrap.widgets import Meter
# from PIL import Image, ImageTk
# import math
# from tkinter import ttk
# from ttkbootstrap import Style
# import subprocess
# from ttkbootstrap.scrolled import ScrolledFrame
# import pandas as pd  # Import pandas module
# import sqlite3
# from openpyxl.workbook import Workbook

# # Load data from Excel file
# df = pd.read_excel('sports.xlsx')

# # Store data in SQLite database
# conn = sqlite3.connect('sports.db')
# df.to_sql('sports', conn, if_exists='replace', index=False)

# # Global variable to store the username
# current_user = None


# def get_recommendations(preferences):
#     conn = sqlite3.connect('sports.db')
#     cursor = conn.cursor()
#     cursor.execute(f"SELECT [{preferences}] FROM sports")
#     recommendations = cursor.fetchall()
#     conn.close()
#     return recommendations

# def show_recommendation_cards(recommendations):
#     for i, recommendation in enumerate(recommendations):
#         # Create a frame for the recommendation card
#         card_frame = ttk.Frame(cards_frame)
#         card_frame.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")

#         # Add a label to display the recommendation
#         recommendation_label = ttk.Label(card_frame, text=recommendation[0], font=("Arial", 12))
#         recommendation_label.pack()

# # Create a user interface with tkinter
# root = tk.Tk()
# root.title("Sports Recommendation System")
# root.geometry('925x500+300+200')

# # Create a ttkbootstrap style
# style = Style(theme="superhero")

# # Create a frame to contain all widgets
# main_frame = ScrolledFrame(root)
# main_frame.pack(fill=tk.BOTH, expand=tk.YES)

# style.configure("Inverted.TLabel", background=style.colors.dark, foreground=style.colors.light)

# # Create a frame for the header with a specified height and inverted colors
# header_frame = ttk.Frame(main_frame, height=100)
# header_frame.pack(fill='x')


# # Create the main label with inverted colors
# welcome_label = Label(header_frame, text="SPORTS TUTORIAL APP", font=('Courier New', 35, 'bold'), style="Inverted.TLabel", borderwidth=12, relief="groove")
# welcome_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# # Adjust position of the main label to create the shadow effect
# welcome_label.lift() 

# separator = ttk.Separator(main_frame, orient='horizontal')
# separator.pack(fill='x', padx=20, pady=20)


# # Create a frame for the course details
# course_d_frame = ttk.Frame(main_frame, padding=10, borderwidth=2, relief="solid", height=400, width=400)
# course_d_frame.pack(pady=10, anchor=tk.CENTER, expand=True)

# # Add a meter showing the course completion progress
# course_completion_meter = Meter(course_d_frame, metersize=100, padding=5, amountused=25, metertype="semi", subtext="current course")
# course_completion_meter.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# # Create a frame for course details
# course_details_frame = ttk.Frame(course_d_frame, padding=10, borderwidth=2, relief="solid", height=200, width=200)
# course_details_frame.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# # Add labels for course details
# course_name_label = ttk.Label(course_details_frame, text="Course Name: Badminton", font=("Arial", 14))
# course_name_label.grid(row=0, column=0, pady=5, sticky='w')

# instructor_label = ttk.Label(course_details_frame, text="Instructor: sapp", font=("Arial", 14))
# instructor_label.grid(row=1, column=0, pady=5, sticky='w')

# duration_label = ttk.Label(course_details_frame, text="Duration: 6 weeks", font=("Arial", 14))
# duration_label.grid(row=2, column=0, pady=5, sticky='w')




# # Separator between course details and recommendations
# separator = ttk.Separator(main_frame, orient='horizontal')
# separator.pack(fill='x', padx=20, pady=20)


# recommendation_frame = Frame(main_frame)
# recommendation_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

# meter = Meter(
#     recommendation_frame,
#     metersize=180,
#     padding=5,
#     amountused=25,
#     metertype="semi",
#     subtext="miles per hour",
#     interactive=True,
# )





# title_label = ttk.Label(recommendation_frame, text="Sports Recommendation System", font=("Arial", 24))
# title_label.pack(pady=20)

# instruction_label = ttk.Label(recommendation_frame, text="Select an age group to see suitable sports recommended to you.", font=("Arial", 16))
# instruction_label.pack(pady=10)

# age_group_combobox = ttk.Combobox(recommendation_frame, values=["Children (Ages 0-12):", "Teenagers (Ages 13-19):", "Young Adults (Ages 20-39):", "Middle-Aged Adults (Ages 40-59):", "Older Adults (Ages 60+):"], font=("Arial", 14), state="readonly")
# age_group_combobox.pack(pady=10)

# cards_frame = ttk.Frame(main_frame)
# cards_frame.pack(padx=10, pady=10)

# recommendation_label = ttk.Label(recommendation_frame, text="", font=("Arial", 14))
# recommendation_label.pack(pady=10)

# def show_recommendations():
#     selected_age_group = age_group_combobox.get()
#     if selected_age_group:
#         recommendations = get_recommendations(selected_age_group)
#         recommendation_text = f"Recommendations for {selected_age_group}:\n"
#         if recommendations:
#             show_recommendation_cards(recommendations)
#             # for recommendation in recommendations:
#             #     recommendation_text += f"- {recommendation}\n"  # Fetch the first element of the tuple
#         else:
#             recommendation_text += "No recommendations found for the selected age group."
#         recommendation_label.config(text=recommendation_text)
#     else:
#         recommendation_label.config(text="Please select an age group.")


# recommend_button = ttk.Button(recommendation_frame, text="Recommend", style="primary.TButton", command=show_recommendations)
# recommend_button.pack(pady=10)

# root.mainloop()


#-------------------------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------
import tkinter as tk
import math
from ttkbootstrap.widgets import Button, Entry, Label, Frame
from ttkbootstrap.widgets import Meter
from PIL import Image, ImageTk
import math
from tkinter import ttk
from ttkbootstrap import Style
import subprocess
from ttkbootstrap.scrolled import ScrolledFrame
import pandas as pd  # Import pandas module
import sqlite3
from openpyxl.workbook import Workbook
from PIL import Image, ImageDraw


def create_rounded_rectangle(width, height, radius, color):
    image = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), fill=color)
    draw.pieslice((0, 0, 2 * radius, 2 * radius), 180, 270, fill=color)
    draw.pieslice((width - 2 * radius, 0, width, 2 * radius), 270, 360, fill=color)
    draw.pieslice((0, height - 2 * radius, 2 * radius, height), 90, 180, fill=color)
    draw.pieslice((width - 2 * radius, height - 2 * radius, width, height), 0, 90, fill=color)
    draw.rectangle((radius, 0, width - radius, height), fill=color)
    draw.rectangle((0, radius, width, height - radius), fill=color)
    return image


root = tk.Tk()
root.title("Sports Recommendation System")
root.geometry('925x500+300+200')


# Store data in SQLite database
conn = sqlite3.connect('sport.db')


# Global variable to store the username
current_user = None


def get_recommendations(preferences):
    conn = sqlite3.connect('sport.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT [{preferences}] FROM sport")
    recommendations = cursor.fetchall()
    conn.close()
    return recommendations


rounded_rectangle_image = create_rounded_rectangle(200, 100, 10, "lightblue")

# Convert the PIL image to Tkinter-compatible image
rounded_rectangle_photo = ImageTk.PhotoImage(rounded_rectangle_image)

# Define a rounded frame style
style = ttk.Style()
style.element_create("Rounded.Frame", "image", rounded_rectangle_photo, border=0, sticky="nsew")
style.layout("Rounded.TFrame", [("Rounded.Frame", {"sticky": "nsew"})])

def navigate_to_next_page(sport):
    # You can pass the username to the next page here
    print(f"Navigating to the next page for {sport} with username: {current_user}")

# Create a function to display recommendation cards
def show_recommendation_cards(recommendations):
    # Clear existing recommendation frames
    for widget in cards_frame.winfo_children():
        widget.destroy()

    # Define background color for recommendation frames
    bg_color = style.lookup("Inverted.TLabel", "background")

    for i, recommendation in enumerate(recommendations):
        # Create a frame for the recommendation card
        card_frame = ttk.Frame(cards_frame, height=300, padding=(60,5), style="Inverted.TLabel",borderwidth=20, relief="solid")
        card_frame.grid(row=i, column=0, padx=10, pady=10, sticky="nsew")

        # Add a colored label behind the frame
        background_label = ttk.Label(card_frame, background=bg_color)
        background_label.place(relwidth=1, relheight=1)

        # Add a label to display the recommendation
        recommendation_label = ttk.Label(card_frame, text=recommendation[0], font=("helvetica", 18))
        recommendation_label.pack()

        # Add a button to navigate to the next page
        navigate_button = ttk.Button(card_frame, text="Explore", command=lambda sport=recommendation[0]: navigate_to_next_page(sport))
        navigate_button.pack(pady=5, padx=10)

# Add a custom style for the rounded frame







# Create a user interface with tkinter


# Create a ttkbootstrap style
style = Style(theme="superhero")

# Create a frame to contain all widgets
main_frame = ScrolledFrame(root)
main_frame.pack(fill=tk.BOTH, expand=tk.YES)

style.configure("Inverted.TLabel", background=style.colors.dark, foreground=style.colors.light)
style.configure("Sidebar.TButton", font=("Arial", 15), width=15)

# Create a frame for the sidebar
sidebar_frame = ttk.Frame(main_frame,   padding=20,style="Inverted.TLabel", borderwidth=12, )
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

# Add components to the sidebar
sidebar_label = ttk.Label(sidebar_frame, text="Navbar", font=("Arial", 16))
sidebar_label.pack(pady=10)
button_width = 20

sidebar_button1 = ttk.Button(sidebar_frame, text="Recommendation", style="Sidebar.TButton")
sidebar_button1.pack(pady=5)

sidebar_button2 = ttk.Button(sidebar_frame, text="Test", style="Sidebar.TButton")
sidebar_button2.pack(pady=5)

sidebar_button3 = ttk.Button(sidebar_frame, text="Explore", style="Sidebar.TButton")
sidebar_button3.pack(pady=5)

# Create a frame for the content
content_frame = ttk.Frame(main_frame)
content_frame.pack(fill=tk.BOTH, expand=tk.YES)

# Create a frame for the header with a specified height and inverted colors
header_frame = ttk.Frame(content_frame, height=100)
header_frame.pack(fill='x')

# Create the main label with inverted colors
welcome_label = Label(header_frame, text="SPORTS TUTORIAL APP", font=('Courier New', 35, 'bold'), style="Inverted.TLabel", borderwidth=12, relief="groove")
welcome_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Adjust position of the main label to create the shadow effect
welcome_label.lift() 

separator = ttk.Separator(content_frame, orient='horizontal')
separator.pack(fill='x', padx=20, pady=20)

# Create a frame for the course details
course_d_frame = ttk.Frame(content_frame, padding=10, borderwidth=2, relief="solid", height=400, width=400)
course_d_frame.pack(pady=10, anchor=tk.CENTER, expand=True)

# Add a meter showing the course completion progress
course_completion_meter = Meter(course_d_frame, metersize=100, padding=5, amountused=25, metertype="semi", subtext="current course")
course_completion_meter.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Create a frame for course details
course_details_frame = ttk.Frame(course_d_frame, padding=10, borderwidth=2, relief="solid", height=200, width=200)
course_details_frame.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Add labels for course details
course_name_label = ttk.Label(course_details_frame, text="Course Name: Badminton", font=("Arial", 14))
course_name_label.grid(row=0, column=0, pady=5, sticky='w')

instructor_label = ttk.Label(course_details_frame, text="Instructor: sapp", font=("Arial", 14))
instructor_label.grid(row=1, column=0, pady=5, sticky='w')

duration_label = ttk.Label(course_details_frame, text="Duration: 6 weeks", font=("Arial", 14))
duration_label.grid(row=2, column=0, pady=5, sticky='w')

# Separator between course details and recommendations
separator = ttk.Separator(content_frame, orient='horizontal')
separator.pack(fill='x', padx=20, pady=20)

recommendation_frame = Frame(content_frame)
recommendation_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

meter = Meter(
    recommendation_frame,
    metersize=180,
    padding=5,
    amountused=25,
    metertype="semi",
    subtext="miles per hour",
    interactive=True,
)

title_label = ttk.Label(recommendation_frame, text="Sports Recommendation System", font=("Arial", 24))
title_label.pack(pady=20)

instruction_label = ttk.Label(recommendation_frame, text="Select an age group to see suitable sports recommended to you.", font=("Arial", 16))
instruction_label.pack(pady=10)

age_group_combobox = ttk.Combobox(recommendation_frame, values=["Children (Ages 0-12)", "Teenagers (Ages 13-19)", "Young Adults (Ages 20-39)", "Middle-Aged Adults (Ages 40-59)", "Older Adults (Ages 60+)"], font=("Arial", 14), state="readonly")
age_group_combobox.pack(pady=10)

cards_frame = ttk.Frame(content_frame)
cards_frame.pack(padx=10, pady=10)

recommendation_label = ttk.Label(recommendation_frame, text="", font=("Arial", 14))
recommendation_label.pack(pady=10)

def show_recommendations():
    selected_age_group = age_group_combobox.get()
    if selected_age_group:
        recommendations = get_recommendations(selected_age_group)
        recommendation_text = f"Recommendations for {selected_age_group}:\n"
        if recommendations:
            show_recommendation_cards(recommendations)
        else:
            recommendation_text += "No recommendations found for the selected age group."
        recommendation_label.config(text=recommendation_text)
    else:
        recommendation_label.config(text="Please select an age group.")

recommend_button = ttk.Button(recommendation_frame, text="Recommend", style="Sidebar.TButton", command=show_recommendations)
recommend_button.pack(pady=10)

root.mainloop()

