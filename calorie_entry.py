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
from PIL import Image, ImageTk

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

def enter_raw_data():
    conn = sqlite3.connect("calorie_counter.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO calorie_counter (meal, calories) 
    VALUES 
    ('chapati', 104),
    ('bread', 82),
    ('lady finger', 35),
    ('cheese', 350),
    ('rice', 242),
    ('idly', 58)
    """)

    conn.commit()
    print("Added entry to database")

def calorie_counter1():
    conn=sqlite3.connect('calorie_counter.db')
    c1 = conn.cursor()

    # Create a table to store user entries
    c1.execute("""
        CREATE TABLE IF NOT EXISTS calorie_counter (
        id INTEGER PRIMARY KEY,
        meal TEXT,
        calories INT
        )
    """)
    
    # meal_calories = 0
    # meal1 = item1_entry.get()
    # meal2 = item2_entry.get()
    # meal3 = item3_entry.get()
    # meal4 = item4_entry.get()

    # # # Retrieve calories for meal1
    # print(meal1,meal2,meal3,meal4)
    # c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal1,))
    # calorie_entry1 = int(c1.fetchone())
    # print(calorie_entry1)
    

    # # # Retrieve calories for meal2
    # c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal2,))
    # calorie_entry2 = int(c1.fetchone())
    

    # # # Retrieve calories for meal3
    # c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal3,))
    # calorie_entry3 = int(c1.fetchone())
   

    # # # Retrieve calories for meal4
    # c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal4,))
    # calorie_entry4 = int(c1.fetchone())
    

    # print(calorie_entry1, calorie_entry2, calorie_entry3, calorie_entry4)
    # meal_calories = calorie_entry1+calorie_entry2+calorie_entry3+calorie_entry4

    

    # meal_list = [item1_entry.get(), item2_entry.get(), item3_entry.get(), item4_entry.get()]
    # for meal in meal_list:
    #     if meal:  # Check if meal entry is not empty
    #         c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal,))
    #         calorie_entries = cursor.fetchall()
    #         print(calorie_entries)
    #         if calorie_entries:  # Check if any entries were found for the meal
    #             for entry in calorie_entries:
    #                 meal_calories += entry[0]
    #             # result_label.config(text=f"Total calories from the meal: {meal_calories} kcal")
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
    meal_calories = 0
    meal_entries = [item1_entry.get(), item2_entry.get(), item3_entry.get(), item4_entry.get()]

    for meal in meal_entries:
        if meal:  # Check if the meal entry is not empty
            c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal,))
            result = c1.fetchone()
            if result:  # Check if the query result is not None
                calorie_entry = int(result[0])
                meal_calories += calorie_entry
            else:
                print(f"No calorie information found for {meal}")
        else:
            print("Empty meal entry")

    print("Total meal calories:", meal_calories)



    calorie_label.config(text=f"Total calories from the meal: {meal_calories} kcal")
# def calorie_counter():
#     weight = float(weight_entry.get())
#     height = float(height_entry.get())
#     age = int(age_entry.get())
#     gender = gender_var.get()

#     if gender == "Male":
#         bmr = 10 * weight + 6.25 * height - 5 * age + 5
#     else:
#         bmr = 10 * weight + 6.25 * height - 5 * age - 161

#     result_label.config(text=f"Your BMR: {bmr} kcal/day")
# Create the main application window
    

def show_calorie_table_info():
    # Display the table with appropriate images
    con=sqlite3.connect('calorie_counter.db')
    c = con.cursor()    
    
    # Create labels for table headers
    header_labels = ["Name", "Calories", "Image"]
    for i, header in enumerate(header_labels):
        label = tk.Label(frame2, text=header, font=("Arial", 12, "bold"))
        label.grid(row=0, column=i, padx=10, pady=20)

    # Retrieve all entries from the database
    c.execute("SELECT * FROM calorie_counter")
    entries = c.fetchall()

    # Display the entries in the table
    for i, entry in enumerate(entries):
        name = entry[1]
        calories = entry[2]

        # Create labels for name and calories
        name_label = tk.Label(frame2, text=name)
        name_label.grid(row=i+1, column=0, padx=10, pady=5)

        calories_label = tk.Label(frame2, text=calories)
        calories_label.grid(row=i+1, column=1, padx=10, pady=5)

        # Create an image label
        image_path = f"assets/shots.png"  # Assuming the images are stored in a folder named "images"
        try:
            image_pil = Image.open(image_path)
            image_pil = image_pil.resize((50, 50))  # Resize the image as needed
            image_tk = ImageTk.PhotoImage(image_pil)
            image_label = tk.Label(frame2, image=image_tk)
            image_label.image = image_tk  # Keep a reference to the image to prevent it from being garbage collected
            image_label.grid(row=i + 1, column=2, padx=10, pady=5)
        except FileNotFoundError:
            print(f"Image not found for {name}: {image_path}")
    con.close()
   


# Create the main application window
window = tk.Tk()
window.title("Calorie Tracker")

# Create a frame
frame = tk.Frame(window)
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)

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
raw_data=tk.Button(frame1,text='Enter raw data',command=enter_raw_data)
# show_calorie_chart=tk.Button(frame2,text='Show Calorie Chart',command=show_calorie_table_info)
# Result display
result_label = tk.Label(frame, text="")
calorie_label = tk.Label(frame1, text="")

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
raw_data.grid(row=6,column=0, columnspan=2)
calorie_label.grid(row=7, column=0, columnspan=2)

# Frame2 layout
# show_calorie_chart.grid(row=0,column=0)
show_calorie_table_info()

# Pack the frame
frame.grid(row=0, column=0)
frame1.grid(row=1, column=0)
frame2.grid(row=0, column=1)

# Start the GUI event loop
window.mainloop()

# Close the database connection when the application exits
conn.close()



