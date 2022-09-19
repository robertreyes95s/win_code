import requests
from bs4 import BeautifulSoup

url = "https://www.timeanddate.com/moon/phases/"
page  = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="main-content-div")

table_element = results.find_all("div", class_="tb-scroll")


