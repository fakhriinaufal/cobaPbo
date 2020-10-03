# class / blueprints / rancangan
class Mahasiswa:
    # constructor
    def __init__(self, nama, umur):
        # atribut / variabel yang nempel ke objek
        self.nama = nama # ini public
        self.__umur = umur # ini private


    # method / function yang nempel ke object
    def menyapa(self):
        print(f"Hai, namaku {self.nama}.")

    # get => dapetin nilai
    def getUmur(self):
        return self.__umur

    # set => mengubah nilai
    def setUmur(self, umurBaru):
        self.__umur = umurBaru

if __name__ == "__main__":
    objek1 = Mahasiswa("Hilman", 98)
    objek1.alamat = "Jember"
    print(f"Halo namaku {objek1.nama}, rumahku di {objek1.alamat}")
    print(objek1.__dict__)
    print(f"umurku {objek1.getUmur()}")
    objek1.setUmur(13)
    print(f"umurku {objek1.getUmur()}")


    # access modifier
    # public, protected, private