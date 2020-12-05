import random
import time

class Kumanda():

    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def TvAc(self):
        if(self.tv_durum=="Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    def TvKapat(self):
        if(self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapatılıyor...")
            self.tv_durum = "Kapalı"

    def SesAyarları(self):
        while True:
            cevap = input("Sesi Azalt: '<'\n Sesi Artır: '>'\n Çıkış: Çıkış")

            if(cevap == "<"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("Ses:",self.tv_ses)
            elif(cevap == ">"):
                if(self.tv_ses != 31):
                    self.tv_ses+=1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses Güncellendi.", self.tv_ses)
                break

    def KanalEkle(self,kanal):
        print("Kanal Ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal)
        print("Kanal Eklendi.")

    def RastgeleKanalDegistir(self):

        rastgele_kanal = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele_kanal]
        print("Şu anki kanal: ", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu: {}\n Tv Ses: {}\n Kanal Listesi: {}\n Şu anki Kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda = Kumanda()

print("""Televizyon Kumanda Uygulaması
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanalları Sayısı
6. Rastgele Kanal Aç
7. Televizyon Bilgileri

Çıkmak için 'q' tuşuna basınız.
""")

while True:

    islem = input("İşlem Seçiniz")

    if(islem == "q"):
        print("Program sonlandırılıyor.")
        break
    elif(islem == "1"):
        kumanda.TvAc()
    elif(islem == "2"):
        kumanda.TvKapat()
    elif(islem == "3"):
        kumanda.SesAyarları()
    elif(islem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak giriniz.")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecek_kanallar in kanal_listesi:
            kumanda.KanalEkle(eklenecek_kanallar)

    elif(islem == "5"):
        print("Kanal Sayısı",len(kumanda))
    elif(islem == "6"):
        kumanda.RastgeleKanalDegistir()
    elif(islem == "7"):
        print(kumanda)
    else:
        print("Geçersiz işlem")