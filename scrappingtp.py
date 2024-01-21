
import requests
from bs4 import BeautifulSoup as bs


url='https://lenouvelliste.com/'
#def scrape_journal(url):
    # Envoyer une requête pour récupérer le contenu de la page
 #   response = requests.get(url)

paj= requests.get(url)


soup=bs(paj.text,'html.parser')

print(soup)

