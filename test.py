
try:
    from googlesearch import search
    import requests
    from bs4 import BeautifulSoup
    import json
except ImportError:
    print("No module named 'google' found")
 
# to search
query = "Software Engineering+People"

results = {}
#links = []
#contents = []

'''
headers = {
    'Accept-Encoding': 'identity',
}
'''

for j in search(query, tld="co.in", num=10, stop=5, pause=20):
    #links.append(j)
    print(j)
    google_result = requests.get(j).text
    #google_result.encoding = 'utf-8-sig'
    #contents.append(google_result.text)
    #print(google_result.text)
    results[j] = google_result
    with open("output.txt", "a", encoding="utf-8-sig") as f:
        print(f"Result Link: {j}\n\n\n {results.get(j)}\n\n\n\n\n", file=f)
    
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
