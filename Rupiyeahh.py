# ------------------------------------------------------------#
#                  Money Management App                      #
#                   written in python                        #
#                      Kelompok 6                            #
# ------------------------------------------------------------#

import os, time, sys
from datetime import date


def simpanRiwayat(data): # menyimpan history ke teks file
    with open("rupiYeahRiwayat.txt", "w") as file: # membuat teks file 
        for i in data: # melakukan perulangan pada data 
            file.write(f"{i[0]},{i[1]},{i[2]},{i[3]}\n") # menuliskan data ke teks file


def loadHistory(): # mencari data sebelumnya
    try: #kode try except guna mencegah terjadinya program berhenti tiba tiba
        with open("rupiYeahRiwayat.txt", "r") as file: # jika ada file yang sama maka akan ddibuka dengan mode read 
            baca = file.readlines() # membaca data 
            return [lines.strip().split(",") for lines in baca] # mengembalikan data yang ada dalam bentuk lis
    except:
        return [] # jika tidak ada maka akan mengembalikan list kosong


def simpanSaldo(data): # menyimpan saldo agar bisa diakases lagi
    with open("rupiYeahSaldo.txt", "w") as file: # membaut teks file 
        file.write(str(data)) # menulis data ke teks fiel


def loadSaldo(): # mencari apa sudah ada data 
    try: 
        with open("rupiYeahSaldo.txt", "r") as file: # membuka teks file dalam mode read atau baca
            baca = file.readline() # membaca data 
            return int(baca) # mengembalikan data dalam bentuk integer 
    except:
        saldoAwal = 0 # jika tidak ada maka dibuat variabel saldoAawal dengan nilai 0 
        simpanSaldo(saldoAwal) # menyimpan saldo awal ke data teks file agar bisa digunakan kembali
        return saldoAwal # mengembalikan nilai saldo awal 



history = loadHistory() # mengecek apa sudah ada data riwayat sebelumnya
saldo = loadSaldo() # mengecek apa sudah ada data saldo sebelumnya
tabunganAwal = saldo # menyamakan nilai saldo dengan tabunganAwal berfungsi pada fungsi evaluasi 
tp = 99 # garis


def menu():  # ini fungsi menu dimana pengguna dapat memilih fitur yang ingin digunakan
    masukan = True # inisialisasi variabel masukan dengan nilai boolean sebagai pembuka perulangan
    while masukan == True: # perulangan ada 
        os.system("cls")
        print("|" + "=" * tp + "|")
        print("|" + "Selamat datang di RupiYeah!".center(tp) + "|")
        print(
            "|"
            + "bikin setiap rupiah yang kamu keluarkan, jadi worth it #AntiBoncos".center(
                tp
            ).title()
            + "|"
        )
        print("|" + "=" * tp + "|")
        print(
            "|"
            + f"kamu memiliki saldo sebesar Rp{saldo:,.2f} saat ini".center(tp)
            + "|"
        )
        print("|" + "=" * tp + "|")
        print("|" + "1. Masukkan Pengeluaran".ljust(tp) + "|")
        print("|" + "2. Masukkan Pemasukan".ljust(tp) + "|")
        print("|" + "3. Hapus Pengeluaran/Pemasukan".ljust(tp) + "|")
        print("|" + "4. Atur Budget (50/30/20 rule)".ljust(tp) + "|")
        print("|" + "5. Cek History pengeluaran dan pemasukan".ljust(tp) + "|")
        print("|" + "6. Evaluasi keuangan".ljust(tp) + "|")
        print("|" + "7. keluar dari program".ljust(tp) + "|")
        print("|" + "=" * tp + "|")
        opsi = input("\nMau ngapain hari ini? (1/2/3/4/5/6/7): ".title())
        if opsi == "1":
            os.system("cls")
            pengeluaran()
        elif opsi == "2":
            os.system("cls")
            pemasukan()
        elif opsi == "3":
            os.system("cls")
            hapusRiwayat(history)
        elif opsi == "4":
            os.system("cls")
            aturBudget()
        elif opsi == "5":
            os.system("cls")
            cekRiwayat(history)
        elif opsi == "6":
            os.system("cls")
            evaluasi()
        elif opsi == "7":
            os.system("cls")
            print("|" + "=" * tp + "|")
            print("|" + "Terima kasih telah menggunakan RupiYeah".center(tp) + "|")
            print("|" + "#AntiBoncos".center(tp).title() + "|")
            print("|" + "=" * tp + "|")
            sys.exit()
        else:
            print("harap berikan input yang benar!")
            time.sleep(2)


