import tkinter as tk
import customtkinter as ctk
import yt_dlp
import os
from PIL import Image

def downloadMP4():
    url = link.get()

    download_folder = '/Users/navaneethkrishna/Downloads'
    os.makedirs(download_folder, exist_ok=True)

    opts = {
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'format': 'best'
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        print("DONE")
    except Exception as e:
        print(f"Error {e}")

def downloadWEBM():
    url = link.get()

    download_folder = '/Users/navaneethkrishna/Downloads'
    os.makedirs(download_folder, exist_ok=True)

    opts = {
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'format': 'bv*+ba/b',
    }

    try:
        with yt_dlp.YoutubeDL(opts) as yimport tkinter as tk
import customtkinter as ctk
import yt_dlp
import os
from PIL import Image

def downloadMP4():
    url = link.get()

    download_folder = '/Users/navaneethkrishna/Downloads'
    os.makedirs(download_folder, exist_ok=True)

    opts = {
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'format': 'best'
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        print("DONE")
    except Exception as e:
        print(f"Error {e}")

def downloadWEBM():
    url = link.get()

    download_folder = '/Users/navaneethkrishna/Downloads'
    os.makedirs(download_folder, exist_ok=True)

    opts = {
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'format': 'bv*+ba/b',
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        print("DONE")
    except Exception as e:
        print(f"Error {e}")

def downloadMP3():
    url = link.get()

    download_folder = '/Users/navaneethkrishna/Downloads'
    os.makedirs(download_folder, exist_ok=True)

    opts = {
        'outtmpl': f'{download_folder}/%(title)s.mp3',
        'format': 'bestaudio/b',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Convert to audio
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '320',  # 320kbps for best quality
        }]

    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        print("DONE")
    except Exception as e:
        print(f"Error {e}")

def download_video(url, opts):
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        print("Download Complete")
    except Exception as e:
        print(f"Error: {e}")

def downloadThumbnail():
    url = link.get()
    download_folder = '/Users/navaneethkrishna/Downloads'
    opts = {
        'outtmpl': f'{download_folder}/thumbnail',  # Save with video title
        'skip_download': True,  # Don't download video/audio
        'writethumbnail': True  # Download thumbnail only
    }
    download_video(url, opts)

    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get('title', 'Unknown Title')


    image_path = f'{download_folder}/thumbnail.webp'
    image = Image.open(image_path)
    img = ctk.CTkImage(light_image=image, size=(355, 200))
    img_label = ctk.CTkLabel(app, image=img, text="")
    img_label.grid(row = 3, column=0, columnspan=3, padx = 10, pady = 20)
    title_label = ctk.CTkLabel(app, text=title, font=("Arial", 16, "bold"))
    title_label.grid(row = 4, column=0, columnspan=3, padx = 10)


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")

# Confirm Button (Uniform Size)
button_width = 220  # Adjust as needed
button_height = 40

url_var = tk.StringVar()

title = ctk.CTkLabel(app, text="Insert a YouTube URL", font=("Arial", 22, "bold"))
title.grid(row=0, column=0, columnspan=3, pady=(10, 5))

link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

extract = ctk.CTkButton(app, text="Confirm", command=downloadThumbnail, width=button_width, height=button_height)
extract.grid(row=1, column=2, padx=10, pady=5)

# Download Buttons (Same Size)
bestMP4 = ctk.CTkButton(app, text="Download Space Efficient [MP4]", command=downloadMP4, width=button_width, height=button_height)
bestMP4.grid(row=2, column=0, padx=10, pady=5)

bestWEBM = ctk.CTkButton(app, text="Download Best Quality [WEBM]", command=downloadWEBM, width=button_width, height=button_height)
bestWEBM.grid(row=2, column=1, padx=10, pady=5)

bestMP3 = ctk.CTkButton(app, text="Download Only Audio [MP3]", command=downloadMP3, width=button_width, height=button_height)
bestMP3.grid(row=2, column=2, padx=10, pady=5)



app.mainloop()dl:
            ydl.download([url])
        print("DONE")
    except Exception as e:
        print(f"Error {e}")

def downloadMP3():
    url = link.get()

    download_folder = '/Users/navaneethkrishna/Downloads'
    os.makedirs(download_folder, exist_ok=True)

    opts = {
        'outtmpl': f'{download_folder}/%(title)s.mp3',
        'format': 'bestaudio/b',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Convert to audio
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '320',  # 320kbps for best quality
        }]

    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        print("DONE")
    except Exception as e:
        print(f"Error {e}")

def download_video(url, opts):
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        print("Download Complete")
    except Exception as e:
        print(f"Error: {e}")

def downloadThumbnail():
    url = link.get()
    download_folder = '/Users/navaneethkrishna/Downloads'
    opts = {
        'outtmpl': f'{download_folder}/thumbnail',  # Save with video title
        'skip_download': True,  # Don't download video/audio
        'writethumbnail': True  # Download thumbnail only
    }
    download_video(url, opts)

    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get('title', 'Unknown Title')


    image_path = f'{download_folder}/thumbnail.webp'
    image = Image.open(image_path)
    img = ctk.CTkImage(light_image=image, size=(355, 200))
    img_label = ctk.CTkLabel(app, image=img, text="")
    img_label.grid(row = 3, column=0, columnspan=3, padx = 10, pady = 20)
    title_label = ctk.CTkLabel(app, text=title, font=("Arial", 16, "bold"))
    title_label.grid(row = 4, column=0, columnspan=3, padx = 10)


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")

# Confirm Button (Uniform Size)
button_width = 220  # Adjust as needed
button_height = 40

url_var = tk.StringVar()

title = ctk.CTkLabel(app, text="Insert a YouTube URL", font=("Arial", 22, "bold"))
title.grid(row=0, column=0, columnspan=3, pady=(10, 5))

link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

extract = ctk.CTkButton(app, text="Confirm", command=downloadThumbnail, width=button_width, height=button_height)
extract.grid(row=1, column=2, padx=10, pady=5)

# Download Buttons (Same Size)
bestMP4 = ctk.CTkButton(app, text="Download Space Efficient [MP4]", command=downloadMP4, width=button_width, height=button_height)
bestMP4.grid(row=2, column=0, padx=10, pady=5)

bestWEBM = ctk.CTkButton(app, text="Download Best Quality [WEBM]", command=downloadWEBM, width=button_width, height=button_height)
bestWEBM.grid(row=2, column=1, padx=10, pady=5)

bestMP3 = ctk.CTkButton(app, text="Download Only Audio [MP3]", command=downloadMP3, width=button_width, height=button_height)
bestMP3.grid(row=2, column=2, padx=10, pady=5)



app.mainloop()
