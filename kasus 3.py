def rp(angka):
    return "Rp"+ f"{angka:,.0f}".replace(",",".")


class PaketEkspedisi:
    TARIF = {"reguler":19000, "express":30000}

    def __init__(self, resi, pengirim, layanan, berat, nilai):
        layanan = layanan.strip().lower()
        if layanan not in self.TARIF:
            raise ValueError("Layanan harus reguler atau express")
        if berat <= 0:
            raise ValueError("Berat paket harus lebih dari 0")
        if nilai <= 0:
            raise ValueError("Nilai barang harus lebih dari 0")
        self.resi = resi
        self.pengirim = pengirim
        self.layanan = layanan
        self.berat = berat
        self.nilai = nilai

    def ongkos_dasar(self):
        return self.berat * self.TARIF[self.layanan]

    def asuransi(self):
        if self.nilai >= 1000000:
            return self.nilai * 0.02
        return 0

    def surcharge(self):
        return 0

    def total_ongkos(self):
        return self.ongkos_dasar() + self.surcharge() + self.asuransi()

    def cetak_resi(self):
        print("\n=== RESI PENGIRIMAN ===")
        print("Nomor resi      :", self.resi)
        print("Pengirim        :", self.pengirim)
        print("Layanan         :", self.layanan)
        print(f"Berat           : {self.berat} kg")
        print(f"Tarif dasar     : {rp(self.ongkos_dasar())}")
        print(f"Heavy surcharge : {rp(self.surcharge())}")
        print(f"Biaya asuransi  : {rp(self.asuransi())}")
        print(f"Total ongkos    : {rp(self.total_ongkos())}")
        print("===========================")

print("===== EKSPEDISI NUSANTARA LOGISTIK =====")
try:
    resi = input("Nomor resi: ")
    pengirim = input("Nama pengirim: ")
    layanan = input("Jenis layanan: ")
    berat = float(input("Berat paket: "))
    nilai = float(input("Nilai barang: "))

    paket = PaketEkspedisi(resi, pengirim, layanan, berat, nilai)
    paket.cetak_resi()
except ValueError as e:
    print("Error:", e)