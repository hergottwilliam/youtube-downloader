import tkinter as tk
from pytube import YouTube

# add the ability to copy and paste into bar
# make pretty gui

window = tk.Tk()

label = tk.Label(text="YouTube Downloader")
link_label = tk.Label(text="Provide link to YouTube Video")
user_link = tk.Entry()
path_label = tk.Label(text="Provide path for video download")
user_path = tk.Entry()
download_button = tk.Button(text="Download video")

label.pack()
link_label.pack()
user_link.pack()
path_label.pack()
user_path.pack()
download_button.pack()

def download_video(event):
    print(user_link.get())
    print(user_path.get())
    yt = YouTube(user_link.get())
    video = yt.streams.get_highest_resolution()
    video.download(user_path.get())

download_button.bind("<Button-1>", download_video)

window.mainloop()