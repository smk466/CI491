import name_email_comparison
from find_names_and_emails import retrieve_names_and_emails
import find_names_and_email_two as fnet

nameEmailDictionary = {}
    
def write_to_file(content: list[str]) -> None:
    with open("output.txt", "w", encoding="utf-8-sig") as f:
        print(f'Now writing {len(content)} pages into output.txt')       
        #nameList, emailList, matchingNamesEmails = retrieve_names_and_emails(content)
        nameList, emailList, matchingNamesEmails = fnet.names_and_emails(content)
        for name in nameList:
            print(f'Name: {name}', file=f)
        for email in emailList:
            print(f'Email: {email}', file=f)
        for matches in matchingNamesEmails:
            print(f'Name-Email: {matches}', file=f)

        #matchingNames = name_email_comparison.compareLists(nameList, emailList) 

        #for i in matchingNames:
        #    print(i, file=f)

        #     for name in nameList:
        #         for email in emailList:
        #             if determine_name_and_email_similarity(name, email):
        #                 nameEmailDictionary[name] = email
        #                 #emailList.remove(email)
        #             else:
        #                 nameEmailDictionary[name] = "None"   
        # #print(f'Name email dictionary: {nameEmailDictionary}')
        # print('\n\n\n\n\n', file=f)
        # for name, email in nameEmailDictionary.items(): 
        #     #print(f'Name: {name}, Email: {email}', file=f)
        #     print("Name: {0:50} Email: {1}".format(name, email), file=f)

    f.close()