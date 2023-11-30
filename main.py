import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')   

    span = soup.find_all('span', class_='text')
    author = soup.find_all('small', class_='author')


    for sp in range(len(span)):
        print(span[sp].text, "\n", author[sp].text, "\n")

else:
    print(f"error: {response.status_code}")
