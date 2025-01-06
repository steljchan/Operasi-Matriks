def hitung_invers(matriks):
    """Menghitung invers dari matriks persegi."""
    if len(matriks) != len(matriks[0]):
        raise ValueError("Matriks harus persegi untuk menghitung invers!")

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
        raise ValueError("Matriks tidak memiliki invers karena determinannya 0!")

    cofactors = []
    for i in range(len(matriks)):
        cofactor_row = []
        for j in range(len(matriks)):
            minor_mat = minor(matriks, i, j)
            cofactor_row.append(((-1) ** (i + j)) * determinan(minor_mat))
        cofactors.append(cofactor_row)

    cofactors = list(map(list, zip(*cofactors)))  # Transpose
    invers = [[round(cofactors[i][j] / det, 2) for j in range(len(cofactors))] for i in range(len(cofactors))]
    return invers


def pilih_matriks_invers(masukan_a, masukan_b, label_hasil):
    """Menampilkan jendela untuk memilih matriks yang akan dihitung inversnya."""
    import tkinter as tk
    from tkinter import messagebox

    def tampilkan_hasil(matriks, label):
        try:
            invers = hitung_invers(matriks)
            hasil = "\n".join(["\t".join(map(str, row)) for row in invers])
            label_hasil.config(text=f"Hasil Invers ({label}):\n{hasil}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    window_invers = tk.Toplevel()
    window_invers.title("Pilih Matriks untuk Invers")

    tk.Button(window_invers, text="Matriks A", 
              command=lambda: tampilkan_hasil([[int(cell.get()) for cell in row] for row in masukan_a], "A")).pack()
    tk.Button(window_invers, text="Matriks B", 
              command=lambda: tampilkan_hasil([[int(cell.get()) for cell in row] for row in masukan_b], "B")).pack()
