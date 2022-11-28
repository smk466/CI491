import re
from difflib import SequenceMatcher
from operator import contains
import nameEmailComparison


try:
    from googlesearch import search
    from random import randint
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    from bs4 import BeautifulSoup
    import json
    import time
    
except ImportError:
    print("No module named 'google' found")

# to search
query = "Software Engineering+People"
queryForLinkedin = 'site:linkedin.com/in/ AND "software engineering"'

links = []

excludedLinkKeywords = ['.jpg', '.png', '.jpeg', 'youtube','wikipedia']

page_title =[]
page_body =[]
page_head = []
content = []
names = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}

#for i in range(4):
#    links.append(results[i])

nameEmailDictionary = {}

def get_links_from_search_query():
    ##GET LINKS FROM SEARCH QUERY:
    totalPageCount = 0
    pageCount = 0
    pageLimit = 50
    linkContainsExcluded = False
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
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
            time.sleep(randint(20,40))
            pageCount = 0
            
def retrieve_webpage_contents():
    ##ACHIEVE  CONTENT:
    totalPageCountSoup = 0
    for i in links:
        totalPageCountSoup += 1
        page = requests.get(i, headers=headers, verify=False)
        if 100 <= page.status_code <= 399:
            soup = BeautifulSoup(page.content, features = 'html.parser', from_encoding="iso-8859-1")
            print(f'{totalPageCountSoup}). Success ({page.status_code}): {i}')
        else:
            print(f'{totalPageCountSoup}). Error(s) ({page.status_code}): {i}')
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
        
    print(f'Now writing {len(content)} pages into output.txt')
    
def find_and_check_names():
    import spacy
    english_nlp = spacy.load('en_core_web_sm')
    english_nlp.max_length = 10000000
    alphabetKeysList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    f = open("name_dictionary.json", "r")
    nameDictionary = json.load(f)
    f.close()

    with open("output.txt", "w", encoding="utf-8-sig") as f:
        #print(content)
        for text in content:
            #print (text)
            spacy_parser = english_nlp(text)
            emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            nameList = []
            emailList = []

            for entity in spacy_parser.ents:
                if entity.label_ == 'PERSON':
                    if '\n' in entity.text:
                        entity.text.replace('\n', ' ')
                    if entity.text[:1].upper() in alphabetKeysList: # and entity.text.isalpha():
                        firstChar = entity.text[:1].upper()
                        for name in nameDictionary[firstChar]:
                            if (entity.text.find(name.lower()) != -1):
                                x = content.index(text)
                                new_text =  re.sub(r"[^a-zA-Z0-9 ]","", entity.text)
                                #print(f'Found Name: {new_text} of webpage number: {x+1}', file=f)
                                nameList.append(new_text)
                elif re.fullmatch(emailRegex, entity.text):
                    #print(f'Found Email: {entity.text} of webpage number: {x+1}', file=f)
                    emailList.append(entity.text)
            nameList = list(set(nameList))
            emailList = list(set(emailList))

            for name in nameList:
                print(f'Name: {name}', file=f)
            for email in emailList:
                print(f'Email: {email}', file=f)

            matchingNames = nameEmailComparison.compareLists(nameList, emailList)   

        #     for name in nameList:
        #         for email in emailList:
        #             if determine_name_and_email_similarity(name, email):
        #                 nameEmailDictionary[name] = email
        #                 #emailList.remove(email)
        #             else:
        #                 nameEmailDictionary[name] = "None"   
        # #print(f'Name email dictionary: {nameEmailDictionary}')
        # print('\n\n\n\n\n', file=f)
        # for name, email in nameEmailDictionary.items(): 
        #     #print(f'Name: {name}, Email: {email}', file=f)
        #     print("Name: {0:50} Email: {1}".format(name, email), file=f)
            for i in matchingNames:
                print(i, file=f)


    
    f.close()

import pandas as pd 
data = {'name': ['Tom','John'], 'Email':['Tome345@gmail']}
df = pd.DataFrame(data)
print(data)
def determine_name_and_email_similarity(name, email):
    return SequenceMatcher(None, name, email).ratio() > 0.5
        

def main():
    ##GET LINKS FROM SEARCH QUERY:
    links = []
    for j in search(query, tld="co.in", num=2, stop=2, pause=2):
        links.append(j)
    get_links_from_search_query()
    retrieve_webpage_contents()
    find_and_check_names()
    print("Done!")
    
if __name__ == '__main__':
    main()
