from difflib import SequenceMatcher
from operator import contains

from web_content_retrieve import retrieve_webpage_contents
from google_retrieve_links import get_links_from_search_query
from web_content_text_cleaner import remove_new_lines
from write_output import write_to_file

from web_scrape_classes import LinkContent
from web_scrape_classes import Person
from connect import connect

import find_names_and_emails as fne
import pandas as pd
import pymysql
from sqlalchemy import create_engine
# import config
import psycopg2
#SQL
import mysql.connector
from mysql.connector import errorcode
from sqlalchemy import create_engine

#queryForLinkedin = 'site:linkedin.com/in/ AND "software engineering"'

def determine_name_and_email_similarity(name: str, email: str) -> bool:
    return SequenceMatcher(None, name, email).ratio() > 0.5

#queryForLinkedin = 'site:linkedin.com/in/ AND "software engineering"'

# def determine_name_and_email_similarity(name: str, email: str) -> bool:
#     return SequenceMatcher(None, name, email).ratio() > 0.5


        
def main() -> None:
    numOfLinks: int = int(input("Number of links to web scrape: "))
    links: list[str] = get_links_from_search_query(numOfLinks)
    content: list[str] = retrieve_webpage_contents(links)
    write_to_file(content)
    print("Done!")
    
    nameList, emailList, matchingNamesEmails = fne.names_and_emails(content)
    
    # for name in matchingNamesEmails:
    #     for n in nameList:
    #         if name[0] == n:
    #             nameList.remove(n)
           
    df1=pd.DataFrame(nameList, columns=['Name'])
    df1['Email'] ='NULL'
    df2 = pd.DataFrame(matchingNamesEmails, columns = ['Name','Email'])
    df = df1.append(df2)
    
    print(df)
    print("Done")

    host = 'fieldscrape-db-1.cnapnv5e3bss.us-east-1.rds.amazonaws.com'
    port=5432
    user='postgres'
    passwd='Seniordesign22_ci491'
    database='fieldscrape-db-1'

    # mydb=create_engine('mysql+pymysql://' + user + ':' + passwd + '@' + host + ':' + str(port) + '/' + database , echo=False)
    # df.to_sql(name="table", con=mydb, if_exists = 'replace', index=False)
    cnx = pymysql.connect(host = host, user = user, port = port, password = passwd, db = database)
    print(cnx)
    # cursor = cnx.cursor()
    # #insert Database Name
    # db_name = 'fieldscrape-db'

    # connect()
    
    content: list[LinkContent] = retrieve_webpage_contents(links)
    cleanedContent: list[LinkContent] = remove_new_lines(content)
    write_to_file(cleanedContent)
    print("Done!")
    
if __name__ == '__main__':
    main()
