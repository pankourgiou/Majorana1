import tkinter as tk
import psutil
from PIL import Image, ImageTk

# Load image
image_path = "Your_path/majorana1.png"
img = Image.open(image_path)

# Create main window
root = tk.Tk()
root.title("CPU Usage Monitor")
root.geometry(f"{img.width}x{img.height}")

# Convert image for Tkinter
img = ImageTk.PhotoImage(img)
background_label = tk.Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

# CPU usage label in the center
cpu_label = tk.Label(root, text="CPU Usage: 0%", font=("Arial", 20), fg="white", bg="black")
cpu_label.place(relx=0.5, rely=0.5, anchor="center")

# Function to update CPU usage
def update_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    root.after(1000, update_cpu)

# Start updating
update_cpu()

root.mainloop()
