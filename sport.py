import sqlite3
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
import cv2
from PIL import Image, ImageTk
import CongratsPage

# create a styled tk window
style = Style('lumen')
window = style.master
window.title("Sports")
window.geometry("1000x700")

progressbar = ttk.Progressbar(window, style='success.Horizontal.TProgressbar', orient='horizontal', mode='determinate')
progressbar.pack(fill='x')

# create a notebook (multiple pages)
notebook = ttk.Notebook(window)

# connect to the database
conn = sqlite3.connect('rules.db')
cursor = conn.cursor()

# fetch all sports
cursor.execute("SELECT * FROM Badminton")
sports = cursor.fetchall()

# Function to dynamically adjust font size based on window size
def adjust_font_size(event):
    new_font_size = max(8, int(window.winfo_width() / 80))

    # Iterate through all frames in the notebook
    for frame in notebook.winfo_children():
        # Iterate through all labels in the frame
        for label in frame.winfo_children():
            # Update the font size of the label
            label.configure(font=('Arial', new_font_size))
            label.update()

# Bind the <Configure> event of the window to the adjust_font_size function
window.bind('<Configure>', adjust_font_size)

def update_text_width(event):
    # Get the width of the notebook or window
    width = event.width

    # Calculate the wraplength based on the width
    wrap_length = int(width * 0.8)  # Adjust the multiplier as needed
    
    # Update the wraplength for all labels
    for label in [sport_name_label, sport_info_label, ...]:  # Add all your labels here
        label.config(wraplength=wrap_length)

# Bind the <Configure> event of the window or notebook to the update_text_width function
window.bind('<Configure>', update_text_width)


# iterate over sports data and create a page for each column in db