def hapusRiwayat(data): # ini fungsi menghapus riwayat
    global saldo, history # inisialisasi variabel saldo dari scope global agar bisa digunakan di scope local

    if (
        len(history) == 0 
    ):  # pengecekan jika pengguna sudah pernah memasukkan catatan keuangan sebelumnya
        print("|" + "Riwayat pengeluaran kamu".center(152, "=").title() + "|")
        print(
            "|"
            + "No.".center(4)
            + "|"
            + "Pengeluaran".center(30)
            + "|"
            + "Pemasukan".center(30)
            + "|".center(30)
            + "Kategori".center(30)
            + "|"
            + "tanggal".center(25)
            + "|"
        )
        print("|" + "=" * 152 + "|")
        print("|" + "kamu belum memiliki catatan keuangan selama ini".center(152) + "|")
        print("sistem akan mengembalikan mu ke menu dalam beberapa detik".center(152))
        time.sleep(1.5)
        menu()
    else:
        if len(history) == 0: 
            print("|" + "Riwayat pengeluaran kamu".center(152, "=").title() + "|")
            print(
                "|"
                + "No.".center(4)
                + "|"
                + "Pengeluaran".center(30)
                + "|"
                + "Pemasukan".center(30)
                + "|".center(30)
                + "Kategori".center(30)
                + "|"
                + "tanggal".center(25)
                + "|"
            )
            print("|" + "=" * 152 + "|")
            print("|" + "kamu belum memiliki catatan keuangan selama ini".center(152) + "|")
            print("sistem akan mengembalikan mu ke menu dalam beberapa detik".center(152))
            time.sleep(1.5)
            menu()
        else:
            nomor = 0
            print("|" + "Riwayat pengeluaran kamu".center(152, "=").title() + "|")
            print(
                "|"
                + "No.".center(4)
                + "|"
                + "Pengeluaran".ljust(30)
                + "|"
                + "Pemasukan".ljust(44)
                + "|"
                + "Kategori".ljust(45)
                + "|"
                + "tanggal".ljust(25)
                + "|"
            )
            print("|" + "=" * 152 + "|")
            for i in data:
                masukan = f"-" if i[1] == "-" else f"Rp {int(i[1]):,.2f}" # jika index ke satu pada i bernilai "-" maka cetak "-" jika tidak, tulis dalam bentuk rupiah
                pengeluaran = f"-" if i[0] == "-" else f"Rp {int(i[0]):,.2f}"# jika index ke nol pada i bernilai "-" maka cetak "-" jika tidak, tulis dalam bentuk rupiah
                nomor += 1 # sistem penomoran, yang akan menjadi acuan penghapusan riwayat
                print(
                    f"|{str(nomor).center(4)}|{str(masukan).ljust(30)}|{str(pengeluaran).ljust(44)}|{i[2].ljust(45)}|{i[3].ljust(25)}|"
                )
            print("|" + "=" * 152 + "|")
            print("|" + "Total Saldo".center(136) + "|" + f"Rp{saldo:,.2f}".center(15) + "|")
            try:
                hapus = input("masukkan no riwayat yang ingin dihapus: ")
                if hapus == "":
                    print("harap masukkan input yang benar!\nNomor riwayat yang dihapus tidak bisa kosong!\nSistem akan mengembalikan anda ke menu dalam beberapa detik")
                    time.sleep(2)
                    menu()
                elif int(hapus) <= 0: 
                    print("harap masukkan input yang benar!\nNomor riwayat yang dihapus harus sesuai dengan riwayat!\nSistem akan mengembalikan anda ke menu dalam beberapa detik")
                    time.sleep(2)
                    menu()
            except ValueError:
                print("harap masukkan input yang benar!\nNomor riwayat tidak bisa ditulis dalam bentuk karakter!\nSistem akan mengembalikan anda ke menu dalam beberapa detik")
                time.sleep(2)
                menu()
        if len(str(history[int(hapus) - 1][1])) > 1: # pengecekan apakah riwayat yang dihapus merupakan pemasukan atau merupakan pengeluaran
            saldo = saldo + int(history[int(hapus) - 1][1]) # mengembalikan saldo
            history.pop(int(hapus) - 1)  # menghapus riwayat sesuai dengan nomor
            simpanRiwayat(history)
            simpanSaldo(saldo) # menyimpan ke teks file agar bisa diakses kembali
            print("riwayat berhasil di hapus! ")
        else: # proses yang sama
            saldo = saldo - int(history[int(hapus) - 1][0]) 
            simpanSaldo(saldo)
            history.pop(int(hapus) - 1) 
            simpanRiwayat(history)
            print("riwayat berhasil di hapus! ")
    opsi = input("kembali ke menu?(y/n) : ")
    if opsi == "y":
        menu()
    else:
        print("|" + "=" * tp + "|")
        print("|" + "Terima kasih telah menggunakan RupiYeah".center(tp) + "|")
        print("|" + "#AntiBoncos".center(tp).title() + "|")
        print("|" + "=" * tp + "|")
        time.sleep(2)
        return "terima kasih !"


