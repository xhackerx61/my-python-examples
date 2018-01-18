import urllib.request
from bs4 import BeautifulSoup
import http
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

__Author__ = "Aslan"

try:
    linkler = []
    urlMain = "url here"
    getSource = urllib.request.urlopen(urlMain).read()
    soup = BeautifulSoup(getSource, 'html.parser')
    #linkleri al
    link2 = soup.find_all('h3', attrs={'class': 'entry-title'})
    for i in range(0, 6):
        temizLink = str(link2[i])
        mainTitle = str(link2[i].text)
        temizLink = temizLink.replace('<h3 class="entry-title"><a href="', '')
        temizLink = temizLink.replace('" rel="bookmark">' + mainTitle + '</a></h3>', '')
        linkler.append(temizLink)
    sayac = 0
    while sayac < 6:
        newUrl = linkler[sayac]
        getSource = urllib.request.urlopen(newUrl).read()
        soup = BeautifulSoup(getSource, 'html.parser')
        # sayfa detayı
        title = soup.find_all('h1', attrs={'class': 'entry-title'})
        content = soup.find_all('div', attrs={'id': 'book_review_summary'})
        button = soup.find_all('a', attrs={'class': 'custom-link'})
        resim = soup.find_all('img', attrs={'id': 'book_review_cover_image'})
        allContent = str(resim[0]) + "<br/>" + str(content[0]) + "<br/>" + str(button[0])
        mesaj = MIMEMultipart()
        mesaj["From"] = "mail@mail.com" #type your mail here
        mesaj["To"] = "mail@mail.com" #type your mail here
        mesaj["Subject"] = str(title[0].text)
        yazi = allContent
        mesaj_govdesi = MIMEText(yazi, "plain")
        mesaj.attach(mesaj_govdesi)
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login("mail here", "pass here")
        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print("Yayınlandı ID= " + str(sayac + 1))
        mail.close()
        sayac = sayac + 1
    print("İşlem Bitti!\nToplam Yayınlanan : " + str(sayac))


except urllib.error.URLError:
    print('Internet Baglantisi Yok!')
except http.client.IncompleteRead:
    print("Yavaş Bağlantı")
except http.client.IncompleteRead:\
      print('Bir Baglanti Hatasi Oluştu!')
except sys.stderr.write:
    print("Bir sorun oluştu!")
except sys.stderr.flush():
    print("Hata")
