import subprocess
import tkinter as tk
from tkinter import messagebox
import pygame
import threading

def open_terminal(command):
    try:
        terminal_emulator = 'konsole'
        full_command = [terminal_emulator, '-e', 'bash', '-c', command]
        subprocess.run(full_command)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def on_activate():
    command_to_run = "ollama run llama3"
    stop_background_music()
    open_terminal(command_to_run)

def on_abort():
    stop_background_music()
    root.destroy()

def play_background_music(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.set_volume(0.5)  # Set initial volume
    pygame.mixer.music.play(loops=-1)  # Play the music in a loop

def stop_background_music():
    pygame.mixer.music.stop()

def toggle_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        play_pause_button.config(text="Play")
    else:
        pygame.mixer.music.unpause()
        play_pause_button.config(text="Pause")

def change_volume(value):
    volume = float(value) / 100  # Scale from 0 to 1
    pygame.mixer.music.set_volume(volume)

def update_gif_frame():
    global current_frame_index
    # Get the next frame
    current_frame = gif_frames[current_frame_index]
    gif_label.config(image=current_frame)
    current_frame_index += 1
    if current_frame_index >= len(gif_frames):
        current_frame_index = 0
    # Schedule the next update
    root.after(100, update_gif_frame)

root = tk.Tk()
root.title("AI Activation")
root.geometry("800x500")  # Default size
root.minsize(800, 500)  # Minimum size
root.configure(bg='black')  # Set background color

# Frame for Pocket-AI ASCII art in the center
ascii_frame = tk.Frame(root, bg='black')
ascii_frame.grid(row=0, column=1, sticky='nsew')

# Insert the ASCII art with gold color
ascii_art = """
        ██████╗  ██████╗  ██████╗██╗  ██╗███████╗████████╗     █████╗ ██╗
        ██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝    ██╔══██╗██║
        ██████╔╝██║   ██║██║     █████╔╝ █████╗     ██║       ███████║██║
        ██╔═══╝ ██║   ██║██║     ██╔═██╗ ██╔══╝     ██║       ██╔══██║██║
        ██║     ╚██████╔╝╚██████╗██║  ██╗███████╗   ██║       ██║  ██║██║
        ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═╝  ╚═╝╚═╝

                        By: Lloyd Enterina Agonia
"""

text_area = tk.Text(ascii_frame, wrap=tk.NONE, bg='black', fg='green')
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
text_area.insert(tk.END, ascii_art, 'gold')
text_area.tag_config('gold', foreground='gold')

# Insert the rest of the text with green color
instructions = """
Welcome, User!

    You can ask this AI anything, It's like chatgpt but offline ;)

    Note:
        -Since it is offline it cannot tell you recent events.
        -It has only general knowledge and sometimes.
        -Its responses are not always true or correct.
        -It is also multilingual but will not be 100% accurate.

                            Select an option:

To activate AI press "activate"           To cancel or exit press "abort"
"""
text_area.insert(tk.END, instructions, 'green')
text_area.tag_config('green', foreground='green')
text_area.config(state=tk.DISABLED)

# Frame for GIF animation on the right
gif_frame = tk.Frame(root, bg='black')
gif_frame.grid(row=0, column=2, sticky='ns')

# Load GIF frames (Replace with your GIF frames)
gif_frames = [
    tk.PhotoImage(file="gif/1.gif").subsample(2),  # Adjust subsample for size reduction
    tk.PhotoImage(file="gif/2.gif").subsample(2),
    tk.PhotoImage(file="gif/3.gif").subsample(2),
    tk.PhotoImage(file="gif/4.gif").subsample(2),
    tk.PhotoImage(file="gif/5.gif").subsample(2),
    tk.PhotoImage(file="gif/6.gif").subsample(2),
    tk.PhotoImage(file="gif/7.gif").subsample(2),
    tk.PhotoImage(file="gif/8.gif").subsample(2),
    tk.PhotoImage(file="gif/9.gif").subsample(2),
    tk.PhotoImage(file="gif/10.gif").subsample(2),
    tk.PhotoImage(file="gif/11.gif").subsample(2),
    tk.PhotoImage(file="gif/12.gif").subsample(2),
    tk.PhotoImage(file="gif/13.gif").subsample(2),
    tk.PhotoImage(file="gif/14.gif").subsample(2),
    tk.PhotoImage(file="gif/15.gif").subsample(2),
    tk.PhotoImage(file="gif/16.gif").subsample(2),
    tk.PhotoImage(file="gif/17.gif").subsample(2),
    tk.PhotoImage(file="gif/18.gif").subsample(2),
    tk.PhotoImage(file="gif/19.gif").subsample(2),
    tk.PhotoImage(file="gif/20.gif").subsample(2),

    # Add more frames as needed
]

# Label for GIF animation
gif_label = tk.Label(gif_frame, bg='black')
gif_label.pack(pady=10)

# Start displaying GIF frames
current_frame_index = 0
update_gif_frame()

# Buttons and controls frame
control_frame = tk.Frame(root, bg='black')
control_frame.grid(row=1, column=1, sticky='ew', padx=10, pady=(0, 10))

# Activate button
activate_button = tk.Button(control_frame, text="Activate", command=on_activate, bg='black', fg='green', width=10, height=2)
activate_button.grid(row=0, column=0, padx=5, pady=5)

# Abort button
abort_button = tk.Button(control_frame, text="Abort", command=on_abort, bg='black', fg='green', width=10, height=2)
abort_button.grid(row=0, column=1, padx=5, pady=5)

# Pause/Play button for music control
play_pause_button = tk.Button(control_frame, text="Pause", command=toggle_music, bg='black', fg='green', width=10, height=2)
play_pause_button.grid(row=0, column=2, padx=5, pady=5)

# Volume slider
volume_slider = tk.Scale(control_frame, from_=0, to=100, orient=tk.HORIZONTAL, bg='black', fg='green', command=change_volume, length=200)
volume_slider.set(50)  # Set initial volume to 50%
volume_slider.grid(row=0, column=3, padx=5, pady=5)

# Start background music
play_background_music('background_music.wav')

root.mainloop()
