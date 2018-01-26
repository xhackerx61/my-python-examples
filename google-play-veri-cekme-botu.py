import urllib.request
from bs4 import BeautifulSoup
import http
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import time
import os
os.system("mode con: cols=80 lines=20")
print("""
                  ________                     .__          
                 /  _____/  ____   ____   ____ |  |   ____  
                /   \  ___ /  _ \ /  _ \ / ___\|  | _/ __ \ 
                \    \_\  (  <_> |  <_> ) /_/  >  |_\  ___/ 
                 \______  /\____/ \____/\___  /|____/\___  >
                        \/             /_____/           \/ 
                                              ___  __         
                Play Store Veri Çekme Botu   / _ \/ /__ ___ __
                Ver : 1.0 || Author : Aslan / ___/ / _ `/ // /
                                           /_/  /_/\_,_/\_, / 
                                                       /___/                                                                                          
""")
try:
    print("""
    
                () Çıkış : q
                () İşlem Yapmak İçin Url Bekleniyor...
    
    """)
    durum = True
    while durum:
        getUrl = input("URL : ")
        if(getUrl != "q"):
            getSource = urllib.request.urlopen(getUrl).read()
            soup = BeautifulSoup(getSource, 'html.parser')
            a = soup.find_all("a", attrs={'class': 'title'})
            linkler = []

            # linkleri al
            for i in range(0, 46):
                link = str(a[i])
                basla = (link.find('href="/')) + 6
                bitir = (link.find('" title='))
                link = link[basla:bitir]
                link = link.replace('" tabindex="-1', '')
                # [42:77]
                linkler.append("https://play.google.com" + link + "&hl=tr")
            # her linki ziyaret et
            for j in range(0, 46):
                newSource = urllib.request.urlopen(linkler[j]).read()
                newSoup = BeautifulSoup(newSource, 'html.parser')
                ad = newSoup.find_all("div", attrs={'class': 'id-app-title'})
                detay = newSoup.find_all("div", attrs={'jsname': 'C4s9Ed'})
                urunfoto = newSoup.find_all("img", attrs={'class': 'cover-image'})
                keywords = str(ad[0].text) + """
                apk indir,full apk indir,full indir,hileli versiyon,hileli apk,hileli apk indir,hileli versiyon indir,hileli sürüm indir,
                apk hileleri,android hileli versiyon indir,android indir,android apk,android apk indir,indir,apk,android,2018,son sürüm hileli indir
                """
                urunfoto = str(urunfoto[0]).replace('src="//', 'src="http://')
                urunBilgi = str(detay[0].text) + "<br/>" + keywords
                baslik = str(ad[0].text) + " | Apk İndir,Full Sürüm,Hileli Apk"

                #mail islemleri(bloggerda yayınlama)
                mesaj = MIMEMultipart()
                mesaj["From"] = "mail@mail.com"
                mesaj["To"] = "mail2@mail.com"
                mesaj["Subject"] = baslik
                yazi = "<center>" + urunfoto + "<br/>" + urunBilgi + "</center>"
                mesaj_govdesi = MIMEText(yazi, "plain")
                mesaj.attach(mesaj_govdesi)
                mail = smtplib.SMTP("smtp.yandex.com", 587)
                mail.ehlo()
                mail.starttls()
                mail.login("mail@mail.com", "cokgizlisifre")
                mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
                mail.close()
                print("Yayınlandı ID : " + str(j))
                if j % 5 == 0:
                    print("Durdurmak İçin Ctrl + C Komutunu Kullanın")
                    print("1dk Bekleme Süresi Başladı")
                    for k in range(0, 60, 1):
                        time.sleep(1)
                        print("Kalan Süre : " + str(60-k))
            print("\nBilgi : İşlem Başarıyla Sonuçlandı!")
        elif getUrl == 'q':
            print("\nÇıkış Yapılıyor...")
            durum = False
        else:
            print("Geçersiz İşlem")
except urllib.error.URLError:
    print('Internet Baglantisi Yok!')
except http.client.IncompleteRead:
    print("Yavaş Bağlantı")
except http.client.IncompleteRead:\
    print('Bir Baglanti Hatasi Oluştu!')
except sys.stderr.write:
    print("Bir yazm hatası oluştu!")
except sys.stderr.flush():
    print("başka bi hata")
except smtplib.SMTPDataError(code=554):
    print("Spam şüphesi,biraz bekleyip tekrar deneyin.")
