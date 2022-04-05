#Sarina D0219381

#Class
class Mahasiswa:
    
    jumlah_mahasiswa = 0 #Variable
    
    def __init__(self, inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim
        Mahasiswa.jumlah_mahasiswa += 1
        
ina = Mahasiswa("Sarina","D0219381")
sarina = Mahasiswa("Sarina Abbas","D0218011")

print(Mahasiswa.jumlah_mahasiswa)
