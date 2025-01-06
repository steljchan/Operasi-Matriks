import tkinter as tk
from tkinter import messagebox
from Add import tambah_matriks
from Sub import kurang_matriks
from Mul import kali_matriks
from Determinant import pilih_matriks_determinan
from Inverse import pilih_matriks_invers

def minta_dimensi_matriks():
    try:
        baris_a = int(input_baris_a.get())
        kolom_a = int(input_kolom_a.get())
        baris_b = int(input_baris_b.get())
        kolom_b = int(input_kolom_b.get())

        if baris_a <= 0 or kolom_a <= 0 or baris_b <= 0 or kolom_b <= 0:
            raise ValueError("Dimensi matriks harus bilangan positif!")
        if baris_a > 4 or kolom_a > 4 or baris_b > 4 or kolom_b > 4:
            raise ValueError("Dimensi maksimum untuk setiap matriks adalah 4x4!")

        input_matriks(baris_a, kolom_a, baris_b, kolom_b)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def input_matriks(baris_a, kolom_a, baris_b, kolom_b):
    global masukan_a, masukan_b
    for widget in frame_input.winfo_children():
        widget.destroy()

    # Input Matriks A
    tk.Label(frame_input, text="Matriks A:").grid(row=0, column=0, columnspan=kolom_a, pady=10)
    masukan_a = [[tk.Entry(frame_input, width=5) for _ in range(kolom_a)] for _ in range(baris_a)]
    for i in range(baris_a):
        for j in range(kolom_a):
            masukan_a[i][j].grid(row=i + 1, column=j, padx=2, pady=2)

    # Input Matriks B
    tk.Label(frame_input, text="Matriks B:").grid(row=baris_a + 1, column=0, columnspan=kolom_b, pady=10)
    masukan_b = [[tk.Entry(frame_input, width=5) for _ in range(kolom_b)] for _ in range(baris_b)]
    for i in range(baris_b):
        for j in range(kolom_b):
            masukan_b[i][j].grid(row=baris_a + i + 2, column=j, padx=2, pady=2)

    # Tombol operasi
    frame_tombol = tk.Frame(frame_input)
    frame_tombol.grid(row=0, column=max(kolom_a, kolom_b) + 1, rowspan=baris_a + baris_b + 4, padx=20)

    tk.Button(frame_tombol, text="Tambah", command=lambda: tambah_matriks(masukan_a, masukan_b, label_hasil)).pack(fill="x", pady=5)
    tk.Button(frame_tombol, text="Kurang", command=lambda: kurang_matriks(masukan_a, masukan_b, label_hasil)).pack(fill="x", pady=5)
    tk.Button(frame_tombol, text="Kali", command=lambda: kali_matriks(masukan_a, masukan_b, label_hasil)).pack(fill="x", pady=5)
    tk.Button(frame_tombol, text="Determinan", command=lambda: pilih_matriks_determinan(masukan_a, masukan_b, label_hasil)).pack(fill="x", pady=5)
    tk.Button(frame_tombol, text="Invers", command=lambda: pilih_matriks_invers(masukan_a, masukan_b, label_hasil)).pack(fill="x", pady=5)

# GUI Setup
root = tk.Tk()
root.title("Operator Matriks")

label_judul = tk.Label(root, text="Operator Matriks", font=("Arial", 16, "bold"))
label_judul.grid(row=0, column=0, columnspan=4, pady=10)

tk.Label(root, text="Masukkan dimensi Matriks A (m x n):").grid(row=1, column=0, columnspan=2)
input_baris_a = tk.Entry(root, width=5)
input_kolom_a = tk.Entry(root, width=5)
input_baris_a.grid(row=1, column=2)
input_kolom_a.grid(row=1, column=3)

tk.Label(root, text="Masukkan dimensi Matriks B (m x n):").grid(row=2, column=0, columnspan=2)
input_baris_b = tk.Entry(root, width=5)
input_kolom_b = tk.Entry(root, width=5)
input_baris_b.grid(row=2, column=2)
input_kolom_b.grid(row=2, column=3)

tk.Button(root, text="Submit Dimensi", command=minta_dimensi_matriks).grid(row=3, column=0, columnspan=4)

frame_input = tk.Frame(root)
frame_input.grid(row=4, column=0, columnspan=4, pady=10)

label_hasil = tk.Label(root, text="Hasil akan ditampilkan di sini.", font=("Arial", 10))
label_hasil.grid(row=6, column=0, columnspan=6)

root.mainloop()
