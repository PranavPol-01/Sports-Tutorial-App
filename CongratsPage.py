# import tkinter as tk
# from tkinter import ttk

# class CongratulationsPage(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Congratulations")

#         # Message Label
#         self.message_label = ttk.Label(self, text="Congrats! You completed the assessment.", font=("Helvetica", 20))
#         self.message_label.pack(pady=50)

#         # Blue Tick Image
#         self.blue_tick_image = tk.PhotoImage(file="bluetick.png")  # Replace with the path to your blue tick image
#         self.blue_tick_label = ttk.Label(self, image=self.blue_tick_image)
#         self.blue_tick_label.pack()

#         # Take Test Button
#         self.take_test_button = ttk.Button(self, text="Take Test", command=self.take_test)
#         self.take_test_button.pack(side=tk.BOTTOM, pady=30)

#     def take_test(self):
#         print("Redirecting to the test page...")  # Placeholder for redirection functionality

# if __name__ == "__main__":
#     app = CongratulationsPage()
#     app.mainloop()



# import tkinter as tk
# from tkinter import ttk

# class CongratulationsPage(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Congratulations")

#         # Set background color
#         self.configure(bg="#1a3356")  # Dark blue background color

#         # Message Label with customized text color and background color
#         self.message_label = ttk.Label(self, text="Congrats! You completed the assessment.", font=("Helvetica", 20), foreground="#ffffff", background="#1a3356")
#         self.message_label.pack(pady=50)

#         # Blue Tick Image
#         self.blue_tick_image = tk.PhotoImage(file="bluetick.png")  # Replace with the path to your blue tick image
#         self.blue_tick_label = ttk.Label(self, image=self.blue_tick_image, background="#1a3356")
#         self.blue_tick_label.pack()

#         # Take Test Button with customized background color
#         self.take_test_button = ttk.Button(self, text="Take Test", command=self.take_test, style="DarkBlue.TButton")
#         self.take_test_button.pack(side=tk.BOTTOM, pady=30)

#         # Style definition for the button
#         self.style = ttk.Style()
#         self.style.configure("DarkBlue.TButton", background="#003366", foreground="#ffffff", font=("Helvetica", 12))

#     def take_test(self):
#         print("Redirecting to the test page...")  # Placeholder for redirection functionality

# if __name__ == "__main__":
#     app = CongratulationsPage()
#     app.mainloop()


# --------------------------------------------------------------------------->
# import tkinter as tk
# from tkinter import ttk


# class CongratulationsPage(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Congratulations")

#         # Set background color
#         self.configure(bg="#1a3356")  # Dark blue background color

#         # Message Label with customized text color and background color
#         self.message_label = ttk.Label(self, text="Congrats! You completed the assessment.", font=("Helvetica", 20), foreground="#ffffff", background="#1a3356")
#         self.message_label.pack(pady=50)

#         # Blue Tick Image
#         self.blue_tick_image = tk.PhotoImage(file="bluetick.png")  # Replace with the path to your blue tick image
#         self.blue_tick_label = ttk.Label(self, image=self.blue_tick_image, background="#1a3356")
#         self.blue_tick_label.pack()

#         # Take Test Button with customized background and text color
#         self.take_test_button = ttk.Button(self, text="Take Test", command=self.take_test, style="DarkBlue.TButton")
#         self.take_test_button.pack(side=tk.BOTTOM, pady=30)

#         # Style definition for the button
#         self.style = ttk.Style()
#         self.style.configure("DarkBlue.TButton", background="#003366", foreground="#1a3356", font=("Arial", 12))

#     def take_test(self):
#         print("Redirecting to the test page...")  # Placeholder for redirection functionality

# if __name__ == "__main__":
#     app = CongratulationsPage()
#     app.mainloop()


import tkinter as tk
from tkinter import ttk


class CongratulationsPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Congratulations")

        # Set background color
        self.configure(bg="#1a3356")  # Dark blue background color

        # Message Label with customized text color and background color
        self.message_label = ttk.Label(self, text="Congrats! You completed the assessment.", font=("Helvetica", 20), foreground="#ffffff", background="#1a3356")
        self.message_label.pack(pady=50)

        # Green Tick Image
        self.blue_tick_image = tk.PhotoImage(file="greentick.png")  # Replace with the path to your blue tick image
        self.resized_image = self.blue_tick_image.subsample(4,4)
        self.blue_tick_label = ttk.Label(self, image=self.resized_image, background="#1a3356")
        self.blue_tick_label.pack()

        resized_image = self.blue_tick_image.zoom(2, 3)

        # Deny Button with customized background and text color
        self.take_test_button = ttk.Button(self, text="No! Thanks", command=self.take_test, style="DarkBlue.TButton")
        self.take_test_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Take Test Button
        self.additional_button = ttk.Button(self, text="Take Test", command=self.additional_action, style="DarkBlue.TButton")
        self.additional_button.pack(side=tk.LEFT, padx=30, pady=10)

        # Style definition for the buttons
        self.style = ttk.Style()
        self.style.configure("DarkBlue.TButton", background="#003366", foreground="#1a3356", font=("Arial", 12))

        self.take_test_button.pack(side=tk.BOTTOM, pady=30, padx=20)
        self.additional_button.pack(side=tk.BOTTOM, pady=30, padx=20)

    def take_test(self):
        print("Redirecting to the test page...")  # Placeholder for redirection functionality

    def additional_action(self):
        print("Additional button clicked.")  # Placeholder for additional button functionality

if __name__ == "__main__":
    app = CongratulationsPage()
    app.mainloop()
