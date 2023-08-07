import os
import tkinter as tk
from tkinter import filedialog
import pygame

def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def create_gui():
    root = tk.Tk()
    root.title("Simple Music Player")
    root.geometry("300x200")

    label = tk.Label(root, text="Music Player", font=("Helvetica", 16))
    label.pack(pady=10)

    play_button = tk.Button(root, text="Play", command=play_music)
    play_button.pack(pady=5)

    pause_button = tk.Button(root, text="Pause", command=pause_music)
    pause_button.pack(pady=5)

    resume_button = tk.Button(root, text="Resume", command=resume_music)
    resume_button.pack(pady=5)

    stop_button = tk.Button(root, text="Stop", command=stop_music)
    stop_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    pygame.mixer.init()
    create_gui()
