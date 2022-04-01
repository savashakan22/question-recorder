from tkinter import *
from datetime import datetime

import soru_takip as st

root = Tk()
root.geometry("1200x400")
root.title("Soru takip sistemi v1.1")

def soru_kaydet():
    isim    = isim_entry.get()
    bolum   = bolum_entry.get()
    ders    = ders_entry.get()
    soru    = soru_entry.get()
    konu    = konu_entry.get()
    
    if tarih_entry.get() != "":
        tarih   = tarih_entry.get()

    else:
        tarih   = str(datetime.now().strftime(("%d-%m-%Y")))


    st.ogrenci(isim).soru_ekle(bolum, ders, soru, konu, tarih)

    ders_entry.delete(0, "end")
    soru_entry.delete(0, "end")
    konu_entry.delete(0, "end")

def analiz_et():
    pass




#isim yazma yeri
isim_label = Label(root, text = "İsim", )
isim_label.place(x = 100, y = 10)

isim_entry = Entry(root, bd = 2, bg = "black", fg = "white")
isim_entry.place(x = 100, y = 50)


#Bolum (TYT/AYT) yazma yeri
bolum_label = Label(root, text = "Bolüm (TYT/AYT)")
bolum_label.place(x = 300, y = 10)

bolum_entry = Entry(root, bd = 2)
bolum_entry.place(x = 300, y = 50)


#Ders yazma yeri
ders_label = Label(root, text = "Ders")
ders_label.place(x = 500, y = 10)

ders_entry = Entry(root, bd = 2)
ders_entry.place(x = 500, y = 50)


#Soru girme yeri
soru_label = Label(root, text = "Soru sayısı")
soru_label.place(x = 700, y = 10)

soru_entry = Entry(root, bd = 2)
soru_entry.place(x = 700, y = 50)

#konu girme yeri
konu_label = Label(root, text = "Konu")
konu_label.place(x = 700, y= 110)

konu_entry = Entry(root, bd = 2)
konu_entry.place(x = 700, y = 160)

#tarih girme yeri
tarih_label = Label(root, text = "Tarih (GG-AA-YYYY formatında) {Girilmesi şart değil, girilmesse o günün tarihini atar}")
tarih_label.place(x = 100, y = 110)

tarih_entry = Entry(root, bd = 2)
tarih_entry.place(x = 100, y = 160)

#soru_ekle butonu
soru_kaydet_button = Button(root, text = "Ekle", command = soru_kaydet)
soru_kaydet_button.place(x = 850, y = 50)


#analiz butonu
analiz_button = Button(root, text = "Analiz et", command = analiz_et)
analiz_button.place(x = 100, y = 400)




root.mainloop()