# # import tkinter as tk
# # import sqlite3

# # # Create a SQLite database (or connect to an existing one)
# # conn = sqlite3.connect("calorie_tracker.db")
# # cursor = conn.cursor()

# # # Create a table to store user entries
# # cursor.execute("""
# #     CREATE TABLE IF NOT EXISTS calorie_entries (
# #         id INTEGER PRIMARY KEY,
# #         name TEXT,
# #         calories INT
# #     )
# # """)
# # conn.commit()

# # def add_entry():
# #     name = name_entry.get()
# #     calories = int(calories_entry.get())

# #     # Insert the entry into the database
# #     cursor.execute("INSERT INTO calorie_entries (name, calories) VALUES (?, ?)", (name, calories))
# #     conn.commit()

# # def show_result():
# #     name = name_entry.get()

# #     # Retrieve total calorie intake for the specified user
# #     cursor.execute("SELECT SUM(calories) FROM calorie_entries WHERE name=?", (name,))
# #     total_calories = cursor.fetchone()[0]

# #     result_label.config(text=f"Total calories for {name}: {total_calories} kcal")

# # # Create the main application window
# # window = tk.Tk()
# # window.title("Calorie Tracker")

# # # Entry fields
# # name_label = tk.Label(window, text="Name:")
# # name_entry = tk.Entry(window)
# # calories_label = tk.Label(window, text="Calories:")
# # calories_entry = tk.Entry(window)

# # # Buttons
# # add_button = tk.Button(window, text="Add Entry", command=add_entry)
# # show_button = tk.Button(window, text="Show Result", command=show_result)

# # # Result display
# # result_label = tk.Label(window, text="")

# # # Layout
# # name_label.grid(row=0, column=0)
# # name_entry.grid(row=0, column=1)
# # calories_label.grid(row=1, column=0)
# # calories_entry.grid(row=1, column=1)
# # add_button.grid(row=2, column=0, columnspan=2)
# # show_button.grid(row=3, column=0, columnspan=2)
# # result_label.grid(row=4, column=0, columnspan=2)

# # # Start the GUI event loop
# # window.mainloop()

# # # Close the database connection when the application exits
# # conn.close()




# # //////////////////////////////////// NEWLY CODE ////////////////////////////// page 70 to 397
# import tkinter as tk
# import sqlite3
# from PIL import Image, ImageTk
# # import tkinter as tk
# import math
# from ttkbootstrap.widgets import  *
# from ttkbootstrap.widgets import Meter
# from PIL import Image, ImageTk
# import math
# from tkinter import ttk
# from ttkbootstrap import Style
# import subprocess
# from ttkbootstrap.scrolled import ScrolledFrame
# # import sqlite3
# from openpyxl.workbook import Workbook
# from PIL import Image, ImageDraw
# from tkinter.scrolledtext import ScrolledText
# import sys
# from PIL import ImageTk, Image


# # Create a SQLite database (or connect to an existing one)
# conn = sqlite3.connect("calorie_tracker.db")
# cursor = conn.cursor()

