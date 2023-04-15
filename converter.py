import tkinter as tk
import pytube
from tkinter import ttk
from PIL import Image, ImageTk
from urllib.request import urlopen

#functuonality for the buttons
def convert():
    url = url_entry.get()
    yt = pytube.YouTube(url)
    thumbnail_url = yt.thumbnail_url
    u = urlopen(thumbnail_url)
    raw_data = u.read()
    u.close()

    video_name = yt.title
    video_label = ttk.Label(frame, text=video_name)
    video_label.pack(pady=10)

    thumbnail = ImageTk.PhotoImage(data=raw_data ,size=(300, 300))
    thumbnail_label = ttk.Label(frame, image=thumbnail)
    thumbnail_label.image = thumbnail
    thumbnail_label.pack(pady=10)

def switch_modes():
    if check_button.instate(["selected"]):
        return True
    else:
        return False

def download_url():
    url = url_entry.get()
    yt = pytube.YouTube(url)

    if switch_modes() == True:
        yt.streams.get_highest_resolution().download()
    else:
        yt.streams.filter(only_audio=True).first().download()


root = tk.Tk()
style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")


root.geometry("800x600")
root.title("Youtube Downloader")

#widgets
frame = ttk.Frame(root)
frame.pack()

widgets_frame = tk.Frame(frame)
widgets_frame.pack()

url_label = ttk.Label(widgets_frame, text="URL:")
url_label.grid(row=0, column=0, padx=10)

url_entry = ttk.Entry(widgets_frame)
url_entry.grid(row=0, column=1, pady=10)

url_button = ttk.Button(widgets_frame, text='Convert', command=convert)
url_button.grid(row=1, column=0, pady=10)

download_button = ttk.Button(widgets_frame, text='Download', command=download_url)
download_button.grid(row=1, column=1, pady=10, columnspan=2)

mp4_label = ttk.Label(widgets_frame, text='MP4')
mp4_label.grid(row=2, column=2,)

mp3_label = ttk.Label(widgets_frame, text="MP3")
mp3_label.grid(row=2, column=0,)

check_button = ttk.Checkbutton(widgets_frame,style='Switch', command=switch_modes)
check_button.grid(row=2, column=1,)


root.mainloop()