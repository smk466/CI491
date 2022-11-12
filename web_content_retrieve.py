from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

page_title: list =[]
page_body: list =[]
page_head: list = []
content: list = []
names: list = []
headers: dict[str, str] = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}

success_link: list = []

def retrieve_webpage_contents(links: list) -> list:
    ##ACHIEVE  CONTENT:
    totalPageCountSoup: int = 0
    for i in links:
        totalPageCountSoup += 1
        page = requests.get(i, headers=headers, verify=False)
        if 100 <= page.status_code <= 399:
            soup = BeautifulSoup(page.content, features = 'html.parser', from_encoding="iso-8859-1")
            #soup = BeautifulSoup(page.content, features = 'parser', from_encoding="iso-8859-1")
            print(f'{totalPageCountSoup}). Success ({page.status_code}): {i}')
            success_link.append(i)
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

        for p in soup.findAll('p'):
            p.replace_with(" %s " % p.string)
            
        for a in soup.findAll('a'):
            a.replace_with(" %s " % a.string)
            

        # get text
        text = soup.get_text().lower()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        #text = text.replace('\n', ' ')
        text = '\n'.join(chunk for chunk in chunks if chunk)
        #text = ' '.join(chunk for chunk in chunks if chunk)       
        content.append(text)
    #print(f'Content size in web_content_retrieve: {len(content)}')
    write_content_text_to_file()
    return content

def write_content_text_to_file() -> None:
    with open("output_contents.txt", "w", encoding="utf-8-sig") as f:
        for text in content:
            print(f'Link: {success_link[content.index(text)]}\n\n{text}\n\n', file=f)
    f.close
    