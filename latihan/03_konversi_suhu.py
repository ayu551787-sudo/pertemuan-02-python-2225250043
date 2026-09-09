# Konstanta
KELVIN_OFFSET = 273.15

# Input suhu Celsius
celsius = float(input("Masukkan suhu Celsius: "))

# Perhitungan konversi
fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

# Output hasil
print(f"Suhu Fahrenheit : {fahrenheit:.2f} °F")
print(f"Suhu Kelvin     : {kelvin:.2f} K")