# # Create a table to store user entries
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS calorie_entries (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         calories INT
#     )
# """)
# conn.commit()

# # def add_entry():
# #     name = name_entry.get()
# #     calories = int(calories_entry.get())

# #     # Insert the entry into the database
# #     cursor.execute("INSERT INTO calorie_entries (name, calories) VALUES (?, ?)", (name, calories))
# #     conn.commit()

# def show_result():
#     name = name_entry.get()

#     # Retrieve total calorie intake for the specified user
#     cursor.execute("SELECT SUM(calories) FROM calorie_entries WHERE name=?", (name,))
#     total_calories = cursor.fetchone()[0]
#     print(total_calories)
#     result_label.config(text=f"Total calories of a day for {name}: {total_calories} kcal")

# def enter_raw_data():
#     conn = sqlite3.connect("calorie_counter.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS calorie_counter (
#         id INTEGER PRIMARY KEY,
#         meal TEXT,
#         calories INT,
#         image BLOB
#         )
#     """)
#     cursor.execute("""
#         INSERT INTO calorie_counter (meal, calories, image) 
#         VALUES 
#         ('chapati', 104, 'assets/chapati.png'),
#         ('bread', 82, 'assets/bread.png'),
#         ('lady finger', 35, 'assets/lady finger.png'),
#         ('cheese', 350, 'assets/cheese.png'),
#         ('rice', 242, 'assets/rice.png'),
#         ('idli', 58, 'assets/idli.png')
#     """)

#     conn.commit()
#     print("Added entry to database")


# def calorie_counter1():
#     con = sqlite3.connect("calorie_counter.db")
#     c1 = con.cursor()
    
#     # meal_calories = 0
#     # meal1 = item1_entry.get()
#     # meal2 = item2_entry.get()
#     # meal3 = item3_entry.get()
#     # meal4 = item4_entry.get()

#     # # # Retrieve calories for meal1
#     # print(meal1,meal2,meal3,meal4)
#     # c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal1,))
#     # calorie_entry1 = int(c1.fetchone())
#     # print(calorie_entry1)
    

#     # # # Retrieve calories for meal2
#     # c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal2,))
#     # calorie_entry2 = int(c1.fetchone())
    

#     # # # Retrieve calories for meal3
#     # c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal3,))
#     # calorie_entry3 = int(c1.fetchone())
   

#     # # # Retrieve calories for meal4
#     # c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal4,))
#     # calorie_entry4 = int(c1.fetchone())
    

#     # print(calorie_entry1, calorie_entry2, calorie_entry3, calorie_entry4)
#     # meal_calories = calorie_entry1+calorie_entry2+calorie_entry3+calorie_entry4

    

#     # meal_list = [item1_entry.get(), item2_entry.get(), item3_entry.get(), item4_entry.get()]
#     # for meal in meal_list:
#     #     if meal:  # Check if meal entry is not empty
#     #         c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal,))
#     #         calorie_entries = cursor.fetchall()
#     #         print(calorie_entries)
#     #         if calorie_entries:  # Check if any entries were found for the meal
#     #             for entry in calorie_entries:
#     #                 meal_calories += entry[0]
#     #             # result_label.config(text=f"Total calories from the meal: {meal_calories} kcal")
#     #         else:
#     #             print(f"No entries found for meal: {meal}")  # Debugging


    

#     # meal_calories = 0
#     # meal = item1_entry.get()

#     # cursor.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal,))
#     # calorie_entries = cursor.fetchall()

#     # if calorie_entries:  # Check if any entries were found for the meal
#     #     for entry in calorie_entries:
#     #         meal_calories += entry[0]
#     #     result_label.config(text=f"Total calories from the meal: {meal_calories} kcal")
#     # else:
#     #     result_label.config(text=f"No entries found for meal: {meal}")

#     # cursor.execute("SELECT calories FROM entries WHERE meal=?", (meal,))
#     # calorie_entries = cursor.fetchone()[0]
#     # result_label.config(text=f"Total calories from the meal: {calorie_entries} kcal")

#     # if calorie_entries:  # Check if any entries were found for the meal
#     #     for entry in calorie_entries:
#     #         meal_calories += entry[0]
#     meal_calories = 0
#     meal_entries = [item1_entry.get(), item2_entry.get(), item3_entry.get(), item4_entry.get()]

#     for meal in meal_entries:
#         if meal:  # Check if the meal entry is not empty
#             c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal,))
#             result = c1.fetchone()
#             if result:  # Check if the query result is not None
#                 calorie_entry = int(result[0])
#                 meal_calories += calorie_entry
#             else:
#                 print(f"No calorie information found for {meal}")
#         else:
#             print("Empty meal entry")

#     print("Total meal calories:", meal_calories)
#     calorie_label.config(text=f"Total calories from the meal: {meal_calories} kcal")
#     con.close()
#     # Starting the new cursor to point to the calorie_tracker.db
#     conn = sqlite3.connect("calorie_tracker.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO calorie_entries (name, calories) VALUES (?, ?)", (user_name_entry.get(), meal_calories))
#     conn.commit()
#     conn.close()

# # def calorie_counter():
# #     weight = float(weight_entry.get())
# #     height = float(height_entry.get())
# #     age = int(age_entry.get())
# #     gender = gender_var.get()

# #     if gender == "Male":
# #         bmr = 10 * weight + 6.25 * height - 5 * age + 5
# #     else:
# #         bmr = 10 * weight + 6.25 * height - 5 * age - 161

# #     result_label.config(text=f"Your BMR: {bmr} kcal/day")
# # Create the main application window
    

# def show_calorie_table_info():
#     # Display the table with appropriate images
#     con=sqlite3.connect('calorie_counter.db')
#     c = con.cursor()    
    
#     # Create labels for table headers
#     header_labels = ["Name", "Calories", "Image"]
#     for i, header in enumerate(header_labels):
#         label = tk.Label(frame2, text=header, font=("Arial", 12, "bold"))
#         label.grid(row=0, column=i, padx=10, pady=20)

#     # Retrieve all entries from the database
#     c.execute("SELECT * FROM calorie_counter")
#     entries = c.fetchall()

#     # Display the entries in the table
#     for i, entry in enumerate(entries):
#         name = entry[1]
#         calories = entry[2]
#         image = entry[3]

#         # Create labels for name and calories
#         name_label = tk.Label(frame2, text=name)
#         name_label.grid(row=i+1, column=0, padx=10, pady=5)

#         calories_label = tk.Label(frame2, text=calories)
#         calories_label.grid(row=i+1, column=1, padx=10, pady=5)

#         # Create an image label
#         image_path = image  # Assuming the images are stored in a folder named "images"
#         try:
#             image_pil = Image.open(image_path)
#             image_pil = image_pil.resize((50, 50))  # Resize the image as needed
#             image_tk = ImageTk.PhotoImage(image_pil)
#             image_label = tk.Label(frame2, image=image_tk)
#             image_label.image = image_tk  # Keep a reference to the image to prevent it from being garbage collected
#             image_label.grid(row=i + 1, column=2, padx=10, pady=5)
#         except FileNotFoundError:
#             print(f"Image not found for {name}: {image_path}")
#     con.close()
#     frame2.pack(side="right",padx=100)


# # Create the main application window
# window = tk.Tk()
# root = tk.Tk()
# window.title("Calorie Tracker")

# # Create a frame
# frame = tk.Frame(window)
# frame1 = tk.Frame(window)
# frame2 = tk.Frame(window)


# # frame3 = tk.Frame(window) #empty frames
# # frame4 = tk.Frame(window) #empty frames
# # frame5 = tk.Frame(window) #empty frames
# # frame2.place(x=50,y=39)

# # Entry fields
# name_label = tk.Label(frame, text="Name:")
# name_entry = tk.Entry(frame)
# # calories_label = tk.Label(frame, text="Calories:")
# # calories_entry = tk.Entry(frame)

# title = tk.Label(frame1, text="Calorie Counter")
# user_name = tk.Label(frame1, text="Your Name:")
# user_name_entry = tk.Entry(frame1)
# item1 = tk.Label(frame1, text="Food item 1:")
# item1_entry = tk.Entry(frame1)
# item2 = tk.Label(frame1, text="Food item 2:")
# item2_entry = tk.Entry(frame1)
# item3 = tk.Label(frame1, text="Food item 3:")
# item3_entry = tk.Entry(frame1)
# item4 = tk.Label(frame1, text ="Food item 4:")
# item4_entry = tk.Entry(frame1)
# #title_empty = tk.Label(frame3, text="                          ")   #empty title

# # Buttons
# # add_button = tk.Button(frame, text="Add Entry", command=add_entry)
# show_button = tk.Button(frame, text="Show Result", command=show_result)
# calorie_counter_button = tk.Button(frame1, text="Calculate Calories", command=calorie_counter1)
# # raw_data=tk.Button(frame1,text='Enter raw data',command=enter_raw_data)
# # show_calorie_chart=tk.Button(frame2,text='Show Calorie Chart',command=show_calorie_table_info)
# # Result display
# result_label = tk.Label(frame, text="")
# calorie_label = tk.Label(frame1, text="")

# # Layout
# # frame layout
# name_label.grid(row=0, column=0)
# name_entry.grid(row=0, column=1)
# # calories_label.grid(row=1, column=0)
# # calories_entry.grid(row=1, column=1)
# # add_button.grid(row=2, column=0, columnspan=2)
# show_button.grid(row=3, column=0, columnspan=2)
# result_label.grid(row=4, column=0, columnspan=2)


# # frame1 layout
# title.grid(row=0, column=0)
# user_name.grid(row=1, column=0)
# user_name_entry.grid(row=1, column=1)
# item1.grid(row=2, column=0)
# item1_entry.grid(row=2, column=1)
# item2.grid(row=3, column=0)
# item2_entry.grid(row=3, column=1)
# item3.grid(row=4, column=0)
# item3_entry.grid(row=4, column=1)
# item4.grid(row=5, column=0)
# item4_entry.grid(row=5, column=1)
# calorie_counter_button.grid(row=6, column=0, columnspan=2)
# # raw_data.grid(row=6,column=0, columnspan=2)
# calorie_label.grid(row=7, column=0, columnspan=2)


# # Frame2 layout
# # show_calorie_chart.grid(row=0,column=0)
# show_calorie_table_info()

# # enter_raw_data()


# # Pack the frame
# frame1.pack(side="right",padx=20)
# frame.pack(side="right",pady=40)  
# # frame2.grid(row=0, column=5)   necessary part of it !!!!!!!!!!!!!!!!!!!
# # frame2.pack(side="right")
# # frame3.grid(row=0,column=0) # empty frame


# # Start the GUI event loop
# window.mainloop()

# # Close the database connection when the application exits
# conn.close()




















# really corrected code everything has been checked and it is working vertically properly
# import tkinter as tk
# from tkinter import ttk
# import sqlite3
# from PIL import Image, ImageTk


# def show_result():
#     name = name_entry.get()
#     cursor.execute("SELECT SUM(calories) FROM calorie_entries WHERE name=?", (name,))
#     total_calories = cursor.fetchone()[0]
#     print(total_calories)
#     result_label.config(text=f"Total calories of a day for {name}: {total_calories} kcal")


# def calorie_counter1():
#     con = sqlite3.connect("calorie_counter.db")
#     c1 = con.cursor()
#     meal_calories = 0
#     meal_entries = [item1_entry.get(), item2_entry.get(), item3_entry.get(), item4_entry.get()]

#     for meal in meal_entries:
#         if meal:
#             c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal,))
#             result = c1.fetchone()
#             if result:
#                 calorie_entry = int(result[0])
#                 meal_calories += calorie_entry
#             else:
#                 print(f"No calorie information found for {meal}")
#         else:
#             print("Empty meal entry")

#     print("Total meal calories:", meal_calories)
#     calorie_label.config(text=f"Total calories from the meal: {meal_calories} kcal")
#     con.close()

#     conn = sqlite3.connect("calorie_tracker.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO calorie_entries (name, calories) VALUES (?, ?)", (user_name_entry.get(), meal_calories))
#     conn.commit()
#     conn.close()


# def show_calorie_table_info():
#     con = sqlite3.connect('calorie_counter.db')
#     c = con.cursor()
    
#     header_labels = ["Name", "Calories", "Image"]
#     for header in header_labels:
#         label = tk.Label(frame2, text=header, font=("Arial", 12, "bold"))
#         label.grid(row=0, column=header_labels.index(header), padx=10, pady=5)

#     c.execute("SELECT * FROM calorie_counter")
#     entries = c.fetchall()

#     for i, entry in enumerate(entries, start=1):
#         name = entry[1]
#         calories = entry[2]
#         image = entry[3]

#         name_label = tk.Label(frame2, text=name)
#         name_label.grid(row=i, column=0, padx=10, pady=5)

#         calories_label = tk.Label(frame2, text=calories)
#         calories_label.grid(row=i, column=1, padx=10, pady=5)

#         try:
#             image_pil = Image.open(image)
#             image_pil = image_pil.resize((50, 50))
#             image_tk = ImageTk.PhotoImage(image_pil)
#             image_label = tk.Label(frame2, image=image_tk)
#             image_label.image = image_tk
#             image_label.grid(row=i, column=2, padx=10, pady=5)
#         except FileNotFoundError:
#             print(f"Image not found for {name}: {image}")

#     con.close()


# # Create a SQLite database
# conn = sqlite3.connect("calorie_tracker.db")
# cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS calorie_entries (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         calories INT
#     )
# """)
# conn.commit()


# # Create the main application window
# window = tk.Tk()
# window.title("Calorie Tracker")

# # Create a canvas for scrolling
# canvas = tk.Canvas(window)
# canvas.pack(side="left", fill="both", expand=True)

# # Add a scrollbar to the canvas
# scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
# scrollbar.pack(side="right", fill="y")

# # Configure the canvas to use the scrollbar
# canvas.configure(yscrollcommand=scrollbar.set)
# canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# # Create a frame inside the canvas to contain the widgets
# scrollable_frame = tk.Frame(canvas)

# # Add the scrollable frame to the canvas
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# # Entry fields
# frame = tk.Frame(scrollable_frame)
# name_label = tk.Label(frame, text="Name:")
# name_entry = tk.Entry(frame)
# show_button = tk.Button(frame, text="Show Result", command=show_result)
# result_label = tk.Label(frame, text="")
# frame.pack()

# # Layout for entry fields
# name_label.grid(row=0, column=0)
# name_entry.grid(row=0, column=1)
# show_button.grid(row=1, column=0, columnspan=2)
# result_label.grid(row=2, column=0, columnspan=2)

# # Entry fields
# frame1 = tk.Frame(scrollable_frame)
# title = tk.Label(frame1, text="Calorie Counter")
# user_name = tk.Label(frame1, text="Your Name:")
# user_name_entry = tk.Entry(frame1)
# item1 = tk.Label(frame1, text="Food item 1:")
# item1_entry = tk.Entry(frame1)
# item2 = tk.Label(frame1, text="Food item 2:")
# item2_entry = tk.Entry(frame1)
# item3 = tk.Label(frame1, text="Food item 3:")
# item3_entry = tk.Entry(frame1)
# item4 = tk.Label(frame1, text="Food item 4:")
# item4_entry = tk.Entry(frame1)
# calorie_counter_button = tk.Button(frame1, text="Calculate Calories", command=calorie_counter1)
# calorie_label = tk.Label(frame1, text="")
# frame1.pack()

# # Layout for entry fields
# title.grid(row=0, column=0)
# user_name.grid(row=1, column=0)
# user_name_entry.grid(row=1, column=1)
# item1.grid(row=2, column=0)
# item1_entry.grid(row=2, column=1)
# item2.grid(row=3, column=0)
# item2_entry.grid(row=3, column=1)
# item3.grid(row=4, column=0)
# item3_entry.grid(row=4, column=1)
# item4.grid(row=5, column=0)
# item4_entry.grid(row=5, column=1)
# calorie_counter_button.grid(row=6, column=0, columnspan=2)
# calorie_label.grid(row=7, column=0, columnspan=2)

# # Entry fields
# frame2 = tk.Frame(scrollable_frame)
# show_calorie_table_info()
# frame2.pack()

# # Pack the scrollable frame into the canvas
# scrollable_frame.pack(side="left", fill="both", expand=True)

# # Start the GUI event loop
# window.mainloop()

# # Close the database connection when the application exits
# conn.close()


























import tkinter as tk
import sqlite3
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# Create a SQLite database for the Calorie Tracker
conn_calorie = sqlite3.connect("calorie_tracker.db")
cursor_calorie = conn_calorie.cursor()

cursor_calorie.execute("""
    CREATE TABLE IF NOT EXISTS calorie_entries (
        id INTEGER PRIMARY KEY,
        name TEXT,
        calories INT
    )
""")
conn_calorie.commit()

def show_result():
    name = name_entry.get()
    cursor_calorie.execute("SELECT SUM(calories) FROM calorie_entries WHERE name=?", (name,))
    total_calories = cursor_calorie.fetchone()[0]
    result_label.config(text=f"Total calories of a day for {name}: {total_calories} kcal")

def calorie_counter():
    con = sqlite3.connect("calorie_counter.db")
    c1 = con.cursor()
    meal_calories = 0
    meal_entries = [item1_entry.get(), item2_entry.get(), item3_entry.get(), item4_entry.get()]

    for meal in meal_entries:
        if meal:
            c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal,))
            result = c1.fetchone()
            if result:
                calorie_entry = int(result[0])
                meal_calories += calorie_entry
            else:
                print(f"No calorie information found for {meal}")
        else:
            print("Empty meal entry")

    calorie_label.config(text=f"Total calories from the meal: {meal_calories} kcal")
    con.close()

    conn = sqlite3.connect("calorie_tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO calorie_entries (name, calories) VALUES (?, ?)", (user_name_entry.get(), meal_calories))
    conn.commit()
    conn.close()

