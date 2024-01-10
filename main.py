# Dictionary Harga Menu Makanan dan Minuman
menu = {
    '1': {'item': 'Udang Asam manis',     'harga': 90000},
    '2': {'item': 'Lobster bakar',        'harga': 100000},
    '3': {'item': 'Cumi Bakar',           'harga': 50000},
    '4': {'item': 'Kepiting saus padang', 'harga': 200000},
    '5': {'item': 'Kerang Saus padang',   'harga': 50000},
    '6': {'item': 'Es Josu',              'harga': 8000},
    '7': {'item': 'Kopi Luwak',           'harga': 20000},
    '8': {'item': 'Es Campur',            'harga': 50000},
    '9': {'item': 'Jus Alpukat',          'harga': 20000},
    '10': {'item': 'Jus Pir',             'harga': 30000},
}

def tampilkan_menu(daftar):
    print("{:<10} {:<25} {:<15}".format('No', 'Nama', 'Harga'))
    print("---------------------------------------------")
    for nomor, detail in daftar.items():
        print("{:<10} {:<25} Rp {:<15}".format(nomor, detail['item'], detail['harga']))

def pesan_makanan():
    pesanan = {}
    while True:
        tampilkan_menu(menu)
        pilihan = input("Pilih nomor menu (atau ketik '0' untuk mengakhiri): ")

        if pilihan.lower() == '0':
            break

        if pilihan in menu:
            jumlah = int(input(f"Jumlah {menu[pilihan]['item']}: "))
            pesanan[menu[pilihan]['item']] = {'jumlah': jumlah, 'harga': menu[pilihan]['harga']}
        else:
            print("Pilihan tidak valid. Silakan pilih nomor menu yang benar.")
    return pesanan

def hitung_total(pesanan):
    total = 0
    for item, info in pesanan.items():
        total += info['jumlah'] * info['harga']
    return total

def cetak_struk(pesanan, total_harga):
    print("\n--- Struk Pembelian ---")
    print("\n--- KANTIN CIKARANG JAYA ---")
    print("Menu yang di pesan")
    for item, info in pesanan.items():
        print(f"{info['jumlah']} {item} - Rp {info['jumlah'] * info['harga']}")
    print("----------------------")
    print(f"Total Harga   : Rp {total_harga}")

    # Meminta input jumlah uang pembeli
    uang_pembeli = int(input("Masukkan jumlah uang pembeli: "))

    # Menghitung kembalian
    kembalian = uang_pembeli - total_harga

    # Menampilkan informasi uang pembeli dan kembalian
    print(f"Uang Pembeli  : Rp {uang_pembeli}")
    print(f"Kembalian     : Rp {kembalian}")

    print("Terima kasih atas pesanan Anda di kantin kami! Semoga makanan yang Anda pilih memberikan kepuasan untuk lidah Anda.")

print("     =================================")
print("           KANTIN CIKARANG JAYA         ")
print("     =================================")
pembeli = input("Masukkan nama Pembeli: ")
print("Nama Pembeli :", pembeli)

while True:
    daftar_pesanan = pesan_makanan()
    total_harga = hitung_total(daftar_pesanan)
    cetak_struk(daftar_pesanan, total_harga)

    ulang = input("Apakah Anda ingin memesan lagi? (Ketik '1' untuk ya, '0' untuk tidak): ")
    if ulang != '1':
        print("Terima kasih atas kunjungan Anda!")
        break
