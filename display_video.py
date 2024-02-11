#<---------- Original code --------->
# import tkinter as tk
# from PIL import Image, ImageTk
# from pytube import YouTube
# import requests
# from io import BytesIO
# import os

# class VideoPlayerApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Video Player")
#         self.video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example video URL (Rick Astley - Never Gonna Give You Up)

#         # Download thumbnail and video
#         self.thumbnail_path = self.download_thumbnail()
#         self.video_path = self.download_video()

#         # Display the thumbnail
#         self.thumbnail_label = tk.Label(self.master)
#         self.thumbnail_label.pack()
#         self.load_thumbnail()

#         # Button to play the video
#         self.play_button = tk.Button(self.master, text="Play Video", command=self.play_video)
#         self.play_button.pack()

#     def download_thumbnail(self):
#         yt = YouTube(self.video_url)
#         thumbnail_url = yt.thumbnail_url
#         response = requests.get(thumbnail_url)
#         thumbnail_image = Image.open(BytesIO(response.content))
#         thumbnail_path = "thumbnail.jpg"
#         thumbnail_image.save(thumbnail_path)
#         return thumbnail_path

#     def load_thumbnail(self):
#         thumbnail_image = Image.open(self.thumbnail_path)
#         thumbnail_photo = ImageTk.PhotoImage(thumbnail_image)
#         self.thumbnail_label.config(image=thumbnail_photo)
#         self.thumbnail_label.image = thumbnail_photo

#     def download_video(self):
#         yt = YouTube(self.video_url)
#         video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
#         video_path = os.path.join(os.getcwd(), video_stream.default_filename)
#         video_stream.download()
#         return video_path

#     def play_video(self):
#         os.startfile(self.video_path)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = VideoPlayerApp(root)
#     root.mainloop()




# #<---------- New Code --------->
import tkinter as tk
from PIL import Image, ImageTk
from pytube import YouTube
import requests
from io import BytesIO
import os

class VideoPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Player")
        self.video_url = "https://youtu.be/gK8hi6cwIKs?si=uQ4R1ClJgCGmZzSr"  # Example video URL (Nishant chahar LEET CODE video)

        # Download thumbnail and video
        self.thumbnail_path = self.download_thumbnail()
        self.video_path = self.download_video()

        # Display the thumbnail
        self.thumbnail_label = tk.Label(self.master, height = 500, width = 600)
        self.thumbnail_label.pack()
        self.load_thumbnail()

        # Button to play the video
        self.play_button = tk.Button(self.master, text="Play Video", command=self.play_video, bg="blue", fg="white", font=("Arial", 14))
        self.play_button.pack(pady=10)

    def download_thumbnail(self):
        yt = YouTube(self.video_url)
        thumbnail_url = yt.thumbnail_url
        response = requests.get(thumbnail_url)
        thumbnail_image = Image.open(BytesIO(response.content))
        thumbnail_path = "thumbnail.jpg"
        thumbnail_image.save(thumbnail_path)
        return thumbnail_path

    def load_thumbnail(self):
        thumbnail_image = Image.open(self.thumbnail_path)
        thumbnail_photo = ImageTk.PhotoImage(thumbnail_image)
        self.thumbnail_label.config(image=thumbnail_photo)
        self.thumbnail_label.image = thumbnail_photo

    def download_video(self):
        yt = YouTube(self.video_url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video_path = os.path.join(os.getcwd(), video_stream.default_filename)
        video_stream.download()
        return video_path

    def play_video(self):
        os.startfile(self.video_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()




# # # NEW ONES------------------------------->>>>>>>>>>>>>>>>>>>>>>>
# import tkinter as tk
# from tkinter import ttk
# import webbrowser

# class VideoPlayerApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Video Player")

#         self.notebook = ttk.Notebook(self.master)
#         self.notebook.pack(fill=tk.BOTH, expand=True)

#         self.tab = tk.Frame(self.notebook)
#         self.notebook.add(self.tab, text="Video")

#         self.video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
#         self.webview = tk.Label(self.tab)
#         self.webview.pack(fill=tk.BOTH, expand=True)
#         self.load_video()

#         self.play_button = tk.Button(self.tab, text="Play Video", command=self.play_video)
#         self.play_button.pack(pady=10)

#     def load_video(self):
#         html = f"""<!DOCTYPE html>
#         <html>
#         <body>
#         <video width="800" height="600" controls autoplay>
#           <source src="{self.video_url}" type="video/mp4">
#           Your browser does not support the video tag.
#         </video>
#         </body>
#         </html>
#         """
#         self.webview.configure(text=html)

#     def play_video(self):
#         webbrowser.open(self.video_url)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = VideoPlayerApp(root)
#     root.mainloop()


# ------------------------>>>>>>RECENT ONES THAT WAS NOT WORKING PROPERLY<<<<<<<-------------------------

# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import webbrowser
# import requests
# from io import BytesIO

# class VideoPlayerApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Video Player")

#         self.main_frame = tk.Frame(self.master)
#         self.main_frame.pack(fill=tk.BOTH, expand=True)

#         self.video_frame = tk.Frame(self.main_frame)
#         self.video_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         self.thumbnail_frame = tk.Frame(self.main_frame)
#         self.thumbnail_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         self.video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example video URL (Rick Astley - Never Gonna Give You Up)

#         self.thumbnail_image = self.download_thumbnail()
#         self.thumbnail_label = tk.Label(self.thumbnail_frame, image=self.thumbnail_image)
#         self.thumbnail_label.pack(fill=tk.BOTH, expand=True)

#         self.load_video()

#         self.play_button = tk.Button(self.video_frame, text="Play Video", command=self.play_video)
#         self.play_button.pack(pady=10)

#     def download_thumbnail(self):
#         response = requests.get(f"https://img.youtube.com/vi/{self.get_video_id()}/maxresdefault.jpg")
#         thumbnail_data = response.content
#         thumbnail_image = Image.open(BytesIO(thumbnail_data))
#         thumbnail_image = thumbnail_image.resize((320, 180))  # Resize thumbnail to fit
#         thumbnail_photo = ImageTk.PhotoImage(thumbnail_image)
#         return thumbnail_photo

#     def load_video(self):
#         html = f"""<!DOCTYPE html>
#         <html>
#         <body>
#         <video width="800" height="600" controls autoplay>
#           <source src="{self.video_url}" type="video/mp4">
#           Your browser does not support the video tag.
#         </video>
#         </body>
#         </html>
#         """
#         webview = tk.Label(self.video_frame)
#         webview.pack(fill=tk.BOTH, expand=True)
#         webview.configure(text=html)

#     def play_video(self):
#         webbrowser.open(self.video_url)

#     def get_video_id(self):
#         return self.video_url.split("=")[-1]

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = VideoPlayerApp(root)
#     root.mainloop()
