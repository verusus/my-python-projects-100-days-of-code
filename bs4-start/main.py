from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
hacker_web_page = response.text
soup = BeautifulSoup(hacker_web_page, "html.parser")
print(soup.select(selector=".titleline"))
print(soup.find(name="span", class_="titleline").get_text())
print(soup.find_all(name="a")[0].get("href"))
print(soup.find(name="span", class_="score").get_text())




# with open("website.html", encoding="utf8") as file:
#     content = file.read()
#     # print(content)
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
#
# h3_heading = soup.findAll(name="h3", class_="heading")
# print(h3_heading[0].getText())
#
# company_hrl = soup.select_one(selector="p a")
# print(company_hrl)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# print(soup.select(selector=".heading"))
