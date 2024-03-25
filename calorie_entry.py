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

    result_label.config(text=f"Total calories for {name}: {total_calories} kcal")

# Create the main application window
window = tk.Tk()
window.title("Calorie Tracker")

# Entry fields
name_label = tk.Label(window, text="Name:")
name_entry = tk.Entry(window)
calories_label = tk.Label(window, text="Calories:")
calories_entry = tk.Entry(window)

# Buttons
add_button = tk.Button(window, text="Add Entry", command=add_entry)
show_button = tk.Button(window, text="Show Result", command=show_result)

# Result display
result_label = tk.Label(window, text="")

# Layout
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
calories_label.grid(row=1, column=0)
calories_entry.grid(row=1, column=1)
add_button.grid(row=2, column=0, columnspan=2)
show_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

# Start the GUI event loop
window.mainloop()

# Close the database connection when the application exits
conn.close()

