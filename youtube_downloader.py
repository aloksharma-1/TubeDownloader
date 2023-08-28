import os
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import threading
import unicodedata
from string import ascii_letters, digits

def sanitize_filename(filename):
    # Normalize and replace invalid characters with underscores
    valid_filename_chars = "-_.() %s%s" % (ascii_letters, digits)
    sanitized_filename = ''.join(c for c in filename if c in valid_filename_chars)
    sanitized_filename = sanitized_filename.replace(' ', '_')
    sanitized_filename = unicodedata.normalize('NFKD', sanitized_filename).encode('ASCII', 'ignore').decode()
    return sanitized_filename

def download_video(link, download_path):
    try:
        yt = YouTube(link)
        video_stream = yt.streams.get_highest_resolution()
        
        if not video_stream:
            raise ValueError("Video stream not available.")
        
        video_title = sanitize_filename(yt.title)
        video_stream.download(output_path=download_path, filename=f"{video_title}.mp4")
        
        messagebox.showinfo("Success", "Video downloaded successfully.")
    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", "An error occurred while downloading the video.")

def download_button_clicked(link_var, download_path, download_button):
    video_link = link_var.get()
    
    if not video_link:
        messagebox.showwarning("Warning", "Please enter a valid video link.")
        return
    
    # Disable the "Download Video" button during download
    download_button.config(state=tk.DISABLED)
    
    # Start the download process in a separate thread
    download_thread = threading.Thread(target=download_video, args=(video_link, download_path))
    download_thread.start()
    
    # Periodically check if the thread has finished and re-enable the button
    def check_thread():
        if download_thread.is_alive():
            download_button.after(100, check_thread)
        else:
            download_button.config(state=tk.NORMAL)
    
    check_thread()

def main():
    win = tk.Tk()
    win.geometry("400x400")
    win.title(" TubeDownloader ")
    win.iconbitmap('E:\\project\\icon.ico') 
    win.resizable(False, False)  # Disable window resizing

    # Create a canvas with a gradient background
    canvas = tk.Canvas(win, width=400, height=400)
    canvas.pack()

    # Draw the gradient background for the entire screen
    gradient_color = ("#4287f5", "#ffffff")  # Starting and ending colors
    for i in range(400):
        gradient_color = "#%02x%02x%02x" % (
            int(66 + (255 - 66) * (400 - i) / 400),
            int(135 + (255 - 135) * (400 - i) / 400),
            int(245 + (255 - 245) * (400 - i) / 400)
        )
        canvas.create_line(0, i, 400, i, fill=gradient_color)

    link_var = tk.StringVar()

    download_path = "YOUR_DOWNLOAD_PATH"  # Change this to your desired download location
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    label = tk.Label(canvas, text="YouTube Video Downloader", font=("Helvetica", 18), bg=gradient_color)
    label.place(relx=0.5, rely=0.15, anchor="center")

    entry = tk.Entry(canvas, textvariable=link_var, width=40)
    entry.place(relx=0.5, rely=0.3, anchor="center")

    download_button = tk.Button(canvas, text="Download Video", command=lambda: download_button_clicked(link_var, download_path, download_button), bg=gradient_color)
    download_button.place(relx=0.5, rely=0.4, anchor="center")

    win.mainloop()

if __name__ == "__main__":
    main()
