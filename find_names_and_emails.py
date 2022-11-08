import spacy
import json
import re

english_nlp = spacy.load('en_core_web_sm')
english_nlp.max_length = 10000000
alphabetKeysList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def retrieve_names_and_emails(content):
    nameList = []
    emailList = []
    print(f'Content size in find_names_and_emails: {len(content)}')

    count = 0
    for text in content:
        #print (text)
        spacy_parser = english_nlp(text)
        emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        tempNameList = []
        tempEmailList = []

        for entity in spacy_parser.ents:
            if entity.label_ == 'PERSON':
                if '\n' in entity.text:
                    entity.text.replace('\n', ' ')
                if entity.text[:1].upper() in alphabetKeysList: # and entity.text.isalpha():
                    tempNameList.extend(verify_by_name_dictionary(entity.text))
                    print(f'Temp name list (verified names): {tempNameList}')
            elif re.fullmatch(emailRegex, entity.text):
                #print(f'Found Email: {entity.text} of webpage number: {x+1}', file=f)
                tempEmailList.append(entity.text)
        nameList.extend(list(set(tempNameList)))
        emailList.extend(list(set(tempEmailList)))
        count += 1
        print(f'Name list: {nameList}')
        print(f'Email list: {emailList}')
        #print(f'Check content iteration: {count}')
        
        #print(f'Name list size: {len(nameList)}')
        #print(f'Email list size: {len(emailList)}')
        #with open("output_content.txt", "a", encoding="utf-8-sig") as f:
        #    print(f'Content Count: {count} \n\n {text}', file=f)
    
    return nameList, emailList

def verify_by_name_dictionary(entityText):
    f = open("name_dictionary.json", "r")
    nameDictionary = json.load(f)
    f.close()

    verifiedNameList = []

    firstChar = entityText[:1].upper()
    for name in nameDictionary[firstChar]:
        #if (entityText.find(name.lower()) != -1):
        if (entityText.split(" ")[0] == name.lower()):
            #x = content.index(text)
            new_text =  re.sub(r"[^a-zA-Z0-9 ]","", entityText)
            #print(f'Found Name: {new_text} of webpage number: {x+1}', file=f)
            verifiedNameList.append(new_text)
    
    return verifiedNameList