def pengeluaran():  # ini fungsi untuk mencatata pengeluaran
    os.system("cls") # mengclear terminal agar terlihat rapih
    keluar = True # inisialisasi variabel keluar dengan nilai boolean sebagai pembuka loop 
    global saldo, history # menginisialisasi variabel global saldo dan history agar dapat digunakan di fungsi 
    while keluar == True:
        # pengeluaran = int(input("masukkan pengeluaran: "))
        # if pengeluaran < 0: 
        #     print("Pengeluaran tidak boleh sama dengan atau kurang dari 0 !\nharap catat pengeluaran dengan benar!\nSistem akan mengembalikan anda ke menu dalam beberapa detik.")
        #     time.sleep(2)
        #     break
        try: 
            pengeluaran = int(input("masukkan pengeluaran (dalam bentuk angka): "))
            if pengeluaran <= 0: 
                print("Pengeluaran tidak boleh sama dengan atau kurang dari 0 atau berbentuk karakter!!\nharap catat pengeluaran dengan benar!\nSistem akan mengembalikan anda ke menu dalam beberapa detik.")
                time.sleep(2)
                break
        except ValueError:
            print("Pengeluaran tidak boleh sama dengan atau kurang dari 0 atau berbentuk karakter!!!\nharap catat pengeluaran dengan benar!\nSistem akan mengembalikan anda ke menu dalam beberapa detik.")
            time.sleep(2)
            break
        sumber = input("pengeluarannya digunakan untuk apa (max 20 karakter): ")
        if len(sumber) >= 20: 
            print("Masukan anda melebihi batas karakter!\nharap catat pengeluaran anda dengan benar!\nSistem akan mengembalikan anda ke menu dalam beberapa detik.")
            time.sleep(2)
            break
        elif len(sumber) == 0: 
            print("Masukan anda tidak boleh kosong!\nharap catat pengeluaran anda dengan benar!\nSistem akan mengembalikan anda ke menu dalam beberapa detik.")
            time.sleep(2)
            break
        os.system("cls")
        print("|" + "masukkan pengeluaran".center(tp, "=").title() + "|")
        print("|" + "=" * tp + "|")
        print(
            "|"
            + f"pengeluaran sebesar Rp{pengeluaran:,.2f} untuk {sumber} berhasil dimasukkan".center(
                tp
            )
            + "|"
        )
        saldo -= int(pengeluaran) # mengurangi total saldo dengan pengeluaran 
        sumber = f"{sumber}" # memasukkan sumber/kategori pengeluaran
        tanggal = f"{date.today()}" # mencatat tanggal pengeluaran
        masuk = "-" # memasukkan tanda kurang/strip pada list yang menduduk tempat pemasukan, berfungsi agar terlihat rapih dan tidak kosong
        print("|" + "=" * tp + "|")
        history.append([masuk, pengeluaran, sumber, tanggal]) # memasukkan semua variabel tersebut ke list history
        simpanRiwayat(history) # menyimpan ke teks file agar bisa diakses lagi
        simpanSaldo(saldo) # menyimpan ke teks file
        print("|" + "1. Kembali Ke Menu".ljust(tp) + "|")
        print("|" + "2. Masukkan Pengeluaran Lagi".ljust(tp) + "|")
        print("|" + "=" * tp + "|")
        opsi = input("Kembali ke menu ?: ")
        if opsi == "1":
            keluar = False
            menu()
        elif opsi == "2":
            os.system("cls")
            keluar == True
        else:
            print("harap masukkan opsi yang benar!")


