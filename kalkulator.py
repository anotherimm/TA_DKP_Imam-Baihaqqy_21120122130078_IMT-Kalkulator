from tkinter import *
import tkinter as tkinter
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("IMT Kalkulator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        # self.image_icon = PhotoImage(file="Images/icon.png")
        self.top = PhotoImage(file="Images/imt.png")
        self.box = PhotoImage(file="Images/box.png")
        self.scale = PhotoImage(file="Images/scale.png")
        self.manusia_image = PhotoImage(file="Images/man.png")
        
        # self.icon_photo = Label(self.root, image=self.image_icon)
        # self.icon_photo.pack()

        self.top_image = Label(self.root, image=self.top, background="#f0f1f5")
        self.top_image.place(x=-10, y=-10)

        self.bottom_box = Label(self.root, width=72, height=18, bg="burlywood1")
        self.bottom_box.pack(side=BOTTOM)

        Label(self.root, image=self.box).place(x=20, y=100)
        Label(self.root, image=self.box).place(x=240, y=100)

        Label(self.root, image=self.scale, bg="burlywood1").place(x=20, y=310)

        self.height = StringVar()
        self.weight = StringVar()

        self.height_label = Label(self.root, text="Tinggi Badan (cm)", font='arial 12', bg="#fff")
        self.height_label.place(x=60, y=130)
        self.height_entry = Entry(self.root, textvariable=self.height, width=5, font='arial 50', bg="#fff", fg='#00008B', bd=0, justify=CENTER)
        self.height_entry.place(x=35, y=160)

        self.weight_label = Label(self.root, text="Berat Badan (kg)", font='arial 12', bg="#fff")
        self.weight_label.place(x=290, y=130)
        self.weight_entry = Entry(self.root, textvariable=self.weight, width=5, font='arial 50', bg="#fff", fg='#00008B', bd=0, justify=CENTER)
        self.weight_entry.place(x=255, y=160)

        self.manusia = Label(self.root, image=self.manusia_image, bg="burlywood1")
        self.manusia.place(x=70, y=400)

        self.calculate_button = Button(self.root, text="Lihat Hasil", width=15, height=2, font="arial 10 bold", bg="#8B7355", fg="white", command=self.calculate_bmi)
        self.calculate_button.place(x=280, y=340)

        self.reset_button = Button(self.root, text="Reset", width=10, height=2, font="arial 10 bold", bg="#8B7355", fg="white", command=self.reset)
        self.reset_button.place(x=280, y=535)

        self.label1 = Label(self.root, font="arial 50 bold", bg="burlywood1", fg="#fff")
        self.label1.place(x=125, y=305)

        self.label2 = Label(self.root, font="arial 20 bold", bg="burlywood1", fg="#fff")
        self.label2.place(x=125, y=430)

        self.label3 = Label(self.root, font="arial 10 bold", bg="burlywood1")
        self.label3.place(x=125, y=500)

    def calculate_bmi(self):
        height_str = self.height.get()
        weight_str = self.weight.get()

        if height_str.isnumeric() and weight_str.isnumeric():
            h = int(height_str)
            w = int(weight_str)

            m = h / 100
            bmi = round(float(w / m ** 2), 1)
            self.label1.config(text=bmi)

            if bmi <= 18.5:
                self.label2.config(text="Kekurangan Berat Badan")
                self.label3.config(text="Anda memiliki berat badan lebih rendah \ndari tubuh normal")
            elif bmi > 18.5 and bmi <= 25:
                self.label2.config(text="Berat Badan Normal")
                self.label3.config(text="Anda memiliki badan yang sehat")
            elif bmi > 25 and bmi <= 30:
                self.label2.config(text="Kelebihan Berat Badan")
                self.label3.config(text="Anda memiliki berat badan lebih \ndari tubuh normal")
            else:
                self.label2.config(text="Obesitas")
                self.label3.config(text="Anda memiliki resiko kesehatan")
        else:
            self.label1.config(text="")
            self.label2.config(text="")
            self.label3.config(text="Silahkan masukkan angka bukan huruf.")
    def reset(self):
        self.set_height(0)
        self.set_weight(0)
        self.label1.config(text="")
        self.label2.config(text="")
        self.label3.config(text="")

    def get_height(self):
        return self.height.get()

    def get_weight(self):
        return self.weight.get()

    def set_height(self, value):
        self.height.set(value)

    def set_weight(self, value):
        self.weight.set(value)


bmi_calculator = BMI_Calculator(root)
root.mainloop()
