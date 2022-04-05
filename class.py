class Mahasiswa:
    def __init__(self, inputNama, inputNim, inputAngkatan):
        self.nama = inputNama
        self.nim = inputNim
        self.angkatan = inputAngkatan

Mhs1 = Mahasiswa("Sarina","D0219381", 2019)
Mhs2 = Mahasiswa("Redi","D0218011",2018)

print(Mhs1.nama, Mhs2.nim)