def show_calorie_table_info():
    con = sqlite3.connect('calorie_counter.db')
    c = con.cursor()

    header_labels = ["Name", "Calories", "Image"]
    for header in header_labels:
        label = tk.Label(frame2, text=header, font=("Arial", 12, "bold"))
        label.grid(row=0, column=header_labels.index(header), padx=10, pady=5)

    c.execute("SELECT * FROM calorie_counter")
    entries = c.fetchall()

    for i, entry in enumerate(entries, start=1):
        name = entry[1]
        calories = entry[2]
        image = entry[3]

        name_label = tk.Label(frame2, text=name)
        name_label.grid(row=i, column=0, padx=10, pady=5)

        calories_label = tk.Label(frame2, text=calories)
        calories_label.grid(row=i, column=1, padx=10, pady=5)

        try:
            image_pil = Image.open(image)
            image_pil = image_pil.resize((50, 50))
            image_tk = ImageTk.PhotoImage(image_pil)
            image_label = tk.Label(frame2, image=image_tk)
            image_label.image = image_tk
            image_label.grid(row=i, column=2, padx=10, pady=5)
        except FileNotFoundError:
            print(f"Image not found for {name}: {image}")

    con.close()

# Create a SQLite database for the BMI Tracker
conn_bmi = sqlite3.connect("bmi_tracker.db")
cursor_bmi = conn_bmi.cursor()

