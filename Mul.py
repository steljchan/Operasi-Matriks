def kali_matriks(masukan_a, masukan_b, label_hasil):
    try:
        A = [[int(cell.get()) for cell in row] for row in masukan_a]
        B = [[int(cell.get()) for cell in row] for row in masukan_b]
        hasil = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
        label_hasil.config(text="Hasil Perkalian:\n" + "\n".join(["\t".join(map(str, row)) for row in hasil]))
    except ValueError:
        label_hasil.config(text="Error: Semua elemen matriks harus angka!")
