print("Operasi Matematika")
print("1. Jumlah  [+]")
print("2. Kurang  [-]")
print("3. Kali    [*]")
print("4. Bagi    [/]")

menu = input("Pilih Operasi (1/2/3/4): ")

bilper = int(input("Masukkan bilangan pertama :"))
bilke = int(input("Masukkan bilangan kedua :"))

def penjumlahan(bilper, bilke):
    Jumlah = bilper + bilke
    return Kurang

def pengurangan(bilper, bilke):
    Kurang = bilper - bilke
    return Kurang

def perkalian(bilper, bilke):
    Kali = bilper * bilke
    return Kali

def pembagian(bilper, bilke):
    Bagi = bilper / bilke
    return Bagi

if menu == ("1"):
    print("Hasil operasi dari", bilper, "+", bilke, "=",penjumlahan(bilper, bilke))
elif menu == ("2"):
    print("Hasil operasi dari", bilper, "-", bilke, "=",pengurangan(bilper, bilke))
elif menu == ("3"):
    print("Hasil operasi dari", bilper, "*", bilke, "=",perkalian(bilper, bilke))
else:
    print("Hasil operasi dari", bilper, "/", bilke, "=",pembagian(bilper, bilke))





