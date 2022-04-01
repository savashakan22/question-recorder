from datetime import datetime
import pandas as pd
import os
import numpy as np

global soru_takip
soru_takip = pd.DataFrame({
                            "tarih"     : [],
                            "isim"      : [],
                            "bolum"     : [],
                            "ders"      : [],
                            "soru"      : [],
                            "konu"      : []
})

if os.path.isfile('soru_takip.csv'):
    soru_takip = pd.read_csv('soru_takip.csv')

else:
    soru_takip.to_csv('soru_takip.csv')
    
    
class ogrenci:


    def __init__(self, isim):
        self.isim = isim
        pass

    
    def soru_ekle(self, bolum, ders, soru, konu, tarih):
        """ Öğrencinin adına soru ekler.
                    bolum       -->     Sorunun TYT mi AYT mi olduğu
                    ders        -->     Hangi ders
                    soru        -->     Kaç soru
                    tarih       -->     Tarih GG-AA-YYYY şeklinde. defaulttayken o günün tarihin ekler
                    konu        -->     Dersin konusu"""

        global soru_takip

        soru_takip = soru_takip.append(pd.DataFrame({
                            "tarih"     : [tarih],
                            "isim"      : [self.isim],
                            "bolum"     : [bolum],
                            "ders"      : [ders],
                            "soru"      : [soru],
                            "konu"      : [konu] 
        }))
        
        soru_takip.to_csv("soru_takip_{0}.csv".format(self.isim))
    
    def analiz(self):
        pass
        

