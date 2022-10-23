
try:
    from googlesearch import search
    from random import randint
    import requests
    from bs4 import BeautifulSoup
    import json
    import time
except ImportError:
    print("No module named 'google' found")

# to search
query = "Software Engineering+People"


#link = search(query, tld="co.in", num=1, stop=1, pause=2)
#res = requests.get(link)

#print(res.text)
#print(res.status_code)



#for i in range(4):
#    links.append(results[i])

##GET LINKS FROM SEARCH QUERY:
links = []
totalPageCount = 0
pageCount = 0
pageLimit = 30
for j in search(query, tld="co.in", num=10, stop=300, pause=2):
    links.append(j)
    totalPageCount += 1
    print(f'{totalPageCount}). {j}')
    pageCount += 1
    if (pageCount == pageLimit):
        time.sleep(randint(20,40))
        pageCount = 0


##ACHIEVE  CONTENT:
page_title =[]
page_body =[]
page_head = []
content = []
names = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}
for i in links:
    page = requests.get(i, headers=headers, verify=False)
    if page.status_code == 200 and ".jpg" not in i:
        soup = BeautifulSoup(page.content, features = 'html.parser')
    else:
        continue

    #Extract title of the page:
    # page_title.append(soup.title.text)
    #Extract body of the page:
    page_body.append(soup.body)
    # Extract head of page
    page_head.append(soup.head)
    #product = soup.select('div.thumbnail')
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text().lower()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    content.append(text)


print(len(content))
#find names
import spacy
english_nlp = spacy.load('en_core_web_sm')
english_nlp.max_length = 10000000
#webpages = enumerate(content)

with open("output.txt", "w", encoding="utf-8-sig") as f:
    for text in content:
        #print (text)
        spacy_parser = english_nlp(text)
        for entity in spacy_parser.ents:
            if entity.label_ == 'PERSON':
                x = content.index(text)
                print(f'Found Name: {entity.text} of webpage number: {x+1}', file=f)
        
        #print(f'Found: {entity.text} of type: {entity.label_}')
#print(page.text)
# print(page.status_code)





#links2 = []
#for i in range(5-9):
 #   links2.append(results[i])



#for i in links:
 #   google_result = requests.get(i).text
 #   with open("output.txt", "a") as f:
  #      print(google_result, file=f)

#for i in links2:
#    google_result = requests.get(i).text
 #   with open("output.txt", "a") as f:
  #      print(google_result, file=f)

#for i in links2:
 #   google_result = requests.get(i).text
  #  with open("output.txt", "a") as f:
   #     print(google_result, file=f)
