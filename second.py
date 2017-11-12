# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html, "html.parser")
#
# nameList = bsObj.find_all("span", {"class": "green"})
#
# for name in nameList:
#     print(name.get_text())

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# 子要素
# for child in bsObj.find("table", {"id": "giftList"}).children:
#     print(child)


# 兄弟要素
# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#     print(sibling)


# 親要素
# print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())


# メールアドレス正規表現 [A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)
# images = bsObj.find_all("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
#
# for image in images:
#     print(image["src"])

tags = bsObj.find_all(lambda tag: len(tag.attrs) == 1)

for tag in tags:
    print(tag)
