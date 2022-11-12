import spacy
import json
import re
import name_email_comparison as nec

english_nlp = spacy.load('en_core_web_sm')
english_nlp.max_length: int = 10000000
alphabetKeysList: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def names_and_emails(content: list[str]) -> tuple[list[str], list[str], list[str]]:
    nameList: list[str] = []
    emailList: list[str] = []
    matchingNamesEmails: list[str] = [] 
    for text in content:
        tempNameList, tempEmailList = retrieve_names_and_emails(text)
        tempNameList = list(set(tempNameList))
        tempEmailList = list(set(tempEmailList))
        matchingNamesEmails.extend(nec.compareLists(tempNameList, tempEmailList))
        nameList.extend(tempNameList)
        emailList.extend(tempEmailList)
        print(f"Name list: {nameList}")
    return nameList, emailList, matchingNamesEmails

def retrieve_names_and_emails(text: str) -> list[str]:
    tempNameList: list = []
    tempEmailList: list = []
    #tempMatchingNamesEmails: list = []
    spacy_parser = english_nlp(text)
    for entity in spacy_parser.ents:
        if (identify_emails(entity)):
            tempEmailList.extend(retrieve_emails(entity))
        elif (identify_names_via_spacy(entity)):
            if ('\n' in entity.text):
                entity.text.replace('\n', ' ')
            if (is_first_character_alphabet(entity) and verify_names_by_name_dictionary(entity)):
                print(f"Entity text: {entity.text}")
                tempNameList.append(entity.text)
    print(f"TempName list: {tempNameList}")
    return tempNameList, tempEmailList

def identify_names_via_spacy(entity) -> bool:
    return entity.label_ == 'PERSON'
           
def is_first_character_alphabet(entity) -> bool:
    return entity.text[:1].upper() in alphabetKeysList
            
def verify_names_by_name_dictionary(entity) -> bool:
    with open("name_dictionary.json", "r") as f:
        nameDictionary: dict[str, str] = json.load(f)
    firstChar = entity.text[:1].upper()
    return any((entity.text.split(" ")[0] == name.lower()) for name in nameDictionary[firstChar])
    
def retrieve_emails(entity) -> list[str]:
    #tempEmailList: list = []
    #if (identify_emails(entity.text)):
    #    tempEmailList.append(entity.text)
    return [entity.text]
    
def identify_emails(entity) -> bool:
    emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(emailRegex, entity.text)