cursor_bmi.execute("""
    CREATE TABLE IF NOT EXISTS bmi_entries (
        id INTEGER PRIMARY KEY,
        name TEXT,
        weight_kg REAL,
        height_cm REAL
    )
""")
conn_bmi.commit()

def calculate_bmi():
    name = name_entry_bmi.get()
    weight_kg = float(weight_entry_bmi.get())
    height_cm = float(height_entry_bmi.get())

    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 1)

    cursor_bmi.execute("INSERT INTO bmi_entries (name, weight_kg, height_cm) VALUES (?, ?, ?)",
                       (name, weight_kg, height_cm))
    conn_bmi.commit()

    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        category = "Underweight"
        recommendations = [
            "1. Swimming: Freestyle, breaststroke, or backstroke are good options to build muscle mass.",
            "2. Weightlifting: Focus on compound exercises like squats, deadlifts, and bench presses.",
            "3. Yoga: Helps in improving flexibility, strength, and overall well-being."
        ]
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
        recommendations = [
            "1. Walking: Brisk walking is a great way to maintain overall health and fitness.",
            "2. Cycling: Ride a bicycle to improve cardiovascular health and leg strength.",
            "3. Dancing: Fun and effective for cardiovascular fitness and overall well-being."
        ]
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        recommendations = [
            "1. Running: Start with a mix of walking and running to build endurance and burn calories.",
            "2. Aerobics: High-energy workouts like Zumba or aerobics classes can help with weight loss.",
            "3. Interval Training: Incorporate intervals of high-intensity exercise with periods of rest."
        ]
    else:
        category = "Obesity"
        recommendations = [
            "1. High-Intensity Interval Training (HIIT): Effective for burning calories and improving cardiovascular health.",
            "2. CrossFit: Combines strength training and high-intensity cardio for a full-body workout.",
            "3. Rowing: Low-impact exercise that engages multiple muscle groups and helps with weight loss."
        ]

    result_label_bmi.config(text=f"BMI: {bmi} ({category})\n\nExercise Recommendations:\n" + "\n".join(recommendations))

