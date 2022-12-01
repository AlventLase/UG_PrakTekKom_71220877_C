print("Pemeriksa Kelipatan 9")
kel = int(input("Masukkan Kelipatan 9 yang ingin diperiksa: "))

def kelipatan_sembilan():
    jawaban = (kel%9)
    return jawaban

if kelipatan_sembilan() == 0:
    print("BENAR")
else:
    print("SALAH")