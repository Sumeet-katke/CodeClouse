import pygame
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def play_music():
    global paused
    paused = False
    pygame.mixer.init()
    pygame.mixer.music.unpause()
    status_bar.config(text="Music Resumed")

def pause_music():
    global paused
    paused = True
    pygame.mixer.music.pause()
    status_bar.config(text="Music Paused")

def load_music():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)
        status_bar.config(text=f"Now playing: {file_path}")

def update_progress():
    if 'file_path' not in globals():
        status_bar.config(text="No music loaded")
    else:
        if paused:
            pass
        else:
            current_time = pygame.mixer.music.get_pos() / 1000 if pygame.mixer.get_init() else 0
            converted_current_time = time_format(current_time)
            status_bar.config(text=f"Now playing: {file_path} - Time: {converted_current_time}")
    root.after(1000, update_progress)

def time_format(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

root = tk.Tk()
root.title("Music Player")
root.geometry("400x300")

paused = False

load_button = tk.Button(root, text="Load Music", command=load_music)
load_button.pack(pady=20)

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=10)

status_bar = tk.Label(root, text="Welcome to the Music Player", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)

update_progress()
root.mainloop()
