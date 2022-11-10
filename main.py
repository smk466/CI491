from difflib import SequenceMatcher
from operator import contains

from web_content_retrieve import retrieve_webpage_contents
from google_retrieve_links import get_links_from_search_query
from write_output import write_to_file

#queryForLinkedin = 'site:linkedin.com/in/ AND "software engineering"'

def determine_name_and_email_similarity(name: str, email: str) -> bool:
    return SequenceMatcher(None, name, email).ratio() > 0.5
        
def main():
    numOfLinks: int = int(input("Number of links to web scrape: "))
    links: list = get_links_from_search_query(numOfLinks)
    content: list = retrieve_webpage_contents(links)
    write_to_file(content)
    print("Done!")
    
if __name__ == '__main__':
    main()
