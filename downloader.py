import tkinter as tk
from pytube import YouTube

window = tk.Tk()
window.geometry("500x250")
window.title("YouTube Downloader")
window.config()


link_label = tk.Label(text="Provide link to YouTube Video")
user_link = tk.Entry()
path_label = tk.Label(text="Provide path for video download, ex: /home/<username>/Downloads")
user_path = tk.Entry()
download_button = tk.Button(text="Download video")

link_label.pack()
user_link.pack()
path_label.pack()
user_path.pack()
download_button.pack()

def download_video(event):
    yt = YouTube(user_link.get())
    video = yt.streams.get_highest_resolution()
    video.download(user_path.get())

download_button.bind("<Button-1>", download_video)

window.mainloop()