for i, sport in enumerate(sports, start=1):
    # create a frame for each page
    frame_1 = ttk.Frame(notebook)
    notebook.add(frame_1, text=f'Introduction')

    # add sport name label
    sport_name_label = ttk.Label(frame_1, text=f'{sport[0]}', style='primary.TLabel', font=('Arial', 20), padding=5,wraplength=590)
    sport_name_label.pack(pady=20)

    # add sport information label
    sport_info_label = ttk.Label(frame_1, text=f'{sport[1]}', font=('Arial', 14), padding=5, wraplength=790)
    sport_info_label.pack()
    
    frame_2 = ttk.Frame(notebook)
    notebook.add(frame_2, text=f'Rules')
    image = Image.open(".\\assets\\shots.png")
    # Calculate the aspect ratio
    aspect_ratio = image.width / image.height
    new_width = min(590, int(590 * aspect_ratio))
    new_height = min(590, int(590 / aspect_ratio))

    # Resize the image if new_width and new_height are greater than 0
    if new_width > 0 and new_height > 0:
        image = image.resize((new_width, new_height), Image.LANCZOS)

    # Convert the PIL Image to a tk.PhotoImage
    shot = ImageTk.PhotoImage(image)

    # add sport information label
    sport_info_label = ttk.Label(frame_2, text=f'{sport[2]}',font=('Arial', 14), padding=5,wraplength=590, image=shot, compound='right')
    sport_info_label.pack()

    frame_3 = ttk.Frame(notebook)
    notebook.add(frame_3, text=f'Change of Ends')

    # add sport information label
    sport_info_label = ttk.Label(frame_3, text=f'{sport[3]}',font=('Arial', 14), padding=5,wraplength=790)
    sport_info_label.pack()

    

   

    # frame_4 = ttk.Frame(notebook)
    # notebook.add(frame_4, text=f'Serving')

    # # create a label to display the video frames
    # video_label = tk.Label(frame_4)
    # video_label.pack()

    # # open the video file with OpenCV
    # video = cv2.VideoCapture('.\\assets\dimensions.png')

    # def play_video():
    #     # read a frame from the video
    #     ret, frame = video.read()

    #     if ret:
    #         # convert the frame to RGB (OpenCV uses BGR by default)
    #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #         # convert the frame to a PhotoImage
    #         video = ImageTk.PhotoImage(image=Image.fromarray(frame))

    #         # update the label with the new PhotoImage
    #         video_label.config(image=video)
    #         video_label.image = video

    #         # call this function again after 33 ms (for approximately 30 frames per second)
    #         window.after(33, play_video)

    # # start playing the video
    # play_video()
    
    # # add sport information label
    # sport_info_label = ttk.Label(frame_4, text=f'{sport[4]}',font=('Arial', 14), padding=5,wraplength=590, image= video , compound='right')
    # sport_info_label.pack()


    frame_4 = ttk.Frame(notebook)
    notebook.add(frame_4, text=f'Serving')

    # create a label to display the video frames
    video_label = tk.Label(frame_4)
    video_label.grid(row=0, column=1,sticky='nsew')
    #video_label.pack()

    # open the video file with OpenCV
    video = cv2.VideoCapture('.\\assets\\badminton-drive-serve-like-a-boss-badmintonserve.mp4')
    
    # def play_video():
    #     # read a frame from the video
    #     ret, frame = video.read()

    #     if ret:
    #         frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))

    #         # convert the frame to RGB (OpenCV uses BGR by default)
    #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #         # convert the frame to a PhotoImage
    #         video_image = ImageTk.PhotoImage(image=Image.fromarray(frame))

    #         # update the label with the new PhotoImage
    #         video_label.config(image=video_image)
    #         video_label.image = video_image

    #         # call this function again after 33 ms (for approximately 30 frames per second)
    #         window.after(33, play_video)


    def play_video():
        # read a frame from the video
        ret, frame = video.read()

        # if the video has ended, reset it to the first frame
        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = video.read()

        #frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))
        #frame = cv2.resize(frame, (video_label.winfo_width(), video_label.winfo_height()))
        # calculate the aspect ratio of the video
        aspect_ratio = frame.shape[1] / frame.shape[0]

    # calculate the new width and height based on the aspect ratio
        new_width = min(video_label.winfo_width(), int(video_label.winfo_height() * aspect_ratio))
        new_height = min(video_label.winfo_height(), int(video_label.winfo_width() / aspect_ratio))

        if new_width > 0 and new_height > 0:
            frame = cv2.resize(frame, (new_width, new_height))

    # resize the frame to the new size
        #frame = cv2.resize(frame, (new_width, new_height))
        # convert the frame to RGB (OpenCV uses BGR by default)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # convert the frame to a PhotoImage
        video_image = ImageTk.PhotoImage(image=Image.fromarray(frame))

        # update the label with the new PhotoImage
        video_label.config(image=video_image)
        video_label.image = video_image

        # call this function again after 33 ms (for approximately 30 frames per second)
        window.after(33, play_video)

    # start playing the video
    play_video()

    # add sport information label
    sport_info_label = ttk.Label(frame_4, text=f'{sport[4]}',font=('Arial', 14), padding=5,wraplength=590, compound='right')
    sport_info_label.grid(row=0, column=0, sticky='nsew')
    #sport_info_label.pack()
    frame_4.grid_columnconfigure(0, weight=1)
    frame_4.grid_columnconfigure(1, weight=1)
    frame_4.grid_rowconfigure(0, weight=1)

    # frame_5 = ttk.Frame(notebook)
    # notebook.add(frame_5, text=f'Court Dimensions')
    
    # # add sport information label
    # dimensions = tk.PhotoImage(file=".\\assets\dimensions.png")
    # aspect_ratio = dimensions.width() / dimensions.height()
    # new_width = min(590, int(590 * aspect_ratio))
    # new_height = min(590, int(590 / aspect_ratio))

    # if new_width > 0 and new_height > 0:
    #     image = Image.resize((new_width, new_height))

    # dimensions = ImageTk.PhotoImage(image)    
    # sport_info_label = ttk.Label(frame_5, text=f'{sport[5]}',font=('Arial', 14), padding=5,wraplength=590, image=dimensions, compound='right')
    # sport_info_label.pack()

    frame_5 = ttk.Frame(notebook)
    notebook.add(frame_5, text=f'Court Dimensions')

    # Load the image with PIL
    image = Image.open(".\\assets\\dimensions.png")

    # Calculate the aspect ratio
    aspect_ratio = image.width / image.height
    new_width = min(590, int(590 * aspect_ratio))
    new_height = min(590, int(590 / aspect_ratio))

    # Resize the image if new_width and new_height are greater than 0
    if new_width > 0 and new_height > 0:
        image = image.resize((new_width, new_height), Image.LANCZOS)

    # Convert the PIL Image to a tk.PhotoImage
    dimensions = ImageTk.PhotoImage(image)

    sport_info_label = ttk.Label(frame_5, text=f'{sport[5]}',font=('Arial', 14), padding=5,wraplength=590, image=dimensions, compound='right')
    sport_info_label.pack()  

