import json
import re

import spacy
from spacy.language import Language
from spacy.tokens import Doc
from spacy.tokens import Span
from spacy.tokens import Token

import name_email_comparison as nec
from web_scrape_classes import LinkContent
from web_scrape_classes import Person

english_nlp: Language = spacy.load('en_core_web_sm')
english_nlp.max_length: int = 10000000
alphabetKeysList: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

entities: list[Span] = []
#tokens: list[Token] = []
docs: list[Doc] = []

def names_and_emails(content: list[LinkContent]) -> tuple[list[str], list[str], list[str]]:
    nameList: list[str] = []
    emailList: list[str] = []
    #matchingNamesEmails: list[str] = [] 
    matchingNamesEmails: list[Person] = []
    for webObj in content:
        tempNameList: list[str] = retrieve_names(webObj.content)
        tempEmailList: list[str] = retrieve_emails(webObj.content)
        tupleList, personList = nec.compareLists(tempNameList, tempEmailList)
        #matchingNamesEmails.extend(tupleList)
        matchingNamesEmails.extend(personList)
        nameList.extend(tempNameList)
        emailList.extend(tempEmailList)
        write_entity_text_to_file()
        write_doc_text_to_file()
    return nameList, emailList, matchingNamesEmails

# def retrieve_names(text: str) -> list[str]:
#     tempNameList: list = []
#     doc: Doc = english_nlp(text)
#     docs.append(doc)
#     for token in doc:
#         # if '\n' in token.text:
#         #     token.text.replace('\n', ' ')
#         if (is_first_character_alphabet(token)) and (is_the_name_in_name_dictionary(token)):
#             new_text =  re.sub(r"[^a-zA-Z0-9 ]","", token.text)
#             tempNameList.append(new_text)
#         tokens.append(token)
#     return list(set(tempNameList))

def retrieve_names(text: str) -> list[str]:
    tempNameList: list = []
    spacy_parser: Doc = english_nlp(text)
    docs.append(spacy_parser)
    for entity in spacy_parser.ents:
        if '\n' in entity.text:
            entity.text.replace('\n', ' ')
        if (is_it_a_name_via_spacy(entity)) and (is_first_character_alphabet(entity)) and (is_the_name_in_name_dictionary(entity)):
            new_text = re.sub(r"[^a-zA-Z0-9 ]","", entity.text)
            tempNameList.append(remove_extras(separate_combined_text(new_text)))
        entities.append(entity)
    return list(set(tempNameList))

def retrieve_emails(text: str) -> list[str]:
    return list(set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)))

def remove_extras(text: str) -> str:
    if " (newline) " in text:
        subStr: str = " (newline) "
        text: str = text[:text.index(subStr) + len(subStr)]
    pattern = r'[0-9]'
    return re.sub(pattern, '', text)

def separate_combined_text(text: str) -> str:
    strList: list = text.split()
    for word in strList:
        charUpper: bool = False
        for char in word:
            if word.index(char) > 0 and char.isupper():
                newWord: str = f"{word[:word.index(char)]} {word[word.index(char):]}"
                newWordList: list = newWord.split()
                strList[strList.index(word)] = newWordList[0]
                if is_the_name_in_name_dictionary_string(newWordList[1]):
                    strList.append(newWordList[1])
                charUpper = True
                break
        if charUpper:
            continue
    return " ".join(strList)

def is_it_a_name_via_spacy(entity: Span) -> bool:
    return entity.label_ in ['PERSON', "ORG"]
           
def is_first_character_alphabet(entity: Span) -> bool:
    return entity.text[:1].upper() in alphabetKeysList
            
def is_the_name_in_name_dictionary(entity: Span) -> bool:
    with open("name_dictionary.json", "r") as f:
        nameDictionary: dict[str, str] = json.load(f)
    firstChar = entity.text[:1].upper()
    return any((entity.text.split(" ")[0].lower() == name.lower()) for name in nameDictionary[firstChar] if "Data" not in entity.text)

def is_the_name_in_name_dictionary_string(text: str) -> bool:
    with open("name_dictionary.json", "r") as f:
        nameDictionary: dict[str, str] = json.load(f)
    firstChar = text[:1].upper()
    return any((text.split(" ")[0].lower() == name.lower()) for name in nameDictionary[firstChar])
    
def identify_emails(entity: Span) -> bool:
    emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(emailRegex, entity.text)

# def write_entity_text_to_file() -> None:
#     with open("output_entities.txt", "w", encoding="utf-8-sig") as f:
#         for token in tokens:
#             print(f'Entity index: {tokens.index(token)}\n\n{token.text}\n\n', file=f)
#     f.close

def write_entity_text_to_file() -> None:
    with open("output_entities.txt", "w", encoding="utf-8-sig") as f:
        for entity in entities:
            print(f'Entity index: {entities.index(entity)}\n\n{entity.text} ({entity.label_})\n\n', file=f)
    f.close
    
def write_doc_text_to_file() -> None:
    with open("output_doc.txt", "w", encoding="utf-8-sig") as f:
        for doc in docs:
            print(f'Doc: {docs.index(doc)}\n\n{doc}\n\n', file=f)
    f.close
    
"""
TODO:
1. Need to format names that are written in "last name, first name" as spacy doesn't recognize names like that
2. Need to find the cause and avoid name and other text's combination
3. Need to find out why spacy does not recognize names that are written seemly normal
4. Need to find out why some content texts are displaying "none" instead of information we might need
5. Need to also check entity labels with "ORG" as well because some names are labeled as "ORG"
"""