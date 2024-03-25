# import tkinter as tk
# import sqlite3

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

# def add_entry():
#     name = name_entry.get()
#     calories = int(calories_entry.get())

#     # Insert the entry into the database
#     cursor.execute("INSERT INTO calorie_entries (name, calories) VALUES (?, ?)", (name, calories))
#     conn.commit()

# def show_result():
#     name = name_entry.get()

#     # Retrieve total calorie intake for the specified user
#     cursor.execute("SELECT SUM(calories) FROM calorie_entries WHERE name=?", (name,))
#     total_calories = cursor.fetchone()[0]

#     result_label.config(text=f"Total calories for {name}: {total_calories} kcal")

# # Create the main application window
# window = tk.Tk()
# window.title("Calorie Tracker")

# # Entry fields
# name_label = tk.Label(window, text="Name:")
# name_entry = tk.Entry(window)
# calories_label = tk.Label(window, text="Calories:")
# calories_entry = tk.Entry(window)

# # Buttons
# add_button = tk.Button(window, text="Add Entry", command=add_entry)
# show_button = tk.Button(window, text="Show Result", command=show_result)

# # Result display
# result_label = tk.Label(window, text="")

# # Layout
# name_label.grid(row=0, column=0)
# name_entry.grid(row=0, column=1)
# calories_label.grid(row=1, column=0)
# calories_entry.grid(row=1, column=1)
# add_button.grid(row=2, column=0, columnspan=2)
# show_button.grid(row=3, column=0, columnspan=2)
# result_label.grid(row=4, column=0, columnspan=2)

# # Start the GUI event loop
# window.mainloop()

# # Close the database connection when the application exits
# conn.close()




# //////////////////////////////////// NEWLY CODE //////////////////////////////
import tkinter as tk
import sqlite3
import tkinter as tk
import sqlite3

# Create a SQLite database (or connect to an existing one)
conn = sqlite3.connect("calorie_tracker.db")
cursor = conn.cursor()

# Create a table to store user entries
cursor.execute("""
    CREATE TABLE IF NOT EXISTS calorie_entries (
        id INTEGER PRIMARY KEY,
        name TEXT,
        calories INT
    )
""")
conn.commit()

def add_entry():
    name = name_entry.get()
    calories = int(calories_entry.get())

    # Insert the entry into the database
    cursor.execute("INSERT INTO calorie_entries (name, calories) VALUES (?, ?)", (name, calories))
    conn.commit()

def show_result():
    name = name_entry.get()

    # Retrieve total calorie intake for the specified user
    cursor.execute("SELECT SUM(calories) FROM calorie_entries WHERE name=?", (name,))
    total_calories = cursor.fetchone()[0]
    print(total_calories)
    result_label.config(text=f"Total calories for {name}: {total_calories} kcal")

