
from difflib import SequenceMatcher
from operator import contains

from web_content_retrieve import retrieve_webpage_contents
from google_retrieve_links import get_links_from_search_query
from write_output import find_and_check_names

# to search

queryForLinkedin = 'site:linkedin.com/in/ AND "software engineering"'



#for i in range(4):
#    links.append(results[i])



def determine_name_and_email_similarity(name, email):
    return SequenceMatcher(None, name, email).ratio() > 0.5
        

def main():
    ##GET LINKS FROM SEARCH QUERY:
    #links = []
    #for j in search(query, tld="co.in", num=2, stop=2, pause=2):
    #    links.append(j)
    links = get_links_from_search_query()
    content = retrieve_webpage_contents(links)
    find_and_check_names(content)
    print("Done!")
    
if __name__ == '__main__':
    main()
