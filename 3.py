class Tiga:
    def hitung_nilai_akhir(uts, uas):
        return 0.4 * uts + 0.6 * uas

    def hitung_nilai_akhir_semua(data_mahasiswa):
        data_nilai_akhir = {}
        for nama, nilai in data_mahasiswa.items():
            nilai_akhir = Tiga.hitung_nilai_akhir(nilai['uts'], nilai['uas'])
            data_nilai_akhir[nama] = nilai_akhir
        return data_nilai_akhir

    def tampilkan_nilai_akhir(data_nilai_akhir):
        print("Hasil Nilai Akhir Mahasiswa:")
        for nama, nilai_akhir in data_nilai_akhir.items():
            print(f"Nama: {nama}\tNilai Akhir: {nilai_akhir:.2f}")

    def main():
        data_mahasiswa = {
            'Rudi': {'uts': 80, 'uas': 85},
            'Ruda': {'uts': 75, 'uas': 90},
            'RudaL': {'uts': 35, 'uas': 50}
        }
        data_nilai_akhir = Tiga.hitung_nilai_akhir_semua(data_mahasiswa)
        Tiga.tampilkan_nilai_akhir(data_nilai_akhir)
        
if __name__ == "__main__":
    Tiga.main()

