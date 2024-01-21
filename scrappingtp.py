
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import csv


url='https://lenouvelliste.com/'

paj= requests.get(url)


soup=bs(paj.text,'html.parser')



#d'abord jwenn articles yo
article_tags = soup.find_all('div', class_='lnv-featured-article-sm')

# boucle pou pran contenu ke nou bezwen yo
for tag in article_tags:
        # titre yo
        title = tag.find('h1').text.strip()

        # imaj yo
        image = urljoin(url, tag.find('img')['src']) if tag.find('img') else None

        # description yo si genyen
        description = tag.find('p', class_='article-intro').text.strip() if tag.find('p', class_='article-intro') else None

        # lyen yo
        link = urljoin(url, tag.find('a')['href']) if tag.find('a') else None

        
        print("Titre article:", title)
        print("Image article:", image)
        print("Description article:", description)
        print("Lien article:", link)
        print("\n\n")

        lis_contenu=[]
        lis_contenu.append([title, image, description, link])
        
        #Mt fe with open li pat mache alors mwen ouvril konsa pito
        csv_file = open('scrap.csv', 'a', newline='', encoding='utf-8')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Titre', 'Image', 'Description', 'Lien'])
        
        csv_writer.writerows(lis_contenu)

        print("Ekri reussi")
        