def pemasukan():  # ini fungsi untuk mencatat pemasukan
    os.system("cls") # membersihkan terminal agar terlihat bersih
    keluar = True # menginisialisasi variabel keluar dengan nilai True sebagai pembuka loop
    global saldo, history # mengambil variabel global saldo dan history agar bisa digunakan di fungsi
    while keluar == True: 
        try: 
            pemasukan = int(input("masukkan pemasukan (masukkan dalam bentuk angka): ")) # memasukkan jumlah pemasukan 
            if pemasukan <= 0: 
                print("pemasukan tidak boleh sama dengan atau kurang dari 0 atau berbentuk karakter!\nharap catat pengeluaran dengan benar!\nSistem akan mengembalikan anda ke menu dalam beberapa detik.")
                time.sleep(2)
                break
        except ValueError:
            print("pemasukan tidak boleh sama dengan atau kurang dari 0 atau berbentuk karakter!!\nharap catat pengeluaran dengan benar!\nSistem akan mengembalikan anda ke menu dalam beberapa detik.")
            time.sleep(2)
            break
        sumber = input("pemasukan ini bersumber dari mana (max 20 karakter): ") # memasukkan kategori/sumber pemasukan 
        if len(sumber) >= 20: 
            print("Masukan anda melebihi batas karakter!\nharap catat pengeluaran anda dengan benar!\nSistem akan mengembalikan anda ke menu dalam beberapa detik.")
            time.sleep(2)
            break
        elif len(sumber) == 0: 
            print("Masukan anda tidak boleh kosong!\nharap catat pengeluaran anda dengan benar!\nSistem akan mengembalikan anda ke menu dalam beberapa detik.")
            time.sleep(2)
            break
        os.system("cls")
        print("|" + "masukkan pemasukan".center(tp, "=").title() + "|")
        print("|" + "=" * tp + "|")
        print(
            "|"
            + f"pemasukan sebesar Rp{pemasukan:,.2f} dari {sumber} berhasil dimasukkan".center(
                tp
            )
            + "|"
        )
        saldo += int(pemasukan) # menambahkan pemasukan dengan total saldo
        sumber = f"{sumber}" # memasukkan kategori/sumber pemasukan 
        tanggal = f"{date.today()}" # memasukkan tanggal/pemasukan
        pengeluaran = "-" # menambahkan strip pada list yang menjadi tempat pengeluaran
        print("|" + "=" * tp + "|")
        history.append([pemasukan, pengeluaran, sumber, tanggal]) # memasukkan catatan keuangan ke list
        simpanRiwayat(history) # menyimpan teks file agar bisa diakses lagi 
        simpanSaldo(saldo) # menyimpan ke teks file
        print("|" + "1. Kembali Ke Menu".ljust(tp) + "|")
        print("|" + "2. Masukkan pemasukan Lagi".ljust(tp) + "|")
        print("|" + "=" * tp + "|")
        opsi = input("Kembali ke menu ?: ")
        if opsi == "1":
            keluar = False
            menu()
        elif opsi == "2":
            os.system("cls")
            keluar == True
        else:
            print("harap masukkan opsi yang benar!")