# Create the main application window
window = tk.Tk()
window.title("Calorie Tracker & BMI Calculator")

# Create a canvas for scrolling
canvas = tk.Canvas(window)
canvas.pack(side="left", fill="both", expand=True)

# Add a scrollbar to the canvas
scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas to contain the widgets
scrollable_frame = tk.Frame(canvas)

# Add the scrollable frame to the canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Entry fields for BMI calculator
frame4 = tk.Frame(scrollable_frame)
frame4.pack(side="top", pady=10)

name_label_bmi = tk.Label(frame4, text="Name:")
name_entry_bmi = tk.Entry(frame4)
weight_label_bmi = tk.Label(frame4, text="Weight (kg):")
weight_entry_bmi = tk.Entry(frame4)
height_label_bmi = tk.Label(frame4, text="Height (cm):")
height_entry_bmi = tk.Entry(frame4)

# Button for BMI calculation
calculate_button_bmi = tk.Button(frame4, text="Calculate BMI", command=calculate_bmi)

# Result display for BMI
result_label_bmi = tk.Label(frame4, text="")

# Layout for BMI calculator entry fields
name_label_bmi.grid(row=0, column=0)
name_entry_bmi.grid(row=0, column=1)
weight_label_bmi.grid(row=1, column=0)
weight_entry_bmi.grid(row=1, column=1)
height_label_bmi.grid(row=2, column=0)
height_entry_bmi.grid(row=2, column=1)
calculate_button_bmi.grid(row=3, column=0, columnspan=2)
result_label_bmi.grid(row=4, column=0, columnspan=2)

