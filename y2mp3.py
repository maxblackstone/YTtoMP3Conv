#!/bin/env python

import yt_dlp as youtube_dl
import sys
import tkinter as tk
from tkinter import *
import os
import time

# Change save path to Downloads folder
SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'

# Set yt-dlp options
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s',
}

# Function definitions

def download(url):
    if __name__ == "__main__":
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)

# Function to call download(), time process and add labels
def printValue():
    url = entry.get()
    var = tk.StringVar()
    var.set(f'Youtube URL is: {url}')
    tk.Label(window, textvariable=var, pady=20).pack()
    tic = time.time()
    download(url)
    toc = time.time() - tic
    tk.Label(window, text=f'Download time: {round(toc, 2)} seconds').pack()
    tk.Label(window, text='Enjoy your song!').pack()

# GUI

window = tk.Tk()
window.geometry("700x500")

# Don't allow the screen to be resized
window.resizable(0,0)
window.title("Youtube To MP3 Converter")

# Create URL entry point
tk.Label(window, text="Please insert URL below:").pack()
entry = tk.Entry(window)
entry.pack()


# Create button to call printValue()
tk.Button(
    window,
    text="Convert Video!", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

entry.pack()
window.mainloop()