def calorie_counter1():
    conn = sqlite3.connect("calorie_counter.db")
    cursor = conn.cursor()

    # Create a table to store user entries
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calorie_counter (
        id INTEGER PRIMARY KEY,
        meal TEXT,
        calories INT
        )
    """)
    conn.commit()
    meal_calories = 0
    meal1 = item1_entry.get()
    meal2 = item2_entry.get()
    meal3 = item3_entry.get()
    meal4 = item4_entry.get()

    # Retrieve calories for meal1
    cursor.execute("SELECT SUM(calories) FROM calorie_counter WHERE meal=?", (meal1,))
    calorie_entry1 = cursor.fetchone()[0]
    # if calorie_entry1:
    #     calorie_entries1 = calorie_entry1[0]
    #     meal_calories += calorie_entries1

    # Retrieve calories for meal2
    cursor.execute("SELECT SUM(calories) FROM calorie_counter WHERE meal=?", (meal2,))
    calorie_entry2 = cursor.fetchone()[0]
    # if calorie_entry2:
    #     calorie_entries2 = calorie_entry2[0]
    #     meal_calories += calorie_entries2

    # Retrieve calories for meal3
    cursor.execute("SELECT SUM(calories) FROM calorie_counter WHERE meal=?", (meal3,))
    calorie_entry3 = cursor.fetchone()[0]
    # if calorie_entry3:
    #     calorie_entries3 = calorie_entry3[0]
    #     meal_calories += calorie_entries3

    # Retrieve calories for meal4
    cursor.execute("SELECT SUM(calories) FROM calorie_counter WHERE meal=?", (meal4,))
    calorie_entry4 = cursor.fetchone()[0]
    # if calorie_entry4:
    #     calorie_entries4 = calorie_entry4[0]
    #     meal_calories += calorie_entries4

    print(calorie_entry1, calorie_entry2, calorie_entry3, calorie_entry4)

    

    # meal_list = [item1_entry.get(), item2_entry.get(), item3_entry.get(), item4_entry.get()]
    # for meal in meal_list:
    #     if meal:  # Check if meal entry is not empty
    #         cursor.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal,))
    #         calorie_entries = cursor.fetchall()
    #         print(calorie_entries)
    #         if calorie_entries:  # Check if any entries were found for the meal
    #             for entry in calorie_entries:
    #                 meal_calories += entry[0]
    #         else:
    #             print(f"No entries found for meal: {meal}")  # Debugging


    

    # meal_calories = 0
    # meal = item1_entry.get()

    # cursor.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal,))
    # calorie_entries = cursor.fetchall()

    # if calorie_entries:  # Check if any entries were found for the meal
    #     for entry in calorie_entries:
    #         meal_calories += entry[0]
    #     result_label.config(text=f"Total calories from the meal: {meal_calories} kcal")
    # else:
    #     result_label.config(text=f"No entries found for meal: {meal}")

    # cursor.execute("SELECT calories FROM entries WHERE meal=?", (meal,))
    # calorie_entries = cursor.fetchone()[0]
    # result_label.config(text=f"Total calories from the meal: {calorie_entries} kcal")

    # if calorie_entries:  # Check if any entries were found for the meal
    #     for entry in calorie_entries:
    #         meal_calories += entry[0]



    result_label.config(text=f"Total calories from the meal: {meal_calories} kcal")
def calorie_counter():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    age = int(age_entry.get())
    gender = gender_var.get()

    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    result_label.config(text=f"Your BMR: {bmr} kcal/day")
# Create the main application window
window = tk.Tk()
window.title("Calorie Tracker")

# Create a frame
frame = tk.Frame(window)
frame1 = tk.Frame(window)
# Entry fields
name_label = tk.Label(frame, text="Name:")
name_entry = tk.Entry(frame)
calories_label = tk.Label(frame, text="Calories:")
calories_entry = tk.Entry(frame)

title = tk.Label(frame1, text="Calorie Counter")
item1 = tk.Label(frame1, text="Food item 1:")
item1_entry = tk.Entry(frame1)
item2 = tk.Label(frame1, text="Food item 2:")
item2_entry = tk.Entry(frame1)
item3 = tk.Label(frame1, text="Food item 3:")
item3_entry = tk.Entry(frame1)
item4 = tk.Label(frame1, text ="Food item 4:")
item4_entry = tk.Entry(frame1)

# Buttons
add_button = tk.Button(frame, text="Add Entry", command=add_entry)
show_button = tk.Button(frame, text="Show Result", command=show_result)
calorie_counter_button = tk.Button(frame1, text="Calculate Calories", command=calorie_counter1)

# Result display
result_label = tk.Label(frame, text="")

# Layout
# frame layout
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
calories_label.grid(row=1, column=0)
calories_entry.grid(row=1, column=1)
add_button.grid(row=2, column=0, columnspan=2)
show_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

# frame1 layout
title.grid(row=0, column=0)
item1.grid(row=1, column=0)
item1_entry.grid(row=1, column=1)
item2.grid(row=2, column=0)
item2_entry.grid(row=2, column=1)
item3.grid(row=3, column=0)
item3_entry.grid(row=3, column=1)
item4.grid(row=4, column=0)
item4_entry.grid(row=4, column=1)
calorie_counter_button.grid(row=5, column=0, columnspan=2)

# Pack the frame
frame.pack()
frame1.pack()

# Start the GUI event loop
window.mainloop()

# Close the database connection when the application exits
conn.close()

# Start the GUI event loop
window.mainloop()

# Close the database connection when the application exits
conn.close()

