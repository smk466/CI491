#from find_names_and_emails import retrieve_names_and_emails
import find_names_and_emails as fne
import csv
from web_scrape_classes import LinkContent

nameEmailDictionary: dict = {}

def write_to_csv(content: list[LinkContent]) -> None:
    fields: list = ["Link", "Name", "Email"]
    filename: str = "output.csv"
    nameList, emailList, matchingNamesEmails, content = fne.names_and_emails(content)
    with open(filename, "w", encoding="utf-8-sig") as csvfile:
        print(f'Now writing {len(content)} pages into output.csv')
        csvwriter = csv.writer(csvfile)
        csv.field_size_limit
        csvwriter.writerow(fields)
        for webObj in content:
            for personObj in webObj.personList:
                csvwriter.writerow([webObj.link, personObj.name, personObj.email])
    
def write_to_output_txt(content: list[LinkContent]) -> None:
    with open("output.txt", "w", encoding="utf-8-sig") as f:
        print(f'Now writing {len(content)} pages into output.txt')       
        #nameList, emailList, matchingNamesEmails = retrieve_names_and_emails(content)
        nameList, emailList, matchingNamesEmails, content = fne.names_and_emails(content)
        for name in nameList:
            print(f'Name: {name}', file=f)
        for email in emailList:
            print(f'Email: {email}', file=f)
        for person in matchingNamesEmails:
            print(f'Name: {person.name}\nEmail: {person.email}\nLink: {person.link}\n', file=f)
            
        # for person in matchingNamesEmails:
        #     print(f'Name: {person.name}\nEmail: {person.email}\nPhone: {person.phone}\nPosition: {person.position}\nLink: {person.link}\n\n', file=f)
            
        for webObj in content:
            print(f"Link: {webObj.link}\nPersonList Count: {len(webObj.personList)}\n", file=f)
            
        # for matches in matchingNamesEmails:
        #     print(f'Name-Email: {matches}', file=f)
    f.close()