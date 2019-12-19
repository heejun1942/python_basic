import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"

#request = requests.get(url)
request = requests.get(url).text
#print(request) #<Response [200]> 200은 제대로 받아옴을 의미

soup = BeautifulSoup(request, 'html.parser')
#print(soup)
kospi = soup.select_one("#KOSPI_now")
print(kospi.text)