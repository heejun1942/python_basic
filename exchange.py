import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/marketindex/"

req = requests.get(url).text
soup= BeautifulSoup(req, 'html.parser')
# ex=soup.select_one("#exchangeList > li.on > .head .usd > .head_info point_dn >  .value")
ex=soup.select_one("#exchangeList .value")
print(ex.text)