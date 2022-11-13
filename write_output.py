#from find_names_and_emails import retrieve_names_and_emails
import find_names_and_emails as fne

nameEmailDictionary = {}
    
def write_to_file(content: list[str]) -> None:
    with open("output.txt", "w", encoding="utf-8-sig") as f:
        print(f'Now writing {len(content)} pages into output.txt')       
        #nameList, emailList, matchingNamesEmails = retrieve_names_and_emails(content)
        nameList, emailList, matchingNamesEmails = fne.names_and_emails(content)
        for name in nameList:
            print(f'Name: {name}', file=f)
        for email in emailList:
            print(f'Email: {email}', file=f)
        for matches in matchingNamesEmails:
            print(f'Name-Email: {matches}', file=f)
    f.close()