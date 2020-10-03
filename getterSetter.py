class Mahasiswa:
    # constructor
    def __init__(self, nama, umur):
        # atribut / properti / variabel yang nempel ke objek
        self.nama = nama # ini public
        self.__umur = umur # ini private

    # method / function yang nempel ke object
    def menyapa(self):
        print(f"Hai, namaku {self.nama}.")

    @property # ini decorator
    def umur(self):
        return self.__umur

    # @umur.getter
    # def umur(self):
    #     return self.__umur

    @umur.setter
    def umur(self, umurBaru):
        self.__umur = umurBaru


objek1 = Mahasiswa("Hilman", 98)
objek1.umur = 12
print(f"Halo namaku {objek1.nama}, umurku {objek1.umur}")
objek1.menyapa()
