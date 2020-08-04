from classes.divisi import Divisi


class IT(Divisi):
    def __init__(self, nama, umur):
        super().__init__(nama, umur)
        self._Divisi__gaji = self.__gaji = 20000
        self._Divisi__lembur = self.__lembur = 9000

    def info(self):
        return f'Divisi IT dengan gaji {self.__gaji} perjam\n' \
               f'\tdan lembur {self.__lembur} perjam'
