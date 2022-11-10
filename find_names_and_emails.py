import spacy
import json
import re
import name_email_comparison

english_nlp = spacy.load('en_core_web_sm')
english_nlp.max_length: int = 10000000
alphabetKeysList: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def retrieve_names_and_emails(content: list) -> tuple[list[str], list[str], list[str]]:
    nameList: list[str] = []
    emailList: list[str] = []
    matchingNamesEmails: list[str] = []
    #print(f'Content size in find_names_and_emails: {len(content)}')

    for text in content:
        spacy_parser = english_nlp(text)
        emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        tempNameList: list[str] = []
        tempEmailList: list[str] = []

        for entity in spacy_parser.ents:
            if entity.label_ == 'PERSON':
                if '\n' in entity.text:
                    entity.text.replace('\n', ' ')
                if entity.text[:1].upper() in alphabetKeysList: # and entity.text.isalpha():
                    tempNameList.extend(verify_by_name_dictionary(entity.text))
            elif re.fullmatch(emailRegex, entity.text):
                #print(f'Found Email: {entity.text} of webpage number: {x+1}', file=f)
                tempEmailList.append(entity.text)
        nameList.extend(list(set(tempNameList)))
        emailList.extend(list(set(tempEmailList)))

        matchingNamesEmails.extend(name_email_comparison.compareLists(nameList, emailList))
    
    return nameList, emailList, matchingNamesEmails

def verify_by_name_dictionary(entityText) -> list[str]:
    with open("name_dictionary.json", "r") as f:
        nameDictionary = json.load(f)
    verifiedNameList: list[str] = []

    firstChar = entityText[:1].upper()
    for name in nameDictionary[firstChar]:
        #if (entityText.find(name.lower()) != -1):
        if (entityText.split(" ")[0] == name.lower()):
            #x = content.index(text)
            new_text =  re.sub(r"[^a-zA-Z0-9 ]","", entityText)
            #print(f'Found Name: {new_text} of webpage number: {x+1}', file=f)
            verifiedNameList.append(new_text)

    return verifiedNameList


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