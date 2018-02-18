__Author__ = "Aslan"

from bs4 import BeautifulSoup
import urllib.request
import os
import http
from os import path
print ("""
 _____                _                 _   
/  __ \              | |               | |  
| /  \/  ___   _ __  | |_   ___  _ __  | |_ 
| |     / _ \ | '_ \ | __| / _ \| '_ \ | __|
| \__/\| (_) || | | || |_ |  __/| | | || |_ 
 \____/ \___/ |_| |_| \__| \___||_| |_| \__|
______  _             _                     
| ___ \(_)           | |                    
| |_/ / _  _ __    __| |  ___  _ __         
| ___ \| || '_ \  / _` | / _ \| '__|        
| |_/ /| || | | || (_| ||  __/| |           
\____/ |_||_| |_| \__,_| \___||_|           
                                            
    __Author__ = Aslan | Version = Beta                                           
""")
while True:
    try:
        getUrl = input("URL Bekleniyor: ")
        getSource = urllib.request.urlopen(getUrl).read()
        soup = BeautifulSoup(getSource, 'html.parser')
        title = soup.find_all('h1', attrs={'class', 'entry-title'})
        detay = soup.find_all('div', attrs={'class', 'td-post-content'})
        yaziBaslik = str(title[0].text)
        yaziDetay = detay[0].text
        chars = ['?', '!', '.', ',', '-', '#', '<', '>', '$', '%', '&', '|', ')', '(', ']', '[', '\'', '~', '_', '/',
                 '\\', '*']
        for i in chars:
            yaziBaslik = yaziBaslik.replace(i, "")
        yaziBaslik = "".join(yaziBaslik.rstrip())

        ls = os.listdir()
        checkTitle = yaziBaslik + '.rtf'
        for j in ls:
            if checkTitle == j:
                print("Zaten eklenmiş.")
                break
                exit(1)
        else:
            dosya = open(yaziBaslik + '.rtf', 'a')
            dosya.write(yaziDetay)
            dosya.close()
            print('Eklendi')

    except urllib.error.URLError:
        print('Internet Baglantisi Yok!')
    except http.client.IncompleteRead:
        print("Yavaş Bağlantı")
    except http.client.IncompleteRead:\
        print('Bir Baglanti Hatasi Oluştu!')
    except sys.stderr.write:
        print("Bir yazma hatası oluştu!")
