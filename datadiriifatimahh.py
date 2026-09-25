# DATA DIRI
nama = "Siti FATIMAH"
nim = "123456144"
tempat_lahir = "Dusun Kanari"
alamat = "Polewali Mandar"
hobi = "Bermain badminton dan membaca"

tahun_lahir = int(input("Masukkan tahun lahir : "))
ipk = float(input("Masukkan IPK : "))


# PERHITUNGAN DATA DIRI
tahun_sekarang = 2026
umur = tahun_sekarang - tahun_lahir
umur_10_tahun_lagi = umur + 10
jumlah_karakter = len(nama)
tahun_umur_30 = tahun_lahir + 30


# OUTPUT DATA DIRI

print("HASIL DATA DIRI")
print("nama :", nama)
print("nim :", nim)
print("tempat lahir :", tempat_lahir)
print("alamat :", alamat)
print("hobi :", hobi)
print("tahun lahir :", tahun_lahir)
print("ipk :", ipk)

print("HASIL PERHITUNGAN")
print("umur saat ini :", umur)
print("umur 10 tahun lagi :", umur_10_tahun_lagi)
print("jumlah karakter nama :", jumlah_karakter)
print("tahun saat berumur 30 :", tahun_umur_30)

print("TIPE DATA")
print("nama :", type(nama))
print("nim :", type(nim))
print("tempat lahir :", type(tempat_lahir))
print("alamat :", type(alamat))
print("hobi :", type(hobi))
print("tahun lahir :", type(tahun_lahir))
print("ipk :", type(ipk))