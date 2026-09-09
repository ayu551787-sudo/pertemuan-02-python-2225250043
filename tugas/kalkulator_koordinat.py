
# 1. Menampilkan judul program
print("KALKULATOR KOORDINAT DUA TITIK")

# 2. Membaca x1, y1, x2, dan y2 sebagai float
x1 = float(input("x titik A: "))
y1 = float(input("y titik A: "))
x2 = float(input("x titik B: "))
y2 = float(input("y titik B: "))

# 3. Menghitung perubahan koordinat dx dan dy
dx = x2 - x1
dy = y2 - y1

# 4. Menghitung jarak Euclidean (tanpa pustaka math)
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

# 5. Menghitung koordinat titik tengah
titik_tengah_x = (x1 + x2) / 2
titik_tengah_y = (y1 + y2) / 2

# 6. Menampilkan seluruh hasil menggunakan f-string dengan 2 angka desimal
print()
print(f"Titik A       : ({x1:.2f}, {y1:.2f})")
print(f"Titik B       : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan     : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B  : {jarak:.2f}")
print(f"Titik tengah  : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")
