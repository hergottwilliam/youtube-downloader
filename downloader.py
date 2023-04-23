from pytube import YouTube

link = input("Youtube link: ")
yt = YouTube(link)

video = yt.streams.get_highest_resolution()

video.download("/home/hergo/Downloads")