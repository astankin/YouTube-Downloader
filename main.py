import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk


def widgets():
    image = Image.open('yt_logo.png')
    image = image.resize((150, 75))
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.image = photo
    label.grid(row=1, column=1)
    link_label = Label(root, text="YouTube линк :", pady=5, padx=5, font=('Arial', 11, 'bold'))
    link_label.grid(row=2, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=35, textvariable=video_Link, font="Arial 14")
    root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    destination_label = Label(root, text="Запази в :", pady=5, padx=9, font=('Arial', 11, 'bold'))
    destination_label.grid(row=3, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=27, textvariable=download_Path, font=("Arial", 14))
    root.destinationText.grid(row=3, column=1, pady=5, padx=5)

    browse_b = Button(root, text="Търси", command=browse, width=10, bg="#248aa2", fg="white", relief=GROOVE)
    browse_b.grid(row=3, column=2, pady=1, padx=1)

    download_b = Button(root, text="Свали Видео", command=download, width=20, pady=10, padx=15, relief=GROOVE,
                        bg="#248aa2",
                        fg="white",
                        font="Georgia, 13")
    download_b.grid(row=4, column=1, pady=20, padx=20)


def browse():
    download_directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    download_Path.set(download_directory)


def download():
    youtube_link = video_Link.get()
    download_folder = download_Path.get()

    get_video = YouTube(youtube_link)

    video_stream = get_video.streams.first()

    video_stream.download(download_folder)

    messagebox.showinfo("УСПЕШНО",
                        "СВАЛЕН И ЗАПАЗЕН В\n"
                        + download_folder)


root = tk.Tk()
root.eval("tk::PlaceWindow . center")
root.geometry("550x290")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.iconbitmap("yt.ico")
root.config()

video_Link = StringVar()
download_Path = StringVar()

widgets()
root.mainloop()
