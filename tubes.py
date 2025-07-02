import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Fungsi iteratif untuk menghitung jumlah kata dan karakter
def hitung_kata_karakter_iteratif(teks):
    in_word = False
    jumlah_kata = 0
    jumlah_karakter = 0

    for char in teks:
        jumlah_karakter += 1

        if char != ' ' and not in_word:
            in_word = True
            jumlah_kata += 1
        elif char == ' ':
            in_word = False

    return jumlah_kata, jumlah_karakter

# Fungsi rekursif untuk menghitung jumlah karakter
def hitung_karakter_rekursif(teks):
    if teks == "":
        return 0  # Basis rekursi
    return 1 + hitung_karakter_rekursif(teks[1:])  # Rekursi

# Fungsi rekursif untuk menghitung jumlah kata
def hitung_kata_rekursif(teks, index=0, in_word=False):
    if index == len(teks):  # Basis rekursi
        return 0 if in_word else 0

    char = teks[index]
    if char != ' ' and not in_word:
        return 1 + hitung_kata_rekursif(teks, index + 1, True)
    elif char == ' ':
        return hitung_kata_rekursif(teks, index + 1, False)
    else:
        return hitung_kata_rekursif(teks, index + 1, in_word)

# Wrapper untuk menghitung kata dan karakter secara rekursif
def hitung_kata_karakter_rekursif(teks):
    jumlah_karakter = hitung_karakter_rekursif(teks)
    jumlah_kata = hitung_kata_rekursif(teks)
    return jumlah_kata, jumlah_karakter

# Grafik untuk menyimpan data
teks_values = []
iterative_times = []
recursive_times = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(teks_values, iterative_times, label='Iteratif', marker='o', linestyle='-')
    plt.plot(teks_values, recursive_times, label='Rekursif', marker='o', linestyle='-')
    plt.title('Perbandingan Waktu Eksekusi: Iteratif vs Rekursif')
    plt.xlabel('Teks Input')
    plt.ylabel('Waktu Eksekusi (detik)')
    plt.legend()
    plt.grid(True)
    plt.show()

def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Teks Input", "Iteratif (s)", "Rekursif (s)"]
    min_len = min(len(teks_values), len(iterative_times), len(recursive_times))
    for i in range(min_len):
        table.add_row([teks_values[i], iterative_times[i], recursive_times[i]])
    print(table)

# Program utama
while True:
    try:
        teks_input = input("Masukkan teks (atau ketik 'exit' untuk keluar): ")
        if teks_input.lower() == 'exit':
            print("Program selesai. Terima kasih!")
            break

        teks_values.append(teks_input)

        # Ukur waktu eksekusi untuk metode iteratif
        start_time = time.time()
        jumlah_kata_iteratif, jumlah_karakter_iteratif = hitung_kata_karakter_iteratif(teks_input)
        iterative_times.append(time.time() - start_time)

        # Ukur waktu eksekusi untuk metode rekursif
        start_time = time.time()
        jumlah_kata_rekursif, jumlah_karakter_rekursif = hitung_kata_karakter_rekursif(teks_input)
        recursive_times.append(time.time() - start_time)

        # Cetak hasil jumlah kata dan karakter
        print(f"Metode Iteratif: Jumlah Kata = {jumlah_kata_iteratif}, Jumlah Karakter = {jumlah_karakter_iteratif}")
        print(f"Metode Rekursif: Jumlah Kata = {jumlah_kata_rekursif}, Jumlah Karakter = {jumlah_karakter_rekursif}")

        # Cetak tabel waktu eksekusi
        print_execution_table()

        # Perbarui grafik
        update_graph()

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")