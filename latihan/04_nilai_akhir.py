# Konstanta bobot penilaian
BOBOT_TUGAS = 0.20
BOBOT_UTS = 0.30
BOBOT_UAS = 0.50

# Menerima input nama dan nilai
nama = input("Masukkan nama mahasiswa: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

# Menghitung nilai akhir berbobot
nilai_akhir = (nilai_tugas * BOBOT_TUGAS) + (nilai_uts * BOBOT_UTS) + (nilai_uas * BOBOT_UAS)

# Menampilkan hasil dengan 2 angka desimal
print()
print(f"Nama        : {nama}")
print(f"Nilai Akhir : {nilai_akhir:.2f}")