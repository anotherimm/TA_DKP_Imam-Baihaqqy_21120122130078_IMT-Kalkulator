from tkinter import *
import subprocess
class InfoWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Informasi IMT")
        self.window.configure(bg="#FFD39B")

        self.info_text = """
        Indeks Massa Tubuh (IMT) adalah perhitungan yang didapatkan dengan membagi berat badan (dalam kilogram) 
        dengan ukuran tinggi badan (dalam meter). Nilai IMT merupakan salah satu acuan untuk melihat posisi berat 
        badan Anda.

        IMT dapat dibagi menjadi kategori berikut:
        - Kekurangan Berat Badan: IMT kurang dari 18.5
        - Berat Badan Normal: IMT antara 18.5 dan 24.9
        - Kelebihan Berat Badan: IMT antara 25 dan 29.9
        - Obesitas: IMT 30 atau lebih

        Nilai IMT merupakan salah satu pengukuran yang dilihat oleh dokter untuk menilai risiko Anda mengalami 
        suatu penyakit kronis, seperti jantung dan diabetes.

        Harap dicatat bahwa IMT hanyalah salah satu indikator dan tidak dapat menggantikan evaluasi medis yang 
        lebih komprehensif. Konsultasikan dengan profesional kesehatan Anda untuk informasi lebih lanjut.
        """

        self.info_textbox = Text(self.window, font=("Arial", 12), wrap="word")
        self.info_textbox.insert(END, self.info_text)
        self.info_textbox.configure(state="disabled")

        self.info_textbox.pack(fill=BOTH, expand=True, padx=20, pady=20)

        self.close_button = Button(self.window, text="Tutup", command=self.close_window, font=("Arial", 12))
        self.close_button.pack(pady=10)

        self.kalkulator_button = Button(self.window, text="Kalkulator", command=self.kalkulator_window, font=("Arial", 12))
        self.kalkulator_button.pack(pady=10)

        self.window.update_idletasks()
        width = self.info_textbox.winfo_reqwidth() + 40
        height = self.info_textbox.winfo_reqheight() + 100
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def close_window(self):
        self.window.destroy()
    
    def kalkulator_window(self):
        self.window.destroy()
        subprocess.call(["python", "kalkulator.py"])
        self.window.destroy()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    info_window = InfoWindow()
    info_window.run()
