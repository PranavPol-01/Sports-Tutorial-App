from tkinter import *
from PIL import Image, ImageTk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button, Entry, Frame
from ttkbootstrap.dialogs import Messagebox
import subprocess

# Toggle password visibility
def toggle_password_visibility():
    global show_password
    show_password = not show_password
    if show_password:
        code.config(show="")
        show_password_icon.config(image=hide_password_icon_image)
    else:
        code.config(show="*")
        show_password_icon.config(image=show_password_icon_image)

# Clear entry text when clicked
def clear_entry(event):
    if event.widget.get() == 'Username' or event.widget.get() == 'Password':
        event.widget.delete(0, 'end')
        event.widget.config(fg='black')

# Open the signup page using subprocess
def sign_up():
    print("Navigating to signup page...")  # Debug message    
    subprocess.run(["python", "signup.py"])
    print("Signup page opened")  # Debug message
    root.destroy()
    

def sign_in():
    username = user.get()
    password = code.get()

    if username == "admin" and password == "pswd":
        Messagebox.show_info("Login Successful", "Welcome, " + username + "!")
        
    else:
        Messagebox.show_error("Login Failed", "Invalid username or password")
    root.destroy()

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.resizable(False, False)

style = Style(theme='superhero')

# Create a frame for the image
image_frame = Frame(root, width=400, height=500, bootstyle="dark")
image_frame.place(x=40, y=0)

# Add an image to the image frame
image_path = "./assets/Data_security_01.jpg"  # Adjust the path to your image
login_image = Image.open(image_path)
login_image = login_image.resize((400, 500))  # Resize the image to fit the frame
login_image = ImageTk.PhotoImage(login_image)

image_label = Label(image_frame, image=login_image)
image_label.place(x=0, y=0)

# Create the login frame
login_frame = Frame(root, width=350, height=350, bootstyle="dark")
login_frame.place(x=480, y=70)

heading = Label(login_frame, text='Sign in', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=120, y=5)

user = Entry(login_frame, width=25, font=('Microsoft yaHei UI Light', 11))
user.place(x=65, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", clear_entry)

code = Entry(login_frame, width=25, font=('Microsoft yaHei UI Light', 11), show='*')
code.place(x=65, y=130)
code.insert(0, 'Password')
code.bind("<FocusIn>", clear_entry)

# Show/hide password icon
# Load the eye icons using PIL
show_password_icon_image = Image.open("./assets/view_709612.png")
hide_password_icon_image = Image.open("./assets/hidden_2355322.png")

# Resize the images if needed
show_password_icon_image = show_password_icon_image.resize((24, 24))
hide_password_icon_image = hide_password_icon_image.resize((24, 24))

# Convert images to Tkinter PhotoImage objects
show_password_icon_image = ImageTk.PhotoImage(show_password_icon_image)
hide_password_icon_image = ImageTk.PhotoImage(hide_password_icon_image)

# Create a label to display the eye icon
show_password_icon = Label(login_frame, image=show_password_icon_image)
show_password_icon.place(x=305, y=135)  # Adjusted position slightly
show_password_icon.bind("<Button-1>", lambda event: toggle_password_visibility())

# Flag to track whether password is visible or not
show_password = False

signin = Button(login_frame, width=20, text='Sign in', command=sign_in, padding='7')
signin.place(x=100, y=184)

label = Label(login_frame, text="Don't have an account ?", font=('Microsoft yaHei UI Light', 9))
label.place(x=60, y=250)

# Use a button to open the signup page
sign_up_button = Button(login_frame, width=7, text='Sign up', command=sign_up)
sign_up_button.place(x=210, y=250)

# Map foreground color for Entry widget
style.map('TEntry', foreground=[
    ('disabled', 'gray'),
    ('focus !disabled', 'white'),
    ('hover !disabled', 'yellow')
])

root.mainloop()
