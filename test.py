
try:
    from googlesearch import search
    import requests
    from bs4 import BeautifulSoup
    import json
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
for j in search(query, tld="co.in", num=2, stop=2, pause=2):
   links.append(j)


##ACHIEVE  CONTENT:
page_title =[]
page_body =[]
page_head = []
content = []
names = []
for i in links:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, features = 'html.parser')
    #Extract title of the page:
    page_title.append(soup.title.text)
    #Extract body of the page:
    page_body.append(soup.body)
    # Extract head of page
    page_head.append(soup.head)
    #product = soup.select('div.thumbnail')
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()
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
#webpages = enumerate(content)
for text in content:
    #print (text)
    spacy_parser = english_nlp(text)
    for entity in spacy_parser.ents:
        if entity.label_ == 'PERSON':
            x = content.index(text)
            print(f'Found Name: {entity.text} of webpage number: {x+1}')
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

for i in links2:
    google_result = requests.get(i).text
    with open("output.txt", "a") as f:
        print(google_result, file=f)

#for i in links2:
 #   google_result = requests.get(i).text
  #  with open("output.txt", "a") as f:
   #     print(google_result, file=f)
