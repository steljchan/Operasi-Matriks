import tkinter as tk
from tkinter import messagebox

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

    tk.Button(frame_tombol, text="Tambah", command=tambah_matriks).pack(fill="x", pady=5)
    tk.Button(frame_tombol, text="Kurang", command=kurang_matriks).pack(fill="x", pady=5)
    tk.Button(frame_tombol, text="Kali", command=kali_matriks).pack(fill="x", pady=5)
    tk.Button(frame_tombol, text="Determinan", command=pilih_matriks_determinan).pack(fill="x", pady=5)
    tk.Button(frame_tombol, text="Invers", command=pilih_matriks_invers).pack(fill="x", pady=5)

def ambil_matriks(masukan):
    try:
        return [[int(masukan[i][j].get()) for j in range(len(masukan[0]))] for i in range(len(masukan))]
    except ValueError:
        messagebox.showerror("Error", "Semua elemen matriks harus berupa bilangan bulat!")
        return None

def tampilkan_hasil(matriks, judul):
    if not matriks:
        return
    hasil = "\n".join(["\t".join(map(str, baris)) for baris in matriks])
    label_hasil.config(text=f"{judul}:\n{hasil}")

def tambah_matriks():
    A = ambil_matriks(masukan_a)
    B = ambil_matriks(masukan_b)
    if A is None or B is None:
        return
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        messagebox.showerror("Error", "Dimensi Matriks A dan B harus sama untuk penjumlahan!")
        return
    hasil = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    tampilkan_hasil(hasil, "Hasil Penjumlahan")

def kurang_matriks():
    A = ambil_matriks(masukan_a)
    B = ambil_matriks(masukan_b)
    if A is None or B is None:
        return
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        messagebox.showerror("Error", "Dimensi Matriks A dan B harus sama untuk pengurangan!")
        return
    hasil = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    tampilkan_hasil(hasil, "Hasil Pengurangan")

def kali_matriks():
    A = ambil_matriks(masukan_a)
    B = ambil_matriks(masukan_b)
    if A is None or B is None:
        return
    if len(A[0]) != len(B):
        messagebox.showerror("Error", "Jumlah kolom Matriks A harus sama dengan jumlah baris Matriks B untuk perkalian!")
        return
    hasil = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    tampilkan_hasil(hasil, "Hasil Perkalian")

def hitung_determinan(matriks, label):
    if len(matriks) != len(matriks[0]):
        messagebox.showerror("Error", "Matriks harus persegi untuk menghitung determinan!")
        return

    def determinan(mat):
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for c in range(len(mat)):
            sub_mat = [baris[:c] + baris[c + 1:] for baris in mat[1:]]
            det += ((-1) ** c) * mat[0][c] * determinan(sub_mat)
        return det

    det = determinan(matriks)
    label_hasil.config(text=f"Hasil Determinan ({label}): {det}")

def pilih_matriks_determinan():
    window_determinan = tk.Toplevel(root)
    window_determinan.title("Pilih Matriks untuk Determinan")
    tk.Button(window_determinan, text="Matriks A", command=lambda: hitung_determinan(ambil_matriks(masukan_a), "A")).pack()
    tk.Button(window_determinan, text="Matriks B", command=lambda: hitung_determinan(ambil_matriks(masukan_b), "B")).pack()

def hitung_invers(matriks, label):
    if len(matriks) != len(matriks[0]):
        messagebox.showerror("Error", "Matriks harus persegi untuk menghitung invers!")
        return

    def determinan(mat):
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for c in range(len(mat)):
            sub_mat = [baris[:c] + baris[c + 1:] for baris in mat[1:]]
            det += ((-1) ** c) * mat[0][c] * determinan(sub_mat)
        return det

    def minor(mat, i, j):
        return [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]

    det = determinan(matriks)
    if det == 0:
        messagebox.showerror("Error", f"Matriks {label} tidak memiliki invers (determinannya 0)!")
        return

    cofactors = []
    for i in range(len(matriks)):
        cofactor_row = []
        for j in range(len(matriks)):
            minor_mat = minor(matriks, i, j)
            cofactor_row.append(((-1) ** (i + j)) * determinan(minor_mat))
        cofactors.append(cofactor_row)

    cofactors = list(map(list, zip(*cofactors)))  # Transpose
    invers = [[round(cofactors[i][j] / det, 2) for j in range(len(cofactors))] for i in range(len(cofactors))]
    tampilkan_hasil(invers, f"Hasil Invers ({label})")

def pilih_matriks_invers():
    window_invers = tk.Toplevel(root)
    window_invers.title("Pilih Matriks untuk Invers")
    tk.Button(window_invers, text="Matriks A", command=lambda: hitung_invers(ambil_matriks(masukan_a), "A")).pack()
    tk.Button(window_invers, text="Matriks B", command=lambda: hitung_invers(ambil_matriks(masukan_b), "B")).pack()

# GUI
root = tk.Tk()
root.title("Operator Matriks")

# Label Judul
label_judul = tk.Label(root, text="Operator Matriks", font=("Arial", 16, "bold"))
label_judul.grid(row=0, column=0, columnspan=4, pady=10)

# Input Dimensi Matriks
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

# Frame untuk masukan matriks dan operasi
frame_input = tk.Frame(root)
frame_input.grid(row=4, column=0, columnspan=4, pady=10)

# Label untuk hasil
label_hasil = tk.Label(root, text="Hasil akan ditampilkan di sini.", font=("Arial", 10))
label_hasil.grid(row=6, column=0, columnspan=6)

root.mainloop()
