class Kosmetik:
    def __init__(self, nama, harga_supplier):
        self.nama = nama
        self.harga_supplier = harga_supplier

    def hitung_harga_jual(self):
        return self.harga_supplier * 1.1  # Harga jual = harga supplier + 10%

def hitung_harga_jual_semua(kosmetik_list):
    for kosmetik in kosmetik_list:
        print(f"Harga jual untuk {kosmetik.nama}: Rp {kosmetik.hitung_harga_jual():,.2f}")

def main():
    # Membuat daftar kosmetik
    kosmetik_list = [
        Kosmetik("Lipstik", 50000),
        Kosmetik("Bedak", 75000),
        Kosmetik("Maskara", 60000)
    ]

    # Menampilkan harga jual untuk setiap kosmetik
    print("Harga jual untuk setiap kosmetik:")
    hitung_harga_jual_semua(kosmetik_list)

if __name__ == "__main__":
    main()
