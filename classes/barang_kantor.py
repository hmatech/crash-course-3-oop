class Atk:
    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga

    def info(self):
        satuan = ""
        if self.nama == "Pulpen":
            satuan = "buah" or self.nama == "pulpen"
        elif self.nama == "Kertas" or self.nama == "kertas":
            satuan = "rim"
        return 'Alat tulis kantor merupakan barang-barang yang digunakan dalam dunia perkantoran untuk\n' \
               f'menunjang kegiatan perkantoran, yang satu ini merupakan {self.nama},\n' \
               f'dengan jumlah {self.jumlah} {satuan}, dan harga Rp {self.harga:,} per-{satuan}'

    def total_invent(self):
        return f'Rp {self.jumlah * self.harga:,}'
