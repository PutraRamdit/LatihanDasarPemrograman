class Kosmetik:
    def __init__(self, nama, harga_supplier):
        self.nama = nama
        self.harga_supplier = harga_supplier

    def hitung_harga_jual(self):
        return self.harga_supplier * 1.1  # Harga jual = harga supplier + 10%
    
    def hitung_modal(self):
        return self.harga_supplier
    
    def hitung_laba(self):
        return self.hitung_harga_jual() - self.harga_supplier

def hitung_harga_jual_semua(kosmetik_list):
    total_modal = 0
    total_laba = 0
    for kosmetik in kosmetik_list:
        modal = kosmetik.hitung_modal()
        laba = kosmetik.hitung_laba()
        total_modal += modal
        total_laba += laba
        print(f"Harga jual untuk {kosmetik.nama}: Rp {kosmetik.hitung_harga_jual():,.2f} | Modal: Rp {modal:,.2f} | Laba: Rp {laba:,.2f}")
    
    print(f"Total modal: Rp {total_modal:,.2f}")
    print(f"Total laba: Rp {total_laba:,.2f}")

def main():
    # Membuat daftar kosmetik
    kosmetik_list = [
        Kosmetik("Lipstik", 50000),
        Kosmetik("Bedak", 75000),
        Kosmetik("Maskara", 60000)
    ]

    # Menampilkan harga jual, modal, dan laba untuk setiap kosmetik
    print("Harga jual, modal, dan laba untuk setiap kosmetik:")
    hitung_harga_jual_semua(kosmetik_list)

if __name__ == "__main__":
    main()
