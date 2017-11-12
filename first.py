from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)

    except HTTPError as e:
        print(e)
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1

    except AttributeError as e:
        return None

    return title


title = get_title("http://www.pythonscraping.com/pages/page1.html")


if None == title:
    print("Title could not be found")
else:
    print(title)