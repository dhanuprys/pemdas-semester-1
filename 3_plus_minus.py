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
    is_continue = True
    while is_continue:
        if counter == 1:
            output += str(counter + 4)
            total += counter + 4
        elif counter % 2 == 0:
            output += f"+{str(counter + 8)}"
            total += counter + 8
        else:
            output += f"-{str(counter + 4)}"
            total -= counter + 4

        if counter == end:
            is_continue = False

        counter += 1
    print(output, end=f"={total}\n")

def try_again_prompt() -> bool:
    """Menerima konfirmasi dari pengguna apakah ingin lanjut atau tidak

    Returns:
        bool: True jika jawabannya "y" dan False untuk selain "y"
    """
    response = input("Apakah anda ingin mengulang proses? (y/N): ")
    return response.lower() == "y"

def main():
    while True:
        START = 1
        END = input_nilai_end()

        # Memulai proses kalkulasi 
        kalkulasi_nilai(START, END)

        if not try_again_prompt():
            print("Terimakasih telah menggunakan program ini!")
            break

        print()
    

if __name__ == "__main__":
    main()