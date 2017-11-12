from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import datetime
import random
import re

# random.seed(datetime.datetime.now())
#
#
# def get_links(article_url):
#     html = urlopen("http://en.wikipedia.org" + article_url)
#     bsObj = BeautifulSoup(html, "html.parser")
#
#     return bsObj.find("div", {"id": "bodyContent"}).find_all("a", href=re.compile("^(/wiki/)((?!:).)*$"))
#
#
# links = get_links("/wiki/Kevin_Bacon")
#
# while len(links) > 0:
#     new_article = links[random.randint(0, len(links) - 1)].attrs['href']
#     print(new_article)
#     links = get_links(new_article)

# pages = set()
#
#
# def get_links(page_url):
#     global pages
#
#     html = urlopen("http://en.wikipedia.org" + page_url)
#     bsObj = BeautifulSoup(html, "html.parser")
#
#     try:
#         print(bsObj.h1.get_text())
#         print(bsObj.find(id="mw-content-text").find_all("p")[0].get_text())
#         print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
#
#     except AttributeError:
#         print("This page is missing something! No worries though!")
#
#     for link in bsObj.find_all("a", href=re.compile("^(/wiki/)")):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 # 新しいページに出会った
#                 new_page = link.attrs['href']
#                 print("---------------------\n" + new_page)
#                 pages.add(new_page)
#                 get_links(new_page)
#
#
# get_links("")

pages = set()
random.seed(datetime.datetime.now())


def get_internal_links(bsObj, include_url):
    include_url = urlparse(include_url).scheme + "://" + urlparse(include_url).netloc
    internal_links = []

    for link in bsObj.find_all("a", href=re.compile("^(\/|.*"+include_url+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internal_links:
                if link.attrs['href'].startswith("/"):
                    internal_links.append(include_url+link.attrs['href'])

                else:
                    internal_links.append(link.attrs['href'])

    return internal_links


def get_external_links(bsObj, exclude_url):
    external_links = []

    for link in bsObj.find_all("a", href=re.compile("^(http|www)((?!"+exclude_url+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in external_links:
                external_links.append(link.attrs['href'])

    return external_links


def get_random_external_link(starting_page):
    html = urlopen(starting_page)
    bsObj = BeautifulSoup(html, "html.parser")
    external_links = get_external_links(bsObj, urlparse(starting_page).netloc)

    if len(external_links) == 0:
        print("No external links, looking around the site for one")
        domain = (urlparse(starting_page).scheme+"://"+urlparse(starting_page).netloc)

        internal_links = get_internal_links(bsObj, starting_page)

        return get_random_external_link(internal_links[random.randint(0, len(internal_links)-1)])

    else:
        return external_links[random.randint(0, len(external_links)-1)]


def follow_external_only(starting_site):
    external_link = get_random_external_link(starting_site)
    print("Random external link is: "+external_link)
    follow_external_only(external_link)


follow_external_only("http://oreilly.com")