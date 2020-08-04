from classes.divisi import Divisi


class RnD(Divisi):
    def __init__(self, nama, umur):
        super().__init__(nama, umur)
        self._Divisi__gaji = self.__gaji = 17000
        self._Divisi__lembur = self.__lembur = 7500

    def info(self):
        return f'Divisi Research and Development dengan gaji {self.__gaji} perjam\n' \
               f'\tdan lembur {self.__lembur} perjam'
