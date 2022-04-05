print ("Perhitungan Aritmatika : 1. Penjumlahan")
print ("                         2. Pengurangan")
print ("                         3. Perkalian")
print ("                         4. Pembagian")

print ()

a = int (input ("Silahkan Pilih(1/2/3/4) : "))
b = int (input ("Masukkan Angka Pertama : "))
c = int (input ("Masukkan Angka Kedua : "))

if (a==1 ):
    print ("Hasil")
    print  (b," + " ,c," = ",(b + c))

elif(a==2):
    print ("Hasil")
    print  (b," - " ,c," = ",(b - c))
    
elif(a==3):
    print ("Hasil")
    print  (b," * " ,c," = ",(b * c))
    
elif(a==4):
    print ("Hasil")
    print  (b," / " ,c," = ",(b / c))
    
else:
    print ("SALAH PILIH")
print ()
print ()