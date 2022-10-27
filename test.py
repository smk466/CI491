
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
import re
##GET LINKS FROM SEARCH QUERY:
from googlesearch import search
links = []

for j in search(query, tld="co.in", num=2, stop=50, pause=2):
    #youtube = re.compile(r"http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?")
    #if not youtube.match(j):
    links.append(j)
    print(j)
    
    


#YT = r"http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?"
'''for  i in links:
    youtube = re.match(YT, i)
 print(youtube)'''


#links = [i for i in links if not youtube.match(i)]


##ACHIEVE  CONTENT:
page_title =[]
page_body =[]
page_head = []
content = []
names = []
for i in links:
    if ".jpg" in i:
        continue
    #if i == youtube:
        #print("found")
    else:
        try:

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
            text = soup.get_text().lower()
            #text = soup.get_text()
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)
            content.append(text)
        except Exception as e:
            #print("Error")
            continue


print(len(content))
#find names
import spacy
import re
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

#EMAIL  
    EMAIL_REGEX = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
    emails = re.findall(EMAIL_REGEX, text)
    print(emails)

'''

# Load pre-existing spacy model
import spacy
nlp=spacy.load('en_core_web_sm')

# Getting the pipeline component
ner=nlp.get_pipe("ner")
TRAIN_DATA = [
              ("software in webpage one", {"entities": [(0, 8, "PRODUCT")]}),
              ("xml in webpage one", {"entities": [(0, 3, "PRODUCT")]}),
              ("bachelor of webpage one", {"entities": [(0,8, "ORG")]}),
              ("in software webpage one", {"entities": [(3, 11, "PRODUCT")]}),
              ("of webpage bachelor one", {"entities": [(11,19, "ORG")]}),
              ("android bachelor one", {"entities": [(0,7, "PRODUCT")]}),
              ("baker bachelor one", {"entities": [(0,5, "PRODUCT")]}),
              ("bachelor baker one", {"entities": [(9,14, "PRODUCT")]}),
              ("one baker", {"entities": [(4,9, "PRODUCT")]})
        
              ]

for _, annotations in TRAIN_DATA:
  for ent in annotations.get("entities"):
    ner.add_label(ent[2])

# Disable pipeline components you dont need to change
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

# Import requirements
#import random
from spacy.util import minibatch, compounding
from pathlib import Path

# TRAINING THE MODEL
with nlp.disable_pipes(*unaffected_pipes):

  # Training for 30 iterations
  for iteration in range(30):

    # shuufling examples  before every iteration
    #random.shuffle(TRAIN_DATA)
    losses = {}
    # batch up the examples using spaCy's minibatch
    batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        texts, annotations = zip(*batch)
        nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                    drop=0.5,  # dropout - make it harder to memorise data
                    losses=losses,
                )
        #print("Losses", losses)

#english_nlp = spacy.load('en_core_web_sm')
#webpages = enumerate(content)
for text in content:
    #print (text)
    spacy_parser = nlp(text)
    for entity in spacy_parser.ents:
        if entity.label_ == 'PERSON':
            x = content.index(text)
            print(f'Found Name: {entity.text} of webpage number: {x+1}')
        #print(f'Found: {entity.text} of type: {entity.label_}')
'''
#links2 = []
#for i in range(5-9):
 #   links2.append(results[i])



