def hitung_determinan(matriks):
    """Menghitung determinan matriks persegi."""
    if len(matriks) != len(matriks[0]):
        raise ValueError("Matriks harus persegi untuk menghitung determinan!")

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

    return determinan(matriks)


def pilih_matriks_determinan(masukan_a, masukan_b, label_hasil):
    """Menampilkan jendela untuk memilih matriks yang akan dihitung determinannya."""
    import tkinter as tk
    from tkinter import messagebox

    def tampilkan_hasil(matriks, label):
        try:
            det = hitung_determinan(matriks)
            label_hasil.config(text=f"Hasil Determinan ({label}): {det}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    window_determinan = tk.Toplevel()
    window_determinan.title("Pilih Matriks untuk Determinan")

    tk.Button(window_determinan, text="Matriks A", 
              command=lambda: tampilkan_hasil([[int(cell.get()) for cell in row] for row in masukan_a], "A")).pack()
    tk.Button(window_determinan, text="Matriks B", 
              command=lambda: tampilkan_hasil([[int(cell.get()) for cell in row] for row in masukan_b], "B")).pack()
