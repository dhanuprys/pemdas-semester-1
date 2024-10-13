def input_nilai_end() -> int:
    """Menerima input dari user

    Returns:
        int: Hasil input yang sudah dikonversi menjadi tipe data int
    """
    while True:
        user_input: str = ""
        
        try:
            user_input = input("Masukkan nilai end: ")
            return int(user_input)
        except ValueError:
            print(f"'{user_input}' bukan merupakan bilangan yang valid.")
            print("Harap memasukkan bilangan lagi.", end="\n\n")

def kalkulasi_nilai(start: int, end: int):
    """Menghitung kalkulasi nilai dengan pola plus minus

    Args:
        start (int): Nilai awal dari perulangan
        end (int): Nilai akahir dari perulangan
    """
    output = ""
    total = 0
    counter = start
    while counter <= end:
        hasil = 0
        
        if counter % 2 == 0:
            hasil = counter + 3
        else:
            hasil = counter + 2

        if counter > 1:
            # Jika perulangan sudah berada pada nomor kedua dan
            # seterusnya maka blok kode dibawah ini akan di-eksekusi
            if counter % 2 == 0:
                output += "+"
                total += hasil
            else:
                output += "-"
                total -= hasil

            output += str(hasil)
        else:
            # Jika perulangan masih berada pada nomor pertama
            # maka blok kode ini akan di-eksekusi
            output += str(hasil)
            total += hasil

        counter += 1
    print(output, end=f"={total}\n")

def try_again_prompt() -> bool:
    """Menerima konfirmasi dari pengguna apakah ingin lanjut atau tidak

    Returns:
        bool: True jika jawabannya "y" dan False untuk selain "y"
    """
    response = input("Apakah anda ingin mengulang proses? (y): ")
    return response.lower() == "y"

def main():
    while True:
        START = 1
        END = input_nilai_end()

        # Memulai proses kalkulasi 
        kalkulasi_nilai(START, END)

        if not try_again_prompt():
            break
        else:
            print()
    

if __name__ == "__main__":
    main()