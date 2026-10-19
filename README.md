# Ujian Live Coding Pemrograman Berorientasi Objek (PBO)

## Identitas

| Keterangan | Isian |
|---|---|
| Nama | Ahmad Cahya Fashluhi |
| NIM | 2595114018 |
| Kelas | TI A |
| Mata Kuliah | Pemrograman Berorientasi Objek (PBO) |
| Dosen Pengampu | [isi nama dosen] |
| Tanggal Ujian | 19 Oktober 2026 |

## Kasus Pilihan

| No | Kasus | Tingkat | File | Konsep PBO |
|---|---|---|---|---|
| 1 | Kasus 2: Sistem Penggajian Karyawan Honorer | Dasar | `kasus_2_gaji.py` | Class, objek, konstruktor, method perhitungan, validasi atribut |
| 2 | Kasus 3: Sistem Tarif Ekspedisi Logistik | Menengah | `kasus_3_ekspedisi.py` | Class, objek, method, percabangan, validasi |

> Catatan: sesuaikan nama file Kasus 3 dengan nama file yang tertera di soal.

### Ringkasan Kasus 2: GajiKaryawan
- Atribut: ID karyawan, nama, jumlah jam kerja seminggu (valid 1 sampai 80 jam).
- Tarif dasar Rp30.000 per jam, batas normal 40 jam.
- Jam lembur dibayar 1,5 kali tarif dasar (Rp45.000 per jam).
- Pajak 5% hanya jika gaji kotor mencapai atau melebihi Rp1.500.000.
- Method: gaji pokok, upah lembur, potongan pajak, gaji bersih, cetak slip gaji.

### Ringkasan Kasus 3: PaketEkspedisi
- Atribut: nomor resi, nama pengirim, jenis layanan, berat paket (kg), nilai barang.
- Tarif per kg: Reguler Rp10.000, Express Rp18.000.
- Berat lebih dari 10 kg dikenakan heavy surcharge flat Rp20.000.
- Nilai barang minimal Rp1.000.000 dikenakan asuransi 1% dari nilai barang.
- Tolak layanan selain Reguler/Express, serta berat atau nilai barang negatif/nol.
- Method: ongkos dasar, asuransi, surcharge, total ongkos kirim, cetak resi.

## Petunjuk Menjalankan Program

1. Pastikan Python 3 sudah terpasang. Cek dengan perintah:
   ```
   python --version
   ```
2. Buka folder proyek `Ujian_LiveCoding_PBO_NIM_Nama` di VS Code.
3. Buka terminal di VS Code (`Ctrl + ``).
4. Jalankan program per kasus:
   ```
   python kasus_2_gaji.py
   python kasus_3_ekspedisi.py
   ```
5. Masukkan data sesuai prompt yang muncul di layar, lalu program akan mencetak slip gaji atau resi pengiriman.

### Contoh Uji

**Kasus 2** (input: H-104, Hendra, 48 jam), output yang diharapkan:
- Gaji kotor Rp1.560.000, pajak Rp78.000, gaji bersih Rp1.482.000.

**Kasus 3** (input: EXP-9901, Dian, Express, 12 kg, 1500000), output yang diharapkan:
- Tarif dasar Rp216.000, heavy surcharge Rp20.000, asuransi Rp15.000, total ongkos Rp251.000.

## Waktu Pengerjaan

| Keterangan | Waktu |
|---|---|
| Waktu Mulai | [isi, contoh: 10.00 WIB] |
| Waktu Selesai | [isi, contoh: 12.00 WIB] |
| Total Durasi | [isi, contoh: 2 jam 0 menit] |
