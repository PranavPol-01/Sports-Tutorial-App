
from tkinter import *
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button, Entry, Label, Frame
from PIL import Image, ImageTk
import subprocess

# Toggle password visibility
def toggle_password_visibility(event=None):
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
    if event.widget.get() == 'Email' or event.widget.get() == 'Username' or event.widget.get() == 'Password':
        event.widget.delete(0, 'end')
        event.widget.config(fg='black')

# Open the login page using subprocess
def navigate_to_login():
    print("Navigating to login page...")
    subprocess.run(["python", "login.py"]) 
    print("Login page opened")  
    root.destroy()


def sign_up():
    Messagebox.show_info("Sign Up", "Sign Up Successful!")
    root.destroy()

root = Tk()
root.title('Sign Up')
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

# Create the sign-up frame
signup_frame = Frame(root, width=350, height=350, bootstyle="dark")
signup_frame.place(x=480, y=70)

heading = Label(signup_frame, text='Sign Up', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=120, y=5)

# Email Entry
emailid = Entry(signup_frame, width=25, font=('Microsoft yaHei UI Light', 11))
emailid.place(x=65, y=80)
emailid.insert(0, 'Email')
emailid.bind("<FocusIn>", clear_entry)

# Username Entry
user = Entry(signup_frame, width=25, font=('Microsoft yaHei UI Light', 11))
user.place(x=65, y=130)
user.insert(0, 'Username')
user.bind("<FocusIn>", clear_entry)

# Password Entry
code = Entry(signup_frame, width=25, font=('Microsoft yaHei UI Light', 11), show='*')
code.place(x=65, y=180)
code.insert(0, 'Password')
code.bind("<FocusIn>", clear_entry)


show_password_icon_image = Image.open("./assets/view_709612.png")
hide_password_icon_image = Image.open("./assets/hidden_2355322.png")

show_password_icon_image = show_password_icon_image.resize((24, 24))
hide_password_icon_image = hide_password_icon_image.resize((24, 24))


show_password_icon_image = ImageTk.PhotoImage(show_password_icon_image)
hide_password_icon_image = ImageTk.PhotoImage(hide_password_icon_image)

show_password_icon = Label(signup_frame, image=show_password_icon_image)
show_password_icon.place(x=305, y=185)
show_password_icon.bind("<Button-1>", toggle_password_visibility)

show_password = False

signup_button = Button(signup_frame, width=20, text='Sign up', command=sign_up, padding='7')
signup_button.place(x=100, y=234)

label = Label(signup_frame, text="Already have an account ?", font=('Microsoft yaHei UI Light', 9))
label.place(x=60, y=300)

# Use a button to navigate to the login page
login_button = Button(signup_frame, width=7, text='Login',  command=navigate_to_login)
login_button.place(x=210, y=300)

style.map('TEntry', foreground=[
    ('disabled', 'gray'),
    ('focus !disabled', 'white'),
    ('hover !disabled', 'yellow')
])

root.mainloop()
