import os

FILE_NAME = "phonebook.txt"

# -------------------------------
# 1. Tambah Kontak (Append Mode)
# -------------------------------
def tambah_kontak():
    print("\n=== Tambah Kontak ===")
    nama = input("Nama   : ")
    nomor = input("Nomor  : ")
    email = input("Email (opsional): ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{nama}|{nomor}|{email}\n")

    print("Kontak berhasil ditambahkan!\n")


# ---------------------------------------
# 2. Tampilkan semua kontak (Read Mode)
# ---------------------------------------
def tampilkan_kontak():
    print("\n=== Daftar Semua Kontak ===")

    if not os.path.exists(FILE_NAME):
        print("Belum ada kontak.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

        if not data:
            print("Belum ada kontak.")
            return

        for i, line in enumerate(data, start=1):
            nama, nomor, email = line.strip().split("|")
            print(f"{i}. Nama : {nama}")
            print(f"   Nomor: {nomor}")
            print(f"   Email: {email if email else '-'}")
            print("-" * 30)


# ----------------------------
# 3. Cari kontak
# ----------------------------
def cari_kontak():
    print("\n=== Cari Kontak ===")
    keyword = input("Masukkan nama atau nomor: ").lower()

    if not os.path.exists(FILE_NAME):
        print("Tidak ada file kontak.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

        ditemukan = False
        for line in data:
            nama, nomor, email = line.strip().split("|")
            if keyword in nama.lower() or keyword in nomor:
                print("\nKontak ditemukan:")
                print(f"Nama  : {nama}")
                print(f"Nomor : {nomor}")
                print(f"Email : {email if email else '-'}")
                ditemukan = True

        if not ditemukan:
            print("Kontak tidak ditemukan.")


# ----------------------------
# 4. Menu utama
# ----------------------------
def menu():
    while True:
        print("\n=== SISTEM PHONEBOOK ===")
        print("1. Tambah Kontak")
        print("2. Tampilkan Semua Kontak")
        print("3. Cari Kontak")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_kontak()
        elif pilihan == "2":
            tampilkan_kontak()
        elif pilihan == "3":
            cari_kontak()
        elif pilihan == "4":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid!")


# ----------------------------
# 5. Jalankan program
# ----------------------------
menu()
