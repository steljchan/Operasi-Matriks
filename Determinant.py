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