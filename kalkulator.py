from tkinter import*
import tkinter as tkinter
from tkinter import ttk
from PIL import Image,ImageTk

root = Tk()
root.title("IMT Kalkulator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")

def BMI():
    h=float(Height.get())
    w=float(Weight.get())

    m=h/100
    bmi=round(float(w/m**2),1)
    label1.config(text=bmi)

    if bmi<=18.5:
        label2.config(text="Kekurangan Berat Badan")
        label3.config(text="Anda memiliki berat badan lebih rendah \ndari tubuh normal")
    elif bmi>18.5 and bmi <=25:
        label2.config(text="Berat Badan Normal")
        label3.config(text="Anda memiliki badan yang sehat")
    elif bmi>25 and bmi<=30:
        label2.config(text="Kelebihan Berat Badan")
        label3.config(text="Anda memiliki berat badan lebih \ndari tubuh normal")
    else:
        label2.config(text="Obesitas")
        label3.config(text="Anda memiliki resiko kesehatan")
    pass
def reset():
    height.delete(0, END)
    weight.delete(0, END)
    label1.config(text="")
    label2.config(text="")
    label3.config(text="")
# icon apliksi
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

# title bmi top
top=PhotoImage(file="Images/imt.png")
top_image = Label(root,image=top,background="#f0f1f5")
top_image.place(x=-10,y=-10)

# bottom box
Label(root, width=72, height=18, bg="burlywood1").pack(side=BOTTOM)

#two bottom
box=PhotoImage(file="Images/box.png")
Label(root,image=box).place(x=20,y=100)
Label(root,image=box).place(x=240,y=100)

# scale
scale=PhotoImage(file="Images/scale.png")
Label(root,image=scale,bg="burlywood1").place(x=20,y=310)

#Entry box
Height=IntVar()
Weight=IntVar()
height_label = Label(root, text="Tinggi Badan (cm)", font='arial 12', bg="#fff")
height_label.place(x=60, y=130)
height = Entry(root,textvariable=Height,width=5,font='arial 50',bg="#fff",fg='#00008B',bd=0,justify=CENTER)
height.place(x=35,y=160)

weight_label = Label(root, text="Berat Badan (kg)", font='arial 12', bg="#fff")
weight_label.place(x=290, y=130)
weight = Entry(root,textvariable=Weight,width=5,font='arial 50',bg="#fff",fg='#00008B',bd=0,justify=CENTER)
weight.place(x=255,y=160)

# gambar manusia
manusia_image = PhotoImage(file="Images/man.png")
manusia = Label(root, image=manusia_image, bg="burlywood1")
manusia.image = manusia_image  
manusia.place(x=70, y=400)

# tombol button reset dan lihat hasil
Button(root,text="Lihat Hasil",width=15,height=2,font="arial 10 bold", bg="#8B7355", fg="white", command=BMI).place(x=280,y=340)
Button(root, text="Reset", width=10, height=2, font="arial 10 bold", bg="#8B7355", fg="white", command=reset).place(x=280, y=535)

label1=Label(root,font="arial 50 bold",bg="burlywood1", fg="#fff")
label1.place(x=125,y=305)

label2=Label(root,font="arial 20 bold",bg="burlywood1", fg="#fff")
label2.place(x=125,y=430)

label3=Label(root,font="arial 10 bold",bg="burlywood1", )
label3.place(x=125,y=500)

root.mainloop()