def update_progress(event):
    # Calculate the new progress value based on the current tab index
    current_tab = notebook.index(notebook.select())
    total_tabs = len(notebook.tabs())
    new_value = (current_tab + 1) / total_tabs * 100

    # Update the progress bar
    progressbar['value'] = new_value

notebook.bind('<<NotebookTabChanged>>', update_progress)

# create function to go to the previous page
def go_to_previous_page():
    # get the index of the current page
    current_index = notebook.index(notebook.select())

    # calculate the index of the previous page
    previous_index = (current_index - 1) % len(notebook.tabs())

    # select the previous page
    notebook.select(previous_index)

    update_buttons_visibility()

# create a function to go to the next page
def go_to_next_page():
    # get the index of the current page
    current_index = notebook.index(notebook.select())

    # calculate the index of the next page
    next_index = (current_index + 1) % len(notebook.tabs())

    # select the next page
    notebook.select(next_index)

    update_buttons_visibility()

def update_buttons_visibility():
    # get the index of the current page
    current_index = notebook.index(notebook.select())

    # hide the "Previous" button if the first page is selected, show it otherwise
    if current_index == 0:
        previous_button.pack_forget()
    else:
        previous_button.pack(side='left', padx=5, pady=5)

    # hide the "Next" button if the last page is selected, show it otherwise
    if current_index == len(notebook.tabs()) - 1:
        next_button.pack_forget()
        done_button.pack(side='left', padx=5, pady=5)
    else:
        done_button.pack_forget()
        next_button.pack(side='right', padx=5, pady=5)


current_index = notebook.index(notebook.select())
# create a frame for the buttons
buttons_frame = ttk.Frame(window)
buttons_frame.pack(side='bottom', padx=5, pady=5)

# create a "Previous" button
previous_button = ttk.Button(buttons_frame, text="Previous", bootstyle="Primary, OUTLINE", command=go_to_previous_page)
previous_button.pack(side='left', padx=5, pady=5)
if current_index == 0:
        previous_button.pack_forget()
else:
    previous_button.pack(side='left', padx=5, pady=5)



def open_congrats_page():
    app = CongratsPage.CongratulationsPage()

def on_done_button_clicked():
    window.destroy()
    open_congrats_page()
        
    
next_button = ttk.Button(buttons_frame, text="Next", bootstyle="SUCCESS, OUTLINE", command=go_to_next_page)
done_button = ttk.Button(buttons_frame, text="Done", bootstyle="SUCCESS, OUTLINE", command=on_done_button_clicked)
if current_index == len(notebook.tabs()) - 1:
        next_button.pack_forget()
        done_button.pack(side='left', padx=5, pady=5)
else:
    done_button.pack_forget()
    next_button.pack(side='left', padx=5, pady=5)

# pack the notebook (this will display it)
notebook.pack(expand=True, fill='both')

# start the main event loop
window.mainloop()
