from tkinter import *
import tkinter.font

window = Tk()
window.title("UTS_SARINA")
window.geometry('250x150')

ubahfont = tkinter.font.Font(size=12)
jdl = Label(window, text="KALKULATOR", font=ubahfont).grid(column=0, row=0)
 
lbl = Label(window, text="Masukan Angka Pertama : ",anchor="e",width=20)
lbl.grid(column=0, row=5)
 
nilai1 = Entry(window,width=10)
nilai1.grid(column=1,row=5)
 
 
lbl2 = Label(window, text="Masukan Angka Kedua : ",anchor="e",width=20)
lbl2.grid(column=0, row=6)
 
nilai2 = Entry(window,width=10)
nilai2.grid(column=1,row=6)
 
lbl3 = Label(window, text="Hasil : ",anchor="e",width=20)
lbl3.grid(column=0, row=7)
 
hasil = Label(window, text="0",anchor="w",width=10)
hasil.grid(column=1, row=7)
 
def tambah():
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))
 
def kurang():
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get())))
 
def kali():
    hasil.configure(text=(int(nilai1.get())*int(nilai2.get())))
 
def bagi():
    hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))
 
 
b1 = Button(window, text="+", command=tambah)
b1.grid(column=0, row=8)
 
b2 = Button(window, text="-", command=kurang)
b2.grid(column=0, row=9)
 
b3 = Button(window, text="x", command=kali)
b3.grid(column=1, row=8)
 
b4 = Button(window, text=":", command=bagi)
b4.grid(column=1, row=9)
 
window.mainloop()
