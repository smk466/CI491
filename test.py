
try:
    from googlesearch import search
    from lxml import html
    import spacy
    import requests
    from bs4 import BeautifulSoup
    import json
except ImportError:
    print("No module named 'google' found")
 
# to search
query = "Software Engineering+People"
results = {}
header ={"accept-encoding": "gzip, deflate"}
english_nlp = spacy.load('en_core_web_sm')
#english_nlp.max_length = 10000000
names = []

for j in search(query, tld="co.in", num=10, stop=5, pause=20):
    if ".jpg" in j:
        continue
    print(j)
    google_result = requests.get(j, headers=header)
    #google_result_html = html.fromstring(google_result.content)
    results[j] = google_result.text

    spacy_parser = english_nlp(google_result.text)
    for entity in spacy_parser.ents:
        if entity.label_ == "PERSON":
            names.append(entity.text)

with open("output.txt", "w", encoding="utf-8-sig") as f:
    for link in results:
        print(f"Result Link: {link}\n\n\n {results.get(link)}\n\n\n\n\n", file=f)

print(names)
    
#for i in results.keys():
#    print(results.get(i))
#print(results)
    
#with open("output.txt", "w", encoding="utf-8") as f:
    #print((f"Result Link: {i}\n\n{results.get(i)}\n\n\n" for i in results.keys()), file=f)

#with open("output.txt", "w") as f:
#    print('\n'.join(str(e) for e in links), file=f)


"""
results = search(query, tld="co.in", num=10, stop=50, pause=2)

print(results[0])


links = []


for i in range(0,4):
    links.append(results[i])

links2 = []
for i in range(5,9):
    links2.append(results[i])



for i in links:
    google_result = requests.get(i).text
    with open("output.txt", "a") as f:
        print(google_result, file=f)


for i in links2:
    google_result = requests.get(i).text
    with open("output.txt", "a") as f:
        print(google_result, file=f)
"""
