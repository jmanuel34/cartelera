import json
import requests
from bs4 import BeautifulSoup
URL = "https://www.ecartelera.com/peliculas/indice/e/"
content = requests.get(URL)
soup = BeautifulSoup(content.text, "html.parser")
results=[]
items = soup.find('fl-item')
print (soup.get_text)




