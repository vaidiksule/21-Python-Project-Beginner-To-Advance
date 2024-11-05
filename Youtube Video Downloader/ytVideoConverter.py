import yt_dlp as youtube_dl
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s'
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video Downloaded Successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter YouTube URL: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Invalid Save Location!")
    else:
        download_video(video_url, save_dir)