# Entry fields for Calorie Tracker
frame = tk.Frame(scrollable_frame)
frame.pack(side="top", pady=10)

name_label = tk.Label(frame, text="Name:")
name_entry = tk.Entry(frame)
show_button = tk.Button(frame, text="Show Result", command=show_result)
result_label = tk.Label(frame, text="")
frame.pack()

# Layout for Calorie Tracker entry fields
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
show_button.grid(row=1, column=0, columnspan=2)
result_label.grid(row=2, column=0, columnspan=2)

# Entry fields for Calorie Counter
frame1 = tk.Frame(scrollable_frame)
frame1.pack(side="top", pady=10)

title = tk.Label(frame1, text="Calorie Counter")
user_name = tk.Label(frame1, text="Your Name:")
user_name_entry = tk.Entry(frame1)
item1 = tk.Label(frame1, text="Food item 1:")
item1_entry = tk.Entry(frame1)
item2 = tk.Label(frame1, text="Food item 2:")
item2_entry = tk.Entry(frame1)
item3 = tk.Label(frame1, text="Food item 3:")
item3_entry = tk.Entry(frame1)
item4 = tk.Label(frame1, text="Food item 4:")
item4_entry = tk.Entry(frame1)
calorie_counter_button = tk.Button(frame1, text="Calculate Calories", command=calorie_counter)
calorie_label = tk.Label(frame1, text="")
frame1.pack()

# Layout for Calorie Counter entry fields
title.grid(row=0, column=0)
user_name.grid(row=1, column=0)
user_name_entry.grid(row=1, column=1)
item1.grid(row=2, column=0)
item1_entry.grid(row=2, column=1)
item2.grid(row=3, column=0)
item2_entry.grid(row=3, column=1)
item3.grid(row=4, column=0)
item3_entry.grid(row=4, column=1)
item4.grid(row=5, column=0)
item4_entry.grid(row=5, column=1)
calorie_counter_button.grid(row=6, column=0, columnspan=2)
calorie_label.grid(row=7, column=0, columnspan=2)

# Entry fields for Calorie Table
frame2 = tk.Frame(scrollable_frame)
frame2.pack(side="top", pady=10)

show_calorie_table_info()
frame2.pack()

# Pack the scrollable frame into the canvas
scrollable_frame.pack(side="left", fill="both", expand=True)

# Start the GUI event loop
window.mainloop()

# Close the database connections when the application exits
conn_calorie.close()
conn_bmi.close()