def aturBudget():  # done
    global saldo # inisalisasi variabel global
    if saldo < 0: 
        print("|" + "rencana penggunaan budget".center(tp, "=").title() + "|")
        print("|" + "=" * tp + "|")
        print("|" + "Tabung uangmu dulu, baru rencakan keuangannmu. Keuangan mu sedang mines!".center(tp) + "|")
        print("|" + "=" * tp + "|")
    else: 
        print("|" + "rencana penggunaan budget".center(tp, "=").title() + "|")
        print("|" + "=" * tp + "|")
        kebutuhanPokok = saldo * 0.5
        keinginanPribadi = saldo * 0.3
        tabungan = saldo * 0.2
        print("|" + " ".center(tp) + "|")
        print(
            "|"
            + f"gunakan {kebutuhanPokok:,.2f} untuk kebutuhan pokok".center(tp).title()
            + "|"
        )
        print(
            "|"
            + f"gunakan {keinginanPribadi:,.2f} untuk keinginan pribadi".center(tp).title()
            + "|"
        )
        print(
            "|"
            + f"gunakan {tabungan:,.2f} untuk tabungan/investasi".center(tp).title()
            + "|"
        )
        print("|" + " ".center(tp) + "|")
        print(
            "|"
            + "ingat untuk gunakan uangmu sebijak mungkin agar #AntiBoncos!".center(tp)
            + "|"
        )
        print("|" + "=" * tp + "|")
    opsi = input("kembali ke menu? (y): ")
    if opsi == "y":
        menu()


def cekRiwayat(data):  ## done
    if len(history) == 0: # mengecek apakah list history memiliki nilai didalam atau tidak.
        print("|" + "Riwayat pengeluaran kamu".center(152, "=").title() + "|")
        print(
            "|"
            + "No.".center(4)
            + "|"
            + "Pengeluaran".center(30)
            + "|"
            + "Pemasukan".center(30)
            + "|".center(30)
            + "Kategori".center(30)
            + "|"
            + "tanggal".center(25)
            + "|"
        )
        print("|" + "=" * 152 + "|")
        print("|" + "kamu belum memiliki catatan keuangan selama ini".center(152) + "|")
        print("sistem akan mengembalikan mu ke menu dalam beberapa detik".center(152))
        time.sleep(1.5)
        menu()
    else:
        nomor = 0
        print("|" + "Riwayat pengeluaran kamu".center(152, "=").title() + "|")
        print(
            "|"
            + "No.".center(4)
            + "|"
            + "Pengeluaran".ljust(30)
            + "|"
            + "Pemasukan".ljust(44)
            + "|"
            + "Kategori".ljust(45)
            + "|"
            + "tanggal".ljust(25)
            + "|"
        )
        print("|" + "=" * 152 + "|")
        for i in data: # melakukan perulangan pada parameter data (dalam hal ini variabel history) 
            masukan = f"-" if i[1] == "-" else f"Rp {int(i[1]):,.2f}" # melakukan formatting pada pemasukan
            pengeluaran = f"-" if i[0] == "-" else f"Rp {int(i[0]):,.2f}" # melakukan formatting pada pengeluaran
            nomor += 1
            print(
                f"|{str(nomor).center(4)}|{str(masukan).ljust(30)}|{str(pengeluaran).ljust(44)}|{i[2].ljust(45)}|{i[3].ljust(25)}|"
            )
        print("|" + "=" * 152 + "|")
        print("|" + "Total Saldo".center(136) + "|" + f"Rp{saldo:,.2f}".center(15) + "|")
    opsi = input("kembali ke menu?(y/n) : ")
    if opsi == "y":
        menu()
    else:
        print("terima kasih!")


def evaluasi():
    print("|" + "Evaluasi Keuangan kamu".center(tp, "=").title() + "|")
    print("|" + "=" * tp + "|")
    if saldo < 0:
        print(
            "|"
            + f"Waduh!! Keuangan mu sedang tidak baik baik saja dan berkurang sebanyak Rp{(saldo - tabunganAwal):,.2f}".center(
                tp
            )
            + "|"
        )
    elif saldo > tabunganAwal:
        print(
            "|"
            + f"Hore! Keuangan mu sedang baik baik saja dan bertambah sebanyak Rp{(saldo - tabunganAwal):,.2f}".center(
                tp
            )
            + "|"
        )
    else:
        print("|" + f"Keuanganmu sedang aman aman saja.".center(tp) + "|")
    print("|" + "=" * tp + "|")
    opsi = input("kembali ke menu? (y/n): ")
    if opsi == "y":
        menu()
    elif opsi == "n":
        os.system("cls")
        print("terima kasih!")
    else:
        print("harap masukkan opsi yang benar!")

menu()