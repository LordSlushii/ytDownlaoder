import tkinter as tk
import customtkinter as ctk
import yt_dlp
import os


def startDownload():
    url = link.get()

    download_folder = '/home/navaneethkrishna/Downloads'
    os.makedirs(download_folder, exist_ok=True)


    opts = {
        'outtmpl' : os.path.join(download_folder, '%(title)s.%(ext)s'),
        'format' : 'best'
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error {e}")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")

title = ctk.CTkLabel(app, text= "Insert a YouTube URL")
title.pack(padx=10, pady=10)

url_var = tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx=10, pady=10)

download_button = ctk.CTkButton(app, text="Download", command=startDownload)
download_button.pack(padx = 10, pady = 10)

app.mainloop()
