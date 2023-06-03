from tkinter import *
import subprocess
# oop1
class MainMenu:
    def __init__(self):
        self.window = Tk()
        self.window.title("Main Menu")
        self.window.geometry("470x200+300+200")
        self.window.configure(bg="#FFD39B")
        
        # Membuat frame untuk menyusun tombol
        button_frame = Frame(self.window, bg="#FFD39B")
        button_frame.pack(expand=True)
        
        # Membuat tombol menu pertama
        self.button1 = Button(button_frame, text="IMT Kalkulator", command=self.menu1_action)
        self.button1.pack(pady=20)
        
        # Membuat tombol menu kedua
        self.button2 = Button(button_frame, text="Apa Itu IMT?", command=self.menu2_action)
        self.button2.pack(pady=20)
        
        # Mengatur posisi frame agar berada di tengah layar
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
    
    def menu1_action(self):
        # Tambahkan aksi yang ingin dilakukan saat tombol menu 1 ditekan
        # print("Menu 1 selected")
        subprocess.call(["python", "kalkulator.py"])
        self.window.destroy()
    
    def menu2_action(self):
        # Tambahkan aksi yang ingin dilakukan saat tombol menu 2 ditekan
        # print("Menu 2 selected")
        subprocess.call(["python", "informasi.py"])
        self.window.destroy()
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
