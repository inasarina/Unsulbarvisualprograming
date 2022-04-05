#Class
class Hewan():
    __JumlahKucing = 5  # private
 
    def __init__(self, NamaHewan):
        self.nama = NamaHewan
 
    def hargaHewan(self, HargaHewan):
       hasil = self.__JumlahKucing* HargaHewan
       return hasil
 
imut = Hewan("kucing")
print(imut.hargaHewan(950000))
print(imut.__JumlahKucing)
