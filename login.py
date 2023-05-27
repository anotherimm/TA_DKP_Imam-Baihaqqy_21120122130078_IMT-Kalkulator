from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

class LoginWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Login")
        self.window.geometry("470x580+300+200")
        self.window.resizable(False, False)
        self.window.configure(bg="#FFD39B")
        
        # Set the window icon
        icon_image = ImageTk.PhotoImage(file="Images/icon.png")
        self.window.iconphoto(False, icon_image)

        # Username label and entry
        self.username_label = Label(self.window, text="Username:", font=("Arial", 14))
        self.username_label.pack(pady=10)
        self.username_entry = Entry(self.window, font=("Arial", 14))
        self.username_entry.pack()

        # Password label and entry
        self.password_label = Label(self.window, text="Password:", font=("Arial", 14))
        self.password_label.pack(pady=10)
        self.password_entry = Entry(self.window, show="*", font=("Arial", 14))
        self.password_entry.pack()

        # Error label
        self.error_label = Label(self.window, fg="red", font=("Arial", 12))
        self.error_label.pack(pady=10)

        # Login button
        self.login_button = Button(self.window, text="Login", command=self.login, font=("Arial", 14))
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the credentials are correct
        if self.validate_login(username, password):
            self.window.destroy()
            self.launch_main()
        else:
            self.error_label.config(text="Invalid username or password")

    def validate_login(self, username, password):
        with open("user_database.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    return True
        return False

    def launch_main(self):
        subprocess.call(["python", "menu.py"])

    def run(self):
        self.window.mainloop()

# Membuat sebuah instance dari LoginWindow dan menjalankan aplikas
login_window = LoginWindow()
login_window.run()
