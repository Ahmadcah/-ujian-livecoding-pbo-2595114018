class TagihanLaundry:
    TARIF = {"reguler":8000, "kilat":16000}

    def __init__(self, nama, layanan, berat):
        self.nama = nama
        self.berat = berat
        layanan = layanan.strip().lower()
        if layanan not in self.TARIF:
            raise ValueError("layanan hanya tersedia reguler dan kilat")
        if berat <= 0:
            raise ValueError("berat cucian harus lebih dari 0")
        self.__nama = nama
        self.__layanan = layanan
        self.__berat = berat

    def tarif(self):
        return self.TARIF[self.__layanan]

    def subtotal(self):
        return self.tarif()*self.__berat

    def persen_diskon(self):
        if self.__berat >= 20:
            return 12
        elif self.__berat >=5:
            return 10
        return 0

    def potongan(self):
        return self.subtotal()*self.persen_diskon()/100

    def total_bayar(self):
        return self.subtotal()-self.potongan()

    @staticmethod
    def rp(angka):
        return "Rp"+ f"{angka:,.0f}".replace(",",".")

    def cetak_nota(self):
        def baris(label,nilai):
            print(f"{label:<16}: {nilai}")

        print("==== NOTA PEMBAYARAN LAUNDRY ====")
        baris("pelanggan",self.__nama)
        baris("layanan",f"{self.__layanan.capitalize()} ({self.rp(self.tarif())}/kg)")
        baris("berat",f"{self.__berat} kg")
        baris("subtotal",self.rp(self.subtotal()))
        baris("diskon",f"{self.persen_diskon()}%")
        baris("total bayar",self.rp(self.total_bayar()))
        print("="*35)

if __name__ == "__main__":
    print("==== LAUNDRY FLASH ====")
    nama = input("nama pelanggan: ")
    layanan = input("layanan (reguler/kilat): ")
    try:
        berat = float(input("berat cucian (kg): "))
    except ValueError:
        print("berat cucian harus berupa angka")
        exit(1)

    try:
        tagihan = TagihanLaundry(nama, layanan, berat)
        tagihan.cetak_nota()
    except ValueError as e:
        print(f"Error: {e}")