def input_jari_jari() -> float:
    """Menerima input dari user

    Returns:
        float: Hasil input yang sudah dikonversi menjadi tipe data float
    """
    while True:
        user_input: str = ""
        
        try:
            user_input = input("Masukkan nilai jari-jari: ")
            return float(user_input)
        except ValueError:
            print(f"'{user_input}' bukan merupakan bilangan yang valid.")
            print("Harap memasukkan bilangan lagi.", end="\n\n")

def hitung_luas_segitiga(jari_jari: int | float) -> float:
    """Menghitung luas segitiga

    Args:
        jari_jari (int | float): Jari-jari dari segitiga yang akan dihitung

    Returns:
        float: Hasil perhitungan
    """
    return 3.14 * jari_jari ** 2

def try_again_prompt() -> bool:
    """Menerima konfirmasi dari pengguna apakah ingin lanjut atau tidak

    Returns:
        bool: True jika jawabannya "y" dan False untuk selain "y"
    """
    response = input("Apakah anda ingin mengulang proses? (y): ")
    return response.lower() == "y"

def main():
    """Program yang digunakan untuk menghitung luas dari sebuah segitiga

    Input: jari jari
    Output: luas segitiga
    """
    while True:
        jari_jari = input_jari_jari()
        result = hitung_luas_segitiga(jari_jari)

        # Menampilkan data dan output
        print(f"> PI = 3.14")
        print(f"> Jari-jari = {jari_jari} cm")
        print(f"> Hasil perhitungan luas adalah {result} cm^2")

        # Bertanya apakah user akan mengulang proses atau tidak
        if not try_again_prompt():
            break
        else:
            print()

if __name__ == "__main__":
    main()