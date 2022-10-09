
try:
    from googlesearch import search
    import requests
    from bs4 import BeautifulSoup
    import json
except ImportError:
    print("No module named 'google' found")
 
# to search
query = "Software Engineering+People"


results = search(query, tld="co.in", num=50, stop=50, pause=2)
links = []
for i in range(4):
    links.append(results[i])

links2 = []
for i in range(5-9):
    links2.append(results[i])



for i in links:
    google_result = requests.get(i).text
    with open("output.txt", "a") as f:
        print(google_result, file=f)


for i in links2:
    google_result = requests.get(i).text
    with open("output.txt", "a") as f:
        print(google_result, file=f)

