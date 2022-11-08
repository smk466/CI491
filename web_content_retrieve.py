from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

page_title =[]
page_body =[]
page_head = []
content = []
names = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}

def retrieve_webpage_contents(links):
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
    return content
    