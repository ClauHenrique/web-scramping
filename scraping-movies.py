# nome do filme, genero e diretor

import requests
from bs4 import BeautifulSoup

url = "https://www.adorocinema.com/filmes/melhores/"

response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')   

    title = soup.find_all('a', class_='meta-title-link')
    gen = soup.find_all('div', class_='meta-body-item meta-body-info')
    d = soup.find_all('a', class_='blue-link')

    generos = []

    for c in gen:
        a = c.text.split('/')
        generos.append(a[1])
    
    for f in range(len(title)):
        print(title[f].text, generos[f], d[f].text, "\n")
  
else:
    print(f"error: {response.status_code}")