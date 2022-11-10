from googlesearch import search
from random import randint
from time import sleep

excludedLinkKeywords: list = ['.jpg', '.png', '.jpeg', 'youtube', 'wikipedia']

query: str = "Software Engineering+People"
links: list = []

def get_links_from_search_query(numOfLinks: int) -> list:
    ##GET LINKS FROM SEARCH QUERY:
    totalPageCount: int = 0
    pageCount: int = 0
    pageLimit: int = 50
    linkContainsExcluded: bool = False
    for j in search(query, tld="co.in", num=10, stop=numOfLinks, pause=2):
        for l in excludedLinkKeywords:
            if l in j:
                linkContainsExcluded = True
                break
        if linkContainsExcluded:
            linkContainsExcluded = False
            continue
        links.append(j)
        totalPageCount += 1
        print(f'{totalPageCount}). {j}')
        pageCount += 1
        if (pageCount == pageLimit):
            sleep(randint(20,40))
            pageCount = 0
    return links