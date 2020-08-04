class Divisi:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.__gaji = int()
        self.__lembur = int()

    def info(self):
        pass

    def hitung_gaji(self, hari, lembur):
        totaljam = hari * 8 * self.__gaji
        totallembur = lembur * self.__lembur
        totalgaji = totaljam + totallembur
        return f'Data karyawan:\n' \
               f'\t Nama:\t{self.nama}\n' \
               f'\t Umur:\t{self.umur}\n' \
               f'\t Gaji yang diperoleh dari {hari} hari kerja ditambah lembur {lembur} jam adalah Rp {totalgaji:,}'
