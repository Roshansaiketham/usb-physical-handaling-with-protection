import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import webbrowser
import os

# Global variable for the correct password
password = "password"

# Function to enable USB ports
def enable_usb_ports():
    # Create a password prompt dialog box
    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("300x200")

    def ok_button():
        if password_entry.get() == password:
            subprocess.run([r'C:\Users\rosha\OneDrive\Documents\pendrive\unblock_usb.bat'], text=True)
            password_window.destroy()
            success_label.config(text="USB Ports Enabled Successfully")
        else:
            error_label.config(text="Incorrect password. Please try again.")
            password_entry.delete(0, tk.END)

    password_label = tk.Label(password_window, text="Enter Password: ")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()
    ok_button = tk.Button(password_window, text="OK", command=ok_button)
    ok_button.pack()
    error_label = tk.Label(password_window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()

# Function to disable USB ports
def disable_usb_ports():
    # Create a password prompt dialog box
    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("300x200")

    def ok_button():
        if password_entry.get() == password:
            subprocess.run([r'C:\Users\rosha\OneDrive\Documents\pendrive\block_usb.bat'], text=True)
            password_window.destroy()
            success_label.config(text="USB Ports Disabled Successfully")
        else:
            error_label.config(text="Incorrect password. Please try again.")
            password_entry.delete(0, tk.END)

    password_label = tk.Label(password_window, text="Enter Password: ")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()
    ok_button = tk.Button(password_window, text="OK", command=ok_button)
    ok_button.pack()
    error_label = tk.Label(password_window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()

# Function to open the project info page in a web browser
def open_project_info():
    file_path = r"C:\Users\rosha\OneDrive\Documents\pendrive\Project Information.html"
    webbrowser.open(f"file://{file_path}")
# Function to change button background to sky blue when hovered
def on_enter(event):
    event.widget.config(bg="#87CEEB", relief="solid")

# Function to reset button background when leaving
def on_leave(event):
    event.widget.config(bg="white", relief="raised")

# Main function to set up the tkinter window
def main():
    global root
    root = tk.Tk()
    root.title("USB Security")
    root.geometry("400x500")  # Increase the height to accommodate the image and buttons
    root.configure(bg="black")  # Set the background color to black

    # Load and display the background image at the top
    img = Image.open(r"C:\Users\rosha\OneDrive\Documents\pendrive\usb.gif")
    img = img.resize((200, 100), Image.ANTIALIAS)  # Resize the image with Antialias resampling
    img = ImageTk.PhotoImage(img)
    
    

    # Modify the title label with a custom font and color scheme
    title_text = "USB Security"
    title_color = ["#00FF00", "#00FFFF", "#FFA500"]  # Green, Cyan, Orange
    title_font = ("Impact", 36)
    title_label = tk.Label(root, text=title_text, font=title_font, bg="black")
    title_label.pack(side="top", pady=10)
    title_label.config(fg=title_color[0])

    # Function to update the title text color with a shine effect
    def update_title_color():
        current_color = title_color.pop(0)
        title_color.append(current_color)
        title_label.config(fg=current_color)
        root.after(200, update_title_color)

    # Start the title text color update loop
    root.after(200, update_title_color)

    background_label = tk.Label(root, image=img)
    background_label.pack(side="top", pady=10)
    background_label.image = img  # To prevent garbage collection

    # Create a frame for the buttons at the bottom
    button_frame = tk.Frame(root, bg="black")
    button_frame.pack(side="bottom", pady=10)

    enable_button = tk.Button(button_frame, text="Enable USB Ports", command=enable_usb_ports, bg="Light green")
    disable_button = tk.Button(button_frame, text="Disable USB Ports", command=disable_usb_ports, bg="Red")
    project_info_button = tk.Button(button_frame, text="Project Info", command=open_project_info, bg="Blue")

    # Configure the grid layout
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)

    enable_button.grid(row=0, column=0, padx=10)
    disable_button.grid(row=0, column=1, padx=10)
    project_info_button.grid(row=0, column=2, padx=10)

    enable_button.bind("<Enter>", on_enter)
    enable_button.bind("<Leave>", on_leave)
    disable_button.bind("<Enter>", on_enter)
    disable_button.bind("<Leave>", on_leave)
    project_info_button.bind("<Enter>", on_enter)
    project_info_button.bind("<Leave>", on_leave)

    global success_label
    success_label = tk.Label(root, text="", font=("Arial", 12), bg="black", fg="#008000")
    success_label.pack(side="top", pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
