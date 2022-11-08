from googlesearch import search
from random import randint
from time import sleep

excludedLinkKeywords = ['.jpg', '.png', '.jpeg', 'youtube', 'wikipedia']

query = "Software Engineering+People"
links = []

def get_links_from_search_query():
    ##GET LINKS FROM SEARCH QUERY:
    totalPageCount = 0
    pageCount = 0
    pageLimit = 50
    linkContainsExcluded = False
    for j in search(query, tld="co.in", num=10, stop=50, pause=2):
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