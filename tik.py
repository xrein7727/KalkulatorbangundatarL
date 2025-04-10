import math

def hitung_lingkaran():
    print("\n=== Kalkulator Lingkaran ===")
    print("1. Hitung Luas")
    print("2. Hitung Keliling")
    print("3. Hitung Luas Juring")
    print("4. Hitung Panjang Busur")
    print("5. Hitung Semua")
    print("6. Keluar")
    
    pilihan = input("\nPilih menu (1-6): ")
    
    if pilihan == "6":
        print("Terima kasih telah menggunakan program ini!")
        return
    
    try:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        sudut = 0
        if pilihan in ["3", "4", "5"]:
            sudut = float(input("Masukkan sudut dalam derajat: "))
        
        print("\nPilih nilai π:")
        print("1. 22/7")
        print("2. 3.14")
        pi_choice = input("Pilihan (1-2): ")
        
        if pi_choice == "1":
            pi = 22/7
        else:
            pi = 3.14
        
        if pilihan == "1":
            luas = pi * jari_jari ** 2
            print(f"\nLuas lingkaran: {luas:.2f}")
        
        elif pilihan == "2":
            keliling = 2 * pi * jari_jari
            print(f"\nKeliling lingkaran: {keliling:.2f}")
        
        elif pilihan == "3":
            luas_juring = (pi * jari_jari ** 2 * sudut) / 360
            print(f"\nLuas juring: {luas_juring:.2f}")
        
        elif pilihan == "4":
            panjang_busur = (2 * pi * jari_jari * sudut) / 360
            print(f"\nPanjang busur: {panjang_busur:.2f}")
        
        elif pilihan == "5":
            luas = pi * jari_jari ** 2
            keliling = 2 * pi * jari_jari
            luas_juring = (pi * jari_jari ** 2 * sudut) / 360
            panjang_busur = (2 * pi * jari_jari * sudut) / 360
            
            print(f"\nLuas lingkaran: {luas:.2f}")
            print(f"Keliling lingkaran: {keliling:.2f}")
            print(f"Luas juring: {luas_juring:.2f}")
            print(f"Panjang busur: {panjang_busur:.2f}")
        
        else:
            print("Pilihan tidak valid!")
        
        input("\nTekan Enter untuk melanjutkan...")
        hitung_lingkaran()
        
    except ValueError:
        print("Error: Mohon masukkan angka yang valid!")
        input("\nTekan Enter untuk mencoba lagi...")
        hitung_lingkaran()

if __name__ == "__main__":
    print("Selamat datang di Kalkulator Bangun Datar!")
    hitung_lingkaran()
