nama = "Siti FATIMAH"
nim = "260404100144"
kota_tujuan = "Surabaya"
berat_bagasi = 15.5
punya_ktm = True

kelas_tiket = input("Masukkan kelas tiket (ekonomi/eksekutif): ")
hari_keberangkatan = input("Masukkan hari keberangkatan (weekday/weekend): ")
if kota_tujuan == "Surabaya":
    tarif_dasar = 25000
elif kota_tujuan == "Sumenep":
    tarif_dasar = 45000
elif kota_tujuan == "Malang":
    tarif_dasar = 60000
else:
    print("Kota tujuan tidak dilayani.")

if kelas_tiket == "ekonomi":
    tambahan_kelas = 0
elif kelas_tiket == "eksekutif":
    if kota_tujuan == "Surabaya":
        print("Pesanan ditolak.")
        print("Kelas eksekutif tidak tersedia untuk rute Surabaya.")
        
    tambahan_kelas = 25000
else:
    print("Kelas tiket tidak valid.")

harga = tarif_dasar + tambahan_kelas

if hari_keberangkatan == "weekend":
    harga = harga * 1.15
elif hari_keberangkatan == "weekday":
    harga = harga
else:
    print("Hari keberangkatan tidak valid.")
  

if punya_ktm:
    harga = harga * 0.90

if berat_bagasi <= 20:
    biaya_bagasi = 0
elif berat_bagasi <= 30:
    kelebihan = berat_bagasi - 20
    biaya_bagasi = kelebihan * 5000
else:
    print("Pemesanan ditolak.")
    print("Bagasi lebih dari 30 kg harus dikirim melalui kargo.")

total_pembayaran = harga + biaya_bagasi
print("Nama               :", nama)
print("NIM                :", nim)
print("Kota Tujuan        :", kota_tujuan)
print("Berat Bagasi       :", berat_bagasi, "kg")
print("Punya KTM          :", punya_ktm)
print("Kelas Tiket        :", kelas_tiket)
print("Hari Keberangkatan :", hari_keberangkatan)
print("Tarif Dasar        : Rp", tarif_dasar)
print("Biaya Bagasi       : Rp", biaya_bagasi)
print("Total Pembayaran   : Rp", total_pembayaran)


# TYPE DATA
print("nama              :", type(nama))
print("nim               :", type(nim))
print("kota_tujuan       :", type(kota_tujuan))
print("berat_bagasi      :", type(berat_bagasi))
print("punya_ktm         :", type(punya_ktm))
print("kelas_tiket       :", type(kelas_tiket))
print("hari_keberangkatan:", type(hari_keberangkatan))